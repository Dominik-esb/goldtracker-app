# Half Marathon Plan: September 2026 to August 2027

**Goal:** run a half marathon (21.1 km) in August 2027 in a good time for your fitness level.
**Horizon:** 49 weeks, Monday 14 Sep 2026 to race day Sunday 22 Aug 2027 (placeholder date, swap in your real race).
**Calibrated on:** 90 days of Oura data (17 Jun to 15 Sep 2026, pulled with `oura/fetch_baseline.py`) plus your self-reported running: up to 3 runs a week over the last month, mostly zone 2, and a 10 km in 1:10:00 at 178 bpm average.

## 1. Health baseline

Profile: 25-year-old male, 180 cm, 89 kg (BMI 27.5).

| Metric (90-day average) | Value | Read |
|---|---|---|
| Resting heart rate | 52.5 bpm (range 49 to 61) | Good aerobic base |
| HRV (rMSSD) | 57 ms (September dipped to 54) | Healthy; use 57 as the personal baseline for the daily rule |
| Sleep | 6.9 h/night, 15 of 85 nights under 6 h | Too short for a training build; biggest single limiter |
| Bedtime | Median 01:20, 34 of 85 nights after 02:00, very irregular | Sleep regularity contributor is 69/100, sleep balance 66/100 |
| Sleep score / readiness | 76.5 / 77.6 | Middling, dragged down by sleep timing, not by recovery capacity |
| Readiness under 70 | 11 of 88 days | Roughly one red day a week |
| Steps | 9,970/day, 13 days under 5,000 | Active baseline |
| Stress vs recovery time | 125 min high stress vs 51 min high recovery per day | Stress-dominant days |
| Workouts logged by Oura | 85 in 90 days: 60 walks, 12 strength, 6 cycling, 3 runs | Strength habit faded after early July (7 sessions in June, 5 since) |
| Runs logged by Oura | 3, longest 1.9 km, peak 180 bpm | Your recent 10 km runs are not in Oura: wear the ring and start a run in the app so HR and pace get captured |
| Self-reported running | Up to 3 runs/week, mostly zone 2, 10 km in 1:10 at 178 bpm average | Current fitness marker, see below |
| VO2max, cardiovascular age, resilience | Not available (endpoints return 401 with the current token scopes) | Re-check after the week-2 time trial |

**What the 10 km in 1:10 tells us**

- 7:00 /km at 178 bpm average for 70 minutes. Sustaining 178 for that long means your max heart rate is at least 192; the plan uses a working max of 195.
- That run was a near-maximal effort, around 91 % of max HR, so 1:10 is a fair current 10 km race time. Equivalent times today: 5 km around 33:00, half marathon around 2:35.
- Your engine (resting HR 52, HRV 57) is much better than your running economy, which is normal after only a month of running at 89 kg. Economy and the stretch to 21 km are where the big gains come from, and both respond to volume and consistency rather than intensity.

**What this means for the plan**

1. **You can already run 10 km, so there is no run-walk phase.** The plan starts at 20 km a week across 3 runs, roughly what you are doing now, and builds to 4 runs by week 7 and 5 runs by week 17.
2. **Most of your running is currently too hard.** A "zone 2" run for you means under 156 bpm. If your easy runs sit at 165 to 175 bpm, slow down, walk the hills, and accept 7:30 to 8:00 /km for now. This is the single biggest change and it feels wrong for about six weeks.
3. **Sleep is the limiter.** 6.9 h with a 01:00 to 03:00 bedtime is where most of the gain is. Target 7.5 h and a bedtime before 00:30 on nights before key sessions. Oura's two lowest readiness inputs are sleep balance and sleep regularity.
4. **Strength training restarts now, twice a week.** It was regular in June and has faded. It is the main protection against the shin, knee and Achilles issues that end first-year running plans, especially at 89 kg.
5. **Body weight will trend down on its own** with 30 to 50 km a week. Do not diet during the build; every 1 kg lost at the same fitness is worth roughly 1 min over a half marathon, but under-fuelling costs more in injuries and missed sessions.

## 2. Testing and pacing

**Week 2, Saturday 26 Sep 2026: 5 km time trial** on a flat, measured route after a 15 min warm-up, run as hard as you can sustain evenly. It confirms the paces below and gives Oura a real max-HR reading. Re-test in week 10 and week 22, race a 10 km in week 30 to re-set paces for the half-marathon-specific block.

Heart-rate zones use a working max of 195 bpm. If the 5 km test peaks above 192, set the max to that peak plus 3 and recalculate.

| Zone | Name | % max HR | bpm at max 195 | Feel | Used for |
|---|---|---|---|---|---|
| Z1 | Recovery | under 70 | under 137 | Could sing | Day after hard sessions |
| Z2 | Easy | 70 to 80 | 137 to 156 | Full sentences | 75 to 80 % of all running |
| Z3 | Steady | 80 to 87 | 156 to 170 | Short sentences | Base II steady runs |
| Z4 | Tempo / HM to 10K pace | 87 to 92 | 170 to 179 | A few words | Tempo and HM-pace work |
| Z5 | Interval / 5K pace | above 92 | above 179 | No talking | 1000 m repeats, hill reps |

Your 1:10 10 km at 178 bpm was a Z4 effort for 70 minutes. In this plan that intensity appears once a week at most, in the key session, and never for longer than 35 minutes until Phase 4.

## 3. What "a good time" means for you

Starting paces from your current 10 km time. Update this table after the week-2 test if the 5 km comes in under 32:00.

| Pace | Value now | What it is for |
|---|---|---|
| Easy (Z2) | 7:30 to 8:00 /km | All easy runs and long runs |
| Steady (Z3) | 6:50 /km | Base II steady blocks |
| Tempo | 6:35 /km | Tempo runs |
| 10K pace | 7:00 /km now, 6:20 /km by April | Longer intervals |
| 5K pace | 6:35 /km now | 1000 m repeats |

Goal tiers. The **goal** is one tier faster than where you are today, and the **stretch** is two tiers, which is realistic for a 25-year-old with a resting HR of 52 who has 11 months of consistent training ahead and weight to lose.

| Tier | HM time | Pace | Needs a 10 km of | Needs a 5 km of |
|---|---|---|---|---|
| Today | 2:35 | 7:20 /km | 1:10 | 33:00 |
| **Goal** | **2:10** | **6:09 /km** | 58:30 | 27:30 |
| **Stretch** | **1:59** | **5:38 /km** | 53:30 | 25:15 |

Decide between goal and stretch at the week-30 10 km race: under 55:00 means train the last 12 weeks at 1:59 pace, otherwise at 2:10 pace. Sub-2:10 is a respectable first half marathon; sub-2:00 puts you in the top half of finishers at a typical city half and is the classic "good time" benchmark.

## 4. Phases

| Phase | Weeks | Dates | Runs/wk | Peak km/wk | Purpose |
|---|---|---|---|---|---|
| 1 Base I | 1 to 10 | 14 Sep to 22 Nov 2026 | 3 to 4 | 30 | Slow the easy runs down, strides, strength habit, 5 km test |
| 2 Base II | 11 to 22 | 23 Nov 2026 to 14 Feb 2027 | 4 to 5 | 42 | Winter volume, hills, first tempo runs |
| 3 Strength / 10K | 23 to 34 | 15 Feb to 9 May 2027 | 5 | 50 | VO2max intervals, 10 km race in week 30 |
| 4 HM specific | 35 to 46 | 10 May to 1 Aug 2027 | 5 | 60 | Long runs with HM pace, threshold |
| 5 Taper | 47 to 49 | 2 Aug to 22 Aug 2027 | 5 to 3 | 42 to 18 | Freshen up, race |

Every fourth week is a down week (roughly 70 % volume). Volume never rises more than about 10 % week to week outside of step-backs.

### Weekly template (Phase 2 onward)

| Day | Session |
|---|---|
| Mon | Rest or 30 min easy cycling (you already do this) |
| Tue | Key session 1 (intervals, hills or tempo) with 15 min warm-up and cool-down, then strength A (same day, hard days hard) |
| Wed | Easy run Z2, 40 to 60 min |
| Thu | Easy run Z2 with 6x20 s strides, or key session 2 in Phases 3 and 4 |
| Fri | Rest, then strength B |
| Sat | Easy run Z2, 30 to 45 min (the fifth run, drop it first when readiness is low) |
| Sun | Long run |

**Strength A and B**, 30 min each, from week 1. Evidence favours heavy, low-rep strength work and later light plyometrics over bodyweight circuits for running economy (2 to 4 % gains); injury-prevention evidence is mixed but calf and hip strength are consistently weak in injured runners.

- **A (Tue, after the run):** goblet or barbell squat, Romanian deadlift, Bulgarian split squat, straight-knee calf raise with 3 s lowering, plank and dead bug. Weeks 1 to 4 bodyweight or light, 3x10. Weeks 5 to 10, 3x8 adding load. From week 11, 4x5 heavy (2 reps in reserve) on squat and deadlift.
- **B (Fri):** single-leg squat to a bench, single-leg hip thrust, banded side steps, bent-knee (soleus) calf raise loaded, Nordic hamstring curl from week 5, side plank and Pallof press. 3x8 to 3x15. From Phase 3 add 2x10 pogo hops and 2x5 low box jumps at the end if pain-free.
- Deload on running down weeks (2 sets each). No strength in race week, only B light in taper weeks 47 and 48. Never a heavy session the day before the long run.

**Sleep rules for the build:** bedtime by 00:30 on Mon, Wed and Sat nights (before key sessions and long run); 7.5 h target; keep wake time within a 90 min window. Track the Oura sleep regularity contributor; the plan expects it above 80 by December.

**Log every run in Oura** (start it from the app, or let auto-detection do it with the ring on). Without it the readiness rule below has no workout load to react to, and the 90-day baseline refresh cannot see your training.

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

Total km is a target for the week. Long run is on Sunday. Key session is on Tuesday (and Thursday where two are listed). All other runs are Z2 easy, under 156 bpm. "HM pace" is your goal pace from section 3.

| Wk | Mon | Phase | Runs | Total km | Long run | Key session |
|---:|-----|-------|:----:|--------:|--------:|-------------|
| 1 | 14 Sep 2026 | 1 Base I | 3 | 20 | 8 | Easy Z2 only, get used to running under 156 bpm |
| 2 | 21 Sep 2026 | 1 Base I | 3 | 22 | 8 | 5 km time trial (Sat), sets paces |
| 3 | 28 Sep 2026 | 1 Base I | 3 | 22 | 9 | 4x20 s strides after one easy run |
| 4 | 05 Oct 2026 | 1 Base I | 3 | 24 | 10 | 6x20 s strides |
| 5 | 12 Oct 2026 | 1 Base I | 3 | 26 | 11 | 6x20 s strides |
| 6 | 19 Oct 2026 | 1 Base I | 3 | 18 | 8 | Down week, easy only |
| 7 | 26 Oct 2026 | 1 Base I | 4 | 26 | 11 | 8x100 m hill strides |
| 8 | 02 Nov 2026 | 1 Base I | 4 | 28 | 12 | 3x5 min steady (Z3) |
| 9 | 09 Nov 2026 | 1 Base I | 4 | 30 | 13 | 4x5 min steady |
| 10 | 16 Nov 2026 | 1 Base I | 4 | 22 | 9 | Down week + 5 km re-test (Sat) |
| 11 | 23 Nov 2026 | 2 Base II | 4 | 30 | 13 | 5x5 min steady |
| 12 | 30 Nov 2026 | 2 Base II | 4 | 32 | 14 | 20 min continuous steady |
| 13 | 07 Dec 2026 | 2 Base II | 4 | 34 | 15 | 6x800 m hills |
| 14 | 14 Dec 2026 | 2 Base II | 4 | 24 | 10 | Down week, holidays flexible |
| 15 | 21 Dec 2026 | 2 Base II | 5 | 34 | 15 | 20 min tempo (Z3/4) |
| 16 | 28 Dec 2026 | 2 Base II | 5 | 36 | 16 | 8x800 m hills |
| 17 | 04 Jan 2027 | 2 Base II | 5 | 38 | 16 | 25 min tempo |
| 18 | 11 Jan 2027 | 2 Base II | 5 | 26 | 11 | Down week |
| 19 | 18 Jan 2027 | 2 Base II | 5 | 38 | 16 | 2x15 min tempo |
| 20 | 25 Jan 2027 | 2 Base II | 5 | 40 | 17 | 10x600 m hills |
| 21 | 01 Feb 2027 | 2 Base II | 5 | 42 | 18 | 30 min tempo |
| 22 | 08 Feb 2027 | 2 Base II | 5 | 28 | 12 | Down week + 5 km re-test (Sat) |
| 23 | 15 Feb 2027 | 3 Strength/10K | 5 | 42 | 18 | 6x1000 m at 5K pace, 2 min jog |
| 24 | 22 Feb 2027 | 3 Strength/10K | 5 | 44 | 18 | 5x1200 m at 10K pace |
| 25 | 01 Mar 2027 | 3 Strength/10K | 5 | 46 | 19 | 3x10 min at 10K-HM pace |
| 26 | 08 Mar 2027 | 3 Strength/10K | 5 | 30 | 12 | Down week |
| 27 | 15 Mar 2027 | 3 Strength/10K | 5 | 46 | 19 | 8x1000 m at 5K pace |
| 28 | 22 Mar 2027 | 3 Strength/10K | 5 | 48 | 20 | 4x2000 m at 10K pace |
| 29 | 29 Mar 2027 | 3 Strength/10K | 5 | 50 | 20 | 35 min tempo |
| 30 | 05 Apr 2027 | 3 Strength/10K | 5 | 32 | 13 | Mini taper then 10 km race (Sat/Sun) |
| 31 | 12 Apr 2027 | 3 Strength/10K | 5 | 40 | 16 | Recovery week after race, strides only |
| 32 | 19 Apr 2027 | 3 Strength/10K | 5 | 48 | 20 | 3x3 km at HM pace |
| 33 | 26 Apr 2027 | 3 Strength/10K | 5 | 50 | 21 | 5x1600 m at 10K pace |
| 34 | 03 May 2027 | 3 Strength/10K | 5 | 34 | 14 | Down week |
| 35 | 10 May 2027 | 4 HM specific | 5 | 50 | 21 | Long run with last 6 km at HM pace |
| 36 | 17 May 2027 | 4 HM specific | 5 | 52 | 22 | 2x4 km at HM pace |
| 37 | 24 May 2027 | 4 HM specific | 5 | 54 | 22 | Long run with 3x3 km HM pace |
| 38 | 31 May 2027 | 4 HM specific | 5 | 36 | 14 | Down week |
| 39 | 07 Jun 2027 | 4 HM specific | 5 | 54 | 22 | 6x1 mile at 10K pace |
| 40 | 14 Jun 2027 | 4 HM specific | 5 | 56 | 23 | Long run with 8 km at HM pace |
| 41 | 21 Jun 2027 | 4 HM specific | 5 | 58 | 24 | 3x5 km at HM pace |
| 42 | 28 Jun 2027 | 4 HM specific | 5 | 38 | 15 | Down week |
| 43 | 05 Jul 2027 | 4 HM specific | 5 | 56 | 23 | Long run with 10 km at HM pace |
| 44 | 12 Jul 2027 | 4 HM specific | 5 | 58 | 24 | 5x2 km at HM pace, 90 s jog |
| 45 | 19 Jul 2027 | 4 HM specific | 5 | 60 | 24 | Peak week: long run 14 km at HM pace |
| 46 | 26 Jul 2027 | 4 HM specific | 5 | 40 | 15 | Cut-back week |
| 47 | 02 Aug 2027 | 5 Taper | 5 | 42 | 16 | 3x2 km at HM pace |
| 48 | 09 Aug 2027 | 5 Taper | 4 | 30 | 12 | 2x2 km at HM pace, 6x100 m strides |
| 49 | 16 Aug 2027 | 5 Taper | 3 | 18 | - | RACE WEEK: 2 short easy runs, 4 strides, race Sunday |
## 7. Milestones

| When | Check |
|---|---|
| Week 2 (26 Sep 2026) | 5 km time trial, confirms paces and max HR. Expect 31 to 34 min |
| Week 10 (21 Nov 2026) | 5 km re-test, expect 29 to 30 min |
| Week 22 (13 Feb 2027) | 5 km re-test, expect 27 to 28 min |
| Week 30 (11 Apr 2027) | 10 km race. Under 55:00 unlocks the 1:59 stretch goal; 10 km time x 2.2 predicts the half |
| Week 40 (13 Jun 2027) | Long run of 22 km with 8 km at HM pace done comfortably |
| Week 46 (25 Jul 2027) | Peak long run, 14 km at HM pace inside 24 km |
| Week 49 (22 Aug 2027) | Race |

Oura milestones: sleep regularity contributor above 80 by December; average sleep 7.3 h or more by March; resting HR under 48 by June; easy runs averaging under 156 bpm at 7:00 /km by February (that is the economy gain showing up).

## 8. Race week and race execution

- Carbohydrate load from Thursday: 8 to 10 g per kg body weight per day, low fibre on Saturday.
- Race morning: breakfast 3 h before, 60 to 90 g carbs, caffeine 60 min before if you are used to it.
- Pacing: first 5 km at goal pace plus 5 s/km, middle 10 km at goal pace, last 6 km whatever is left. Positive splits of more than 2 min mean you went out too fast.
- Fuel: one gel at 45 min and one at 75 min, water at every station in warm weather.

## 9. Plan checks against published guidance

- Weekly volume never rises more than 10 % outside step-backs; every fourth week is a down week; roughly 80 % of running is easy. All three match current guidance.
- A cohort study of recreational half marathoners found that over 32 km per week and long runs over 21 km were associated with faster finishes (about 4 min) with no increase in injury rate. The plan peaks at 60 km with a 24 km long run.
- Long runs are 40 % of weekly volume in Phase 1, above the usual 20 to 30 %. That is the accepted beginner exception: weekly volume is too low to keep the long run in range. From Phase 2 it sits at 35 to 40 %.
- The taper is effectively two weeks (week 48 at 50 %, week 49 at 30 % of peak); week 47 is a normal cut-back week with quality kept in. Three-week tapers are not recommended for runners at this level.

## 10. Nutrition

Oura estimates your expenditure at about 3,100 to 3,200 kcal per day over the last 90 days (BMR 1,900 by Mifflin-St Jeor, 750 active kcal). Running adds roughly 60 kcal per km at 89 kg, so expenditure rises with the plan.

**Strategy:** a small deficit while volume is low, maintenance once the hard blocks start. Weight loss comes from the deficit and the mileage together; never from cutting carbs on training days.

| Phase | Expenditure est. | Rest / easy days | Key session or long-run days | Weight aim |
|---|---|---|---|---|
| 1 Base I (Sep to Nov) | 3,100 | 2,800 kcal | 3,100 kcal | 89 to 86 kg by December |
| 2 Base II (Dec to Feb) | 3,300 | 3,000 kcal | 3,300 kcal | 86 to 84 kg by March |
| 3 Strength / 10K (Mar to May) | 3,500 | 3,300 kcal | 3,600 kcal | 84 to 82 kg by May, then hold |
| 4 HM specific and taper (May to Aug) | 3,600 to 3,700 | 3,500 kcal | 3,800 kcal | Hold. No deficit in the last 12 weeks |

**Macros (per day, adjust as body weight drops)**

| | Rest / easy day | Key session day | Long run over 90 min (from week 20) | Race week |
|---|---|---|---|---|
| Protein | 160 g (1.8 g/kg), 4 meals of 40 g | 160 g | 160 g | 160 g |
| Carbohydrate | 350 g (4 g/kg) | 450 g (5 g/kg) | 530 g (6 g/kg) | 700 to 850 g (8 to 10 g/kg) from Thursday |
| Fat | 85 g (1 g/kg) | 85 g | 85 g | 70 g |

**Around runs**

- Easy run: 40 to 60 g carbs 60 to 90 min before (banana and toast, or oats). Morning easy runs under 60 min can be done on coffee and a banana.
- Key session or long run: full meal 2.5 to 3 h before with 100 to 150 g carbs, low fat and fibre.
- Runs over 75 min (Phase 2 onward): 30 to 60 g carbs per hour, starting at 30 min. Practise gels, dates or sports drink on every long run from Phase 3 so race-day fuelling is rehearsed.
- Within 60 min after a key session or long run: 30 to 40 g protein plus 60 to 80 g carbs (500 ml milk with oats and banana, or Quark with fruit and bread).
- Strength A or B: a meal with 40 g protein within 2 h.

**Fluids and salt:** about 3 l a day plus 500 ml per hour of running; in summer long runs add 500 to 1,000 mg sodium per hour (electrolyte tabs or salted food).

**Micronutrients:** vitamin D 1,000 to 2,000 IU per day from October to March. Calcium 1,000 mg a day from food (bone stress risk is higher at 89 kg on new mileage). Get ferritin, vitamin D and full blood count checked once in November and once in May; low ferritin is the most common reason a plan like this stalls.

**Sleep and HRV, which Oura will show you**

- Last large meal 3 h before bed; a small carb and protein snack is fine.
- Caffeine cut-off 14:00. Your median bedtime is 01:20 and late caffeine is the usual cause.
- Alcohol drops HRV and sleep score for one to two nights; keep it to one or two drinks a week and never the night before a key session or long run.

**Sample day, key-session day (about 3,100 kcal, 160 g protein, 450 g carbs)**

| When | Meal |
|---|---|
| Breakfast | 100 g oats with 300 ml milk, banana, 30 g whey or 200 g Quark, honey |
| Lunch | 150 g rice (dry), 180 g chicken or 250 g tofu, vegetables, olive oil |
| Pre-run (90 min before) | 2 slices toast with jam, or a banana and a bar |
| Post-run | 500 ml milk, 60 g oats, banana |
| Dinner | 300 g potatoes, 150 g fish or lean beef, salad, 200 g yoghurt with fruit |

Rest-day version: drop the pre-run and post-run items and halve the rice.

**Rules for the deficit:** weigh yourself weekly, morning average of three days. If readiness or HRV trends down for two weeks, sleep gets worse, or a key session fails twice, eat at maintenance for two weeks before resuming. Below 82 kg the deficit stops for good; the plan gains nothing from lighter than that.

## 11. Refreshing the data

Tokens last 30 days and refresh with `python3 oura/oauth.py refresh`. Re-run the baseline pull every 3 months and after each 5 km test, and update sections 1, 2, 3 and 5. If the VO2max endpoint becomes available, map it to the tiers: roughly 5K 33:00 ≈ 32, 27:30 ≈ 38, 25:15 ≈ 41.
