# Half Marathon Plan: September 2026 to August 2027

**Goal:** run a half marathon (21.1 km) in August 2027 in a "good" time for your fitness level.
**Horizon:** 49 weeks, Monday 14 Sep 2026 to race day Sunday 22 Aug 2027 (placeholder date, swap in your real race).
**Assumption:** you are a healthy adult who can currently jog 3 to 5 km without stopping. If you are already running more than 25 km per week, start at week 7 instead of week 1.

## 1. Health baseline from Oura

The Oura data pull has not happened yet. The credentials supplied are an OAuth **client ID and client secret** for an Oura app. They authenticate the webhook-management endpoints (verified: `GET /v2/webhook/subscription` returns 200) but every `/v2/usercollection/*` endpoint returns 401 with them. Oura only issues user data tokens through the browser OAuth2 authorization-code flow (Personal Access Tokens are deprecated).

To get the baseline:

```bash
export OURA_CLIENT_ID="<client id>" OURA_CLIENT_SECRET="<client secret>"
python3 oura/oauth.py authorize-url        # open the printed link, log in, authorize
python3 oura/oauth.py exchange "<the URL you were redirected to>"
python3 oura/fetch_baseline.py --days 90
```

The script prints the numbers that drive the calibration below: resting heart rate, HRV, sleep duration and score, readiness, VO2max estimate, cardiovascular age, weekly run count and distance. Fill this table in and the plan tiers in section 3 tell you which goal to pick.

| Metric (90-day average) | Value | What it changes |
|---|---|---|
| Resting HR (bpm) | | Below 55: aerobically fit, skip to week 7. Above 70: keep the first 12 weeks strictly easy. |
| HRV rMSSD (ms) | | Personal baseline for the daily go/no-go rule in section 5. |
| Sleep (h/night) | | Under 7 h: fix sleep before adding a fifth run per week. |
| Readiness score | | Personal baseline for the daily rule. |
| VO2max estimate | | Maps to an equivalent 5K/HM time (section 3). |
| Runs per week / km per week | | Determines the starting week. |

## 2. Testing and pacing

**Week 2, Saturday: 5 km time trial** on a flat, measured route after a 15 min warm-up. This sets every training pace. Repeat the test in week 14 and week 26, and race a 10 km in week 30 to re-set paces for the half-marathon-specific block.

Training paces come from the 5K time. Heart-rate zones use max HR; if you do not know it, use the highest value Oura records during the time trial plus 3 bpm.

| Zone | Name | % max HR | Feel | Used for |
|---|---|---|---|---|
| Z1 | Recovery | under 70 | Could sing | Day after hard sessions |
| Z2 | Easy | 70 to 80 | Full sentences | 75 to 80 % of all running |
| Z3 | Steady / marathon pace | 80 to 87 | Short sentences | Base II steady runs |
| Z4 | Tempo / HM to 10K pace | 87 to 92 | A few words | Tempo and HM-pace work |
| Z5 | Interval / 5K pace | above 92 | No talking | 1000 m repeats, hill reps |

## 3. What "a good time" means for you

Pick the row from your week-2 time trial. The **goal** column is one tier faster than your current equivalent, which is realistic with 11 months of consistent training.

| 5 km now | Equivalent HM today | Goal for Aug 2027 | Goal HM pace | Easy pace (Z2) | Tempo pace |
|---|---|---|---|---|---|
| 32:00 | 2:27 | 2:10 | 6:10 /km | 7:30 to 8:00 | 6:25 |
| 30:00 | 2:18 | 2:00 | 5:41 /km | 7:00 to 7:30 | 5:55 |
| 27:00 | 2:04 | 1:50 | 5:13 /km | 6:25 to 6:55 | 5:25 |
| 25:00 | 1:55 | 1:42 | 4:50 /km | 6:00 to 6:25 | 5:00 |
| 23:00 | 1:46 | 1:35 | 4:30 /km | 5:30 to 5:55 | 4:40 |
| 21:00 | 1:37 | 1:28 | 4:10 /km | 5:05 to 5:30 | 4:20 |
| 19:30 | 1:30 | 1:22 | 3:53 /km | 4:45 to 5:10 | 4:02 |

For most recreational runners, sub-2:00 is the classic "good" benchmark, and sub-1:45 puts you in the top quarter of finishers at a typical city half.

## 4. Phases

| Phase | Weeks | Dates | Runs/wk | Peak km/wk | Purpose |
|---|---|---|---|---|---|
| 0 Baseline | 1 to 2 | 14 Sep to 27 Sep 2026 | 3 | 15 | Oura baseline, 5 km test, habit |
| 1 Base I | 3 to 12 | 28 Sep to 6 Dec 2026 | 3 to 4 | 30 | Aerobic base, strides, injury-proofing |
| 2 Base II | 13 to 24 | 7 Dec 2026 to 28 Feb 2027 | 4 to 5 | 42 | Winter volume, hills, first tempo runs |
| 3 Strength / 10K | 25 to 34 | 1 Mar to 9 May 2027 | 5 | 50 | VO2max intervals, 10 km race in week 30 |
| 4 HM specific | 35 to 46 | 10 May to 1 Aug 2027 | 5 | 60 | Long runs with HM pace, threshold |
| 5 Taper | 47 to 49 | 2 Aug to 22 Aug 2027 | 5 to 3 | 42 to 18 | Freshen up, race |

Every fourth week is a down week (roughly 70 % volume). Volume never rises more than about 10 % week to week outside of step-backs.

### Weekly template (Phase 2 onward)

| Day | Session |
|---|---|
| Mon | Rest or 30 min cross-training (bike, swim, row) |
| Tue | Key session 1 (intervals, hills or tempo) with 15 min warm-up and cool-down |
| Wed | Easy run Z2, 40 to 60 min |
| Thu | Easy run Z2 with 6x20 s strides, or key session 2 in Phases 3 and 4 |
| Fri | Rest |
| Sat | Easy run Z2, 30 to 45 min (the fifth run, drop it first when readiness is low) |
| Sun | Long run |

Strength work: 2x per week, 25 min, from week 3 onward. Single-leg squats, Romanian deadlifts, calf raises, glute bridges, planks, side planks. This is the single biggest injury-risk reducer over a 49-week build.

## 5. Daily adjustment rule using Oura

Check readiness before every key session or long run.

| Oura signal | Action |
|---|---|
| Readiness 85 or above, HRV at or above your 30-day average | Green: run the session as planned |
| Readiness 70 to 84 | Amber: run it, but cap intervals at 80 % of prescribed reps or shorten the long run by 20 % |
| Readiness under 70, or HRV more than 20 % below average, or resting HR 5 bpm above baseline | Red: swap the key session for 30 to 40 min Z1/Z2 or take the day off. Move the key session to the next day at most once. |
| Body temperature deviation above +0.5 C two mornings running | Rest until it normalises; you are fighting something |
| Sleep under 6 h before a key session | Downgrade to amber |
| Two red days in a row | Take the rest of the week easy and treat it as a down week |

Weekly check: if the 7-day average readiness trends down for three weeks in a row while volume goes up, hold volume flat for two weeks before continuing.

## 6. Week-by-week plan

Total km is a target for the week. Long run is on Sunday. Key session is on Tuesday (and Thursday where two are listed). All other runs are Z2 easy. "HM pace" is your goal pace from section 3.

| Wk | Mon | Phase | Runs | Total km | Long run | Key session |
|---:|-----|-------|:----:|--------:|--------:|-------------|
| 1 | 14 Sep 2026 | 0 Baseline | 3 | 12 | 5 | Easy running only, log Oura baseline |
| 2 | 21 Sep 2026 | 0 Baseline | 3 | 15 | 6 | 5 km time trial (Sat), sets initial paces |
| 3 | 28 Sep 2026 | 1 Base I | 3 | 16 | 6 | 4x20 s strides after one easy run |
| 4 | 05 Oct 2026 | 1 Base I | 3 | 18 | 7 | 4x20 s strides |
| 5 | 12 Oct 2026 | 1 Base I | 3 | 20 | 8 | 6x20 s strides |
| 6 | 19 Oct 2026 | 1 Base I | 3 | 14 | 6 | Down week, easy only |
| 7 | 26 Oct 2026 | 1 Base I | 4 | 22 | 8 | 6x20 s strides |
| 8 | 02 Nov 2026 | 1 Base I | 4 | 24 | 9 | 8x100 m hill strides |
| 9 | 09 Nov 2026 | 1 Base I | 4 | 26 | 10 | 8x100 m hill strides |
| 10 | 16 Nov 2026 | 1 Base I | 4 | 18 | 7 | Down week |
| 11 | 23 Nov 2026 | 1 Base I | 4 | 28 | 11 | 3x5 min at steady (Z3) pace |
| 12 | 30 Nov 2026 | 1 Base I | 4 | 30 | 12 | 3x6 min steady |
| 13 | 07 Dec 2026 | 2 Base II | 4 | 30 | 12 | 4x5 min steady |
| 14 | 14 Dec 2026 | 2 Base II | 4 | 32 | 13 | 20 min continuous steady |
| 15 | 21 Dec 2026 | 2 Base II | 4 | 34 | 14 | 5x5 min steady |
| 16 | 28 Dec 2026 | 2 Base II | 4 | 24 | 9 | Down week, holiday flexible |
| 17 | 04 Jan 2027 | 2 Base II | 5 | 34 | 14 | 25 min tempo (Z3/4) |
| 18 | 11 Jan 2027 | 2 Base II | 5 | 36 | 15 | 6x800 m hills |
| 19 | 18 Jan 2027 | 2 Base II | 5 | 38 | 16 | 30 min tempo |
| 20 | 25 Jan 2027 | 2 Base II | 5 | 26 | 10 | Down week |
| 21 | 01 Feb 2027 | 2 Base II | 5 | 38 | 16 | 2x15 min tempo |
| 22 | 08 Feb 2027 | 2 Base II | 5 | 40 | 16 | 8x800 m hills |
| 23 | 15 Feb 2027 | 2 Base II | 5 | 42 | 17 | 35 min tempo |
| 24 | 22 Feb 2027 | 2 Base II | 5 | 28 | 11 | Down week |
| 25 | 01 Mar 2027 | 3 Strength/10K | 5 | 42 | 17 | 6x1000 m at 5K pace, 2 min jog |
| 26 | 08 Mar 2027 | 3 Strength/10K | 5 | 44 | 18 | 5x1200 m at 10K pace |
| 27 | 15 Mar 2027 | 3 Strength/10K | 5 | 46 | 18 | 3x10 min at 10K-HM pace |
| 28 | 22 Mar 2027 | 3 Strength/10K | 5 | 30 | 12 | Down week |
| 29 | 29 Mar 2027 | 3 Strength/10K | 5 | 46 | 18 | 8x1000 m at 5K pace |
| 30 | 05 Apr 2027 | 3 Strength/10K | 5 | 48 | 19 | 4x2000 m at 10K pace |
| 31 | 12 Apr 2027 | 3 Strength/10K | 5 | 50 | 20 | 40 min tempo |
| 32 | 19 Apr 2027 | 3 Strength/10K | 5 | 32 | 12 | Mini taper then 10 km race (Sat/Sun) |
| 33 | 26 Apr 2027 | 3 Strength/10K | 5 | 40 | 16 | Recovery week after race, strides only |
| 34 | 03 May 2027 | 3 Strength/10K | 5 | 48 | 20 | 3x3 km at HM pace |
| 35 | 10 May 2027 | 4 HM specific | 5 | 50 | 20 | Long run with last 6 km at HM pace |
| 36 | 17 May 2027 | 4 HM specific | 5 | 52 | 21 | 2x4 km at HM pace |
| 37 | 24 May 2027 | 4 HM specific | 5 | 54 | 22 | Long run with 3x3 km HM pace |
| 38 | 31 May 2027 | 4 HM specific | 5 | 36 | 14 | Down week |
| 39 | 07 Jun 2027 | 4 HM specific | 5 | 54 | 22 | 6x1 mile at 10K pace |
| 40 | 14 Jun 2027 | 4 HM specific | 5 | 56 | 22 | Long run with 8 km at HM pace |
| 41 | 21 Jun 2027 | 4 HM specific | 5 | 58 | 23 | 3x5 km at HM pace |
| 42 | 28 Jun 2027 | 4 HM specific | 5 | 38 | 14 | Down week |
| 43 | 05 Jul 2027 | 4 HM specific | 5 | 56 | 22 | Long run with 10 km at HM pace |
| 44 | 12 Jul 2027 | 4 HM specific | 5 | 58 | 24 | 5x2 km at HM pace, 90 s jog |
| 45 | 19 Jul 2027 | 4 HM specific | 5 | 60 | 24 | Peak week: long run 14 km at HM pace |
| 46 | 26 Jul 2027 | 4 HM specific | 5 | 40 | 15 | Cut-back week |
| 47 | 02 Aug 2027 | 5 Taper | 5 | 42 | 16 | 3x2 km at HM pace |
| 48 | 09 Aug 2027 | 5 Taper | 4 | 30 | 12 | 2x2 km at HM pace, 6x100 m strides |
| 49 | 16 Aug 2027 | 5 Taper | 3 | 18 | - | RACE WEEK: 2 short easy runs, 4 strides, race Sunday |
## 7. Milestones

| When | Check |
|---|---|
| Week 2 (26 Sep 2026) | 5 km time trial, sets paces |
| Week 14 (13 Dec 2026) | 5 km re-test on the Saturday, expect 30 to 60 s faster |
| Week 26 (7 Mar 2027) | 5 km re-test, expect a further 30 to 60 s |
| Week 30 (4 Apr 2027) | 10 km race, confirms goal HM pace (10 km time x 2.2 is a reliable HM prediction for a trained runner) |
| Week 40 (13 Jun 2027) | Long run of 22 km with 8 km at HM pace done comfortably |
| Week 46 (25 Jul 2027) | Peak long run, 14 km at HM pace inside 24 km |
| Week 49 (22 Aug 2027) | Race |

## 8. Race week and race execution

- Carbohydrate load from Thursday: 8 to 10 g per kg body weight per day, low fibre on Saturday.
- Race morning: breakfast 3 h before, 60 to 90 g carbs, caffeine 60 min before if you are used to it.
- Pacing: first 5 km at goal pace plus 5 s/km, middle 10 km at goal pace, last 6 km whatever is left. Positive splits of more than 2 min mean you went out too fast.
- Fuel: one gel at 45 min and one at 75 min, water at every station in warm weather.

## 9. Recalibrating the plan with real data

Once `oura/fetch_baseline.py` has run, update section 1 and adjust:

- **Weekly starting volume:** set week 1 to your current 4-week average, not 12 km, and shift the table so that the progression starts from there.
- **Fifth run per week:** add it only when the 30-day sleep average is at least 7 h and readiness averages above 75.
- **Goal tier:** if Oura's VO2max estimate is 5 or more points above the value implied by your 5 km time (roughly: 5K 30:00 ≈ 35, 25:00 ≈ 42, 21:00 ≈ 50), you are under-racing and can aim two tiers up. If it is 5 points below, aim one tier up at most.
