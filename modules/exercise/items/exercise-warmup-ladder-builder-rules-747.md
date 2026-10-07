---
# Warm-up ladder sprint 2026-10-08.
# The engine-readable ladder builder: given one working weight (logged,
# stated, converted or found today), produce the warm-up rungs -- loads as
# fractions of the working weight, reps, rests -- for barbell, dumbbell and
# machine lifts, upper and lower body, so that any stated working weight
# always yields a ladder (at least one rung). A routing rule over 080 (ramp
# evidence + constants), 018 (jump cap) and 740 (calibration inputs): each
# rule names the row it rests on and its own basis_grade; every number is
# copied from those rows or is a labelled product constant.
#
# Does not replace 080's ramp_rules; it is the builder those rules call.
# 080 still decides WHETHER a lift gets a full / short ramp
# (heavy-compound-full-ramp, moderate-load-short-ramp), the general warm-up
# and the time-cap cut order; this row decides WHICH rungs.
id: exercise/warmup-ladder-builder-rules-747
domain: exercise
grade: D (ladder construction rule over 080, 018 and 740; the last-rung-near-working floor and the calibration inputs borrow those rows' C, the percent templates, rounding, rung caps, dumbbell and deadlift handling and every threshold are product judgement)
lane: "@gym-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/warmup-ramp-sets-heavy-compounds-080"  # heavy <= 6 reps / moderate >= 8; last rung >= 0.75 and 0.85-0.92 for heavy; reps 2-5 near the top; RIR 4+; rests 60-120 s, 120-180 s before work
  - "exercise/warmup-load-rampup-progression-018"  # 20% default jump cap, 15-25% band, tighter into the top set
  - "exercise/working-load-calibration-evidence-748"  # calibration steps upper 5-10% / lower 10-20%, step-down 2.5-5% / 5-10%; 10-rep estimate cap; dumbbell ratios 0.83 / 0.93; novices start light
  - "exercise/rir-set-log-accuracy-077"  # first-set RIR under-called; counted reps outrank estimated RIR
  - "exercise/autoregulation-vs-percentage-prescription-030"  # the load is corrected from the first work set, not the ramp
  - "exercise/machine-free-weight-equivalence-075"  # no machine <-> free-weight conversion
  - "exercise/load-increment-size-evidence-gap-027"  # fixed-stack steps have no literature (sub-gap 5)
  - "a research sprint 2026-10-08: engine-readable ramp_rules so a stated working weight always yields a ladder -- percent steps, reps per step, rest, first-session calibration, upper vs lower, barbell vs dumbbell"
  - "framework:GRADE -- no trial compares ladder shapes before 3-5 rep work (080 gap) or methods of finding a first working weight (740); the builder is a deterministic encoding of protocol (NSCA), coaching schemes (018) and the direction of small trials (080), so D throughout, with C borrowed only where a rule restates 080 or 740."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
inputs:
  - working_weight      # kg; barbell = total incl. bar; dumbbell = per hand; machine = pin / plate load as the machine reads
  - working_reps        # target reps of the first work set
  - target_rir          # RIR target of the work sets (default 2)
  - body_region         # upper | lower (lower = squat, deadlift, RDL, hip thrust, leg press, lunge / split squat, leg curl / extension)
  - implement           # barbell | dumbbell | machine (stack, cable, plate-loaded)
  - weight_source       # logged | stated | converted | none
  - pattern_loaded_today  # true if a lift for the same muscles / pattern already ran today
  - first_lift_today    # true for the first resistance lift of the session
  - bar_kg              # default 20; 15 for a women's bar, 10-15 for a technique / EZ bar
  - load_step_kg        # smallest load change: barbell plate pair (default 2.5), dumbbell rack step (default 2), stack step (default 5)
  - implement_min_kg    # lightest loadable: bar_kg, lightest dumbbell (default 2), first pin (default 5)
constants:
  heavy_working_reps_max: 6          # from 080
  moderate_working_reps_min: 8       # from 080; 7 working reps = middle
  ladder_heavy_upper: [0.50, 0.70, 0.90]   # product; last value inside 080's 0.85-0.92; final gap 10% matches the NSCA upper step (740)
  ladder_heavy_lower: [0.50, 0.70, 0.85]   # product; final gap 15% matches the NSCA lower step (740)
  ladder_heavy_reps: [5, 3, 2]       # 080 rung_reps_near_top 2-5; top rung 1-2 when working reps <= 3
  ladder_middle: [0.55, 0.80]        # product, working reps 7
  ladder_middle_reps: [5, 3]
  ladder_moderate: [0.75]            # 080 moderate-load-short-ramp: one rung at last_rung_min_frac
  ladder_moderate_reps: [4]          # 080: 3-4 reps
  first_lift_extra_rung: 0.50        # product: moderate lift that opens the session gets a 0.50 x 8 rung first
  first_lift_extra_reps: 8
  bar_rung_reps_heavy: 10            # product, inside NSCA 5-10 light reps
  bar_rung_reps_moderate: 5
  jump_cap_frac: 0.20                # 018 default
  jump_cap_light_frac: 0.25          # 018 loose end; allowed for a jump that ends at or below 0.60 of the working weight
  jump_cap_tolerance_steps: 1        # product: a rounded jump may exceed the cap by one load_step_kg
  last_rung_min_frac: 0.75           # from 080
  max_rungs_barbell: 6               # product, bar rung included
  max_rungs_dumbbell: 3              # product: each dumbbell rung is a pick-up / kick-up
  max_rungs_machine: 4               # product
  min_rung_reps: 1
  rest_light_s: 60                   # 080, rungs below 0.70
  rest_heavy_rung_s: [90, 120]       # 080, rungs at or above 0.70
  rest_to_work_s: [120, 180]         # 080, last rung to the first work set
  rung_rir_min: 4                    # 080 ramp_rung_rir_min
  calib_step_up_upper: [0.05, 0.10]  # 740 (NSCA)
  calib_step_up_lower: [0.10, 0.20]  # 740 (NSCA)
  calib_step_down_upper: [0.025, 0.05]  # 740 (NSCA)
  calib_step_down_lower: [0.05, 0.10]   # 740 (NSCA)
  calib_easy_rir: 6                  # product: a calibration set at RIR 6+ takes the big step
  calib_max_sets: 4                  # product: calibration sets before the found load is taken as today's working weight
  db_ratio_flat_press: 0.83          # 740 (Saeterbakken 2011): dumbbell pair total / barbell
  db_ratio_standing_ohp: 0.93        # 740 (Saeterbakken 2013)
  db_ratio_default: 0.80             # product, no data for other lifts: start at or under the lower measured ratio
  stated_check_short_reps: 2         # product: first work set this many reps short of target -> step down
  stated_check_easy_rir_over: 3      # product: first work set this far above target RIR -> step up
  deadlift_floor_min_kg: 60          # product: bar + two 20 kg full-diameter plates sets floor height
ramp_rules:
  - rule: ladder-always-built
    trigger: any working weight is known for a lift (weight_source logged, stated or converted, or found by first-session-calibration)
    action: build a ladder by the rules below; the result has at least one rung; an empty ladder is never returned -- the optional flag (moderate-already-warm) is how a skippable rung is marked
    table: true
    basis: exercise/warmup-ladder-builder-rules-747
    basis_grade: D
  - rule: pick-template
    trigger: ladder build starts
    action: working_reps <= heavy_working_reps_max -> ladder_heavy_upper or ladder_heavy_lower by body_region, reps ladder_heavy_reps; working_reps 7 -> ladder_middle; working_reps >= moderate_working_reps_min -> ladder_moderate, plus first_lift_extra_rung in front when first_lift_today; each fraction times working_weight
    table: true
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: C
  - rule: moderate-already-warm
    trigger: working_reps >= moderate_working_reps_min and pattern_loaded_today
    action: the ladder is the single ladder_moderate rung marked optional; skipping it costs no reps (080, Enes 2025); never add a bar rung
    table: true
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: C
  - rule: barbell-bar-rung
    trigger: implement barbell and the first template rung is above bar_kg, and not moderate-already-warm
    action: put the empty bar first, bar_rung_reps_heavy reps before heavy / middle work, bar_rung_reps_moderate before moderate work
    table: true
    basis: exercise/warmup-load-rampup-progression-018
    basis_grade: D
  - rule: deadlift-from-floor
    trigger: implement barbell, lift pulled from the floor (conventional / sumo deadlift)
    action: the first rung is deadlift_floor_min_kg (or bar on blocks / an RDL with the bar if no full-diameter plates); no empty-bar floor pull; if working_weight <= deadlift_floor_min_kg, pull from blocks or swap to an RDL for the day
    table: true
    basis: exercise/warmup-ladder-builder-rules-747
    basis_grade: D
  - rule: dumbbell-no-bar
    trigger: implement dumbbell
    action: no bar rung; template rungs per hand; drop the lowest rungs until the count is at most max_rungs_dumbbell (keep the top rung); a rung below implement_min_kg becomes implement_min_kg or is dropped if that duplicates the next rung
    table: true
    basis: exercise/warmup-ladder-builder-rules-747
    basis_grade: D
  - rule: machine-stack
    trigger: implement machine
    action: no bar rung; template rungs on the stack; at most max_rungs_machine; the machine's own step sets the rounding (fixed-stack steps have no literature, 027)
    table: true
    basis: exercise/load-increment-size-evidence-gap-027
    basis_grade: D
  - rule: round-to-loadable
    trigger: every rung after the template
    action: round each rung to the nearest loadable value (bar_kg plus whole load_step_kg for a barbell, the rack step for dumbbells, the stack step for machines), ties down; drop any rung that rounds to the previous rung or to or above working_weight
    table: true
    basis: exercise/warmup-load-rampup-progression-018
    basis_grade: D
  - rule: cap-fill
    trigger: after rounding, a jump between successive rungs (bar rung included) is over jump_cap_frac of working_weight -- or over jump_cap_light_frac when the jump ends at or below 0.60 of working_weight -- by more than jump_cap_tolerance_steps x load_step_kg
    action: split that gap into the fewest equal jumps under the cap, round the new rungs as above, reps of an inserted light rung = 5; stop inserting at the implement's max_rungs; if the cap still cannot be met, widen the lightest jumps first, never the last jump into the work set
    table: true
    basis: exercise/warmup-load-rampup-progression-018
    basis_grade: D
  - rule: last-rung-floor
    trigger: the ladder is built and its top rung is under last_rung_min_frac of working_weight
    action: add or move the top rung to the lightest loadable value at or above last_rung_min_frac and under working_weight; if none exists (coarse dumbbell or stack steps), keep the top rung and say so; the rung keeps 2-4 reps
    table: true
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: C
  - rule: tiny-load-fallback
    trigger: after rounding no rung is left (working_weight at or near implement_min_kg, e.g. an empty-bar press or a 2-4 kg raise)
    action: the ladder is one rung at the lightest loadable value under working_weight if one exists, else at working_weight itself, for ceil(working_reps / 2) reps at rung_rir_min or more
    table: true
    basis: exercise/warmup-ladder-builder-rules-747
    basis_grade: D
  - rule: rung-reps
    trigger: every rung
    action: reps from the template; never more reps than working_reps on a rung at or above 0.70; top rung 1-2 reps when working_reps <= 3; at least min_rung_reps; every rung stops at rung_rir_min or more in reserve
    table: true
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: D
  - rule: rung-rest
    trigger: every rung
    action: rest_light_s after rungs below 0.70 (plate-loading time counts), rest_heavy_rung_s after rungs at or above 0.70, rest_to_work_s between the last rung and the first work set
    table: true
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: D
  - rule: first-session-calibration
    trigger: weight_source none (no log for this lift on this implement, no stated number)
    action: start at a starting guess -- implement_min_kg for a novice or an unknown training status, the user's own guess otherwise; do sets of working_reps at that load and ask the RIR; RIR >= calib_easy_rir -> raise by the top of calib_step_up_(upper|lower); RIR 4-5 -> raise by its bottom; RIR within one of target_rir -> this load is today's working weight; RIR below target_rir - 1 or reps short -> lower by calib_step_down_(upper|lower) and that is today's working weight; after calib_max_sets take the last load; the sets before the found load are this lift's ladder (logged as warm-up, not as work sets)
    table: true
    basis: exercise/working-load-calibration-evidence-748
    basis_grade: D
  - rule: calibration-expect-up
    trigger: first-session-calibration with a novice
    action: expect the load to rise across calibration (novices pick 42-57% 1RM, 740; first-set RIR is under-called, 077); say "the first set should feel like 4-6 more reps were left"; never open a novice's first session with a near-failure set
    table: false
    basis: exercise/working-load-calibration-evidence-748
    basis_grade: C
  - rule: stated-weight-check
    trigger: weight_source stated or converted (a remembered number, another gym, another implement) and no log for this lift
    action: build the normal ladder from the stated number; read the first work set (030, not the ramp): reps short by stated_check_short_reps or more, or RIR at or under target_rir - 2 -> lower the remaining sets by calib_step_down; RIR at or over target_rir + stated_check_easy_rir_over -> raise by the bottom of calib_step_up; log the corrected load as the working weight
    table: true
    basis: exercise/autoregulation-vs-percentage-prescription-030
    basis_grade: D
  - rule: rep-max-report
    trigger: the user reports "X kg for N reps" for this lift and implement, N <= 10, close to failure
    action: if N is within 2 of working_reps, use X as the working weight (weight_source stated); otherwise move X one calib_step per 2 reps of difference (down for more target reps, up for fewer) and run stated-weight-check; never estimate from a set over 10 reps (740)
    table: true
    basis: exercise/working-load-calibration-evidence-748
    basis_grade: D
  - rule: barbell-to-dumbbell
    trigger: a barbell working weight is known and today's lift is the dumbbell version
    action: per-hand load = barbell working weight x ratio / 2, rounded DOWN to the rack; ratio db_ratio_flat_press for flat or incline pressing, db_ratio_standing_ohp for standing overhead press, db_ratio_default otherwise; weight_source converted
    table: true
    basis: exercise/working-load-calibration-evidence-748
    basis_grade: C
  - rule: no-machine-conversion
    trigger: a free-weight number is known and today's lift is a machine (or the reverse), or the machine is a different make
    action: no conversion; run first-session-calibration on the machine; the free-weight number may set the user's starting guess only
    table: true
    basis: exercise/machine-free-weight-equivalence-075
    basis_grade: D
  - rule: ladder-not-a-test
    trigger: a rung felt heavy, slow or easy
    action: rungs never change the working weight (080 ramp-not-a-readiness-test); only calibration sets and the first work set do
    table: false
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: D
refraction_notes:
  - note: >
      THE LADDER IS A FORMAT, NOT A FINDING. Nothing tested these exact
      percentages. What the evidence carries is the shape: a last rung near
      the working weight (080), jumps of about a fifth of the working weight
      (018), bigger steps on lower-body lifts than upper (NSCA, 740). Speak a
      ladder as "a standard way to work up", and let the user move a rung.
    grade: D
  - note: >
      DUMBBELL CONVERSION IS A START. The 0.83 and 0.93 ratios come from 12
      and 15 trained men on two pressing lifts. For a row, a lunge or a
      woman lifter the ratio is a guess, so the first work set decides.
    grade: C
  - note: >
      CALIBRATION RIR IS LOW-LEANING. 077: the first set of a lift is where
      RIR is most under-called. A calibration set called "2 left" may have
      had 3. That errs light, which is the safe side for a first session;
      the next session's stated-weight-check or normal progression corrects
      it.
    grade: C
claim: >
  Any working weight yields a warm-up ladder by one fixed recipe. Pick the
  template by working reps: 6 or fewer -> rungs at 50 / 70 / 90% of the
  working weight for upper-body lifts or 50 / 70 / 85% for lower-body lifts,
  5 / 3 / 2 reps; 7 reps -> 55 / 80%, 5 / 3 reps; 8 or more -> one rung at 75%
  for 4 reps (plus 50% x 8 if it opens the session; optional if the muscles
  are already warm). A barbell lift starts with the empty bar (10 reps before
  heavy work, 5 before moderate); a floor deadlift starts at 60 kg; dumbbells
  and machines have no bar rung and at most 3 and 4 rungs. Round each rung to
  a loadable weight, drop duplicates, fill any jump over 20% of the working
  weight (25% in the light half), keep the top rung at 75% or more, and when
  nothing is left (tiny loads) do one light rung of half the working reps.
  Rest 60 s after light rungs, 90-120 s after heavy ones, 2-3 min before the
  first work set; no rung goes closer than 4 reps to failure. With no working
  weight, calibrate: sets of the working reps from a light start, step up
  5-10% (upper) or 10-20% (lower) until a set lands near the target RIR, step
  down 2.5-5% / 5-10% after a miss. A stated or converted number is checked on
  the first work set; barbell to dumbbell is x 0.83 (pressing) or x 0.93
  (standing overhead) per pair, rounded down; machines are never converted.
reasoning: >
  080 established that the performance-relevant part of the ramp is the last
  rung near the working load and gave the rep, RIR and rest constants; 018
  gave the jump cap; 740 gave the calibration step sizes, the 10-rep estimate
  limit, the dumbbell ratios and the novice light bias. What none of them
  gives is a deterministic recipe that never fails on an edge case: an
  empty-bar press, a 300 kg squat that needs extra rungs, a dumbbell rack in
  2 kg steps, a machine with 5 kg plates, a lift with no history at all. This
  row fixes those cases as data. The upper / lower split sits in the top rung
  (90 vs 85%) because the NSCA protocol's step for a near-max set is 5-10%
  upper and 10-20% lower; the bottom of each band sets the final gap. The
  light-half 25% cap is 018's loose end, used so an 80 kg bench does not need
  five rungs. Dumbbell and machine rung caps reflect handling cost (each
  dumbbell rung is a pick-up and a kick-up), not evidence. Not contested:
  the rules restate graded rows; the open questions sit in 080's and 740's
  gaps.
---

# exercise/warmup-ladder-builder-rules-747 -- 작업 무게에서 웜업 단계 만들기 (바벨·덤벨·머신, 상체·하체, 첫 세션)

**One line:** take the working weight, pick a percent template by working
reps, start barbells at the empty bar, round to real plates, fill jumps over
a fifth of the working weight, keep the last rung at 75% or more; with no
working weight, find one in NSCA-sized steps and check it on the first work
set.

## Templates

| Working reps | Upper body | Lower body | Reps per rung |
|---|---|---|---|
| 1-6 (heavy) | bar, 50, 70, 90% | bar, 50, 70, 85% | 10 / 5 / 3 / 2 |
| 7 (middle) | bar, 55, 80% | bar, 55, 80% | 10 / 5 / 3 |
| 8+ (moderate), first of pattern | bar, 75% (+50% x 8 if first lift) | same | 5 / 4 |
| 8+, pattern already warm | 75% x 4, optional | same | 4 |

Rests: 60 s below 70%, 90-120 s from 70%, 2-3 min into the first work set.
Dumbbells and machines: no bar rung, at most 3 / 4 rungs. Floor deadlift:
first rung 60 kg.

## Worked ladders (checked by hand)

1. **Barbell bench, 80 kg x 5 (upper, heavy).** Template 40 / 56 / 72 ->
   rounded 40 / 55 / 72.5. Ladder: 20 x 10, 40 x 5, 55 x 3, 72.5 x 2, then
   80 x 5. Jumps 20 (25%, light half, allowed), 15, 17.5 (21.9%, one plate
   step over 20%, allowed), 7.5.
2. **Back squat, 140 kg x 5 (lower, heavy).** Template 70 / 98 / 119 ->
   70 / 97.5 / 120. Bar 20 -> 70 is 50 kg (35.7%, over the 25% light cap of
   35 kg) -> one rung inserted at 45. Ladder: 20 x 10, 45 x 5, 70 x 5,
   97.5 x 3, 120 x 2, then 140 x 5. Top rung 85.7%.
3. **Dumbbell incline press after a known barbell bench of 80 kg, 8 reps.**
   Converted 80 x 0.83 / 2 = 33.2 -> 32 kg per hand (rounded down). Moderate:
   one rung at 0.75 x 32 = 24 kg x 4 (plus 16 kg x 8 if it opens the
   session). First work set checks the 32 (stated-weight-check).
4. **Leg press, first session, novice, 10 reps, 5 kg stack.** Start 40 kg:
   RIR 6 -> +20% -> 48 -> 50 kg: RIR 4 -> +10% -> 55 kg: RIR 2 -> 55 kg is
   today's working weight; 40 and 50 were the ladder.
5. **Empty-bar overhead press, 20 kg x 8.** Every template rung rounds under
   the bar -> tiny-load-fallback: 20 kg x 4. **Dumbbell lateral raise,
   4 kg x 12, 2 kg rack:** 0.75 x 4 = 3 -> tie rounds down to 2 kg x 4;
   no loadable weight sits between 3 and 4 kg, so last-rung-floor keeps
   the 2 kg rung and says the rack is too coarse.

## 한국어 요약 (답변용)

- 작업 무게가 하나라도 있으면 웜업 단계는 항상 만들어진다. 본세트 반복 수로 틀을 고른다.
- 6회 이하(무거운 날): 상체는 작업 무게의 50·70·90%, 하체는 50·70·85%에서 5·3·2회. 하체의 마지막
  단계가 조금 낮은 건 하체는 한 번에 올리는 폭이 원래 더 크기 때문이다.
- 7회: 55·80%에서 5·3회. 8회 이상: 75%에서 4회 한 번. 그날 첫 운동이면 50%에서 8회를 앞에 한 번
  더 한다. 같은 부위를 이미 했으면 그 한 번도 생략해도 된다.
- 바벨은 빈 봉으로 시작한다(무거운 날 10회, 아니면 5회). 바닥에서 드는 데드리프트는 빈 봉 대신
  60kg(20kg 원판 두 장)부터 시작한다. 덤벨과 머신은 빈 봉 단계가 없고 단계는 3개·4개까지만 둔다.
- 각 단계는 실제로 끼울 수 있는 무게로 맞춘다. 한 번에 작업 무게의 20%(가벼운 구간은 25%)보다 많이
  오르면 중간 단계를 넣는다. 마지막 단계는 작업 무게의 75% 이상으로 둔다.
- 쉬는 시간: 가벼운 단계 뒤 1분, 70% 이상 단계 뒤 1분 30초~2분, 마지막 단계와 본세트 사이 2~3분.
  어떤 웜업 세트도 힘들게 하지 않는다(4회 이상 여유).
- 작업 무게를 모르는 첫 세션: 가볍게 시작해서 본세트 반복 수로 한 세트씩 하고 몇 개 더 할 수 있었는지
  묻는다. 여유가 많으면 상체 5~10%, 하체 10~20% 올리고, 목표 여유에 들어오면 그 무게로 본세트를 한다.
  처음 하는 사람은 대개 너무 가볍게 고르니 무게가 올라갈 거라고 보고 시작한다.
- 기억하는 무게나 다른 기구에서 바꾼 무게는 첫 본세트에서 확인한다. 반복이 2회 이상 모자라면 내리고,
  너무 쉬우면 조금 올린다. 웜업 세트 느낌만으로는 바꾸지 않는다.
- 바벨 벤치 무게를 덤벨로 바꿀 때는 0.83을 곱해 두 손으로 나누고, 서서 하는 숄더프레스는 0.93을
  곱한다. 둘 다 내림한다. 머신과 프리웨이트 사이는 바꾸지 않고 머신에서 새로 찾는다.
- 이 퍼센트들은 검증된 처방이 아니라 정리된 표준 방식이다. 마지막 단계가 작업 무게 가까이 가는 것만
  연구가 받쳐 준다. 사용자가 단계를 조금 바꾸고 싶어 하면 바꿔도 된다.
