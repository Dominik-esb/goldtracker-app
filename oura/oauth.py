#!/usr/bin/env python3
"""Minimal Oura OAuth2 authorization-code helper (no third-party deps).

    export OURA_CLIENT_ID=...  OURA_CLIENT_SECRET=...
    python3 oura/oauth.py authorize-url            # print the link to open in a browser
    python3 oura/oauth.py exchange "<redirect URL or bare code>"
    python3 oura/oauth.py refresh                  # use the stored refresh token

Tokens are stored in oura/data/tokens.json (git-ignored). fetch_baseline.py reads them.
If your Oura app has exactly one redirect URI registered, redirect_uri can be omitted
here and Oura uses the configured one; otherwise set OURA_REDIRECT_URI to match one of them.
"""
import json
import os
import secrets
import sys
import urllib.parse
import urllib.request

AUTHORIZE = "https://cloud.ouraring.com/oauth/authorize"
TOKEN = "https://api.ouraring.com/oauth/token"
SCOPES = "personal daily heartrate workout tag session spo2Daily"
TOKENS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "tokens.json")


def creds():
    cid, sec = os.environ.get("OURA_CLIENT_ID"), os.environ.get("OURA_CLIENT_SECRET")
    if not cid or not sec:
        sys.exit("Set OURA_CLIENT_ID and OURA_CLIENT_SECRET.")
    return cid, sec


def post_token(fields):
    cid, sec = creds()
    fields.update(client_id=cid, client_secret=sec)
    data = urllib.parse.urlencode(fields).encode()
    req = urllib.request.Request(TOKEN, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            tok = json.load(resp)
    except urllib.error.HTTPError as err:
        sys.exit(f"token endpoint {err.code}: {err.read().decode()}")
    os.makedirs(os.path.dirname(TOKENS), exist_ok=True)
    with open(TOKENS, "w") as fh:
        json.dump(tok, fh, indent=1)
    print(f"saved tokens to {TOKENS} (expires_in={tok.get('expires_in')} s)")
    return tok


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "authorize-url":
        cid, _ = creds()
        params = {"response_type": "code", "client_id": cid, "scope": SCOPES, "state": secrets.token_urlsafe(16)}
        if os.environ.get("OURA_REDIRECT_URI"):
            params["redirect_uri"] = os.environ["OURA_REDIRECT_URI"]
        print(AUTHORIZE + "?" + urllib.parse.urlencode(params))
    elif cmd == "exchange" and len(sys.argv) > 2:
        arg = sys.argv[2]
        code = urllib.parse.parse_qs(urllib.parse.urlsplit(arg).query).get("code", [arg])[0] if "code=" in arg else arg
        fields = {"grant_type": "authorization_code", "code": code}
        if os.environ.get("OURA_REDIRECT_URI"):
            fields["redirect_uri"] = os.environ["OURA_REDIRECT_URI"]
        post_token(fields)
    elif cmd == "refresh":
        with open(TOKENS) as fh:
            rt = json.load(fh)["refresh_token"]
        post_token({"grant_type": "refresh_token", "refresh_token": rt})
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
