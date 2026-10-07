---
# Injury-caution follow-up 2026-10-07.
# The plantar-fascia half of "add, don't only subtract" (056 note 4), the
# foot analogue of 074 (shoulder) and 078 (knee). 055 already owns the
# pain-monitoring ceiling and the claim that loading, not rest, is the
# default for a familiar plantar-fascia ache; this row owns the DOSE of the
# heel-raise loading, where it sits in a lifter's week, what else in the
# week loads the same site (squats, calf work, impact), intrinsic-foot work,
# and footwear / inserts. Every treatment trial is in adults with
# ultrasound-verified plantar fasciopathy, mostly middle-aged, around
# BMI 26-27 and mostly not lifters; no trial in lifters was found, so every
# number here is a transported protocol, labelled as such.
#
# foot_rules is structured data for the composer. Each dose row keys to 056
# rungs; numbers are copied from the protocol named in `basis`, never
# derived. Rows marked basis_grade D are product judgement on top of those
# protocols.
#
# Numbering: claimed 080 provisionally; released as 088 in v41 (080-087
# were taken by v40 and the other v41 rows).
id: exercise/plantar-heel-pain-lifter-foot-rules-088
domain: exercise
grade: B (advice plus a heel cup plus load management is the base; heavy-slow heel raises are safe and matched or beat stretching, but added no clinically relevant benefit over that base in the largest trial; self-dosed and fixed progressions do equally well); C (orthoses give a small medium-term pain benefit, custom no better than prefabricated; isometrics give no extra immediate pain relief; intrinsic-foot training lowered running injuries in one trial; BMI, low ankle dorsiflexion and standing work are associations); D (placement in a lifter's week, squat and calf-work rules, lifting footwear)
lane: "@clinical-physio"
locale: universal
as_of: 2003-2023
contested: no
sources:
  - "https://blogs.bmj.com/bjsm/2014/09/15/plantar-fasciitis-important-new-research-by-michael-rathleff/"  # Rathleff MS, Mølgaard CM et al. 2015, Scand J Med Sci Sports 25(3):e292-e300 -- RCT n=48, ultrasound-verified plantar fasciitis (heel pain >= 3 months, fascia >= 4.0 mm; mean age 46, BMI median 27). Both arms: information leaflet + gel heel cup. Strength arm: single-leg heel raise on a step, towel under the toes so they are maximally dorsiflexed at the top, 3 s up / 2 s hold / 3 s down, every second day for 3 months; 3 x 12RM, after 2 weeks 4 x 10RM with a backpack of books, after 4 weeks 5 x 8RM, keep adding books; both legs if one leg cannot do the reps. Stretch arm: plantar-fascia stretch 10 x 10 s, 3 times a day. FFI 29 points better at 3 months (95% CI 6 to 52); 5-7 points, not significant, at 1, 6 and 12 months. Only adverse event: minor DOMS. Fascia thickness fell equally in both arms. Read at full text 2026-10-07
  - "https://vbn.aau.dk/ws/files/308027530/Riel_et_al._2019_Self_dosed_and_pre_determined_progressive_heavy_slow_resistance_training_have_similar_effects_in_people_with_plantar_fasciopathy.pdf"  # Riel H, Jensen MB, Olesen JL, Vicenzino B, Rathleff MS 2019, J Physiother 65(3):144-151 -- RCT n=70: standing heel raise, towel under toes, straight knee, 3 s / 2 s / 3 s, every second day (48 h between sessions), 2 min between sets, 12 weeks; self-dosed (as heavy as possible but no heavier than 8RM, as many sets as possible) vs fixed 12RM -> 10RM -> 8RM. FHSQ pain adjusted MD -6.9 (95% CI -15.5 to 1.7), not significant; improved 24/33 vs 20/32; sessions 36 vs 34 (self-dosing did not raise the dose); only 4 of 70 reached an acceptable symptom state at 12 weeks. Both arms: heel cup; told pain during the exercise is not tissue damage, any tolerable pain allowed; cut activity and rebuild by symptoms; activity that does not leave symptoms outlasting it is fine. Read at full text 2026-10-07
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC10579183"  # Riel H, Vicenzino B, ... Rathleff MS 2023, Br J Sports Med 57(18):1180-1186 (FIX-Heel) -- RCT n=180, ultrasound-confirmed plantar fasciopathy: advice (pathology, risk factors, load management; cut pain-aggravating activity, stay active) + silicone heel cup in all shoes (PA, n=62) vs PA + self-dosed heavy-slow heel raises every other day, as heavy as possible but no heavier than 8RM, as many sets as possible, 2 min rest, tolerable pain allowed, continued to a satisfactory result and then 4 more weeks (PAX, n=59) vs PAX + triamcinolone injection (PAXI, n=59). FHSQ pain at 12 weeks, MID 14.1: PAX vs PA -2.0 (p=0.63); PAXI vs PA -9.1 (p=0.02, below MID); no clinically relevant difference at any time to 52 weeks. Adherence 74% of prescribed sessions; session count not related to improvement. Read at full text (PMC) 2026-10-07
  - "https://vbn.aau.dk/ws/files/287166711/Riel_et_al_2018_Scandinavian_Journal_of_Medicine_26_Science_in_Sports.pdf"  # Riel H et al. 2018, Scand J Med Sci Sports 28(12):2643-2650 -- randomised crossover n=20, plantar fasciopathy: isometric heel-raise holds gave no larger immediate pain reduction than isotonic heel raises or walking; 3 of 20 had a clinically relevant reduction. Read at abstract
  - "https://pubmed.ncbi.nlm.nih.gov/38037331/"  # Koc TA Jr et al. 2023, J Orthop Sports Phys Ther 53(12):CPG1-CPG39 -- heel pain / plantar fasciitis CPG revision: resistance training for foot and ankle musculature recommended (B); orthoses as part of a combined plan, not as an isolated treatment; plantar-fascia and calf stretching, taping, manual therapy, night splints recommended. Full text not reachable (publisher 403, host DNS failure); grade letters read via two clinical summaries (physicaltherapyfirst.com, pplbiomechanics.com) that agree on resistance training B and disagree on the orthosis letter (B vs B/C), so no orthosis letter is carried
  - "https://bjsm.bmj.com/content/52/5/322"  # Whittaker GA, Munteanu SE, Menz HB, Tan JM, Rabusin CL, Landorf KB 2018, Br J Sports Med 52(5):322-329 -- 19 trials, 1,660 participants: orthoses vs sham at 7-12 weeks SMD -0.27 (95% CI -0.48 to -0.06) for pain, moderate quality, clinical importance uncertain; no function benefit; very low quality no effect short and longer term; custom = prefabricated at every time point; 89% of trials high risk of bias
  - "https://research.bond.edu.au/en/publications/strength-training-for-plantar-fasciitis-and-the-intrinsic-foot-mu/"  # Huffer D, Hing W, Newton R, Clair M 2017, Phys Ther Sport 24:44-52 -- systematic review, 7 studies: could not identify how far intrinsic-foot strengthening benefits symptomatic or at-risk people; low external validity. Read at abstract
  - "https://search.pedro.org.au/search-results/record-detail/62997"  # Taddei UT, Matias AB, Duarte M, Sacco ICN 2020, Am J Sports Med 48(14):3610-3619 -- single-blind RCT, 118 recreational runners (20-100 km/week): 8-week foot-core (intrinsic and extrinsic foot-ankle) programme then remote training; control group 2.42 times (95% CI 1.98 to 3.62) as likely to have a running-related injury over 12 months. All running injuries, not plantar-fascia specific. Read at abstract
  - "https://bjsm.bmj.com/content/50/16/972"  # van Leeuwen KDB, Rogers J, Winzenberg T, van Middelkoop M 2016, Br J Sports Med 50(16):972-981 -- 51 studies (46 case-control): BMI > 27 the only significant pooled clinical association, OR 3.7 (95% CI 2.93 to 5.62), strongest in non-athletes; thicker fascia and heel fat pad and subcalcaneal spurs on imaging. Read at abstract
  - "https://www.qxmd.com/r/12728038"  # Riddle DL, Pulisic M, Pidcoe P, Johnson RE 2003, J Bone Joint Surg Am 85(5):872-877 -- matched case-control (50 cases, 100 controls): ankle dorsiflexion <= 0 deg OR 23.3 (95% CI 4.3 to 124.4) vs > 10 deg; BMI > 30 OR 5.6 (1.9 to 16.6); most of the workday on the feet OR 3.6 (1.3 to 10.1). Association only. Read at record
  - "exercise/tendon-fascia-load-management-055"  # within-warehouse: the pain-monitoring ceiling and the "load, don't rest" default; Rathleff 2015's headline is cited there and its protocol detail here
  - "exercise/caution-severity-ladder-056"  # within-warehouse: the rungs every foot_rules dose row keys to; fascia tissue modifier
  - "exercise/injury-history-reinjury-risk-054"  # within-warehouse: why a recovered heel keeps prep
  - "exercise/cut-cardio-placement-rule-063"  # within-warehouse: stepmill / incline walking / running load the fascia; impact modes move off a caution site
  - "exercise/recovery-kinetics-session-spacing-025"  # within-warehouse: 48 h spacing in general
  - "exercise/harm-route-boundary-031"  # within-warehouse: red flags stay with pain-triage
  - "framework:GRADE -- treatment numbers rest on three RCTs from one Danish group (n=48, 70, 180) with ultrasound-confirmed cases; the largest found no added benefit of heel raises over advice + heel cup, so the heel-raise effect is downgraded to 'safe option, not a proven add-on'. Orthosis effect moderate quality, small. Intrinsic-foot evidence is one prevention RCT in runners plus a low-validity review. Risk factors are case-control. No trial in lifters; nothing tests squat, deadlift, calf-hypertrophy or lifting-shoe choices in plantar heel pain."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
foot_rules:
  dose:
    - context: baseline
      rungs: [no-caution, mild, history-old]
      trigger: none -- no foot-specific work is added for prevention in a lifter
      slot: none
      exercise: ordinary calf raises in the program, if any
      sets: program default
      reps: program default
      per_week_target: 0
      tempo: program default
      progression: program default
      pain_rule: none
      duration: none
      basis: no prevention trial of heel raises for plantar heel pain; Taddei 2020 foot-core programme is runners and all injuries
      basis_grade: D
      transport_grade: D
    - context: history
      rungs: [history-recent, history-unknown]
      trigger: a named plantar-fascia / heel-pain episode, recovered, inside 12 months or timing unknown
      slot: accessory, end of a lower-body session
      exercise: standing single-leg heel raise, forefoot on a step, towel under the toes
      sets: 3
      reps: 8-12 (a load the user could lift about 12 times, moving to about 8)
      per_week_target: 2
      tempo: 3 s up, 2 s hold, 3 s down
      progression: add load (dumbbell, belt, machine) when all sets reach the top of the range
      pain_rule: 055 ceiling; a flare moves the user to current-load-pain
      duration: ongoing while the history weight lasts (056)
      basis: Rathleff 2015 exercise at a maintenance dose; product judgement
      basis_grade: D
      transport_grade: D
    - context: current-load-pain
      rungs: [current-load-pain]
      trigger: familiar plantar heel pain in the user's words (first-step morning pain, pain after standing), no red flag, pain-triage has not flagged it
      slot: accessory, end of the session, or a short standalone session at home
      exercise: standing single-leg heel raise, forefoot on a step, rolled towel under the toes (toes fully bent up at the top), knee straight; both legs if one leg cannot reach the reps
      sets: weeks 1-2 3 x 12RM; weeks 3-4 4 x 10RM; week 5 on 5 x 8RM -- or self-dosed as many sets as possible at no heavier than 8RM; 2 min between sets
      reps: 12 -> 10 -> 8 (to a repetition maximum)
      per_week_target: 3-4 (every second day, at least 48 h apart)
      tempo: 3 s up, 2 s hold, 3 s down
      progression: add load (backpack, dumbbell, belt, smith or machine) as the RM target is beaten
      pain_rule: 055 ceiling (about 5/10 during and after, back to the usual level next morning, morning pain not rising week to week); breach -> lighter load or both legs next session
      duration: 12 weeks, then 4 weeks past a satisfactory result; review at 12 weeks
      base_always: advice on load management + a heel cup or insert in everyday shoes
      basis: Rathleff 2015 (fixed); Riel 2019 (self-dosed = fixed); Riel 2023 (no added benefit over the base at 12 weeks)
      basis_grade: B
      transport_grade: C
    - context: closed
      rungs: [current-other, red-flag]
      trigger: heel or foot pain that is not the familiar plantar picture, after trauma, with swelling, numbness or tingling, night or rest pain, or pain that is unknown
      slot: none
      exercise: none prescribed
      sets: 0
      reps: 0
      per_week_target: 0
      tempo: none
      progression: none
      pain_rule: pain-triage before any foot prescription
      duration: none
      basis: exercise/harm-route-boundary-031; exercise/caution-severity-ladder-056
      basis_grade: D
      transport_grade: D
  placement:
    - rule: the heel-raise protocol REPLACES the program's standing calf raise for the affected leg; it is not added on top
      basis_grade: D
      note: the protocol is a heavy standing calf raise; stacking a second calf exercise doubles the site's load with no trial behind it
    - rule: heel-raise days at least 48 h apart; no heavy calf work on the day after a heel-raise day
      basis_grade: C
      note: every-second-day / 48 h recovery in all three trials; 055 spacing note
    - rule: heel raises go after the main lifts, never before squats, deadlifts or lunges
      basis_grade: D
      note: no trial of placement; keeps the calf fresh for the main lifts and the heel raise at its full load
    - rule: no isometric heel-raise holds as a pre-session pain-relief step
      basis_grade: C
      note: Riel 2018 -- isometrics gave no more immediate pain relief than walking or isotonic heel raises
  week_load:
    - rule: squats, deadlifts, hip thrusts and leg press stay in the plan under the 055 ceiling; they are not removed for plantar heel pain
      basis_grade: D
      note: no trial of these lifts in plantar fasciopathy; feet stay flat and planted and the fascia is not the limiting tissue; the ceiling catches the exception
    - rule: cut first the activities that leave symptoms outlasting them -- running, jumping, jump rope, plyometrics, stepmill and long incline walking, long standing -- and rebuild them by symptoms
      basis_grade: B
      note: the load-management advice given to every arm of Riel 2019 and Riel 2023; 063 moves impact cardio off a caution site
    - rule: walking lunges, split squats and other loaded toe-off movements are swapped for a static or machine variant when they breach the ceiling
      basis_grade: D
      note: product judgement; toe dorsiflexion under load tensions the fascia (windlass) -- the same mechanism the heel-raise towel uses on purpose
    - rule: a calf-stretch (gastrocnemius / soleus) and plantar-fascia stretch may be added as daily home work; they do not replace the heel raise
      basis_grade: C
      note: CPG lists stretching; low ankle dorsiflexion is a case-control risk factor (Riddle 2003); stretching lost to heel raises at 3 months (Rathleff 2015)
  footwear:
    - rule: during current-load-pain, a heel cup or prefabricated insert in everyday shoes is part of the base; custom orthoses are not needed
      basis_grade: C
      note: heel cup in all three trials; orthoses small medium-term pain effect, custom = prefabricated (Whittaker 2018); not an isolated treatment (CPG)
    - rule: in the gym the user keeps their usual lifting shoe; the engine does not recommend switching to barefoot, minimalist or heeled lifting shoes for plantar heel pain
      basis_grade: D
      note: no study of lifting footwear in plantar heel pain (GAPS.md)
    - rule: do not tell the user the insert or shoe fixes the cause
      basis_grade: C
      note: orthoses gave a small pain change only at 7-12 weeks, no function change
  intrinsic:
    - rule: intrinsic-foot drills (short foot, toe spread, toe curl against a band, toe yoga) are an optional add-on of 1-2 drills, 2-3 x 10-15, in the warm-up or at home; never a substitute for the heel raise
      basis_grade: D
      note: CPG recommends resistance training of foot and ankle muscles; Huffer 2017 could not show benefit of intrinsic work in plantar fasciitis; the dose is product judgement
    - rule: for a user who runs, the foot-core programme is a reasonable prevention add-on
      basis_grade: C
      note: Taddei 2020, one RCT in recreational runners, all running injuries
refraction_notes:
  - note: >
      THE BASE IS ADVICE, A HEEL CUP AND LOAD MANAGEMENT. In the largest
      trial (180 people with ultrasound-confirmed plantar fasciopathy),
      adding heavy-slow heel raises to advice plus a heel cup made no
      clinically relevant difference at 12 weeks or a year, and adding an
      injection made only a small one. The heel raise remains a safe way to
      keep loading the site and beat stretching at 3 months in an earlier
      trial, but the engine speaks it as "a good way to keep training the
      foot", never as "this is what fixes it".
    grade: B
  - note: >
      THE DOSE THAT WAS TESTED. Single-leg heel raise on a step with a
      rolled towel under the toes, 3 s up, 2 s hold, 3 s down, every second
      day: 3 x 12RM for two weeks, 4 x 10RM for two weeks, then 5 x 8RM,
      adding load in a backpack. Letting people pick their own sets at no
      heavier than 8RM did just as well and did not raise how much they
      did. These were middle-aged, mostly non-lifting adults; the protocol
      transports to a lifter as a heavy standing calf raise, which is why it
      replaces the program's calf raise rather than adding to it.
    grade: B
  - note: >
      SET THE CLOCK HONESTLY. Plantar fasciopathy is slow. In one trial only
      4 of 70 people felt they needed no further treatment after 12 weeks of
      heel raises, and in the heel-raise trials most still had a thickened
      fascia when symptoms had eased. The engine reviews at 12 weeks and
      expects improvement, not resolution, by then.
    grade: B
  - note: >
      WHAT TO CUT, WHAT TO KEEP. The trials cut activity that left
      symptoms lasting beyond it and rebuilt it by symptoms; they did not
      stop people training. For a lifter that means running, jumping, rope,
      stepmill and long standing come down first. Squats, deadlifts and leg
      press stay under the pain ceiling; nothing tests them in this
      condition, and the feet are planted and flat. Loaded toe-off moves
      (walking lunges) are swapped if they breach the ceiling.
    grade: D
  - note: >
      INSERTS AND SHOES HELP A LITTLE, FOR A WHILE. Orthoses lowered pain a
      little versus sham inserts at 7-12 weeks and not before or after;
      custom were no better than off-the-shelf. A heel cup was part of every
      trial's base. No study looks at lifting shoes, barefoot lifting or
      minimalist shoes in plantar heel pain, so the engine leaves the user's
      lifting shoe alone.
    grade: C
  - note: >
      FOOT-MUSCLE DRILLS ARE OPTIONAL. Guideline panels recommend
      strengthening the foot and ankle muscles, but a review could not show
      that intrinsic-foot work helps plantar heel pain itself. One trial in
      runners found a foot-core programme cut running injuries over a year.
      Offer short-foot and toe drills as an add-on, never instead of the
      heel raise.
    grade: C
  - note: >
      RISK FACTORS ARE ASSOCIATIONS. Higher BMI (above 27, strongest in
      non-athletes), ankle dorsiflexion at or below neutral and a workday
      mostly on the feet are linked to plantar fasciitis in case-control
      studies. They explain, they do not diagnose, and the engine does not
      name body weight as the cause to a user who did not raise it.
    grade: C
  - note: >
      WHAT THIS ROW DOES NOT LICENSE. Heel pain after a fall or jump,
      swelling or bruising, numbness, burning or tingling in the sole, pain
      at rest or at night, pain in both heels with other joint symptoms, or
      pain that keeps rising are not the familiar plantar picture. They go
      to the pain-triage skill first (031).
    grade: D
claim: >
  For a lifter with familiar plantar heel pain (first-step morning pain,
  pain after standing, no red flags), the base is advice on load
  management plus a heel cup or insert; keep lifting under the 055 pain
  ceiling. A heavy-slow single-leg heel raise (step, towel under the toes,
  3 s up / 2 s hold / 3 s down, every second day, 12RM to 8RM over five
  weeks, or self-dosed at no heavier than 8RM) is the tested loading: safe,
  better than stretching at 3 months, but no better than the base alone in
  the largest trial. It replaces the program's calf raise, sits after the
  main lifts, and heel-raise days stay 48 h apart. Running, jumping,
  stepmill and long standing come down first; squats and deadlifts stay.
  Expect improvement, not resolution, by 12 weeks. Inserts give a small,
  temporary pain benefit, custom no better than off-the-shelf. Intrinsic
  foot drills are optional. Lifting footwear is untested.
reasoning: >
  Rathleff 2015 was read at full text for the protocol; Riel 2019 at full
  text for the self-dosed equivalence, the 48 h spacing, the 2 min rests,
  the advice given to both arms and the low acceptable-symptom-state rate;
  Riel 2023 at full text for the null add-on result, which is the most
  important correction to the common "heel raises cure plantar fasciitis"
  copy and keeps the heel-raise letter from rising above "safe option".
  Whittaker 2018 supplies the orthosis size and custom = prefabricated.
  The CPG could not be read at full text, so only the letter both secondary
  summaries agree on is carried. Intrinsic work rests on one runner
  prevention trial and a review that found nothing usable for treatment, so
  its dose is product judgement. Every lifter-specific rule (replace the
  calf raise, place after main lifts, keep squats, keep the lifting shoe)
  has no trial and stays at the practitioner floor. The axis is hard with
  block_specifics because the rung (familiar plantar picture vs red flag or
  unknown heel pain) decides whether any dose is given at all.
---

# exercise/plantar-heel-pain-lifter-foot-rules-088 -- 족저근막(발뒤꿈치) 통증이 있는 사람의 카프레이즈·발 운동·신발

**한 줄 그림:** 발뒤꿈치가 아파도 운동은 계속한다. 기본은 생활 속 부하 조절과 힐컵이고, 무겁고 천천히
하는 한발 카프레이즈는 이틀에 한 번 기존 카프레이즈 자리에 넣는다. 12주 안에 다 낫길 기대하진 않는다.

## Dose by rung (engine-readable copy of `foot_rules.dose`)

| Context (056 rungs) | Slot | Exercise | Sets x reps | Per week | Basis |
|---|---|---|---|---|---|
| baseline (no caution, mild, history-old) | none | program's calf raise as is | program default | -- | no prevention trial |
| history (recent, unknown) | end of lower-body day | single-leg heel raise, step + towel | 3 x 8-12, 3-2-3 s tempo | 2 | product judgement |
| current-load-pain (familiar plantar picture) | end of session or home | single-leg heel raise, step + towel, knee straight | 3 x 12RM -> 4 x 10RM -> 5 x 8RM, or self-dosed <= 8RM; 2 min rest | 3-4 (every 2nd day) | Rathleff 2015; Riel 2019; Riel 2023 |
| closed (current-other, red-flag) | none | -- | -- | -- | pain-triage (031) |

Always with current-load-pain: load-management advice and a heel cup or insert in everyday shoes.
Review at 12 weeks; continue 4 weeks past a satisfactory result.

## Week and placement rules

| Rule | Basis |
|---|---|
| Heel raise replaces the program's standing calf raise, not added on top | product judgement |
| Heel-raise days 48 h apart; no heavy calf work the next day | trial design (all three) |
| Heel raise after the main lifts, never before squats / deadlifts / lunges | product judgement |
| No isometric holds as pre-session pain relief | Riel 2018 crossover |
| Running, jumping, rope, stepmill, long standing come down first | trial advice |
| Squats, deadlifts, leg press, hip thrust stay under the 055 ceiling | no trial |
| Walking lunges / loaded toe-off swapped if they breach the ceiling | product judgement |
| Calf and plantar stretching as optional daily home work | CPG; Riddle 2003 association |
| Usual lifting shoe kept; no switch to barefoot / minimalist / heeled | no study |
| Intrinsic-foot drills optional, 1-2 drills, 2-3 x 10-15 | review found no treatment effect; runner prevention trial |

## Evidence vs folklore

| Claim | State |
|---|---|
| Heavy slow heel raises beat stretching at 3 months | One small RCT; gone by 6 months |
| Heel raises add benefit to advice plus a heel cup | Not in the largest RCT (n=180) |
| Following a fixed 12RM -> 8RM plan matters | Self-dosed did equally well |
| Most people are fine after 12 weeks | 4 of 70 reached an acceptable state |
| Isometric holds kill heel pain before training | No more than walking |
| Custom orthoses beat off-the-shelf | No difference in a meta-analysis |
| Inserts fix the cause | Small pain change at 7-12 weeks only |
| Short-foot drills treat plantar fasciitis | Not shown; one runner prevention trial |
| Stop squatting until the heel settles | No trial; the trials kept people active |
| Barefoot or minimalist lifting fixes the foot | No study |

## 한국어 요약 (답변용)

- 아침 첫걸음에 발뒤꿈치가 찌릿하고, 오래 서 있으면 아픈 익숙한 족저근막 통증이고 위험 신호가 없으면:
  운동을 멈추지 않는다. 통증 기준(055: 운동 중·후 10점 중 5점까지, 다음 날 아침 평소 수준으로 돌아옴,
  아침 통증이 주마다 늘지 않음) 안에서 한다.
- 기본은 생활 속 부하 조절과 힐컵(실리콘 뒤꿈치 패드)이다. 가장 큰 연구(180명)에서 이 기본에
  카프레이즈를 더해도 12주·1년 결과가 의미 있게 나아지지 않았다. 그래서 카프레이즈는 "발을 계속
  단련하는 안전한 방법"으로 말하고, "이걸 해야 낫는다"고 말하지 않는다.
- 연구에서 쓴 방법: 계단 끝에 앞발을 올리고 발가락 밑에 수건을 말아 넣어 발가락이 위로 꺾이게 한 뒤,
  무릎을 편 채 한 발로 뒤꿈치를 든다. 3초 올리고, 2초 멈추고, 3초 내린다. 이틀에 한 번. 처음 2주는
  12번 겨우 하는 무게로 3세트, 다음 2주는 10번 무게로 4세트, 그 뒤로는 8번 무게로 5세트. 배낭에 무게를
  넣어 올린다. 세트를 스스로 정해도(8번 무게보다 무겁지 않게, 할 수 있는 만큼) 결과는 같았다. 세트 사이
  2분 쉰다. 한 발로 안 되면 두 발로 시작한다.
- 헬스장에서는 이 운동이 원래 프로그램의 서서 하는 카프레이즈를 대신한다. 위에 하나 더 얹지 않는다.
  메인 운동(스쿼트·데드리프트·런지)이 끝난 뒤에 하고, 카프레이즈 하는 날은 48시간 띄운다. 운동 전에
  버티기(아이소메트릭) 자세로 통증을 줄이려는 건 걷기보다 낫지 않았다.
- 먼저 줄일 것: 달리기, 점프, 줄넘기, 천국의 계단(스텝밀), 오래 경사 걷기, 오래 서 있기처럼 끝난 뒤에도
  통증이 남는 활동. 스쿼트·데드리프트·레그프레스는 통증 기준 안에서 그대로 둔다. 이 상태에서 이 운동들을
  시험한 연구는 없지만, 연구 참가자들도 활동을 끊지 않았다. 걸으며 하는 런지처럼 발가락으로 밀어내는
  동작은 기준을 넘으면 제자리·머신 동작으로 바꾼다.
- 기간: 천천히 낫는다. 12주 운동 뒤에도 "더 치료가 필요 없다"고 느낀 사람은 70명 중 4명이었다.
  12주에 다시 보고, 그때는 "좋아지는 중"을 기대한다.
- 깔창·신발: 평소 신발에 힐컵이나 기성 깔창을 넣는 건 기본에 포함된다. 깔창은 7~12주 사이에 통증을
  조금 줄였고, 맞춤 깔창이 기성품보다 낫지 않았다. 원인을 고친다고 말하지 않는다. 헬스장에서 신는 신발은
  바꾸라고 하지 않는다. 맨발·얇은 신발·역도화가 발뒤꿈치 통증에 좋은지 본 연구가 없다.
- 발바닥 작은 근육 운동(숏풋, 발가락 벌리기, 밴드 걸고 발가락 구부리기)은 선택이다. 1~2개, 2~3세트
  10~15회를 워밍업이나 집에서. 족저근막 통증을 낫게 한다는 근거는 없고, 달리기 하는 사람에게서 부상을
  줄였다는 연구가 하나 있다. 카프레이즈 대신으로 쓰지 않는다. 종아리·발바닥 스트레칭도 집에서 더할 수
  있지만 카프레이즈를 대신하지 않는다.
- 위험 요인(체중이 많이 나감, 발목이 잘 안 굽혀짐, 하루 종일 서서 일함)은 연관일 뿐이다. 사용자가 먼저
  꺼내지 않았으면 체중을 원인으로 말하지 않는다.
- 넘어지거나 뛰어내린 뒤 아픈 뒤꿈치, 붓기·멍, 발바닥 저림·화끈거림, 쉬거나 밤에도 아픈 통증, 다른
  관절 증상과 함께 양쪽 뒤꿈치가 아픈 경우, 계속 심해지는 통증은 여기 해당하지 않는다. 먼저 통증
  확인(pain-triage)으로 보낸다.
