# Half Marathon Plan: September 2026 to August 2027

**Goal:** run a half marathon (21.1 km) in August 2027 in a good time for your fitness level.
**Horizon:** 49 weeks, Monday 14 Sep 2026 to race day Sunday 22 Aug 2027 (placeholder date, swap in your real race).
**Calibrated on:** 90 days of Oura data, 17 Jun to 15 Sep 2026, pulled with `oura/fetch_baseline.py`.

## 1. Health baseline from Oura

Profile: 25-year-old male, 180 cm, 89 kg (BMI 27.5).

| Metric (90-day average) | Value | Read |
|---|---|---|
| Resting heart rate | 52.5 bpm (range 49 to 61) | Good aerobic base for a non-runner, driven by walking and cycling |
| HRV (rMSSD) | 57 ms (September dipped to 54) | Healthy; use 57 as the personal baseline for the daily rule |
| Sleep | 6.9 h/night, 15 of 85 nights under 6 h | Too short for a training build; biggest single limiter |
| Bedtime | Median 01:20, 34 of 85 nights after 02:00, very irregular | Sleep regularity contributor is 69/100, sleep balance 66/100 |
| Sleep score / readiness | 76.5 / 77.6 | Middling, dragged down by sleep timing, not by recovery capacity |
| Readiness under 70 | 11 of 88 days | Roughly one red day a week |
| Steps | 9,970/day, 13 days under 5,000 | Active baseline |
| High-intensity activity | 13.7 min/day, 16 of 89 days with 20 min or more | Little hard work at present |
| Stress vs recovery time | 125 min high stress vs 51 min high recovery per day | Stress-dominant days; running plus better sleep should flip this |
| Workouts | 85 in 90 days: 60 walks, 12 strength, 6 cycling, 3 runs | Strength habit faded after early July (7 sessions in June, 5 in the ten weeks since) |
| Running | 3 runs, longest 1.9 km, 12 min at average 171 bpm, peak 180 bpm | You are starting from zero running volume |
| Measured peak HR | 180 bpm (12-minute run in July) | True max is likely 185 to 195; zones below use a working max of 190 until a hard 5 km shows more |
| VO2max, cardiovascular age, resilience | Not available (endpoints return 401 with the current token scopes) | Re-check after the week-4 time trial |

**What this means for the plan**

1. **You are a fit non-runner, not an unfit person.** Resting HR of 52 and 10k steps a day mean your heart and lungs will progress fast. Your tendons, bones and calves will not: at 89 kg they need a slow ramp, so the first four weeks are run-walk and the fifth run per week is not added until week 17. Do not skip the run-walk phase because it feels too easy.
2. **Sleep is the limiter, not fitness.** 6.9 h with a 01:00 to 03:00 bedtime is where most of the gain is. Target 7.5 h and a bedtime before 00:30 on nights before key sessions. Oura's own contributors say the same: sleep balance and sleep regularity are the two lowest readiness inputs.
3. **Strength training restarts now, twice a week.** It was regular in June and has faded. It is the main protection against the shin, knee and Achilles issues that end first-year running plans, especially for heavier runners.
4. **Body weight will trend down on its own** with 30 to 50 km a week of running. Do not diet during the build; every 1 kg lost at the same fitness is worth roughly 1 min over a half marathon, but under-fuelling costs more in injuries and missed sessions.

## 2. Testing and pacing

**Week 4, Saturday 10 Oct 2026: first continuous 5 km.** Run it as hard as you can sustain evenly after a 15 min warm-up. This sets every training pace. Re-test in week 12 and week 24, race a 10 km in week 30 to re-set paces for the half-marathon-specific block.

Heart-rate zones use a working max of 190 bpm. If your 5 km test shows a peak above 185, raise the max to that peak plus 3 and recalculate.

| Zone | Name | % max HR | bpm at max 190 | Feel | Used for |
|---|---|---|---|---|---|
| Z1 | Recovery | under 70 | under 133 | Could sing | Day after hard sessions |
| Z2 | Easy | 70 to 80 | 133 to 152 | Full sentences | 75 to 80 % of all running |
| Z3 | Steady | 80 to 87 | 152 to 165 | Short sentences | Base II steady runs |
| Z4 | Tempo / HM to 10K pace | 87 to 92 | 165 to 175 | A few words | Tempo and HM-pace work |
| Z5 | Interval / 5K pace | above 92 | above 175 | No talking | 1000 m repeats, hill reps |

Your July run averaged 171 bpm for 12 minutes, which is Z4. That is what almost every new runner does: every run too hard. In this plan most runs stay under 152 bpm. Expect to walk hills in the first months to stay there; that is correct, not a failure.

## 3. What "a good time" means for you

Pick the row from your week-4 test. The **goal** column is one tier faster than your current equivalent, which is realistic with 11 months of consistent training from a low running base.

| 5 km now | Equivalent HM today | Goal for Aug 2027 | Goal HM pace | Easy pace (Z2) | Tempo pace |
|---|---|---|---|---|---|
| 32:00 | 2:27 | 2:10 | 6:10 /km | 7:30 to 8:00 | 6:25 |
| 30:00 | 2:18 | 2:00 | 5:41 /km | 7:00 to 7:30 | 5:55 |
| 27:00 | 2:04 | 1:50 | 5:13 /km | 6:25 to 6:55 | 5:25 |
| 25:00 | 1:55 | 1:42 | 4:50 /km | 6:00 to 6:25 | 5:00 |
| 23:00 | 1:46 | 1:35 | 4:30 /km | 5:30 to 5:55 | 4:40 |
| 21:00 | 1:37 | 1:28 | 4:10 /km | 5:05 to 5:30 | 4:20 |

**Prediction from your data:** a 25-year-old with a resting HR of 52 who has not run typically produces a first 5 km of 26 to 29 min. That puts the realistic goal at **sub-2:00** (5:41/km) with **1:50** (5:13/km) as the stretch target if the week-24 re-test comes in under 24:30 and body weight has dropped to the low 80s. Sub-2:00 puts you in the top half of finishers at a typical city half; 1:50 is around the top third.

## 4. Phases

| Phase | Weeks | Dates | Runs/wk | Peak km/wk | Purpose |
|---|---|---|---|---|---|
| 0 Run-walk | 1 to 4 | 14 Sep to 11 Oct 2026 | 3 | 15 | Tendon adaptation, run-walk to continuous 5 km, first test |
| 1 Base I | 5 to 12 | 12 Oct to 6 Dec 2026 | 3 to 4 | 26 | Aerobic base, strides, strength habit |
| 2 Base II | 13 to 24 | 7 Dec 2026 to 28 Feb 2027 | 4 to 5 | 40 | Winter volume, hills, first tempo runs |
| 3 Strength / 10K | 25 to 34 | 1 Mar to 9 May 2027 | 5 | 48 | VO2max intervals, 10 km race in week 32 |
| 4 HM specific | 35 to 46 | 10 May to 1 Aug 2027 | 5 | 58 | Long runs with HM pace, threshold |
| 5 Taper | 47 to 49 | 2 Aug to 22 Aug 2027 | 5 to 3 | 42 to 18 | Freshen up, race |

Every fourth week is a down week (roughly 70 % volume). Volume never rises more than about 10 % week to week outside of step-backs.

### Weekly template (Phase 2 onward)

| Day | Session |
|---|---|
| Mon | Rest or 30 min easy cycling (you already do this) |
| Tue | Key session 1 (intervals, hills or tempo) with 15 min warm-up and cool-down |
| Wed | Easy run Z2, 40 to 60 min, then strength A |
| Thu | Easy run Z2 with 6x20 s strides, or key session 2 in Phases 3 and 4 |
| Fri | Rest, then strength B |
| Sat | Easy run Z2, 30 to 45 min (the fifth run, drop it first when readiness is low) |
| Sun | Long run |

**Strength A and B**, 25 min each, from week 1: single-leg squats, Romanian deadlifts, calf raises (straight and bent knee, to fatigue), glute bridges, side-lying hip abduction, planks and side planks. Add load over time. Your Oura strength sessions in June averaged 110 to 140 bpm, which is the right intensity.

**Sleep rules for the build:** bedtime by 00:30 on Mon, Wed and Sat nights (before key sessions and long run); 7.5 h target; keep wake time within a 90 min window. Track the Oura sleep regularity contributor; the plan expects it above 80 by December.

## 5. Daily adjustment rule using Oura

Thresholds are set from your 90-day baseline (readiness 78, HRV 57 ms, resting HR 52).

| Oura signal | Action |
|---|---|
| Readiness 85 or above, HRV 55 ms or above | Green: run the session as planned |
| Readiness 70 to 84 | Amber: run it, but cap intervals at 80 % of prescribed reps or shorten the long run by 20 % |
| Readiness under 70, or HRV under 45 ms, or resting HR 57 bpm or above | Red: swap the key session for 30 to 40 min Z1/Z2 or take the day off. Move the key session to the next day at most once. (10 Sep 2026 was such a day: resting HR 61, HRV 35.) |
| Body temperature deviation above +0.5 C two mornings running | Rest until it normalises |
| Sleep under 6 h before a key session | Downgrade to amber |
| Two red days in a row | Take the rest of the week easy and treat it as a down week |

Weekly check: if the 7-day average readiness trends down for three weeks in a row while volume goes up, hold volume flat for two weeks before continuing. Refresh the baseline every 3 months with `python3 oura/fetch_baseline.py --days 90` and update the thresholds: resting HR should drift down towards the mid-40s and HRV up as running fitness builds.

## 6. Week-by-week plan

Total km is a target for the week and includes walking breaks in Phase 0. Long run is on Sunday. Key session is on Tuesday (and Thursday where two are listed). All other runs are Z2 easy, under 152 bpm. "HM pace" is your goal pace from section 3.

| Wk | Mon | Phase | Runs | Total km | Long run | Key session |
|---:|-----|-------|:----:|--------:|--------:|-------------|
| 1 | 14 Sep 2026 | 0 Run-walk | 3 | 9 | 3 | 3x(2 min run / 2 min walk) x 6, easy |
| 2 | 21 Sep 2026 | 0 Run-walk | 3 | 11 | 4 | 3x(3 min run / 2 min walk) x 6 |
| 3 | 28 Sep 2026 | 0 Run-walk | 3 | 13 | 5 | 3x(5 min run / 1 min walk) x 5 |
| 4 | 05 Oct 2026 | 0 Run-walk | 3 | 15 | 5 | First continuous 5 km (Sat): treat as time trial, sets paces |
| 5 | 12 Oct 2026 | 1 Base I | 3 | 16 | 6 | 4x20 s strides after one easy run |
| 6 | 19 Oct 2026 | 1 Base I | 3 | 18 | 7 | 4x20 s strides |
| 7 | 26 Oct 2026 | 1 Base I | 3 | 20 | 8 | 6x20 s strides |
| 8 | 02 Nov 2026 | 1 Base I | 3 | 14 | 6 | Down week, easy only |
| 9 | 09 Nov 2026 | 1 Base I | 4 | 22 | 8 | 6x20 s strides |
| 10 | 16 Nov 2026 | 1 Base I | 4 | 24 | 9 | 8x100 m hill strides |
| 11 | 23 Nov 2026 | 1 Base I | 4 | 26 | 10 | 8x100 m hill strides |
| 12 | 30 Nov 2026 | 1 Base I | 4 | 18 | 7 | Down week + 5 km re-test (Sat) |
| 13 | 07 Dec 2026 | 2 Base II | 4 | 28 | 11 | 3x5 min steady (Z3) |
| 14 | 14 Dec 2026 | 2 Base II | 4 | 30 | 12 | 4x5 min steady |
| 15 | 21 Dec 2026 | 2 Base II | 4 | 32 | 13 | 20 min continuous steady |
| 16 | 28 Dec 2026 | 2 Base II | 4 | 24 | 9 | Down week, holidays flexible |
| 17 | 04 Jan 2027 | 2 Base II | 5 | 32 | 13 | 5x5 min steady |
| 18 | 11 Jan 2027 | 2 Base II | 5 | 34 | 14 | 20 min tempo (Z3/4) |
| 19 | 18 Jan 2027 | 2 Base II | 5 | 36 | 15 | 6x800 m hills |
| 20 | 25 Jan 2027 | 2 Base II | 5 | 26 | 10 | Down week |
| 21 | 01 Feb 2027 | 2 Base II | 5 | 36 | 15 | 25 min tempo |
| 22 | 08 Feb 2027 | 2 Base II | 5 | 38 | 16 | 8x800 m hills |
| 23 | 15 Feb 2027 | 2 Base II | 5 | 40 | 17 | 2x15 min tempo |
| 24 | 22 Feb 2027 | 2 Base II | 5 | 28 | 11 | Down week + 5 km re-test (Sat) |
| 25 | 01 Mar 2027 | 3 Strength/10K | 5 | 40 | 17 | 6x1000 m at 5K pace, 2 min jog |
| 26 | 08 Mar 2027 | 3 Strength/10K | 5 | 42 | 18 | 5x1200 m at 10K pace |
| 27 | 15 Mar 2027 | 3 Strength/10K | 5 | 44 | 18 | 3x10 min at 10K-HM pace |
| 28 | 22 Mar 2027 | 3 Strength/10K | 5 | 30 | 12 | Down week |
| 29 | 29 Mar 2027 | 3 Strength/10K | 5 | 44 | 18 | 8x1000 m at 5K pace |
| 30 | 05 Apr 2027 | 3 Strength/10K | 5 | 46 | 19 | 4x2000 m at 10K pace |
| 31 | 12 Apr 2027 | 3 Strength/10K | 5 | 48 | 20 | 35 min tempo |
| 32 | 19 Apr 2027 | 3 Strength/10K | 5 | 32 | 12 | Mini taper then 10 km race (Sat/Sun) |
| 33 | 26 Apr 2027 | 3 Strength/10K | 5 | 38 | 16 | Recovery week after race, strides only |
| 34 | 03 May 2027 | 3 Strength/10K | 5 | 46 | 20 | 3x3 km at HM pace |
| 35 | 10 May 2027 | 4 HM specific | 5 | 48 | 20 | Long run with last 6 km at HM pace |
| 36 | 17 May 2027 | 4 HM specific | 5 | 50 | 21 | 2x4 km at HM pace |
| 37 | 24 May 2027 | 4 HM specific | 5 | 52 | 22 | Long run with 3x3 km HM pace |
| 38 | 31 May 2027 | 4 HM specific | 5 | 36 | 14 | Down week |
| 39 | 07 Jun 2027 | 4 HM specific | 5 | 52 | 22 | 6x1 mile at 10K pace |
| 40 | 14 Jun 2027 | 4 HM specific | 5 | 54 | 22 | Long run with 8 km at HM pace |
| 41 | 21 Jun 2027 | 4 HM specific | 5 | 56 | 23 | 3x5 km at HM pace |
| 42 | 28 Jun 2027 | 4 HM specific | 5 | 38 | 14 | Down week |
| 43 | 05 Jul 2027 | 4 HM specific | 5 | 54 | 22 | Long run with 10 km at HM pace |
| 44 | 12 Jul 2027 | 4 HM specific | 5 | 56 | 24 | 5x2 km at HM pace, 90 s jog |
| 45 | 19 Jul 2027 | 4 HM specific | 5 | 58 | 24 | Peak week: long run 14 km at HM pace |
| 46 | 26 Jul 2027 | 4 HM specific | 5 | 40 | 15 | Cut-back week |
| 47 | 02 Aug 2027 | 5 Taper | 5 | 42 | 16 | 3x2 km at HM pace |
| 48 | 09 Aug 2027 | 5 Taper | 4 | 30 | 12 | 2x2 km at HM pace, 6x100 m strides |
| 49 | 16 Aug 2027 | 5 Taper | 3 | 18 | - | RACE WEEK: 2 short easy runs, 4 strides, race Sunday |
## 7. Milestones

| When | Check |
|---|---|
| Week 4 (10 Oct 2026) | First continuous 5 km, sets paces and goal tier |
| Week 12 (5 Dec 2026) | 5 km re-test, expect 60 to 90 s faster |
| Week 24 (27 Feb 2027) | 5 km re-test, decides sub-2:00 vs 1:50 goal |
| Week 32 (18 Apr 2027) | 10 km race, confirms goal HM pace (10 km time x 2.2 is a reliable HM prediction) |
| Week 40 (13 Jun 2027) | Long run of 22 km with 8 km at HM pace done comfortably |
| Week 46 (25 Jul 2027) | Peak long run, 14 km at HM pace inside 24 km |
| Week 49 (22 Aug 2027) | Race |

Oura milestones: sleep regularity contributor above 80 by December; average sleep 7.3 h or more by March; resting HR under 48 by June.

## 8. Race week and race execution

- Carbohydrate load from Thursday: 8 to 10 g per kg body weight per day, low fibre on Saturday.
- Race morning: breakfast 3 h before, 60 to 90 g carbs, caffeine 60 min before if you are used to it.
- Pacing: first 5 km at goal pace plus 5 s/km, middle 10 km at goal pace, last 6 km whatever is left. Positive splits of more than 2 min mean you went out too fast.
- Fuel: one gel at 45 min and one at 75 min, water at every station in warm weather.

## 9. Refreshing the data

Tokens last 30 days and refresh with `python3 oura/oauth.py refresh`. Re-run the baseline pull every 3 months and after each 5 km test, and update sections 1, 2 and 5. If the VO2max endpoint becomes available, map it to the goal tiers: roughly 5K 30:00 ≈ 35, 27:00 ≈ 39, 25:00 ≈ 42, 23:00 ≈ 46.
