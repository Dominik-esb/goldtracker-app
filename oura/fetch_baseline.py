#!/usr/bin/env python3
"""Pull a health baseline from the Oura API v2 and print a summary.

Usage:
    export OURA_PAT="<personal access token from https://cloud.ouraring.com/personal-access-tokens>"
    python3 oura/fetch_baseline.py [--days 90]

A Personal Access Token (PAT) is required. An OAuth app client_id/client_secret
pair does NOT work against /v2/usercollection/* endpoints; those need a user token
obtained through the authorization-code flow or a PAT.

Raw responses are written to oura/data/<endpoint>.json (git-ignored).
"""
import argparse
import json
import os
import statistics
import sys
import urllib.parse
import urllib.request
from datetime import date, timedelta

BASE = "https://api.ouraring.com/v2/usercollection"
ENDPOINTS = [
    "personal_info",
    "daily_readiness",
    "daily_sleep",
    "sleep",
    "daily_activity",
    "daily_stress",
    "daily_resilience",
    "daily_cardiovascular_age",
    "vO2_max",
    "workout",
]


def get(path, token, params=None):
    url = f"{BASE}/{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_all(path, token, start, end):
    """Follow next_token pagination and return the concatenated data list."""
    items, next_token = [], None
    while True:
        params = {"start_date": start.isoformat(), "end_date": end.isoformat()}
        if next_token:
            params["next_token"] = next_token
        page = get(path, token, params)
        items.extend(page.get("data", []))
        next_token = page.get("next_token")
        if not next_token:
            return items


def mean(values):
    values = [v for v in values if v is not None]
    return round(statistics.mean(values), 1) if values else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=90)
    args = ap.parse_args()

    token = os.environ.get("OURA_PAT")
    if not token:
        sys.exit("Set OURA_PAT to an Oura personal access token.")

    end = date.today()
    start = end - timedelta(days=args.days)
    out_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(out_dir, exist_ok=True)

    raw = {}
    for ep in ENDPOINTS:
        try:
            raw[ep] = get(ep, token) if ep == "personal_info" else fetch_all(ep, token, start, end)
        except Exception as exc:  # keep going; some endpoints need extra scopes
            print(f"[warn] {ep}: {exc}", file=sys.stderr)
            raw[ep] = None
        with open(os.path.join(out_dir, f"{ep}.json"), "w") as fh:
            json.dump(raw[ep], fh, indent=1)

    pi = raw.get("personal_info") or {}
    print(f"\n== Oura baseline, last {args.days} days ({start} to {end}) ==")
    print(f"age={pi.get('age')} sex={pi.get('biological_sex')} height_m={pi.get('height')} weight_kg={pi.get('weight')}")

    sleep = raw.get("sleep") or []
    long_sleep = [s for s in sleep if s.get("type") == "long_sleep"]
    print("\n-- Sleep --")
    print(f"nights={len(long_sleep)}")
    print(f"avg total sleep h={mean([s.get('total_sleep_duration', 0) / 3600 for s in long_sleep])}")
    print(f"avg resting HR bpm={mean([s.get('lowest_heart_rate') for s in long_sleep])}")
    print(f"avg HRV (rMSSD) ms={mean([s.get('average_hrv') for s in long_sleep])}")
    print(f"avg breathing rate={mean([s.get('average_breath') for s in long_sleep])}")
    ds = raw.get("daily_sleep") or []
    print(f"avg sleep score={mean([d.get('score') for d in ds])}")

    dr = raw.get("daily_readiness") or []
    print("\n-- Readiness --")
    print(f"avg readiness score={mean([d.get('score') for d in dr])}")
    print(f"avg temperature deviation C={mean([d.get('temperature_deviation') for d in dr])}")

    da = raw.get("daily_activity") or []
    print("\n-- Activity --")
    print(f"avg activity score={mean([d.get('score') for d in da])}")
    print(f"avg steps={mean([d.get('steps') for d in da])}")
    print(f"avg active kcal={mean([d.get('active_calories') for d in da])}")
    print(f"avg high-intensity min={mean([d.get('high_activity_time', 0) / 60 for d in da])}")
    print(f"avg medium-intensity min={mean([d.get('medium_activity_time', 0) / 60 for d in da])}")

    st = raw.get("daily_stress") or []
    print("\n-- Stress / resilience --")
    print(f"avg stress-high min={mean([d.get('stress_high', 0) / 60 for d in st])}")
    print(f"avg recovery-high min={mean([d.get('recovery_high', 0) / 60 for d in st])}")
    res = raw.get("daily_resilience") or []
    if res:
        print(f"latest resilience level={res[-1].get('level')}")

    vo2 = raw.get("vO2_max") or []
    cva = raw.get("daily_cardiovascular_age") or []
    print("\n-- Fitness --")
    if vo2:
        print(f"latest VO2max estimate={vo2[-1].get('vo2_max')} (on {vo2[-1].get('day')})")
    if cva:
        print(f"latest cardiovascular age={cva[-1].get('vascular_age')} (on {cva[-1].get('day')})")

    wo = raw.get("workout") or []
    runs = [w for w in wo if (w.get("activity") or "").lower() in ("running", "run", "jogging")]
    print("\n-- Workouts --")
    print(f"total workouts={len(wo)}  runs={len(runs)}")
    if runs:
        km = [w.get("distance", 0) / 1000 for w in runs if w.get("distance")]
        print(f"avg run km={mean(km)}  total run km={round(sum(km), 1)}")
        print(f"runs per week={round(len(runs) / (args.days / 7), 1)}")
    by_act = {}
    for w in wo:
        by_act[w.get("activity")] = by_act.get(w.get("activity"), 0) + 1
    print("by activity=" + json.dumps(dict(sorted(by_act.items(), key=lambda kv: -kv[1]))))


if __name__ == "__main__":
    main()
