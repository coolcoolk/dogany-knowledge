---
# NEAT / daily-activity sprint 2026-10-08.
# The engine-readable rule set for the goal consult's calorie step (and the
# diet card / weekly retro that revisit it): which activity number to use,
# how to ask about the job, how to show a starting maintenance range, when
# the weight trend takes over, and what never to do with watch kcal. It is a
# routing rule over 750, not a primary finding: each rule names the graded
# row it rests on, and every product constant is labelled as one. Same
# posture as nutrition/adherence-rules-074 and the sodium_rules of 716.
#
# neat_rules is structured data (same field shape as 716's sodium_rules:
# rule / surface / trigger / action / never / constants / basis / basis_grade
# / kind). pal_bands and activity_sources are lookup tables for the same
# step. The YAML-subset reader returns every scalar as a string; flow lists
# parse natively. No program code changed.
#
# NOT SET HERE: the resting-energy estimate the bands multiply. The warehouse
# holds no graded resting metabolic rate equation (GAPS); the engine's
# existing estimate is used as given and labelled an estimate.
id: nutrition/neat-rules-751
domain: nutrition
lane: "@meal-craft"
grade: D (synthesis rule over 750 and the weight-reading rules; each rule carries its own basis grade; the PAL band cut points, step thresholds, recalibration timing and adjustment caps are product judgement)
locale: universal
as_of: 2026
contested: no
sources:
  - "nutrition/neat-estimation-watch-steps-evidence-750"  # the evidence row: watch kcal inaccurate (no brand accurate, Apple MAPE about 28%), steps within about 10%, no brand correction, NEAT varies and falls on a diet, self-report overstates, Korean PACT within 10% for about 55-59%, steps arithmetic 0.3-0.6 kcal/kg per 1000 steps
  - "https://www.fao.org/4/Y5686E/y5686e07.htm"  # FAO/WHO/UNU 2004 PAL lifestyle bands 1.40-1.69 / 1.70-1.99 / 2.00-2.40, with office work, construction, non-mechanised farm labour as anchors; above 2.40 hard to sustain
  - "nutrition/body-measure-reading-rules-029"  # confirmed-trend and one-device rules any recalibration must pass
  - "nutrition/self-report-underreporting-007"  # logged intake is a floor; a back-calculated maintenance is in logged-kcal units
  - "nutrition/unlogged-day-not-zero-019"  # an unlogged day is unknown, so it cannot enter the intake mean as zero
  - "nutrition/weekend-drift-073"  # compare like days; the weekly mean is the unit
  - "nutrition/weight-loss-rate-lean-mass-012"  # the weekly-rate band a target is checked against (its provenance caveat travels with it)
  - "nutrition/energy-availability-threshold-010"  # the floor check: an activity estimate never justifies a very low intake
  - "nutrition/adherence-rules-074"  # break weeks are not judged against the loss target; recalibration skips them
  - "source:exercise/stepmill-cardio-slot-rules-095 -- no-eat-back for exercise sessions; this item extends the same rule to the watch's all-day active kcal"
  - "framework:GRADE -- each rule's basis_grade is the grade of the row it routes from; the band cut points (5000 / 10000 steps, +0.1 PAL for 5 h/week of sport), the 14-day / 10-logged-day window, the 7700 kcal/kg conversion convention, the 20 percent step-drop flag and the 200 kcal adjustment cap are product constants with no direct evidence."
applicability:
  axes:
    - key: activity_level
      type: categorical
      role: soft
      unknown_policy: ask
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: ask
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [not_pregnant, none]
activity_sources:
  # priority order for the activity term of maintenance; first available wins
  - source: weight_trend_vs_log
    when: at least 14 days since the target was set, at least 10 complete logged days in the window, two confirmed weight readings per 029, no declared break week in the window
    use: recalibrate maintenance in logged-kcal units
    basis_grade: C
  - source: job_and_steps_band
    when: goal consult, or no qualifying trend window yet
    use: starting PAL band from pal_bands
    basis_grade: D
  - source: step_count_weekly_mean
    when: phone or watch steps available from one device
    use: places the user inside the band; later a relative NEAT signal
    basis_grade: B
  - source: watch_active_kcal
    when: never for the target
    use: same-device weekly trend display only, if the user asks
    basis_grade: B
pal_bands:
  # PAL = total daily energy / resting energy. Starting bands only; lifting sessions are inside the band.
  - band: desk_low_steps
    job: seated most of the working day (office, driving, desk study)
    steps_weekly_mean: under 5000
    pal_low: 1.40
    pal_high: 1.50
  - band: desk_mid_steps
    job: seated most of the day
    steps_weekly_mean: 5000 to 9999
    pal_low: 1.50
    pal_high: 1.65
  - band: on_feet
    job: standing and walking most of the day (retail, service, teaching, nursing, kitchen), or seated job with 10000 or more steps
    steps_weekly_mean: any
    pal_low: 1.65
    pal_high: 1.85
  - band: manual
    job: heavy physical work most of the day (construction, logistics loading, farm labour)
    steps_weekly_mean: any
    pal_low: 1.85
    pal_high: 2.10
  - band: modifier_sport_volume
    job: any
    steps_weekly_mean: any
    pal_low: 0.10    # added to both ends only when the user does 5 or more hours a week of cardio or sport outside lifting
    pal_high: 0.10
  - band: cap
    job: any
    steps_weekly_mean: any
    pal_low: 2.40    # never exceed; FAO notes PAL above 2.40 is hard to sustain
    pal_high: 2.40
neat_rules:
  - rule: ask-job-not-self-rating
    surface: goal_consult
    trigger: the calorie step runs and activity_level is unknown or older than its volatility window
    action: ask what the work day physically involves (mostly seated / on feet / heavy physical) and, if a phone or watch is used, the usual daily steps over the last week; map to pal_bands; do not ask the user to rate how active they are
    never: ["얼마나 활동적이세요? (1~5)", 활동 수준 자기평가 척도]
    constants: two questions at most
    basis: 750 (self-report overstates activity; IPAQ-SF by 84 percent on average)
    basis_grade: B
    kind: evidence
  - rule: unknown-activity-baseline
    surface: goal_consult
    trigger: the user skips or refuses the activity questions
    action: answer first with the desk_mid_steps band and say it is a starting guess that the weight trend will correct; ask at most once more later
    never: [refusing to give a starting estimate, the manual band as a default]
    constants: desk_mid_steps as the stated baseline
    basis: 750 (over-estimation is the common error); refraction Need protocol
    basis_grade: D
    kind: convention
  - rule: show-range-not-point
    surface: goal_consult
    trigger: a starting maintenance is shown
    action: show maintenance as resting estimate x pal_low to resting estimate x pal_high, each rounded to 50 kcal, labelled 시작 추정 (starting estimate); the target is set from the middle of the range
    never: [a single kcal maintenance figure as fact, "정확한 유지 칼로리는 N kcal"]
    constants: round to 50 kcal
    basis: 750 (Korean activity table within 10 percent of DLW for only about 55-59 percent of adults)
    basis_grade: C
    kind: evidence
  - rule: lifting-inside-the-band
    surface: goal_consult
    trigger: the user lifts or does other structured training
    action: do not add session kcal on top of the band; lifting 3-6 times a week stays inside the band; add the modifier_sport_volume only for 5 or more hours a week of cardio or sport
    never: [adding the watch workout kcal, adding a per-session estimate on top of the band]
    constants: modifier +0.10 PAL at 5 h/week
    basis: FAO 2004 (bands describe whole lifestyles, exercise included); 750 (watch reads lifting about double)
    basis_grade: D
    kind: convention
  - rule: watch-kcal-not-in-target
    surface: both
    trigger: the user offers a watch "active kcal" or "total kcal" figure, or asks to eat back watch calories
    action: say the watch's step count and heart rate are useful, its calorie figure is not accurate enough to set or top up a food target (no brand was accurate; errors of about 28 percent and in either direction); the target comes from the band and then the weight trend
    never: [adding watch active kcal to the day's budget, using watch total kcal as maintenance, "워치가 500 kcal 태웠다니 500 kcal 더 드셔도 돼요"]
    constants: none
    basis: 750 (Fuller 2020; Choe 2025); exercise 095 no-eat-back
    basis_grade: B
    kind: evidence
  - rule: no-brand-correction
    surface: both
    trigger: the user asks whether their Apple Watch, Galaxy Watch, Garmin or other device over- or under-counts, or asks for a correction
    action: say the direction differs by device model, activity and body size, so the app applies no correction; if they want to use the number, use it only against itself week to week on the same device
    never: ["애플워치는 20% 빼세요", "갤럭시워치가 제일 정확해요", a brand ranking]
    constants: none
    basis: 750 (Kostrna 2026, Ferreira 2026, Lee 2026, Murakami 2019 disagree in sign)
    basis_grade: C
    kind: evidence
  - rule: watch-lifting-kcal
    surface: both
    trigger: the user quotes a watch kcal figure for a weight-training session
    action: say that in a 2026 test on Korean men the Apple, Galaxy and Garmin watches read lifting at about twice the calorimeter; the session matters for muscle, not for the food target
    never: [the watch session kcal as burned calories]
    constants: none
    basis: 750 (Lee 2026, tables)
    basis_grade: C
    kind: evidence
  - rule: steps-places-in-band
    surface: goal_consult
    trigger: a weekly step mean from one device is available
    action: use it with the job answer to choose the band; use the weekly mean, not a single day
    never: [a single day's steps, mixing phone and watch counts]
    constants: band cut points 5000 and 10000 steps
    basis: 750 (steps within about 10 percent); 029 one-device-only
    basis_grade: B
    kind: evidence
  - rule: steps-to-kcal-question
    surface: both
    trigger: the user asks how many kcal walking more, or N extra steps, is worth
    action: answer with the RESCALE range from 750 (0.3-0.6 kcal per kg per 1000 steps above rest x body_weight_kg), say "about" and that people partly compensate; do not raise the food target for planned extra steps
    never: [an unranged kcal figure per step, "만 보 걸으면 500 kcal"]
    constants: none (range from 750 steps_to_kcal)
    basis: 750 steps_to_kcal (derived arithmetic)
    basis_grade: D
    kind: convention
  - rule: recalibrate-from-trend
    surface: weekly_retro
    trigger: the activity_sources weight_trend_vs_log window is met
    action: logged maintenance = mean logged kcal over complete logged days + (confirmed weekly weight change in kg x 7700 / 7); compare with the current target; propose one change toward it, capped, and say it is in the user's own logged units
    never: [counting unlogged days as zero, recalibrating on unconfirmed or single readings, recalibrating across a declared break week, calling the result the user's true metabolism]
    constants: window 14 days, 10 complete logged days; 7700 kcal per kg conversion (convention; early-diet weight change carries water and glycogen, so the first 7 days of a new deficit are excluded); one proposal per 14 days, at most 200 kcal per change
    basis: 750 (weight trend integrates true expenditure; Hall 2011 slow, adapting response); 007; 019; 029; 074
    basis_grade: C
    kind: evidence
  - rule: logged-units
    surface: both
    trigger: a recalibrated maintenance is shown
    action: call it 내 기록 기준 유지 칼로리 (maintenance in your logged kcal); it already absorbs the user's usual under-logging, so it is the right number to aim the log at, not a measurement of intake
    never: ["실제 대사량은 N kcal", a true-TDEE claim]
    constants: none
    basis: 007 (logged intake under-reports, differentially)
    basis_grade: C
    kind: evidence
  - rule: neat-drop-signal
    surface: weekly_retro
    trigger: on a deficit, the weekly step mean falls 20 percent or more below the mean of the first 2 weeks of the cut, from the same device
    action: mention it once in the user's own numbers as a likely part of slower loss; suggest holding the step level before cutting food further
    never: ["대사가 망가졌어요", "metabolic damage", a kcal figure for the drop]
    constants: 20 percent drop flag; reference = first 2 weeks of the cut
    basis: 750 (activity falls under calorie restriction, Redman 2009; NEAT varies by hundreds of kcal, Levine 1999 / 2005)
    basis_grade: C
    kind: evidence
  - rule: maintenance-drifts-down
    surface: weekly_retro
    trigger: the user asks why loss slowed at the same intake, or the recalibrated maintenance is below the starting range
    action: say expenditure falls as weight falls and as daily movement drops on a diet, so maintenance moves down during a cut; the trend-based number replaces the starting one
    never: [blaming the user, "starvation mode", promising the start number still holds]
    constants: none
    basis: 750 (Redman 2009; Hall 2011)
    basis_grade: C
    kind: evidence
  - rule: floor-check
    surface: goal_consult
    trigger: a proposed target, after any activity estimate, falls below the resting estimate, or the user asks to subtract extra for activity they are unsure of
    action: do not go below the resting estimate on the strength of an activity guess; route deficit size through 012 and energy availability through 010
    never: [a target below the resting estimate justified by watch or step numbers]
    constants: resting estimate as the floor (convention)
    basis: 010; 012
    basis_grade: D
    kind: convention
  - rule: pregnancy-defers
    surface: goal_consult
    trigger: pregnancy_status is pregnant, breastfeeding, or unknown for a user who could be pregnant
    action: no deficit target and no activity-based kcal number; say energy needs in pregnancy and breastfeeding are set with a clinician or dietitian
    never: [a deficit target, a kcal number]
    constants: none
    basis: convention; pregnancy_status block_specifics
    basis_grade: D
    kind: convention
refraction_notes:
  - axis: activity_level
    note: >
      ACTIVITY UNKNOWN -> the desk_mid_steps band is spoken as a starting
      guess, the questions are asked once, and the weight trend corrects it
      from day 14. Unknown never blocks the calorie step.
    grade: D
  - axis: pregnancy_status
    note: >
      PREGNANCY UNKNOWN for a user who could be pregnant -> no deficit target or
      kcal number (block_specifics); general information still given.
    grade: D
  - note: >
      THE ORDER IS THE RULE. Weight trend against the log beats the job band,
      the job band plus steps beats a self-rating, and the watch calorie figure
      is never an input. Every number shown before day 14 is a starting
      estimate and is labelled as one.
    grade: C
claim: >
  The goal consult's calorie step takes its activity term in a fixed order.
  At the start it asks what the work day physically involves and the usual
  weekly step mean from one device, maps them to a PAL band (desk under 5000
  steps 1.40-1.50, desk 5000-9999 1.50-1.65, on feet 1.65-1.85, heavy manual
  1.85-2.10, plus 0.10 only for 5 or more hours a week of sport; lifting sits
  inside the band), and shows maintenance as a rounded range labelled a
  starting estimate. It never adds watch active kcal to the target, applies
  no brand correction, and answers "how much is walking worth" only with a
  ranged per-kg figure. From day 14, with enough logged days and a confirmed
  weight trend, maintenance is recalibrated from the trend in the user's own
  logged units, one capped change at a time; a falling step mean on a cut is
  named as a likely part of slowing loss. Band cut points, windows and caps
  are product constants.
reasoning: >
  750 settles which number is least wrong; this item turns that into a
  deterministic calorie step. The bands borrow the FAO lifestyle anchors and
  split the sedentary range by steps because desk workers are the common user
  and the place where a step mean adds most; the cut points and the sport
  modifier are judgement and say so. The weight-trend recalibration is the
  only route that integrates real expenditure, so it overrides the band as
  soon as the data allow, but it inherits three warehouse limits stated on
  their own items: logged intake is low (007), unlogged days are unknown
  (019), and single weigh-ins are noise (029). The 7700 kcal/kg conversion is
  a convention used over a short window with the first week of a new deficit
  excluded; Hall 2011 is why it is not used for long-range prediction. The
  pregnancy hard gate follows the warehouse's own flagged decision (GAPS
  nutrition item 7) for a calorie-target surface, where it is less arguable
  than on general deficit advice.
---

# nutrition/neat-rules-751 -- 목표 칼로리의 활동량 단계 규칙 (neat_rules)

**One line:** 직업과 걸음 수로 시작 범위를 잡고, 14일 뒤부터는 체중 추세가 정한다. 워치 칼로리는 넣지 않는다.

| Band | Job | Steps (weekly mean) | PAL |
|---|---|---|---|
| desk_low_steps | mostly seated | < 5,000 | 1.40-1.50 |
| desk_mid_steps | mostly seated | 5,000-9,999 | 1.50-1.65 |
| on_feet | standing / walking, or seated + ≥ 10,000 steps | any | 1.65-1.85 |
| manual | heavy physical work | any | 1.85-2.10 |
| + sport | ≥ 5 h/week cardio or sport (not lifting) | — | +0.10 |

| Rule | Surface | Trigger | Action |
|---|---|---|---|
| ask-job-not-self-rating | goal consult | activity unknown | job + weekly steps, no 1-5 rating |
| unknown-activity-baseline | goal consult | questions skipped | desk_mid_steps as a starting guess |
| show-range-not-point | goal consult | maintenance shown | range, 50 kcal rounding, "시작 추정" |
| lifting-inside-the-band | goal consult | user lifts | no session kcal on top |
| watch-kcal-not-in-target | both | watch kcal offered | not an input; no eat-back |
| no-brand-correction | both | "does my watch over-count?" | direction varies; no correction |
| watch-lifting-kcal | both | watch kcal for lifting | about double in a 2026 test |
| steps-places-in-band | goal consult | weekly steps known | weekly mean, one device |
| steps-to-kcal-question | both | "what are N steps worth?" | 0.3-0.6 kcal/kg per 1000 steps, ranged |
| recalibrate-from-trend | weekly retro | 14 days, 10 logged days, confirmed trend | logged maintenance; ≤ 200 kcal change |
| logged-units | both | recalibrated number shown | "내 기록 기준" |
| neat-drop-signal | weekly retro | steps −20% on a cut | hold steps before cutting food |
| maintenance-drifts-down | weekly retro | loss slowed | maintenance falls on a cut |
| floor-check | goal consult | target below resting estimate | not on an activity guess; 010 / 012 |
| pregnancy-defers | goal consult | pregnant / breastfeeding / unknown | no deficit, no kcal number |

## 한국어 요약 (답변용)

- 목표 칼로리를 정할 때 "얼마나 활동적이세요?"라고 점수로 묻지 않는다. 대신 하루 일이 주로 앉아서
  하는 일인지, 서서 걷는 일인지, 몸을 많이 쓰는 일인지와, 휴대폰이나 워치에 찍힌 최근 일주일 평균
  걸음 수를 묻는다.
- 이 답으로 시작 범위를 잡는다. 앉아서 일하고 5,000보 미만이면 휴식 대사량의 약 1.4~1.5배, 앉아서
  일하고 5,000~9,999보면 1.5~1.65배, 서서 일하거나 만 보 이상이면 1.65~1.85배, 육체노동이면 1.85~2.1배다.
  헬스는 이 범위 안에 이미 들어 있고, 유산소나 운동 경기를 주 5시간 이상 할 때만 0.1을 더한다.
  이 기준선은 앱이 정한 값이다.
- 유지 칼로리는 하나의 숫자가 아니라 50 kcal 단위로 반올림한 범위로 보여 주고 '시작 추정'이라고
  적는다. 답을 안 하면 '앉아서 일하고 5,000~9,999보' 범위로 일단 시작한다.
- 워치의 활동 칼로리는 목표에 더하지 않는다. 워치 칼로리만큼 더 먹으라고 하지 않고, "애플워치는 몇 %
  빼세요" 같은 보정도 하지 않는다. 근력운동 칼로리는 2026년 한국 남성 연구에서 워치가 실제의 약 두
  배로 계산했다.
- "만 보 더 걸으면 몇 kcal?"에는 체중 1 kg당 1,000보에 0.3~0.6 kcal(휴식 대비 추가분) 범위로 답한다.
  70 kg이면 만 보에 약 210~420 kcal지만 어림셈이고, 사람은 일부를 먹어서 채우는 경향이 있다.
- 14일이 지나고 기록이 꼬박 채워진 날이 10일 이상이며 체중 추세가 확인되면, 체중 추세와 기록으로
  유지 칼로리를 다시 계산한다(체중 1 kg = 7,700 kcal로 환산하는 관례, 새 감량의 첫 7일은 제외). 한 번에
  200 kcal 이내로, 14일에 한 번만 바꾸자고 제안한다. 이 숫자는 '내 기록 기준 유지 칼로리'다.
- 감량 중 주 평균 걸음 수가 처음 2주보다 20% 이상 줄면, 감량이 느려진 이유일 수 있다고 한 번 말하고
  음식을 더 줄이기 전에 걸음 수를 먼저 지키자고 제안한다. "대사가 망가졌다"는 말은 쓰지 않는다.
- 활동량 추정을 근거로 휴식 대사량 아래로 목표를 내리지 않는다. 임신 중이거나 수유 중이면(또는 모르면)
  감량 목표나 칼로리 숫자를 주지 않고 의료진과 정하도록 안내한다.
