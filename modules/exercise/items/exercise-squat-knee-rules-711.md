---
# Squat-knee sprint 2026-10-07.
# The engine-readable half of 710: how the composer sets squat depth, box
# height, stance, tempo and load for a lifter with a knee caution site, in
# what order it steps back on a breach, and when the squat slot switches to a
# leg press or a split squat (and back). A routing rule, not a primary
# finding: each rule names the graded row it rests on and its own
# basis_grade; every number is a labelled product constant or a value copied
# from 057 / 058.
#
# squat_knee_rules plug into existing vocabulary: 056 rungs, 057's knee
# ceiling (knee_pain_monitoring) and knee_exposure, 058 variant_swaps, 076
# equipment_rules (strength-keep-named-lift, caution-site-machine-first), 078
# knee_prep. Side-agnostic: the caution side (left or right knee) is an input,
# caution_side; the same rules run for either knee.
id: exercise/squat-knee-rules-711
domain: exercise
grade: D (selection and step-back rule over 710, 058, 057, 056, 076 and 075; the step-back levers rest on C-level lab data in healthy lifters, the order, the switch thresholds and every constant are product judgement)
lane: "@gym-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/squat-stance-box-tempo-knee-load-evidence-710"  # depth x load, stance, foot angle, box, tempo, leg press and split squat as switch targets (C/D)
  - "exercise/knee-friendly-squat-depth-variants-058"  # 45 deg squat start, leg-press stop 45-60 deg, long-step split squat, low platform first, knees-behind-toes not a default
  - "exercise/knee-pain-symptom-guided-loading-057"  # knee ceiling 2/10 during / after / next day, one notch per week inside, 2-3 knee days, no heavy back-to-back
  - "exercise/caution-severity-ladder-056"  # rungs that decide which rules fire
  - "exercise/machine-first-selection-rules-076"  # strength-keep-named-lift; caution-site-machine-first
  - "exercise/machine-free-weight-equivalence-075"  # leg press grows the thigh as well as the squat; squat transfers better to jumping
  - "exercise/knee-prep-hip-adductor-abductor-078"  # hip work kept in every knee swap set
  - "exercise/harm-route-boundary-031"  # red-flag knee is routed, not coached
  - "a research sprint 2026-10-07: engine-readable squat_knee_rules for a lifter with one cautious knee -- depth, stance, box, tempo, and when to switch to leg press or split squat"
  - "framework:GRADE -- the levers borrow 710 / 058's C (model and moment data in healthy lifters); the step-back order, the two-breach switch, the load step and the return path have no outcome study behind them (D)."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
constants:
  squat_start_knee_deg: 45          # from 058: lowest-PF-stress squat range, standing -> about 45 deg
  leg_press_stop_knee_deg: [45, 60] # from 058: machine stop for a knee caution site
  box_step_cm: [3, 5]               # product: one box notch (a plate or mat); one notch per progression
  load_stepback_pct: [10, 20]       # product: bar load cut on a breach, with the depth notch
  tempo_eccentric_s: [2, 3]         # product, inside 710's 0.5-8 s growth-neutral band: controlled descent, no bounce
  pause_s: [1, 2]                   # product: pause on the box or at the bottom, no relaxing onto the box
  breach_switch_count: 2            # product: knee-ceiling breaches on the squat in consecutive knee exposures, after a step-back, that switch the slot
  return_trial_weeks: 2             # product: weeks inside the 057 ceiling on the switch variant before a squat re-trial
inputs:
  - caution_side   # left | right | both | none -- which knee carries the caution
  - knee_rung      # 056 rung for the knee site
  - squat_is_named_lift  # from primary_goal: the squat itself is a goal (powerlifting, a squat target or test)
  - last_knee_scores     # 057 during / after / next-day 0-10 for the last knee exposures
squat_knee_rules:
  - rule: route-not-coach
    trigger: knee at 056 rung current-other or red-flag
    action: no squat rule applies; pain-triage first (057 ladder, 031); a machine or split squat does not reopen the site
    basis: exercise/harm-route-boundary-031
    basis_grade: D
  - rule: ceiling-governs-every-variant
    trigger: knee at rung current-load-pain (knee variant), history-recent or history-unknown
    action: every squat, leg press and split squat set runs under the 057 knee ceiling (at most 2/10 during, after and next day); knee days stay 2-3 a week with no heavy back-to-back days; a breach changes the next knee day's content, never removes the day
    basis: exercise/knee-pain-symptom-guided-loading-057
    basis_grade: C
  - rule: healthy-knee-depth-free
    trigger: no knee caution (caution_side none) or knee at rung mild / history-old and pain-free
    action: depth, stance and tempo are training choices; never cap depth for knee safety; never say a deep squat harms a healthy knee
    basis: exercise/knee-friendly-squat-depth-variants-058
    basis_grade: C
  - rule: start-range-box
    trigger: knee at rung current-load-pain and the squat slot is kept
    action: squat to a box set at squat_start_knee_deg (or the deepest box the user squats inside the ceiling, whichever is deeper); box squat with a touch-and-go or a pause_s pause, no dropping onto the box; the box is the depth stop that lets the range be logged and lowered
    basis: exercise/squat-stance-box-tempo-knee-load-evidence-710
    basis_grade: C
  - rule: depth-and-load-together
    trigger: a knee-ceiling breach on a squat set
    action: next knee exposure raises the box one notch (box_step_cm) AND cuts the bar load by load_stepback_pct; never deepen while cutting load, never cut depth alone at the same bar weight
    basis: exercise/squat-stance-box-tempo-knee-load-evidence-710
    basis_grade: C
  - rule: stance-by-response
    trigger: knee caution site and the user reports the squat hurts at the planned stance
    action: try the other stance width (narrow vs wide) at a light working load before stepping back further; keep the width that stays inside the ceiling and record it; feet turned out 0-30 deg to let the knee track over the foot; no width is named knee-friendly in advance
    basis: exercise/squat-stance-box-tempo-knee-load-evidence-710
    basis_grade: C
  - rule: tempo-controlled-not-therapy
    trigger: any squat set at a knee caution site
    action: tempo_eccentric_s descent, no bounce out of the bottom; a pause is allowed; the load is set for that tempo (a slower rep means a lighter bar); never present tempo as a knee treatment
    basis: exercise/squat-stance-box-tempo-knee-load-evidence-710
    basis_grade: D
  - rule: knees-forward-allowed
    trigger: any squat at a knee caution site
    action: do not cue knees behind the toes as a default (058); with a low-back caution never use it
    basis: exercise/knee-friendly-squat-depth-variants-058
    basis_grade: C
  - rule: switch-to-leg-press
    trigger: knee at rung current-load-pain, squat_is_named_lift false, and breach_switch_count consecutive knee exposures breach the ceiling on the squat after a depth-and-load step-back
    action: the squat slot becomes a leg press with the stop at leg_press_stop_knee_deg (076 caution-site-machine-first); same sets; stance on the platform by response (narrow pressed harder in the lab data); thigh growth is kept (075)
    basis: exercise/squat-stance-box-tempo-knee-load-evidence-710
    basis_grade: C
  - rule: switch-to-split-squat-one-side
    trigger: caution_side is left or right (one knee), knee at rung current-load-pain or history-recent, and the squat breaches as in switch-to-leg-press, or the user reports the squat only hurts one side
    action: the squat slot becomes a split squat or Bulgarian split squat with dumbbells, long step (058), low platform before full depth; the caution side sets its own range and load; the good side is not loaded extra to make up the difference; a single-leg leg press is the machine alternative
    basis: exercise/squat-stance-box-tempo-knee-load-evidence-710
    basis_grade: C
  - rule: named-squat-stays
    trigger: squat_is_named_lift true and knee at rung current-load-pain or history-recent
    action: the squat stays the primary slot (076 strength-keep-named-lift) at a box depth and load inside the ceiling; leg press or split squat carries the extra quadriceps volume; if the squat breaches breach_switch_count times even at squat_start_knee_deg, tell the user the squat itself is the problem and offer a leg press block until it settles
    basis: exercise/machine-first-selection-rules-076
    basis_grade: D
  - rule: performance-keep-free-standing
    trigger: primary_goal is jumping, sprinting or a field / court sport and the squat was switched to a leg press
    action: keep one free-standing lower-body pattern a week (split squat or step-up under the ceiling), since the squat transfers better to jumping than the leg press
    basis: exercise/machine-free-weight-equivalence-075
    basis_grade: C
  - rule: hip-work-kept
    trigger: any squat swap or step-back at a knee caution site
    action: keep or add hip-dominant work and the 078 knee_prep in the session; a shallower squat or a leg press loses some glute and adductor stimulus
    basis: exercise/knee-prep-hip-adductor-abductor-078
    basis_grade: B
  - rule: return-to-squat
    trigger: the slot was switched and the user has been inside the ceiling on the switch variant for return_trial_weeks
    action: one squat re-trial set block at the last box height that passed and a light load; if inside the ceiling for a week, lower the box one notch per week (057 progress rule); if it breaches, return to the switch variant and wait another return_trial_weeks
    basis: exercise/knee-pain-symptom-guided-loading-057
    basis_grade: D
answer_rules:
  - question: how deep should I squat with my knee?
    answer: with a painful front of the knee, start shallow to a box (about 45 degrees of knee bend) at a lighter weight and lower the box one notch a week while pain stays at 2/10 or less during, after and the next day; with a knee that does not hurt, depth is a training choice
    basis: exercise/knee-friendly-squat-depth-variants-058
    basis_grade: C
  - question: wide or narrow stance for my knee?
    answer: neither is proven gentler; in the squat a wide stance pressed the knee harder, on the leg press a narrow one did; try both light and keep the one that stays within the pain rule
    basis: exercise/squat-stance-box-tempo-knee-load-evidence-710
    basis_grade: C
  - question: are box squats good for bad knees?
    answer: the box mainly fixes your depth on every rep and shifts some load to the hips; it is a good way to control and progress depth, not a proven knee treatment
    basis: exercise/squat-stance-box-tempo-knee-load-evidence-710
    basis_grade: C
  - question: should I squat slowly (tempo) to protect my knee?
    answer: a controlled 2-3 second descent without bouncing is fine and grows muscle as well as faster reps; there is no study showing it protects the knee, it mostly means a lighter bar
    basis: exercise/squat-stance-box-tempo-knee-load-evidence-710
    basis_grade: D
  - question: should I switch to leg press or split squat?
    answer: if the squat keeps going over the pain rule after making it shallower and lighter, switch to a leg press with a stop (both knees) or to a split squat (one knee); the thigh grows about as well; go back to squats after a couple of quiet weeks if the squat matters to you
    basis: exercise/squat-stance-box-tempo-knee-load-evidence-710
    basis_grade: C
never_say:
  - deep squats are bad for your knees (to a pain-free knee)
  - wide stance (or narrow stance) is easier on the knees
  - box squats fix knee pain
  - slow tempo protects the knee
  - never let your knees pass your toes
  - front squats are safer for the knees than back squats
  - stop training legs until the knee is fully pain-free
refraction_notes:
  - note: >
      THE STEP-BACK ORDER IS A DEFAULT, NOT A TESTED SEQUENCE. Depth and load
      first, stance second, variant last follows the lab data (load and depth
      drive kneecap load; stance effects run in opposite directions by
      exercise) and keeps the squat when possible; no trial compared orders
      or switch points in lifters with knee pain.
    grade: D
  - note: >
      THE SWITCH THRESHOLD IS A PRODUCT CONSTANT. Two consecutive breaches
      after a step-back is a guard against switching on one bad day and
      against grinding on a squat that keeps hurting; it is not from a study.
    grade: D
  - note: >
      ONE-SIDED KNEE MEANS UNILATERAL WORK. A bilateral squat did not show a
      one-sided knee in body-weight squats, so it gives the composer no way to
      dose the two legs apart; split squats and a single-leg leg press do.
      The rule is mechanism and practice, not a trial outcome.
    grade: D
claim: >
  At a knee caution site the squat slot starts at a box near 45 degrees at a
  lighter load, under the 057 knee ceiling, with a controlled 2-3 second
  descent and no bounce. On a breach the box goes up one notch and the bar
  load comes down together; then the other stance width is tried at a light
  load. After two consecutive breaches despite that, a squat that is not a
  goal lift switches to a leg press with a 45-60 degree stop (both knees) or
  to a long-step split squat with the caution side setting its own range and
  load (one knee); a named squat stays at a tolerated box depth with the
  extra volume moved to the machine. Hip work stays in every swap. After two
  weeks inside the ceiling on the switch, the squat is re-tried at the last
  passing box height and lowered a notch a week. A pain-free knee has no
  depth cap, and the answer path never presents stance, box or tempo as a
  proven knee treatment.
reasoning: >
  The levers come from 710 and 058 (healthy-lifter lab data, C); the order,
  switch count, load step, box notch and return window are product constants
  chosen to keep the squat where possible, to avoid switching on noise, and
  to move one dial at a time so the user's response can be read. Side
  handling is side-agnostic via caution_side, mirroring 093's
  unilateral-caution-decouple. injury_history is hard with block_specifics
  because the rung decides whether any rule fires and red flags are routed;
  primary_goal decides named-squat-stays and the performance keep;
  training_status is soft (novices show more knee travel in 710's Lorenzetti
  data, so stance cues matter more for them).
---

# exercise/squat-knee-rules-711 -- 무릎이 신경 쓰이는 사람의 스쿼트 규칙: 깊이·스탠스·박스·템포, 레그프레스·스플릿 스쿼트 전환

**한 줄 그림:** 박스를 45도쯤에 두고 가볍게 시작한다. 아프면 박스를 한 칸 올리고 무게도 같이 줄인다.
그래도 두 번 연속 기준을 넘으면 양쪽 무릎은 레그프레스, 한쪽 무릎은 스플릿 스쿼트로 바꾸고, 2주 조용하면
스쿼트를 다시 시험한다.

## Step-back and switch order (engine-readable)

| Step | When | What the next knee day does | Basis |
|---|---|---|---|
| 0 | red-flag / current-other | no squat rule; triage | 031, 057 |
| 1 | start at current-load-pain | box at about 45 deg, lighter load, 2-3 s down, no bounce | 058, 710 |
| 2 | one breach (over 2/10) | box up one notch AND load down 10-20% | 710, 057 |
| 3 | squat hurts at this stance | try the other width, light | 710 |
| 4 | 2 consecutive breaches after a step-back | leg press, stop 45-60 deg (both knees) / split squat, caution side sets range (one knee) | 710, 058, 076 |
| 4' | squat is a goal lift | squat stays at a tolerated box; extra volume on the machine | 076 |
| 5 | 2 weeks inside on the switch | squat re-trial at the last passing box; one notch lower a week | 057 |

Hip work and 078 knee prep stay in every step.

## 한국어 요약 (답변용)

- 무릎 앞쪽이 아픈 상태라면 박스를 무릎 45도쯤 높이에 두고 가벼운 무게로 시작한다. 2-3초에 걸쳐 내려가고
  바닥에서 튕기지 않는다. 박스에 털썩 앉지 않고, 닿고 바로 올라오거나 1-2초 멈춘다.
- 통증이 운동 중·후·다음 날 중 하나라도 10점 중 2점을 넘으면 다음 무릎 운동 날에 박스를 한 칸(3-5cm)
  올리고 무게도 10-20% 같이 줄인다. 깊이만 줄이고 무게는 그대로 두지 않는다.
- 특정 스탠스에서 아프면 반대 너비(좁게/넓게)를 가볍게 시험해 보고 덜 아픈 쪽을 쓴다. 어느 쪽이 무릎에
  좋다고 미리 정하지 않는다.
- 이렇게 줄였는데도 두 번 연속 기준을 넘으면 바꾼다. 양쪽 무릎이면 멈춤 장치를 45-60도에 둔 레그프레스,
  한쪽 무릎이면 보폭을 길게 한 스플릿 스쿼트나 불가리안 스플릿 스쿼트(덤벨)로 바꾸고, 아픈 쪽이 깊이와
  무게를 정한다. 안 아픈 쪽에 무게를 더 얹어 메우지 않는다.
- 스쿼트 자체가 목표(파워리프팅, 스쿼트 기록)라면 스쿼트는 견딜 수 있는 박스 깊이로 남기고, 나머지
  허벅지 볼륨은 레그프레스나 스플릿 스쿼트로 채운다.
- 점프·달리기·구기 종목이 목표면 레그프레스로 바꿔도 주 1회는 스플릿 스쿼트나 스텝업처럼 서서 하는 하체
  운동을 남긴다.
- 엉덩이 운동과 무릎 준비 운동(078)은 어느 단계에서든 유지한다.
- 바꾼 동작으로 2주 동안 기준 안에 있으면 마지막으로 괜찮았던 박스 높이에서 가볍게 스쿼트를 다시 해 본다.
  일주일 괜찮으면 박스를 한 칸씩 낮춘다.
- 무릎이 아프지 않다면 깊이 제한은 없다. "스탠스를 넓히면 무릎에 좋다", "박스 스쿼트가 무릎을 고친다",
  "천천히 하면 무릎이 보호된다", "무릎이 발끝을 넘으면 안 된다"고 말하지 않는다.
