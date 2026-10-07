---
# Time-crunched session sprint 2026-10-07.
# The engine-readable synthesis of 090 (time-efficiency evidence) for the
# daily program: what the composer does when today's minutes are fewer than
# the planned session needs. It is a routing rule, not a primary finding:
# each rule names the graded row it rests on, and every minute count and
# threshold is a labelled product constant. Same posture as 072 and 073.
#
# It does not replace 072's trim_order or 080's time-cap-cut-order; it puts
# them in one cut_order with the set-keeping levers (supersets, rest, drop
# sets) in FRONT of them, so sets are kept as long as possible. Vocabulary
# matches 072 (per_exercise_min, primary_min, weekly_muscles, cut_keep, set
# levels 3 and 2, session_muscle_point) and 080 (ramp rules). Weekly sets are
# fractional (008); ramp sets never count (072 set_style).
id: exercise/short-session-rules-091
domain: exercise
grade: D (synthesis rule over 090, 072, 080 and 017; each rule carries its own basis_grade; the order and every threshold are product judgement)
lane: "@gym-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/short-session-time-efficiency-evidence-090"  # supersets, drop sets / rest-pause, warm-up and stretching cuts, minimum dose
  - "exercise/set-floor-rule-072"  # floors and the exercise-first trim_order this rule set extends
  - "exercise/warmup-ramp-sets-heavy-compounds-080"  # ramp rules and its time-cap-cut-order
  - "exercise/rest-interval-volume-load-017"  # rest acts through reps kept; heavy compounds need longer rest
  - "exercise/maintenance-vs-growth-volume-cut-071"  # maintenance dose with the load kept; older adults need more
  - "exercise/early-morning-session-brief-rules-073"  # dawn-extend-warmup, which this rule set does not cut
  - "a research sprint 2026-10-07: engine-readable short_session_rules for the daily program, keeping weekly floors"
  - "framework:GRADE -- the directions are borrowed from the cited rows at their own grades (superset volume and time B, pairing type C, drop sets B for growth, rest by lift type B, minimum dose C); the cut order, the micro-session line, the rep-drop trigger and the drop-set accounting are product constants with no direct evidence (D)."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: cardiovascular_condition
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [none]
constants:
  micro_session_min: 20               # product: under this many minutes, run the micro-session shape
  isolation_rest_s: [60, 90]          # 017: isolation / moderate-load rest when reps hold
  compound_rest_trained_min_s: 120    # 017: heavy multi-joint rest floor for a trained lifter (Grgic 2018 ">2 min to maximise")
  compound_rest_untrained_min_s: 60   # 017: 60-120 s adequate untrained
  rest_restore_rep_drop: 2            # product: a set that falls this many reps or more under the previous set restores the full rest
  superset_time_saving_frac: 0.37     # 090, Zhang 2025 pooled; an estimate for the composer's minute model, not a promise
  dropset_time_saving_frac: [0.5, 0.67]  # 090, Sodal 2023 range for the lift it replaces
  dropset_weekly_set_credit: 1        # product: a drop set counts as one working set, whatever its drops
  dropset_max_per_exercise: 1         # product: only the last set of an exercise
short_session_rules:
  - rule: fit-check
    trigger: planned session minutes (composer estimate incl. ramps, rest and transitions) exceed the minutes the user has today
    action: apply cut_order from step 1, re-estimate after each step, stop at the first step that fits; never run a later step when an earlier one already fits
    basis: exercise/set-floor-rule-072
    basis_grade: D
  - rule: shorten-not-skip
    trigger: user says there is too little time today and asks whether to skip
    action: offer the shortened session (or the micro-session) instead of a skip; a skipped day is only the answer when the minutes cannot hold one primary lift at per_exercise_min after its ramp
    basis: exercise/short-session-time-efficiency-evidence-090
    basis_grade: D
  - rule: drop-stretch-and-long-general
    trigger: cut_order step 1
    action: drop pre-lift static stretching and any general warm-up beyond the low end of 080 general_warmup_heavy_min; keep 073 dawn-extend-warmup at its low end; keep the user's own mobility or rehab block (it is a goal, not warm-up)
    basis: exercise/short-session-time-efficiency-evidence-090
    basis_grade: B
  - rule: later-ramps-short
    trigger: cut_order step 2
    action: run 080 time-cap-cut-order (later moderate-load lifts to 0-1 ramp rung); the first heavy compound keeps its full ramp
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: C
  - rule: superset-accessories
    trigger: cut_order step 3
    action: pair accessory and isolation exercises as agonist-antagonist (push with pull, elbow flexor with elbow extensor, knee flexor with knee extensor) or upper with lower; the pair runs A, B, then the normal rest of the slower exercise; same sets, same loads
    basis: exercise/short-session-time-efficiency-evidence-090
    basis_grade: B
  - rule: no-same-muscle-pair
    trigger: any superset is built
    action: never pair two exercises whose direct sets go to the same muscle; that cuts volume load (Zhang 2025 similar-biomechanical subgroup)
    basis: exercise/short-session-time-efficiency-evidence-090
    basis_grade: C
  - rule: fill-primary-rest
    trigger: cut_order step 4
    action: the primary heavy compound keeps its full rest (compound_rest_trained_min_s or compound_rest_untrained_min_s); its rest may hold one set of an unrelated, low-load exercise (a calf, core, rear-delt or opposite-limb accessory) that does not tax the same muscles, grip or lower back; if the primary set's reps fall by rest_restore_rep_drop or more, remove the filler
    basis: exercise/rest-interval-volume-load-017
    basis_grade: C
  - rule: shorten-isolation-rest
    trigger: cut_order step 5
    action: isolation and moderate-load accessory rest to isolation_rest_s; if a set falls rest_restore_rep_drop reps or more under the previous set, restore the planned rest for the rest of that exercise
    basis: exercise/rest-interval-volume-load-017
    basis_grade: B
  - rule: last-set-drop-set
    trigger: cut_order step 6, an accessory at set level 3 on a machine, cable or dumbbell, training_status not novice
    action: replace the last two straight sets with one straight set and one drop set (dropset_max_per_exercise); the drop set counts dropset_weekly_set_credit toward weekly sets, so the exercise now carries 2 sets and never falls below per_exercise_min; not on a free-weight compound, not on the primary lift
    basis: exercise/short-session-time-efficiency-evidence-090
    basis_grade: D
  - rule: then-trim-exercises
    trigger: cut_order step 7
    action: run 072 trim_order steps 1-4 unchanged (drop covered optional isolation, drop redundant same-pattern exercise, on a cut take non-cut_keep muscles to maintenance, accessories 3 -> 2 sets)
    basis: exercise/set-floor-rule-072
    basis_grade: D
  - rule: carry-to-week
    trigger: cut_order step 8, a weekly_muscles muscle lost direct sets today and is now under its weekly floor
    action: add the lost sets to the next session this week that already trains the muscle, up to session_muscle_point for that muscle; anything left is 072 step 5 (name the muscle, no one-set slots, no lighter load)
    basis: exercise/set-floor-rule-072
    basis_grade: D
  - rule: micro-session
    trigger: minutes today under micro_session_min, or cut_order step 7 still does not fit
    action: run only the primary lift (and a second compound of the opposite pattern if minutes allow, as a superset) at working load, per_exercise_min sets each, first heavy lift with its 080 ramp; skip all accessories and carry their sets per carry-to-week; speak it as a real session
    basis: exercise/short-session-time-efficiency-evidence-090
    basis_grade: C
  - rule: density-gate
    trigger: cardiovascular_condition is not none, or unknown
    action: skip superset-accessories, fill-primary-rest, shorten-isolation-rest and last-set-drop-set; use only the stretch, ramp, trim and carry steps; when unknown, say density methods exist without prescribing them
    basis: exercise/short-session-time-efficiency-evidence-090
    basis_grade: D
  - rule: speak-effort
    trigger: a superset, shorter rest or drop set was applied today
    action: one line that it is the same work in less time and will feel harder; no claim that it builds more muscle
    basis: exercise/short-session-time-efficiency-evidence-090
    basis_grade: B
cut_order:
  - step: 1
    rule: drop-stretch-and-long-general
    keeps_sets: true
  - step: 2
    rule: later-ramps-short
    keeps_sets: true
  - step: 3
    rule: superset-accessories
    keeps_sets: true
  - step: 4
    rule: fill-primary-rest
    keeps_sets: true
  - step: 5
    rule: shorten-isolation-rest
    keeps_sets: true
  - step: 6
    rule: last-set-drop-set
    keeps_sets: false
  - step: 7
    rule: then-trim-exercises
    keeps_sets: false
  - step: 8
    rule: carry-to-week
    keeps_sets: true
never:
  - reducing load or effort per set to fit the minutes (072)
  - the primary lift below primary_min sets, or its rest below the compound rest floor
  - a superset of two exercises for the same muscle
  - a drop set or rest-pause set on a free-weight compound or on the primary lift
  - counting ramp sets or drop-set drops as extra weekly sets
  - cutting the first heavy compound's ramp to save time
  - cutting a heavy free-weight compound's rest to fit a superset partner
refraction_notes:
  - note: >
      KEEP SETS FIRST, THEN DROP EXERCISES. Supersets and shorter isolation
      rest take minutes out without taking sets out (090), so they go before
      072's trim, which loses sets or coverage. Stretching and long general
      warm-up go before both because they carry the least for a lifting
      session. The order itself is product judgement; no trial compares
      the levers head to head under one time budget.
    grade: D
  - note: >
      THE PRIMARY LIFT IS PROTECTED. The heavy compound keeps its ramp, its
      sets and its rest; only its rest may hold an unrelated filler set, and
      the filler goes as soon as the primary set loses reps. Rest for a heavy
      compound is what holds its load (017); upper-with-lower superset pairs
      did not differ significantly from straight sets but were imprecise
      (090).
    grade: C
  - note: >
      DROP-SET ACCOUNTING IS OURS. Drop-set trials matched growth with fewer
      straight sets, but none defined how many weekly sets a drop set is
      worth. The rule counts it as one set and lets it replace one of three
      accessory sets, never below two per exercise. Novices skip it: it is a
      to-failure method and the composer has easier levers.
    grade: D
  - note: >
      SHORT IS BETTER THAN SKIPPED, BY INFERENCE. One hard set per exercise
      still builds strength in trained men and one weekly session holds
      muscle (090, 071), so a 15-20 minute session of the main lifts is a
      stimulus. No trial compared shortening with skipping; the 20-minute
      micro-session line is a constant.
    grade: D
  - note: >
      THE WEEK IS THE UNIT. Weekly volume matters more than how it is spread
      across sessions (090, Iversen 2021), so sets lost today move to another
      session that already trains the muscle, within the per-session point.
      A muscle that still misses its floor is named, as in 072.
    grade: C
  - note: >
      HARDER, NOT BETTER. Supersets raise RPE and lactate; say so. With a
      cardiovascular condition the density levers are skipped and only the
      trim levers run, because the evidence measured internal load, not
      safety, in people without that condition.
    grade: D
claim: >
  When today's minutes are fewer than the planned session needs, the daily
  program cuts in this order and stops at the first step that fits: drop
  pre-lift static stretching and trim the general warm-up to its low end;
  shorten ramps on later moderate-load lifts (080); superset accessories as
  agonist-antagonist or upper-lower pairs, never same-muscle; let the primary
  lift's full rest hold one unrelated filler set; cut isolation rest to
  60-90 s while reps hold; for non-novices replace the last two accessory sets
  with one straight set plus a drop set; then run 072's exercise-first trim;
  and carry any weekly_muscles shortfall to the next session that trains that
  muscle this week. Under about 20 minutes it runs a micro-session of the
  primary lift (plus one opposite compound) at working load and full sets. It
  never lightens the load, cuts the primary lift's sets, ramp or rest, pairs
  the same muscle, or uses failure methods on free-weight compounds; density
  levers are skipped with a cardiovascular condition. Directions carry the
  grades of 090, 017, 072 and 080; the order and every number are product
  constants.
reasoning: >
  090 supplies the set-keeping levers (supersets B, pairing type C, drop sets
  B for growth with C transfer to the accounting, rest-by-lift-type B via
  017) and the floor below which a session stops being a stimulus (C). 072
  supplies the floors and the exercise-first trim; 080 supplies the ramp cut
  order. The ordering of the set-keeping levers before the set-losing ones
  follows from the per-exercise and weekly floors (072) and from the absence
  of any cost in growth or strength for the set-keeping levers in the pooled
  data. The rep-drop trigger, the drop-set accounting, the micro-session line
  and the density gate are product judgement (D).
---

# exercise/short-session-rules-091 -- 시간이 모자란 날의 운동 줄이기 규칙

**한 줄 그림:** 세트는 지키고 시간을 뺀다. 스트레칭 → 뒤쪽 워밍업 세트 → 슈퍼세트 → 쉬는 시간 →
드롭세트 → 종목 빼기 순서로, 맞으면 거기서 멈춘다. 빠진 세트는 이번 주 다른 날로 옮긴다.

## Cut order (stop at the first step that fits)

| Step | Rule | Keeps sets | Basis |
|---:|---|---|---|
| 1 | drop static stretching, general warm-up to its low end | yes | 090 |
| 2 | later ramps to 0-1 rung (080 time-cap-cut-order) | yes | 080 |
| 3 | superset accessories, opposite muscles or upper + lower | yes | 090 |
| 4 | one unrelated filler set inside the primary lift's full rest | yes | 017, 090 |
| 5 | isolation rest 60-90 s while reps hold | yes | 017 |
| 6 | last two accessory sets -> one straight + one drop set (not novices) | 3 -> 2 | 090, product |
| 7 | 072 trim_order steps 1-4 | no | 072 |
| 8 | carry lost sets to this week's next session for that muscle | yes, over the week | 072 |

Under 20 minutes (product): primary lift (+ one opposite compound as a superset) at working
weight, 2+ sets each, with its ramp. No accessories; their sets move to the week.

Never: lighter load, fewer primary sets, a shorter primary ramp or rest, same-muscle supersets,
drop sets on barbell compounds, ramp or drop counts as extra sets.

## 한국어 요약 (답변용)

- 오늘 시간이 계획보다 모자라면 이 순서로 줄이고, 시간이 맞는 단계에서 멈춘다.
  1) 운동 전 정적 스트레칭을 빼고 가벼운 전신 워밍업을 짧은 쪽으로. 새벽 워밍업 연장(073)은 짧은
  쪽으로 남기고, 재활·유연성이 목표인 운동은 그대로 둔다.
  2) 뒤쪽 중간 무게 운동의 워밍업 세트를 0~1개로(080). 첫 무거운 운동의 워밍업 세트는 그대로.
  3) 보조 운동을 슈퍼세트로 묶는다. 밀기+당기기, 이두+삼두, 앞허벅지+뒷허벅지, 또는 상체+하체.
  같은 근육 운동끼리는 묶지 않는다.
  4) 메인 운동은 쉬는 시간을 그대로 지키고, 그 사이에 손목·허리·같은 근육을 안 쓰는 가벼운 운동
  한 세트(종아리, 코어 등)를 끼운다. 메인 세트 반복이 줄면 끼운 운동을 뺀다.
  5) 고립 운동은 60~90초만 쉰다. 앞 세트보다 2회 이상 줄면 원래 쉬는 시간으로 돌린다.
  6) 초보가 아니면 보조 운동 3세트 중 마지막 두 세트를 일반 1세트 + 드롭세트 1세트로 바꾼다. 머신·
  케이블·덤벨에서만. 드롭세트는 1세트로 센다.
  7) 그래도 모자라면 072 순서대로 종목을 뺀다.
  8) 빠진 세트는 이번 주에 그 근육을 운동하는 다음 날로 옮긴다. 그래도 모자란 근육은 이름을 말한다.
- 20분도 안 되면 메인 운동 하나(시간이 되면 반대 방향 복합운동 하나를 슈퍼세트로)만 평소 무게로
  2세트 이상 한다. 건너뛰는 것보다 짧게라도 하는 걸 권한다. 다만 이 비교는 연구가 아니라 추론이다.
- 무게나 강도를 낮춰서 시간을 맞추지 않는다. 메인 운동의 세트 수·워밍업 세트·쉬는 시간은 줄이지
  않는다. 바벨 복합운동에는 드롭세트·레스트포즈를 쓰지 않는다.
- 슈퍼세트나 짧은 휴식을 쓴 날은 "같은 운동량을 짧게 한 거라 더 힘들게 느껴진다"고 한 줄 말한다.
  근육이 더 큰다고 말하지 않는다.
- 심혈관 질환이 있거나 모르면 슈퍼세트·짧은 휴식·드롭세트는 쓰지 않고, 종목 빼기와 주간 이월만 한다.
- 순서와 20분, 2회, 드롭세트를 1세트로 세는 것 같은 숫자는 제품 규칙이다. 연구로 정해진 값처럼
  말하지 않는다.
