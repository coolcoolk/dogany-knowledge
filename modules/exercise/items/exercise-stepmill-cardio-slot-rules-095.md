---
# Stepmill-in-a-cut sprint 2026-10-07.
# The engine-readable half of 094: how the program engine fills its cardio
# slot with a stair-climber during a fat-loss phase for a lifter -- the kcal
# estimate it shows and feeds to 063's deficit check, where the session
# goes relative to leg training, how a knee / foot / calf caution site
# changes it, and whether the next step-up adds minutes or intensity. A
# routing rule, not a primary finding: each rule names the graded row it
# rests on and its own basis_grade; every minute value, cap and ratio is a
# labelled constant.
#
# Plugs into 063 vocabulary and never overrides it: dose_bands (start /
# standard / high), step_up (30 min per step, >= 2 weeks), deficit_budget
# (~500 kcal/day total), placement_rules keep-lifting, separate-first,
# lift-first-if-same-session, guard-leg-day, caution-site-mode,
# diet-before-cardio. Caution rungs are 056's (history-old,
# history-recent, history-unknown, current-load-pain, current-other,
# red-flag); ceilings are 057 (knee, 2/10) and 055 / 088 (tendon, fascia).
id: exercise/stepmill-cardio-slot-rules-095
domain: exercise
grade: D (slot rule over 094 and 063; the kcal table is B-backed arithmetic, "intensity adds no fat loss" is B, compensation C, every minute value, cap, ratio and the duration-first order are product constants)
lane: "@gym-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/stepmill-energy-cost-leg-load-evidence-094"  # per-kg energy cost (B), compensation (C), interval = continuous for fat mass (B), local leg fatigue (C), knee load (C), no stepmill + lifting trial (D)
  - "exercise/cut-cardio-placement-rule-063"  # dose_bands, step_up, deficit_budget, placement_rules this item plugs into
  - "exercise/concurrent-cardio-interference-cut-062"  # interference modifiers, same-session and trained-lifter effects
  - "exercise/caution-severity-ladder-056"  # rungs that decide which caution rules fire
  - "exercise/knee-pain-symptom-guided-loading-057"  # knee ceiling 2/10 and knee exposure days
  - "exercise/plantar-heel-pain-lifter-foot-rules-088"  # stepmill is cut first and rebuilt by symptoms at a plantar heel site
  - "exercise/tendon-fascia-load-management-055"  # pain ceiling for calf / Achilles load
  - "exercise/harm-route-boundary-031"  # red-flag pictures are routed, not coached
  - "nutrition/weight-loss-rate-lean-mass-012"  # the measured trend outranks every kcal estimate
  - "nutrition/energy-availability-threshold-010"  # cardio energy lowers energy availability
  - "a research sprint 2026-10-07: engine-readable stepmill_rules for the program's cardio slot in a lifter's cut (energy per 20 min by body mass, placement vs leg training, knee / plantar caution, duration vs intensity progression)"
  - "framework:GRADE -- the kcal arithmetic borrows 094's B (population averages); the low-for-expectations / high-for-ceiling split and no-eat-back borrow 094's C compensation trial; duration-before-intensity rests on 094's B null for intensity plus D reasoning about leg fatigue; placement and caution rules are 063 / 056 / 057 / 088 applied to one mode with no stepmill trial behind them (D)."
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: scale
      unknown_policy: hedge
      rescale:
        per_unit_low: 1.2     # NET kcal per kg per 20 min, easy (copied from 094 energy_cost_per_20min)
        per_unit_high: 2.8    # NET kcal per kg per 20 min, hard
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: injury_history
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: cardiovascular_condition
      type: categorical
      role: hard
      unknown_policy: block_specifics
constants:
  net_kcal_per_kg_per_20min:      # from 094 (Compendium 4.5 / 6.8 / 9.3 MET)
    easy: 1.17
    moderate: 1.93
    hard: 2.77
  intensity_rpe:                  # product mapping on the 6-20 Borg scale; moderate / vigorous bands as in ACSM 2011 via 094
    easy: 9-11
    moderate: 12-13
    hard: 14-17
  kcal_spread: 0.2                 # product: show the estimate as +/- 20% (094: individual resting rates ~20% under the convention)
  kcal_round_to: 10                # product: never show a single-kcal figure
  session_minutes_default: 20      # product: first stepmill slot length
  session_minutes_cap: 45          # product: longer than this, add a session (within 063's band) rather than lengthen
  minutes_per_progression: 10      # product: per-session add; 063 step_up (30 min/week, >= 2 weeks) stays the weekly limit
  hard_sessions_max_per_week: 1    # 063 standard band: at most 1 hard session
  hard_to_moderate_minute_ratio: 1.43   # 2.77 / 1.93: 20 hard min ~ 29 moderate min of energy (arithmetic, product use)
  warmup_minutes_max: 10           # product: a pre-lift easy block up to this is a warm-up, not the cardio slot
  post_leg_day_minutes_max: 20     # product: easy stepmill allowed after a leg session, capped
stepmill_rules:
  - rule: kcal-estimate
    trigger: a stepmill session is planned or logged
    action: net kcal = net_kcal_per_kg_per_20min[level] x body_weight_kg x minutes / 20, level from the user's RPE (intensity_rpe); show it rounded to kcal_round_to with a +/- kcal_spread range and the word "about"; never show the machine console or watch figure as the number
    basis: exercise/stepmill-energy-cost-leg-load-evidence-094
    basis_grade: B
  - rule: kcal-asymmetric-use
    trigger: the estimate feeds a decision
    action: for the 063 deficit-budget check (diet gap plus cardio cost against ~500 kcal/day) use the HIGH end of the range; for any expected-fat-loss message use the LOW end, and say part of the energy tends to come back as appetite
    basis: exercise/stepmill-energy-cost-leg-load-evidence-094
    basis_grade: C
  - rule: no-eat-back
    trigger: the user asks to add the session's kcal to the day's food target, or the food target would otherwise rise with cardio
    action: do not raise the food target by the session's kcal; the deficit is set from the weekly trend (012), cardio is part of it
    basis: exercise/stepmill-energy-cost-leg-load-evidence-094
    basis_grade: C
  - rule: default-easy-moderate
    trigger: any stepmill slot with no reason to go hard
    action: continuous at RPE easy-to-moderate (9-13, can speak in sentences); hands rest on the rails for balance only; a user who leans on the rails is logged at the easy level
    basis: exercise/stepmill-energy-cost-leg-load-evidence-094
    basis_grade: D
  - rule: progress-duration-first
    trigger: 063 diet-before-cardio has passed (room under the deficit ceiling) and 063 step_up allows a step
    action: add minutes_per_progression to a stepmill session at the same intensity until it reaches session_minutes_cap, then add a session within 063's current dose band; raise intensity only under intensity-for-time
    basis: exercise/stepmill-energy-cost-leg-load-evidence-094
    basis_grade: D
  - rule: intensity-for-time
    trigger: the user cannot give more minutes (time is the binding limit) and needs the next step
    action: convert one moderate session to a hard one, replacing minutes at hard_to_moderate_minute_ratio (e.g. 29 moderate min -> 20 hard min); at most hard_sessions_max_per_week; tell the user it saves time, not that it burns more fat
    basis: exercise/stepmill-energy-cost-leg-load-evidence-094
    basis_grade: B
  - rule: hard-is-leg-day
    trigger: the session is hard (RPE 14+, intervals, or the user rates it hard)
    action: apply 063 guard-leg-day -- count it as lower-body fatigue, never on the day before or in the session of the heaviest lower-body day; first choice is an upper-body or rest day
    basis: exercise/cut-cardio-placement-rule-063
    basis_grade: D
  - rule: easy-placement
    trigger: the session is easy or moderate
    action: apply 063 separate-first for trained lifters (non-lifting day or >= 6 h away) and lift-first-if-same-session; after a leg session only easy stepping up to post_leg_day_minutes_max, otherwise prefer cycling or move the slot
    basis: exercise/cut-cardio-placement-rule-063
    basis_grade: C
  - rule: warmup-not-slot
    trigger: an easy stepmill block before lifting of warmup_minutes_max or less
    action: it is a warm-up; it does not count toward the cardio slot or 063 minutes, and its kcal is not added to the deficit
    basis: exercise/cut-cardio-placement-rule-063
    basis_grade: D
  - rule: knee-caution
    trigger: knee at 056 rung history-recent, history-unknown or current-load-pain
    action: count each stepmill session as a knee exposure day (057 knee_days_per_week), start easy at session_minutes_default or less, monitor with the 057 ceiling (2/10 during, after, next day); a breach swaps the next session to cycling (063 caution-site-mode) before any lifting is cut
    basis: exercise/knee-pain-symptom-guided-loading-057
    basis_grade: D
  - rule: foot-calf-caution
    trigger: plantar heel, Achilles or calf at 056 rung history-recent, history-unknown or current-load-pain
    action: 088 -- stepmill is among the first activities cut; swap to cycling or rowing and rebuild stepmill by symptoms under the 055 / 088 ceiling, easy level first, minutes before intensity
    basis: exercise/plantar-heel-pain-lifter-foot-rules-088
    basis_grade: D
  - rule: route-not-coach
    trigger: knee, foot or calf at rung current-other or red-flag
    action: no stepmill rule applies; triage first (031 / 056)
    basis: exercise/harm-route-boundary-031
    basis_grade: D
  - rule: cardio-gate
    trigger: cardiovascular_condition reported or unknown
    action: no hard session and no minute or kcal target is prescribed; general activity information only, medical route (063)
    basis: exercise/cut-cardio-placement-rule-063
    basis_grade: D
answer_rules:
  - question: how many calories does 20 minutes on the stairmaster burn?
    answer: roughly 1.2 kcal per kg of body weight above resting at an easy pace, about 1.9 moderate, about 2.8 hard -- about 90 / 145 / 210 for a 75 kg person; an average, not a measurement, and the machine and watch numbers are not reliable
    basis: exercise/stepmill-energy-cost-leg-load-evidence-094
    basis_grade: B
  - question: is stairmaster HIIT better than steady for fat loss?
    answer: no -- across 29 studies intervals and steady work changed fat and muscle the same; harder sessions save time but tire the legs more, which a lifter pays for in leg training
    basis: exercise/stepmill-energy-cost-leg-load-evidence-094
    basis_grade: B
  - question: should I do stairmaster before or after leg day?
    answer: easy stepping after lifting or on another day is fine; a hard session counts as leg work, so not before or the day before the heaviest leg day; no study has tested stepmill with lifting, this is the general cardio evidence plus how the stepmill tires the legs
    basis: exercise/cut-cardio-placement-rule-063
    basis_grade: D
  - question: is the stairmaster bad for my knees?
    answer: not for healthy knees -- climbing loads the knee at about three times body weight, which is ordinary everyday loading; with front-of-knee pain, count it as a knee day and keep pain within about 2 out of 10 during, after and the next morning
    basis: exercise/knee-pain-symptom-guided-loading-057
    basis_grade: C
  - question: should I eat back the calories the stairmaster says I burned?
    answer: no -- the number is rough, part of exercise energy tends to come back as appetite, and the weekly weight trend already sets the food target
    basis: exercise/stepmill-energy-cost-leg-load-evidence-094
    basis_grade: C
never_say:
  - you burned exactly N kcal (any unrounded or rangeless figure, or the console figure as fact)
  - stairmaster HIIT burns more fat than steady cardio
  - the stepmill does not interfere with leg gains
  - stairs are bad for your knees
  - eat back the calories you burned
  - every calorie you burn on the stepmill is fat lost
refraction_notes:
  - note: >
      MINUTES FIRST IS A CHOICE, NOT A FINDING. No study compares adding
      minutes with adding intensity in a lifter's cut. The order follows from
      two things in 094: intensity does not add fat loss, and hard stepping
      tires the legs a lifter needs. When the user has no more time, the
      intensity swap is fine and is spoken as a time-saver.
    grade: D
  - note: >
      THE KCAL IS A RANGE WITH TWO USES. The same estimate is read high when
      checking the deficit ceiling (protect muscle) and low when talking
      about expected fat loss (protect expectations). Both readings yield to
      the measured weekly trend once there is one.
    grade: C
  - note: >
      CAUTION SITES CHANGE THE MODE BEFORE THE PLAN. At a knee, heel or calf
      caution site the stepmill becomes counted, monitored loading, and the
      first fallback is cycling. Lifting is not cut to make room for cardio,
      and cardio is not kept on the stepmill at the price of a flaring site.
    grade: D
claim: >
  To use a stair-climber in a lifter's fat-loss cardio slot, the engine
  estimates each session's net energy as about 1.2 (easy), 1.9 (moderate)
  or 2.8 (hard) kcal per kg of body weight per 20 minutes, shows it rounded
  with a range, reads it high for the deficit-ceiling check and low for
  expected fat loss, and never adds it back to food. The default session is
  easy to moderate and continuous. When the plan needs more cardio, it adds
  minutes first (10 per session, sessions capped at 45 minutes, within 063's
  weekly step and bands) and makes a session hard only when time is the
  limit, at most once a week, because intensity saves time but does not add
  fat loss and hard stepping tires the legs. A hard session counts as leg
  work and stays off the day before and the session of the heaviest leg
  day; easy sessions follow 063's separate or lift-first rules. At a knee
  caution site each session is a monitored knee day under the 2/10 ceiling;
  at a heel, Achilles or calf site the stepmill is cut first and rebuilt by
  symptoms. A reported or unknown heart condition withholds intensity and
  targets.
reasoning: >
  The rules are ordered as the engine meets them: estimate, decide, place,
  guard. The estimate rests on firm arithmetic over population averages,
  so it is shown as a range and outranked by the measured trend. The
  asymmetric reading follows from 094's compensation trial and the 062
  deficit ceiling: overstating the burn is the error that hurts muscle in
  the ceiling check, and the one that disappoints the user in the
  expectation message. Duration-first rests on the intensity null and the
  local-fatigue finding in 094; it is a default, and the hard-session swap
  keeps the 063 one-hard-session limit. Placement and caution rules apply
  063, 057 and 088 to this one mode without new evidence, so they sit at the
  practitioner floor. Minute values are chosen to fit inside 063's 30-minute
  weekly step, not tested as boundaries.
---

# exercise/stepmill-cardio-slot-rules-095 -- 감량기 유산소 칸을 스텝밀로 채울 때의 규칙

**한 줄 그림:** 소모량은 체중으로 대략 계산해 범위로 보여주고, 다시 먹지 않는다. 늘릴 때는 시간부터, 강도는 시간이
없을 때만. 힘든 스텝밀은 하체 운동으로 친다.

## The rules (engine order)

| # | Rule | When | Do | Basis |
|---|---|---|---|---|
| 1 | kcal-estimate | every session | net kcal/kg/20 min 1.17 / 1.93 / 2.77 x weight; round, +/-20% | 094, arithmetic |
| 2 | kcal-asymmetric-use | estimate feeds a decision | high end for 063 ceiling, low end for expected loss | 094, one RCT |
| 3 | no-eat-back | food target vs cardio | never add session kcal to food | 094, one RCT |
| 4 | default-easy-moderate | default | continuous, RPE 9-13, rails for balance | product |
| 5 | progress-duration-first | 063 step allowed | +10 min per session to 45, then another session | product, on 094 null |
| 6 | intensity-for-time | no more time | 1 hard session max; 20 hard ~ 29 moderate min | 094, meta-analysis |
| 7 | hard-is-leg-day | RPE 14+ / intervals | 063 guard-leg-day | product |
| 8 | easy-placement | easy / moderate | 063 separate-first, lift-first; after legs easy <= 20 min | 062 / 063 |
| 9 | warmup-not-slot | <= 10 min easy before lifting | warm-up, not counted | product |
| 10 | knee-caution | knee rung history-recent+ | knee day, 057 2/10 ceiling, breach -> bike | product |
| 11 | foot-calf-caution | heel / Achilles / calf rung history-recent+ | 088 cut first, bike / row, rebuild by symptoms | product |
| -- | route / cardio-gate | red-flag, heart condition | triage; no hard session, no targets | 031 / 063 |

## 한국어 요약 (답변용)

- 스텝밀 소모량은 체중 1kg당 20분에 쉬운 강도 약 1.2kcal, 보통 약 1.9kcal, 힘든 강도 약 2.8kcal로 계산하고,
  10kcal 단위로 반올림해 "약 ○○kcal(±20%)"로 보여준다. 기계 화면이나 시계 숫자는 쓰지 않는다.
- 적자가 너무 커지지 않았는지 볼 때는 높은 쪽 숫자로, 얼마나 빠질지 말할 때는 낮은 쪽 숫자로 본다. 운동한 만큼
  식욕이 늘어 일부는 다시 먹게 된다. 태운 칼로리만큼 더 먹지 않는다.
- 기본은 말할 수 있을 정도의 쉬운~보통 강도로 쭉 하는 것이다. 손잡이는 균형만 잡을 정도로 가볍게 잡는다.
- 유산소를 늘려야 할 때는 시간부터 늘린다(한 번에 10분, 한 세션 45분까지, 그다음은 세션 추가). 시간이 없을 때만
  한 세션을 힘들게 바꾸고, 주 1회까지다. 세게 해도 지방이 더 빠지지는 않고 시간만 줄어든다.
- 힘든 스텝밀은 하체 운동으로 친다. 가장 무거운 하체 날 전날이나 같은 세션에는 넣지 않는다. 쉬운 스텝밀은 다른
  날이나 웨이트 뒤에 하고, 하체 날 뒤라면 쉬운 강도로 20분까지만.
- 웨이트 전 10분 이내의 가벼운 스텝밀은 준비운동이라 유산소 시간에 넣지 않는다.
- 무릎 앞쪽 통증 이력이 있으면 스텝밀을 하는 날을 무릎 쓰는 날로 세고, 운동 중·후·다음 날 통증을 10점 중 2점
  이내로 지킨다. 넘으면 다음 번은 자전거로 바꾼다. 발뒤꿈치·아킬레스·종아리 통증이 있으면 스텝밀을 먼저
  빼고 자전거나 로잉으로 바꾼 뒤 증상을 보며 다시 늘린다.
- 심장 질환이 있거나 여부를 모르면 힘든 세션과 시간·칼로리 목표는 정하지 않는다.
