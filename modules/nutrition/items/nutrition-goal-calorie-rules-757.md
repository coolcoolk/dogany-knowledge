---
# Goal-calorie sprint 2026-10-08 (
# block 755..759). The engine-readable synthesis for GOAL-SETTING time: what
# to ask first, how the starting calorie and protein targets are sized, the
# floors and stop conditions, and the cadence for adjusting from weigh-ins.
# Rows routed from: 755 (maintenance estimate, calibration), 756 (deficit to
# weight dynamics, guideline deficit sizes), 012 (rate for lean mass), 062
# (deficit protein), 029 (reading weigh-ins), 074 (adherence), 026 (breaks),
# 010 (energy availability), 007 (under-reporting). A routing rule, not a
# primary finding: each rule names the graded row it rests on, and every
# product constant (factors, steps, windows, floors) is labelled as one. Same
# posture as nutrition/adherence-rules-074 and body-measure-reading-rules-029.
#
# ask_first and goal_calorie_rules are structured data for the goal card and
# the weekly retro. The YAML-subset reader returns every scalar as a string;
# flow lists parse natively. No program code was changed and no field guide
# doc was written (GAPS.md).
id: nutrition/goal-calorie-rules-757
domain: nutrition
lane: "@obs-inferential"
grade: D (synthesis rule over 755, 756, 012, 062, 029 and 074; each rule carries its own basis grade; every constant is product judgement)
locale: universal
as_of: 2026
contested: no
sources:
  - "nutrition/maintenance-estimate-calibration-755"  # Mifflin-St Jeor as the start, +/-10 percent band, Korean hedge, weight trend calibrates
  - "nutrition/deficit-weight-dynamics-756"  # 7700 kcal/kg over-predicts; first-weeks water; 500-750 (KR 500-1,000) kcal deficit; 5-10 percent in 6 months; plateau; <800 kcal medical only
  - "nutrition/weight-loss-rate-lean-mass-012"  # 0.5-1 percent of body weight per week for lean-mass retention (thin base, contested)
  - "nutrition/protein-deficit-lean-mass-target-062"  # 1.6-2.4 g/kg in a deficit with RT; older-adult floor 1.2; CKD gate; ~500 kcal deficit stopped RT lean gains
  - "nutrition/body-measure-reading-rules-029"  # 7-day mean, 0.5 kg speak band, confirmed-trend; the only way weigh-ins are read here
  - "nutrition/adherence-rules-074"  # adherence-before-diet-switch, weighing-exit, break-week-weight
  - "nutrition/diet-breaks-refeeds-026"  # maintenance breaks as an appetite tool
  - "nutrition/energy-availability-threshold-010"  # low energy availability is a spectrum, not a cut-off; for heavy trainers
  - "nutrition/self-report-underreporting-007"  # logged intake is a floor
  - "https://doi.org/10.1161/01.cir.0000437739.71477.ee"  # Jensen MD et al. 2013 AHA/ACC/TOS obesity guideline. Circulation 2014;129(25 Suppl 2):S102-S138. PMID 24222017 -- deficit sizes, intake bands, VLCD rule, 6-month plateau
  - "https://doi.org/10.7570/jomes23016"  # Kim KK et al. KSSO 2022 update. J Obes Metab Syndr 2023;32(1):1-24. PMID 36945077 -- individualise the restriction; 500-1,000 kcal; VLED only supervised
  - "framework:GRADE -- each rule's basis_grade is the grade of the row it routes from; the activity factors, the 1200/1500 kcal floors, the 100-200 kcal adjustment step, the 2-week no-verdict window, the 3-week adjustment window and the 5 percent re-estimate trigger are product constants with no direct evidence."
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: ask
    - key: sex
      type: categorical
      role: soft
      unknown_policy: ask
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: ask
    - key: height_cm
      type: numeric
      role: soft
      unknown_policy: ask
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: ask
    - key: activity_level
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: ask
      gate:
        allowed: [not_pregnant, none]
    - key: medication_list
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: renal_condition
      type: categorical
      role: hard
      unknown_policy: hedge
      gate:
        allowed: [none, healthy]
ask_first:
  - order: 1
    ask: what the goal is (lose fat, lose fat and keep or build muscle, maintain, gain) and any target weight or date
    axis: primary_goal
    why: decides whether a deficit exists at all and whether it is sized by kcal or by rate
    if_unknown: ask; no number is set without a goal
  - order: 2
    ask: one screening question -- pregnant or breastfeeding, under 18, a past or current eating disorder, or taking medicine for diabetes or a kidney condition
    axis: pregnancy_status, age_years, medication_list, renal_condition
    why: each one withdraws or changes the deficit number (rules screen-*)
    if_unknown: ask once in the same turn; a refusal keeps the general answer and the baseline text, and the deficit is spoken as a range with the clinician line
  - order: 3
    ask: sex, age, height and current weight (weight is read from the scale log first)
    axis: sex, age_years, height_cm, body_weight_kg
    why: inputs to the maintenance estimate (755)
    if_unknown: a missing input means no kcal number; give the method and the guideline bands instead
  - order: 4
    ask: a usual week's activity, and whether resistance training is part of it
    axis: activity_level, training_status
    why: the activity factor is the largest error in the estimate (755); training sets the protein band and the rate rule
    if_unknown: hedge with the lowest factor (1.2) and say so
  - order: 5
    ask: optional -- whether the user already logs food, and roughly what a usual day looks like
    axis: none
    why: a logging user can be calibrated from week 3; a non-logger is calibrated on weight alone
    if_unknown: skip; never block the target on it
goal_calorie_rules:
  - rule: screen-minor
    surface: goal_setting
    trigger: age_years under 18
    action: no calorie or deficit number; general eating-pattern advice only; suggest a parent, school nurse or clinician for a weight goal
    never: [a kcal target for a minor]
    constants: age 18 (product constant; both guidelines cover adults only)
    basis: nutrition/deficit-weight-dynamics-756
    basis_grade: D
  - rule: screen-pregnancy
    surface: goal_setting
    trigger: pregnancy_status pregnant or breastfeeding
    action: no deficit; refer weight questions to the user's obstetric clinician
    never: [a deficit target, a rate target]
    constants: none
    basis: product safety rule (no source in this module covers pregnancy energy needs; GAPS.md)
    basis_grade: D
  - rule: screen-underweight
    surface: goal_setting
    trigger: BMI from height and weight below 18.5 and the goal is weight loss
    action: no deficit; say the current weight is already below the healthy range; offer a maintenance or strength goal instead
    never: [a deficit target]
    constants: BMI 18.5 (WHO and KSSO underweight cut-off, used as a product gate)
    basis: product safety rule
    basis_grade: D
  - rule: screen-eating-disorder
    surface: goal_setting
    trigger: the user states a current or past eating disorder, or speaks of distress at the scale or around food
    action: no kcal or deficit number and no daily weighing default; suggest support from a clinician; general, non-numeric eating advice only
    never: [kcal target, deficit size, rate target]
    constants: none
    basis: nutrition/adherence-rules-074 (weighing-exit; no ledger axis exists)
    basis_grade: D
  - rule: screen-medication-kidney
    surface: goal_setting
    trigger: medication_list includes insulin or another glucose-lowering drug, or renal_condition is stated and not none
    action: give the target as a general range and say to check it with the prescribing clinician before starting; renal -- the protein number is withdrawn per 062
    never: [start the deficit today without checking]
    constants: none
    basis: nutrition/protein-deficit-lean-mass-target-062 (renal gate); medication line is product judgement
    basis_grade: D
  - rule: maintenance-estimate
    surface: goal_setting
    trigger: sex, age, height and weight known
    action: resting energy by Mifflin-St Jeor times the activity factor; show the result as a range of plus or minus 10 percent and call it a starting estimate
    never: [your metabolism is N kcal, an exact maintenance number]
    constants: activity factors 1.2 mostly sitting / 1.375 light / 1.55 moderate / 1.725 very active (conventional multipliers, not validated here); +/-10 percent band
    basis: nutrition/maintenance-estimate-calibration-755
    basis_grade: B
  - rule: deficit-size-overweight
    surface: goal_setting
    trigger: goal is fat loss and BMI 25 or above (KSSO obesity cut-off is 25)
    action: default deficit 500 kcal/day below the estimate; the user may pick up to 750; first goal 5-10 percent of body weight in about 6 months
    never: [deficit above 1000 kcal/day, a target under 800 kcal/day]
    constants: 500 default (guideline); 750 user ceiling (AHA/ACC/TOS upper prescription; KSSO allows 1,000)
    basis: nutrition/deficit-weight-dynamics-756
    basis_grade: B
  - rule: deficit-size-lean-or-training
    surface: goal_setting
    trigger: goal is fat loss and (BMI under 25, or training_status trained, or the goal names keeping muscle)
    action: size from a rate of 0.5 percent of body weight per week (user may pick up to 1 percent); starting deficit = rate in kg/week x 1100 kcal, capped at 500 kcal/day; pair with the 062 protein band and continued resistance training
    never: [deficit above 500 kcal/day for a lean lifter at the start, the rate spoken as proven to protect muscle]
    constants: 0.5 percent default; 1100 kcal per kg-per-week (7700/7, a first-weeks scale only, 756); 500 kcal cap
    basis: nutrition/weight-loss-rate-lean-mass-012 and nutrition/protein-deficit-lean-mass-target-062
    basis_grade: C
  - rule: intake-floor
    surface: goal_setting
    trigger: estimate minus deficit falls below 1200 kcal (women) or 1500 kcal (men)
    action: shrink the deficit to meet the floor and say why; if the floor leaves almost no deficit, suggest more activity rather than less food
    never: [target under the floor without a clinician, target under 800 kcal/day in any case]
    constants: 1200 / 1500 (lower edge of the AHA/ACC/TOS intake bands, used as a floor -- product constant); 800 (VLCD line, a guideline rule)
    basis: nutrition/deficit-weight-dynamics-756
    basis_grade: D
  - rule: protein-first
    surface: goal_setting
    trigger: any fat-loss target
    action: state the daily protein target with the kcal target; with resistance training 1.6-2.4 g/kg body weight (062), low end for users with more body fat and a modest deficit; over 65, at least 1.2 g/kg
    never: [2.3-3.1 g/kg multiplied by body weight, a protein number for stated kidney disease]
    constants: none (bands are 062's)
    basis: nutrition/protein-deficit-lean-mass-target-062
    basis_grade: B
  - rule: no-straight-line-date
    surface: goal_setting
    trigger: the user asks when they will reach the target, or sets a date
    action: give a range; say the loss slows over the months and the first weeks include water; if the date needs more than the rule ceilings (1 percent a week lean, 1 kg a week overweight), say the date is the thing to move
    never: [a single goal date from 7700 kcal per kg, a deficit raised to meet a date]
    constants: none
    basis: nutrition/deficit-weight-dynamics-756
    basis_grade: B
  - rule: first-two-weeks-no-verdict
    surface: weekly_retro
    trigger: fewer than 14 days since the target started (or since a break ended)
    action: show the weight trend with the note that early change is partly water; no adjustment, no praise for a large first-week drop
    never: [you lost N kg of fat this week, the target is working / not working]
    constants: 14 days (product constant)
    basis: nutrition/deficit-weight-dynamics-756
    basis_grade: B
  - rule: adjust-too-slow
    surface: weekly_retro
    trigger: from week 3, the 7-day-mean trend over at least 3 weeks shows less than half the planned weekly rate, or steady by 029's band, AND logged adherence was high (074)
    action: offer one step of 100-200 kcal/day less (not past the floor), or more daily activity; re-check after 3 more weeks
    never: [an adjustment from one weigh-in or one week, a cut when adherence is unknown or low, steps above 200 kcal]
    constants: 3-week window; 50 percent of plan; 100-200 kcal step
    basis: nutrition/body-measure-reading-rules-029 and nutrition/adherence-rules-074
    basis_grade: D
  - rule: adjust-too-fast
    surface: weekly_retro
    trigger: from week 3, two consecutive weekly comparisons faster than 1 percent of body weight a week (lean or training) or 1 kg a week (overweight)
    action: offer one step of 100-200 kcal/day more; for a training user, mention the lean-mass reason (012)
    never: [faster is better, keep going while hunger and training performance fall]
    constants: 1 percent / 1 kg ceilings; 2 comparisons; 100-200 kcal step
    basis: nutrition/weight-loss-rate-lean-mass-012
    basis_grade: C
  - rule: apparent-maintenance
    surface: weekly_retro
    trigger: from week 3, at least 3 weeks of complete logs and a confirmed trend (029)
    action: may show apparent maintenance = mean logged intake + trend kg/week x 1100; label it as maintenance at the user's logging habits; use it to re-centre the estimate, not to replace the floor
    never: [your true TDEE is N, apparent maintenance below the floor used as a target]
    constants: 1100 kcal per kg-per-week (short-window only, 756)
    basis: nutrition/maintenance-estimate-calibration-755
    basis_grade: C
  - rule: re-estimate-on-loss
    surface: weekly_retro
    trigger: weight trend down 5 percent from the weight the estimate used
    action: re-run the maintenance estimate at the new weight and re-size the deficit by the same rule
    never: [keep the day-1 estimate for the whole diet]
    constants: 5 percent trigger (product constant)
    basis: nutrition/deficit-weight-dynamics-756
    basis_grade: D
  - rule: plateau-is-expected
    surface: weekly_retro
    trigger: around 6 months in, or a steady trend after a period of loss with adherence high
    action: say slowing is expected; offer three choices -- a maintenance phase, a planned break (026), or a re-set target by these rules
    never: [your metabolism is broken, you failed]
    constants: none
    basis: nutrition/deficit-weight-dynamics-756
    basis_grade: B
  - rule: heavy-trainer-caution
    surface: goal_setting
    trigger: training_status trained and activity_level very active, with a deficit target
    action: add one line that a large gap between food and training load can cause problems beyond weight; fatigue, illness, missed periods or falling performance are reasons to eat more and see a clinician
    never: [30 kcal/kg FFM as a diagnostic cut-off]
    constants: none
    basis: nutrition/energy-availability-threshold-010
    basis_grade: C
refraction_notes:
  - note: >
      THE RULES ARE GRADED, THE NUMBERS ARE NOT. Each rule's direction rests
      on its basis row. The activity factors, the 1200/1500 floors, the 1100
      kcal per kg-per-week scale, the 100-200 kcal step, the 14-day and 3-week
      windows and the 5 percent re-estimate trigger are product constants.
      Speak them as the plan's rule, never as tested thresholds.
    grade: D
  - note: >
      THE FLOOR IS A PRODUCT GUARD, NOT A PHYSIOLOGICAL LIMIT. The 1200 and
      1500 kcal figures are the lower edges of the intake bands the American
      guideline prescribes to adults with obesity. Neither guideline names
      them as a safety minimum. They are used here so the app never hands a
      small or older user a target that would be a supervised diet elsewhere.
      Only the under-800 kcal line is a guideline rule.
    grade: D
  - note: >
      TWO SIZING PATHS, ONE BOUNDARY. Guideline deficits (500-750 kcal) come
      from trials in adults with overweight or obesity. The rate rule (0.5-1
      percent per week) comes from one trial in lean athletes. The BMI 25 split
      uses the Korean obesity cut-off as the switch between them. It is a
      product choice: a muscular user above 25 who trains should be treated by
      the lean-or-training path, which the trigger already allows.
    grade: D
  - note: >
      SAFETY SCREEN WITHOUT LEDGER AXES. No axis exists for eating-disorder
      history. Until the framework adds one, screen-eating-disorder is a
      conversational trigger, as in 074. The minor gate is the screen-minor
      rule, not an axis gate, because the refraction engine checks a gate by set
      membership and cannot express a numeric threshold. The
      pregnancy gate is hard with ask, not block_specifics, because a blocked
      unknown would withhold every target from users for whom it does not
      apply; the screening question in ask_first is what closes it.
    grade: D
  - note: >
      ADJUST ON TREND AND ADHERENCE, NEVER ON A WEIGH-IN. Weight readings are
      read only through 029, and a slow trend is checked against logged
      adherence (074) before any cut. Calorie targets move in small steps
      because a 100-200 kcal change is already inside the error of the
      starting estimate (755); a bigger jump would mostly chase noise.
    grade: D
claim: >
  At goal-setting time the engine asks, in order, for the goal, one safety
  screen (pregnancy or breastfeeding, under 18, eating-disorder history,
  diabetes or kidney medicine), body inputs and usual activity. It withholds
  any deficit number for minors, pregnancy, underweight and stated eating
  disorders. It estimates maintenance with Mifflin-St Jeor times an activity
  factor and shows it as a plus or minus 10 percent range. Users with BMI 25
  or more get a 500 kcal/day default deficit (up to 750) and a first goal of
  5-10 percent in six months. Lean or training users get a deficit sized from
  0.5 percent of body weight per week, capped at 500 kcal/day, with protein of
  1.6-2.4 g/kg. Targets never go below 1200 kcal (women) or 1500 kcal (men)
  without a clinician, nor below 800 in any case. The first two weeks get no
  verdict. From week three, the 7-day-mean trend over three weeks, checked
  against adherence, moves the target in 100-200 kcal steps. The estimate is
  re-run after each 5 percent loss, and a plateau near six months is spoken
  as expected. Directions are B-to-C backed; every constant is product
  judgement.
reasoning: >
  Every rule routes one graded row into the goal card or the weekly retro,
  so the item adds no new finding and is graded as a synthesis. The
  strongest rules are those resting on 756 and 062 (guideline deficits,
  dynamic-model slowing, early water, the protein band). The lean-or-training
  sizing borrows 012, whose base is thin, and so carries C. The adjustment
  cadence is the least evidenced part: no trial compares adjustment rules,
  so the cadence is built from the measurement floor (029), the estimate
  error (755) and the adherence rule (074), and is labelled as product
  judgement. The safety screen says less rather than more: where the module
  holds no evidence (pregnancy, minors, eating disorders) the rule withdraws
  the number and routes to a clinician instead of inventing a modified one.
---

# nutrition/goal-calorie-rules-757 -- 목표 설정 때 칼로리·단백질 정하는 규칙

**한 줄 그림:** 먼저 목표와 안전 질문, 그다음 공식으로 시작점을 잡고, 2주는 판정하지 않고, 3주 이상
흐름과 기록을 보고 100-200 kcal씩 고친다.

## Ask first

| # | Ask | Why |
|---|---|---|
| 1 | goal (and any target weight or date) | whether a deficit exists; kcal path or rate path |
| 2 | one screen: pregnant / breastfeeding, under 18, eating disorder, diabetes or kidney medicine | withdraws or changes the number |
| 3 | sex, age, height, weight | the maintenance estimate |
| 4 | usual activity; resistance training? | largest estimate error; protein band |
| 5 | (optional) logs food already? | calibration from week 3 |

## The rules

| Rule | When | Then | Basis |
|---|---|---|---|
| screen-minor / pregnancy / underweight / eating-disorder | screen hit | no deficit number; route | product safety rule, 074 |
| screen-medication-kidney | glucose-lowering drug or kidney condition | range only; check with clinician; protein per 062 | 062 |
| maintenance-estimate | inputs known | Mifflin x activity, +/-10% range | 755 |
| deficit-size-overweight | BMI >= 25, fat loss | 500 kcal default, up to 750; 5-10% in 6 months | 756 |
| deficit-size-lean-or-training | BMI < 25, or trained, or keep muscle | 0.5%/week (up to 1%), cap 500 kcal | 012, 062 |
| intake-floor | target < 1200 (F) / 1500 (M) | shrink deficit; never < 800 | 756 (floor is a constant) |
| protein-first | any fat-loss target | 1.6-2.4 g/kg with RT; >= 1.2 over 65 | 062 |
| no-straight-line-date | date asked or set | a range; move the date, not the deficit | 756 |
| first-two-weeks-no-verdict | day < 14 | no adjustment; early change is partly water | 756 |
| adjust-too-slow | >= 3 weeks < half plan, adherence high | -100 to -200 kcal or more activity | 029, 074 |
| adjust-too-fast | 2 weeks > 1%/week (lean) or 1 kg/week | +100 to +200 kcal | 012 |
| apparent-maintenance | >= 3 weeks complete logs, confirmed trend | logged mean + trend x 1100; "at your logging habits" | 755 |
| re-estimate-on-loss | trend down 5% | re-run the estimate | 756 |
| plateau-is-expected | ~6 months, or steady after loss | maintenance phase, break or re-set | 756, 026 |
| heavy-trainer-caution | trained + very active + deficit | warning signs line | 010 |

## 한국어 요약 (답변용)

- 목표 칼로리를 정하기 전에 묻는 순서: ① 목표(감량, 근육 유지하며 감량, 유지, 증량)와 목표
  체중·날짜 ② 안전 질문 한 번(임신·수유 중인지, 만 18세 미만인지, 섭식장애 경험이 있는지, 당뇨약이나
  콩팥 질환 약을 먹는지) ③ 성별·나이·키·체중 ④ 평소 활동량과 근력 운동 여부 ⑤ (선택) 식단 기록을
  하고 있는지.
- 미성년자, 임신·수유 중, 저체중(BMI 18.5 미만), 섭식장애 경험을 말한 사람에게는 감량 칼로리 숫자를
  주지 않고 전문가에게 연결한다. 당뇨약(특히 인슐린)이나 콩팥 질환이 있으면 범위로만 말하고 시작
  전에 담당 의사와 확인하라고 한다.
- 유지 칼로리는 공식 추정치를 ±10% 범위로 보여 준다. "당신의 대사량은 몇 kcal"라고 단정하지 않는다.
- BMI 25 이상이면 하루 500 kcal 적자가 기본이고 750까지 고를 수 있다. 첫 목표는 6개월에 체중의
  5~10%다. 마른 편이거나 근력 운동을 하거나 근육 유지를 원하면, 주당 체중의 0.5%(최대 1%) 속도로
  적자를 잡고 하루 500 kcal를 넘기지 않는다. 단백질은 근력 운동 시 체중 1 kg당 1.6~2.4 g이다.
- 목표 섭취량은 여성 1200 kcal, 남성 1500 kcal 밑으로 내리지 않는다. 이 숫자는 연구가 정한 안전선이
  아니라 제품의 보호 장치다. 하루 800 kcal 미만은 어떤 경우에도 앱에서 제시하지 않는다.
- 목표 날짜는 범위로 말한다. 날짜를 맞추려고 적자를 키우지 않고, 필요하면 날짜를 옮긴다.
- 처음 2주는 판정하지 않는다. 초반에 빠지는 체중에는 물이 섞여 있다.
- 3주째부터 주간 평균 체중 흐름을 본다. 3주 이상 계획 속도의 절반도 안 되고 기록상 잘 지켰다면,
  하루 100~200 kcal를 줄이거나 활동을 늘리자고 제안한다. 2주 연속 너무 빠르면(마른 사람 주 1% 이상,
  비만인 사람 주 1 kg 이상) 100~200 kcal를 늘린다. 체중 한 번 잰 값으로는 절대 바꾸지 않는다.
- 체중이 5% 줄 때마다 유지 칼로리를 새 체중으로 다시 계산한다. 6개월 무렵 정체는 예상된 일이다.
  유지 기간, 계획된 브레이크, 목표 재설정 중에서 고르게 한다.
- 2주 금지, 3주 창, 100~200 kcal 단계, 5% 재계산, 1200/1500 하한은 모두 제품이 정한 규칙이다.
