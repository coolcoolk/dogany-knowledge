---
# Goal-phase sprint 2026-10-07. The
# engine-readable synthesis for two assistant moments: the GOAL RE-CONSULT
# (the user changes grow / cut / maintain, or a trigger asks them to) and
# the WEEKLY GOAL-FIT CHECK (does this week's training and body-weight
# trend fit the declared phase). It is a routing rule, not a primary
# finding: each row names the graded item it rests on, and every window,
# step and threshold that no source sets is a labelled product constant.
# Same posture as 056 and 072.
#
# Vocabulary matches 072 and compose_rank_rules: goal keys grow / cut /
# maintain (phase_aliases), floors growth / maintenance from 072 set_floor,
# cut_keep, weekly_muscles, set_style. Weekly sets are FRACTIONAL (direct
# 1.0, indirect 0.5, 008). Body-weight readings are spoken only through the
# nutrition 029 bands (7-day means, 0.5 kg band, three readings for a trend).
# The YAML-subset reader returns numbers as strings; cast them.
#
# phase_volume_rules, ramp_rules, weekly_goal_fit_check,
# goal_reconsult_triggers and never are the structured fields.
# Numbering: claimed 081 provisionally; released as 087 in v41 (its
# sibling evidence row 080 -> 086; bare 080 / 081 in the body rewritten).
id: exercise/phase-volume-rules-087
domain: exercise
grade: D (synthesis rule over 070, 071, 072, 086 and nutrition 012 / 029; the per-phase floors, keep-the-load and no-extra-sets-in-a-cut rows carry their own B / C grades; every ramp step, check window and re-consult trigger is product judgement)
lane: "@gym-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/phase-energy-volume-ramp-evidence-086"  # surplus size, previous-volume anchoring, ramp evidence (none), detraining time course
  - "exercise/set-floor-rule-072"  # the growth / maintenance floors, cut_keep split, set_style, trim order this row points at
  - "exercise/maintenance-vs-growth-volume-cut-071"  # maintenance with load kept; a deficit blunts gain, strength still rises
  - "exercise/set-floor-by-experience-070"  # growth floors by experience
  - "exercise/deficit-volume-guidance-016"  # more sets in a deficit to protect muscle -- refuted
  - "exercise/deload-planned-vs-reactive-060"  # deload triggers and recipe the stall branch hands off to
  - "exercise/deload-autoregulation-in-a-cut-085"  # (linked v41) the cut-phase deload reading: cut_falling on two or more main lifts is 085's whole-week deload case; one lift falling is 085's one-lift reset; a slow drift holds the load
  - "exercise/progression-rules-trained-cut-082"  # (linked v41) per-lift progression, stall-define / stall-reset and stall-cut-check inside each phase; this row sets the weekly volume, 082 moves the load
  - "exercise/rir-set-log-accuracy-077"  # RIR as the restart instrument after a layoff
  - "exercise/concurrent-cardio-interference-cut-062"  # cut-phase cardio is a separate rule
  - "nutrition/weight-loss-rate-lean-mass-012"  # 0.5-1%/wk loss rate (one small trial)
  - "nutrition/body-measure-reading-rules-029"  # weight noise bands and trend rule the weekly check speaks through
  - "nutrition/diet-breaks-refeeds-026"  # a maintenance stretch inside a long cut costs no fat loss per restricted week
  - "nutrition/self-report-underreporting-007"  # a flat cut is first an intake-logging question
  - "a research sprint 2026-10-07: engine-readable phase_volume_rules for the goal re-consult and the weekly goal-fit check"
  - "framework:GRADE -- the cut-phase lean-mass blunting is a meta-analysis (B, via 071); a small surplus doing as well as a large one, keeping previous volume doing as well as jumping, and maintenance with load kept are small RCTs (C, via 086 / 071); the loss-rate band is one small trial (C, via nutrition 012); the gain-rate band is a review number (D); every ramp step, check window, stall rule and re-consult trigger is a product constant (D)."
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: ask
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: hedge
phase_volume_rules:
  - phase: grow
    words: eating a small surplus to add muscle
    energy: small surplus
    weight_trend_pct_per_week: 0.25-0.5
    weight_trend_advanced: below 0.25
    weight_trend_basis_grade: D
    priority_muscles: growth
    other_muscles: growth
    weekly_target: the larger of the 072 growth floor and the user's own recent weekly sets for that muscle
    block_step_max_pct: 20
    load: progress
    set_style: unchanged
    basis: exercise/phase-energy-volume-ramp-evidence-086
    basis_grade: C
  - phase: cut
    words: eating a deficit to lose fat while keeping muscle
    energy: deficit
    weight_trend_pct_per_week: -0.5 to -1.0
    weight_trend_basis_grade: C
    deficit_note: near 500 kcal a day or more prevents lean-mass gain on average (071)
    priority_muscles: growth
    priority_source: trainer_fit.cut_keep
    other_muscles: maintenance
    weekly_target: cut_keep muscles at the growth floor, the rest at the maintenance floor; never above the user's recent weekly sets
    load: keep
    set_style: unchanged
    basis: exercise/maintenance-vs-growth-volume-cut-071
    basis_grade: B
  - phase: maintain
    words: eating about what you burn and keeping what you have
    energy: balance
    weight_trend_pct_per_week: steady inside the 029 band
    weight_trend_basis_grade: D
    priority_muscles: maintenance
    other_muscles: maintenance
    weekly_target: at least the 072 maintenance floor; the user may keep their current volume
    min_days_age_60: 2
    load: keep
    set_style: unchanged
    basis: exercise/maintenance-vs-growth-volume-cut-071
    basis_grade: C
ramp_rules:
  - from: cut
    to: grow
    start_from: mean weekly fractional sets per muscle over the last 2 weeks
    step_per_week: the larger of 2 sets or 20% of last week, per muscle, until weekly_target
    load: keep the cut-phase loads, progress as usual
    basis_grade: D
  - from: maintain
    to: grow
    start_from: mean weekly fractional sets per muscle over the last 2 weeks
    step_per_week: the larger of 2 sets or 20% of last week, per muscle, until weekly_target
    load: progress as usual
    basis_grade: D
  - from: grow
    to: cut
    start_from: the same week
    step_per_week: none -- drop muscles outside cut_keep to the maintenance floor at once by removing exercises (072 trim step 3)
    load: keep
    basis_grade: C
  - from: grow
    to: maintain
    start_from: the same week
    step_per_week: none -- the user may keep current volume or drop to the maintenance floor at once
    load: keep
    basis_grade: C
  - from: cut
    to: maintain
    start_from: the same week
    step_per_week: none -- keep current volume; only the eating changes
    load: keep
    basis_grade: D
  - from: layoff
    to: any
    break_weeks_under: 3
    action: resume the previous week's plan unchanged
    basis_grade: C
  - from: layoff
    to: any
    break_weeks_from: 3
    action: restart at the 072 maintenance floor or half the previous weekly sets, whichever is larger, then ramp with the same step; first session per lift at RIR 3 to find the working load, not a percentage of the old best
    basis_grade: D
  - from: any
    to: any
    new_exercise_first_session: lower set level (2) the first time a movement appears in a block; full sets from the second session
    basis_grade: D
weekly_goal_fit_check:
  - check: volume_fit
    reads: weekly fractional sets per weekly_muscles muscle vs the phase weekly_target
    window_weeks: 2
    when_short: name the muscle and the shortfall (072 trim step 5); propose a schedule change, never one-set slots
    basis_grade: D
  - check: weight_fit
    reads: 7-day mean body weight through the nutrition 029 bands
    window_weeks: 3
    speak_only_if: a trend by the 029 rule (three comparable readings moving the same way); otherwise say steady or not enough readings
    grow_too_fast: above 0.5% a week for 3 weeks -> propose a smaller surplus (more fat, not more muscle, 086)
    grow_flat: no rising trend for 4 weeks while main-lift loads also stall -> ask about intake before proposing more food
    cut_too_fast: below -1.0% a week for 2 weeks -> propose a smaller deficit
    cut_flat: no falling trend for 3 weeks -> check intake logging first (nutrition 007), then propose a smaller intake or a planned maintenance stretch (nutrition 026)
    maintain_drift: a trend either way for 4 weeks -> ask whether the goal is still maintain
    basis_grade: D
  - check: strength_fit
    reads: load at matched reps and RIR on the main lifts
    window_weeks: 2
    cut_falling: falling on two or more main lifts -> deficit or fatigue; propose a smaller deficit, a deload (060) or a maintenance stretch (nutrition 026); never more sets
    grow_stall: no rise on the main lifts for 3 weeks -> check sleep, intake and the 060 reactive triggers
    maintain_falling: falling on two or more main lifts -> check that load was kept; from age 60 add a second weekly day
    basis_grade: D
  - check: output
    states: on_track / watch / propose_change
    proposals_per_week_max: 1
    order: strength_fit, then weight_fit, then volume_fit
    basis_grade: D
goal_reconsult_triggers:
  - trigger: the user states a new goal or a phase word (bulk, cut, diet, maintain)
    action: re-consult now
  - trigger: the planned phase length or the target weight is reached
    action: re-consult now
  - trigger: propose_change for the same reason three weeks in a row and not taken up
    action: ask whether the goal still fits
  - trigger: a layoff of 3 weeks or more
    action: re-consult on return, with the layoff ramp
  - trigger: a cut with no declared end after 16 weeks
    action: offer maintain or a maintenance stretch (nutrition 026)
  - trigger: age_years reaches 60
    action: tell the user the maintenance floor rises (072 age_modifiers)
never:
  - raise weekly sets in a cut to protect muscle
  - lower the load per set to make a cut or maintenance week easier
  - start a grow block at a generic high set count far above the user's recent weekly sets
  - speak one week's weight change as on or off target
  - propose a bigger surplus because weight is rising slowly while strength still rises
  - change set_style because the phase changed
refraction_notes:
  - note: >
      THE PHASE MOVES THE ENERGY AND WHICH MUSCLES GROW, NOT THE SET
      STYLE. Grow keeps every muscle at the growth floor, cut keeps only
      cut_keep there and lets the rest fall to maintenance, maintain holds
      the maintenance floor; in all three the load per set is kept and the
      user's set_style stays as chosen.
    grade: C
  - note: >
      START FROM WHAT THE USER DID, NOT FROM A TABLE. A new grow block
      starts at the user's own last two weeks of weekly sets (or the growth
      floor if that is higher) and a block adds about a fifth at most.
      Keeping previous volume grew as well as large jumps in trained men
      (086); the 2-week window and the per-week step are ours.
    grade: C
  - note: >
      GOING DOWN IS IMMEDIATE, GOING UP IS STEPPED. Moving into a cut or
      maintain needs no taper, because keeping muscle needs little volume
      when the load is kept (071). Moving up is stepped by about two sets or
      a fifth a week, mainly so the first week back is not the sore one.
      No lifting trial sets a ramp rate.
    grade: D
  - note: >
      THE WEEKLY CHECK READS TRENDS, NOT WEEKS. Weight speaks only through
      7-day means and three readings (nutrition 029), and one proposal at a
      time, strength first: in a cut, falling strength is the earliest sign
      the deficit or fatigue is too much, since strength normally still
      rises in a moderate deficit (071).
    grade: D
  - note: >
      A FAST GAIN IS A SIGNAL, NOT PROGRESS. Weight rising faster than
      about half a percent a week in a grow phase is mostly fat (086); the
      check proposes a smaller surplus, never "keep going, you are growing
      faster".
    grade: C
claim: >
  For the goal re-consult and the weekly goal-fit check, the assistant should set
  weekly per-muscle volume by phase: grow keeps every muscle at the 072
  growth floor or the user's own recent weekly sets, whichever is higher,
  adding at most about a fifth per block, on a small surplus aimed at
  about 0.25-0.5% body-weight gain a week; cut keeps cut_keep muscles at
  the growth floor, lets the rest fall to the maintenance floor, never
  adds sets and aims at a 0.5-1% weekly loss; maintain holds at least the
  maintenance floor at a steady weight. Load per set is kept in every
  phase and set_style does not change with the phase. Going down in volume
  happens the same week; going up starts from the last two weeks' actual
  sets and steps by about two sets or a fifth a week; after three or more
  weeks off the restart is at the maintenance floor or half the previous
  volume with the load found by RIR. The weekly check reads two-week
  volume, three-week weight trends through the nutrition 029 bands and
  two-week main-lift strength, and makes at most one proposal a week,
  strength first. Only the phase direction, keep-the-load and
  no-extra-sets-in-a-cut rest on trials; ramp steps, windows and triggers
  are product constants.
reasoning: >
  071 and 016 give the cut row (keep is cheap with the load kept; a
  deficit blunts gain; extra sets do not protect). 086 gives the grow row
  (a small surplus does as well as a large one; the user's previous
  volume is the reference) and shows that no trial sets a ramp, so every
  step is labelled. 072 already owns the floors, the cut_keep split and
  the trim order, so this row only says which floor each phase points at
  and how to move between them. The weekly check reuses nutrition 029 for
  weight so the warehouse has one noise rule, and hands fatigue to 060
  and intake to nutrition 007 / 026 instead of restating them. The
  strength-first order follows from 071: in a moderate deficit strength
  still rises on average, so a fall is the most specific early signal.
---

# exercise/phase-volume-rules-087 -- 목표(증량·감량·유지)가 바뀔 때 볼륨 규칙과 주간 점검

**한 줄 그림:** 단계가 바뀌면 칼로리와 "어느 근육을 키울지"가 바뀌고, 세트 방식과 무게는 그대로다.
볼륨은 내릴 때는 바로, 올릴 때는 최근 실제 세트 수에서 조금씩 올린다.

## Per phase (weekly sets are fractional)

| Phase | Weekly target per muscle | Weight trend aimed at | Load |
|---|---|---|---|
| grow | max(072 growth floor, own last 2 weeks); at most about +20% per block | +0.25-0.5% / week (coaching number) | progress |
| cut | `cut_keep` at growth floor, rest at maintenance floor; never above recent sets | -0.5 to -1.0% / week | keep |
| maintain | at least the maintenance floor (2 days from age 60) | steady inside the 029 band | keep |

## Switching

| From -> to | Volume | Speed |
|---|---|---|
| grow -> cut / maintain | drop non-priority muscles to maintenance by removing exercises | same week |
| cut / maintain -> grow | start at last 2 weeks' mean | + max(2 sets, 20%) per muscle per week (product) |
| layoff under 3 weeks | resume as before | -- |
| layoff 3 weeks or more | max(maintenance floor, half the previous) | same step; first session RIR 3 to find the load |

## Weekly goal-fit check

Strength first (2 weeks, main lifts at matched reps and RIR), then weight
(3 weeks, 7-day means through nutrition 029), then volume (2 weeks against
the phase target). States: on_track / watch / propose_change; one proposal a
week at most.

## 한국어 요약 (답변용)

- 단계가 바뀌면 바뀌는 건 먹는 양과 "어느 근육을 키울지"다. 증량기는 모든 근육을 성장 최소선 이상,
  감량기는 우선 근육만 성장 최소선이고 나머지는 유지선, 유지기는 모두 유지선 이상이다. 어느 단계든
  무게는 지키고, 세트 방식(3세트 이상 / 2세트 고강도)은 그대로 둔다.
- 증량기 볼륨은 표의 숫자가 아니라 최근 2주 동안 실제로 한 세트 수에서 시작한다. 한 블록에 20% 정도
  넘게 한꺼번에 올리지 않는다. 증량 속도는 주당 체중의 0.25~0.5%를 기준으로 삼되, 코칭에서 쓰는 숫자다.
- 감량기에는 세트를 늘리지 않는다. 주당 체중의 0.5~1% 정도 빠지는 속도를 기준으로 본다(작은 연구 하나가 근거).
- 볼륨을 내릴 때(증량→감량·유지)는 그 주부터 바로 바꾼다. 올릴 때(감량·유지→증량)는 주마다 근육당
  2세트 또는 20% 중 큰 만큼만 올린다. 이 속도는 제품이 정한 값이고, 연구로 정해진 속도는 없다.
- 3주 넘게 쉬었다 돌아오면 유지선이나 예전 세트 수의 절반 중 큰 쪽에서 다시 시작한다. 첫 운동은 2~3회
  더 할 수 있는 무게로 시작해서 지금 다룰 무게를 찾는다. 예전 최고 기록의 몇 %로 정하지 않는다.
- 매주 점검은 힘 → 체중 → 볼륨 순서로 보고, 제안은 한 주에 하나만 한다. 체중은 한 주 숫자로 말하지
  않고 7일 평균과 세 번 이상 같은 방향일 때만 추세로 말한다.
- 감량 중 주요 운동 무게가 2주 동안 떨어지면 세트를 늘리지 말고, 덜 깎아 먹기·디로드·유지 칼로리 기간
  중 하나를 제안한다. 증량 중 체중이 3주 동안 주 0.5%보다 빨리 늘면 덜 먹기를 제안한다. 대부분 지방이다.
- 목표를 다시 물어보는 때: 사용자가 새 목표를 말할 때, 정한 기간이나 목표 체중에 닿았을 때, 같은 제안을
  3주 연속 안 받아들였을 때, 3주 넘게 쉬고 돌아왔을 때, 끝을 정하지 않은 감량이 16주를 넘었을 때.
- 단계 방향, 무게 지키기, 감량 중 세트 안 늘리기는 연구에 근거가 있다. 올리는 속도, 점검 기간, 다시 묻는
  시점은 제품 규칙이므로 답할 때도 연구로 정해진 값처럼 말하지 않는다.
