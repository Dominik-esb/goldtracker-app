#!/usr/bin/env python3
"""Minimal Oura OAuth2 authorization-code helper with PKCE (no third-party deps).

    export OURA_CLIENT_ID=...  OURA_CLIENT_SECRET=...
    python3 oura/oauth.py authorize-url            # print the link to open in a browser
    python3 oura/oauth.py exchange "<redirect URL or bare code>"
    python3 oura/oauth.py refresh                  # use the stored refresh token

Tokens are stored in oura/data/tokens.json (git-ignored). fetch_baseline.py reads them.

Notes learned the hard way (Sep 2026):
- Oura's documented token URL (api.ouraring.com/oauth/token) rejects codes issued by the
  newer auth server with a generic "invalid_request". The issuer in the callback
  (moi.ouraring.com/oauth/v2/ext/oauth-anonymous) publishes its real token endpoint via
  OpenID discovery, and that one works with client_secret_basic. This helper uses it.
- Do NOT pass redirect_uri on the authorize link: Oura's firewall blocks requests that
  carry a localhost redirect. Register exactly one redirect URI on the app and omit it.
- Authorization codes are single-use and short-lived; exchange within a minute or two.
"""
import base64
import hashlib
import json
import os
import secrets
import sys
import urllib.error
import urllib.parse
import urllib.request

AUTHORIZE = "https://cloud.ouraring.com/oauth/authorize"
DISCOVERY = "https://moi.ouraring.com/oauth/v2/ext/oauth-anonymous/.well-known/openid-configuration"
FALLBACK_TOKEN = "https://moi.ouraring.com/oauth/v2/ext/oauth-token"
SCOPES = "personal daily heartrate workout tag session spo2Daily"
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
TOKENS = os.path.join(DATA, "tokens.json")
PKCE = os.path.join(DATA, "pkce.json")


def creds():
    cid, sec = os.environ.get("OURA_CLIENT_ID"), os.environ.get("OURA_CLIENT_SECRET")
    if not cid or not sec:
        sys.exit("Set OURA_CLIENT_ID and OURA_CLIENT_SECRET.")
    return cid, sec


def token_endpoint():
    try:
        with urllib.request.urlopen(DISCOVERY, timeout=15) as resp:
            return json.load(resp)["token_endpoint"]
    except Exception:
        return FALLBACK_TOKEN


def post_token(fields):
    cid, sec = creds()
    data = urllib.parse.urlencode(fields).encode()
    basic = base64.b64encode(f"{cid}:{sec}".encode()).decode()
    req = urllib.request.Request(
        token_endpoint(), data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Basic {basic}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            tok = json.load(resp)
    except urllib.error.HTTPError as err:
        sys.exit(f"token endpoint {err.code}: {err.read().decode()}")
    os.makedirs(DATA, exist_ok=True)
    with open(TOKENS, "w") as fh:
        json.dump(tok, fh, indent=1)
    print(f"saved tokens to {TOKENS} (scope={tok.get('scope')}, expires_in={tok.get('expires_in')} s)")
    return tok


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "authorize-url":
        cid, _ = creds()
        verifier = secrets.token_urlsafe(48)
        challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
        state = secrets.token_urlsafe(16)
        os.makedirs(DATA, exist_ok=True)
        with open(PKCE, "w") as fh:
            json.dump({"verifier": verifier, "state": state}, fh)
        params = {
            "response_type": "code", "client_id": cid, "scope": SCOPES, "state": state,
            "code_challenge": challenge, "code_challenge_method": "S256",
        }
        print(AUTHORIZE + "?" + urllib.parse.urlencode(params))
    elif cmd == "exchange" and len(sys.argv) > 2:
        arg = sys.argv[2]
        qs = urllib.parse.parse_qs(urllib.parse.urlsplit(arg).query) if "code=" in arg else {}
        code = qs.get("code", [arg])[0]
        fields = {"grant_type": "authorization_code", "code": code}
        if os.path.exists(PKCE):
            with open(PKCE) as fh:
                pk = json.load(fh)
            if qs.get("state") and qs["state"][0] != pk["state"]:
                sys.exit("state mismatch: run authorize-url again and use the new link")
            fields["code_verifier"] = pk["verifier"]
        post_token(fields)
    elif cmd == "refresh":
        with open(TOKENS) as fh:
            rt = json.load(fh)["refresh_token"]
        post_token({"grant_type": "refresh_token", "refresh_token": rt})
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
