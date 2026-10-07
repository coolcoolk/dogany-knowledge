---
# Drill-cue sprint 2026-10-07.
# The engine-readable half of 740: for each of the eleven mobility / prep
# drills the prep catalog uses, the ordered execution steps, ONE external-focus
# cue, ONE common fault with its fix, and what counts as 1 rep (and whether the
# count is per side, per direction or a whole cycle), so the plan line and the
# coach text can never say "10" without a unit. A curation rule, not a primary
# finding: each drill names the graded row it rests on and its own
# basis_grade; every dose is a labelled product constant or a value copied
# from 740 / 074.
#
# drill_cues plug into existing vocabulary: 065 prep_policy (shoulder-primer
# components), 074 shoulder_prehab (external_rotation family dose), 081
# core_rules (bird dog interchangeable with dead bug), 037 controlled-movement
# slot (roll-down), 022 (the whole warm-up carries the effect). drill_id values
# are snake_case catalog keys proposed here; the product catalog's own keys
# are mapped by the composer, not by this row.
id: exercise/drill-cues-rep-units-741
domain: exercise
grade: D (curated step order, fault and rep-unit definitions for eleven prep drills over 740, 074, 065, 081 and 037; cue wording follows 740's external-focus meta-analysis (B, indirect); every step list, fault pick, rep unit and default dose is coaching consensus or product judgement)
lane: "@gym-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/drill-cue-rep-unit-evidence-740"  # external-focus cues (B), CERT rep-unit point (D), per-drill measurement (C/D)
  - "exercise/shoulder-prehab-dose-074"  # band external rotation: OSTRC 3 x 8-16, progress reps then band then weight; reduce load on pain
  - "exercise/shoulder-prep-specific-vs-general-065"  # shoulder primer 1-2 light sets, sub-fatiguing; halo / ER interchangeable
  - "exercise/core-functional-accessory-carry-081"  # bird dog interchangeable with dead bug / Pallof / plank
  - "exercise/ideal-pilates-controlled-movement-037"  # roll-down as articulation, not a hollow hold
  - "exercise/dynamic-warmup-same-day-performance-022"  # the drill is a part of the warm-up, not a lever by itself
  - "exercise/harm-route-boundary-031"  # pain during a drill routes to triage, not a cue fix
  - "a research sprint 2026-10-07: engine-readable execution cues and rep-unit definitions (ordered steps, one common fault, what counts as 1 rep / per side) for roll-down, bear crawl, arm circles, world's greatest stretch, leg swing, halo, thoracic rotation, bird dog, cat-cow, plate pullover, band external rotation"
  - "framework:GRADE -- cue wording borrows 740's B (motor-skill meta-analysis, indirect); three drills have C-level measurement of the position or the muscle (leg swing, thoracic rotation, plate pullover) and band ER sits inside B/C shoulder programmes (074); no study defines a rep, orders the steps, or names the commonest fault for any of the eleven (D)."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
constants:
  side_modes: [whole, per_side, per_direction, per_side_per_direction, distance_or_time]  # the only legal values of side_mode
  count_display_ko:
    whole: "{n}회"
    per_side: "한쪽 {n}회 (양쪽 각각)"
    per_direction: "방향별 {n}회"
    per_side_per_direction: "한쪽, 방향별 {n}회"
    distance_or_time: "{m}m 또는 {s}초"
  hold_display_ko: "한 번에 {h}초 버티기"
  prep_set_effort: sub-fatiguing   # every prep drill stops well short of fatigue (065 no-cuff-fatigue-before-pressing)
drill_cues:
  - drill_id: roll_down
    name_ko: 롤다운
    equipment: none
    steps:
      - stand tall, feet hip-width, knees soft, arms hanging
      - breathe out, nod the chin to the chest and peel the spine down from the top, one segment at a time, arms hanging toward the floor
      - stop where the hamstrings or back say so (hands need not touch the floor); breathe in at the bottom
      - breathe out and roll back up from the bottom of the spine, stacking it piece by piece, head last
    external_cue: lower the spine like a chain being laid on the floor, link by link
    common_fault: hinging at the hips with a flat back and dropping quickly, so the spine does not articulate
    fault_fix: bend the knees more and slow down; start the roll from the head, not the hips
    rep_unit: one roll down and back up to standing
    side_mode: whole
    default_dose:
      sets: 1
      reps: 5
      note: product constant; Pilates text uses 6
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: D
  - drill_id: bear_crawl
    name_ko: 베어 크롤
    equipment: none
    steps:
      - on hands and toes, hands under shoulders, knees under hips
      - lift the knees a few centimetres off the floor; back flat, hips level with the shoulders
      - move the opposite hand and foot forward together in short steps
      - keep the knees low and the hips quiet the whole way; then the other pair
    external_cue: crawl as if a glass of water sits on the low back
    common_fault: hips rising high or swaying side to side, knees climbing up
    fault_fix: shorter steps and slower; knees stay just off the floor
    rep_unit: one step = an opposite hand and foot moving together; a left plus a right step = one cycle
    side_mode: distance_or_time
    count_alt: when counted, count steps per side (8 per side = 16 steps)
    default_dose:
      sets: 2
      distance_m: 10
      time_s: 20
      note: product constant; forward then backward allowed
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: D
  - drill_id: arm_circles
    name_ko: 팔 돌리기
    equipment: none
    steps:
      - stand tall, arms straight out to the sides at shoulder height, palms down
      - make small circles, growing gradually larger, both arms together
      - finish the forward count, then reverse to backward circles
    external_cue: draw circles on the walls with the fingertips
    common_fault: shoulders shrugging up to the ears and the circles turning fast and floppy
    fault_fix: shoulders down, smaller and slower circles, arms long
    rep_unit: one full circle (both arms together)
    side_mode: per_direction
    default_dose:
      sets: 1
      reps: 10
      note: product constant; patient pages give 10-20 per direction
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: D
  - drill_id: worlds_greatest_stretch
    name_ko: 월드 그레이티스트 스트레칭
    equipment: none
    steps:
      - from standing, step one foot forward into a long lunge; back leg long, back knee off the floor
      - put both hands on the floor inside the front foot
      - drop the inside elbow toward the front instep (as far as it goes)
      - bring the hand back down and rotate the chest open, reaching that arm to the ceiling, eyes on the hand
      - hand back to the floor, step back to standing (or straighten the front knee and shift the hips back first) and switch sides
    external_cue: reach the top hand to the ceiling and follow it with the eyes
    common_fault: back knee and hips sagging toward the floor, and the turn coming from the low back with a short arm reach
    fault_fix: keep the back leg long and squeeze the back glute; turn from the upper back and let the eyes lead
    rep_unit: the whole sequence once on one side
    side_mode: per_side
    alternate: sides alternate each rep
    default_dose:
      sets: 1
      reps: 3
      note: product constant; reps are per side
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: D
  - drill_id: leg_swing
    name_ko: 레그 스윙
    equipment: wall or rack for balance
    steps:
      - stand side-on to a wall, inside hand on it, trunk tall
      - swing the outside leg forward and back like a pendulum, small at first then larger
      - keep the trunk still and the standing knee soft
      - for the side-to-side version, face the wall and swing the leg across the body and out
      - finish the count, turn round and do the other leg
    external_cue: swing the foot like a pendulum, toes toward the ceiling in front and the wall behind
    common_fault: the trunk rocking and the low back arching to make the swing bigger
    fault_fix: smaller swings, ribs down, let the range grow only as far as the trunk stays still
    rep_unit: one forward plus one back swing (one full pendulum)
    side_mode: per_side_per_direction
    note_plane: per_direction here means per plane (front-back, side-to-side)
    default_dose:
      sets: 1
      reps: 10
      note: product constant; per leg, per plane; no study sets the count
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: C
  - drill_id: halo
    name_ko: 헤일로
    equipment: light plate, kettlebell or dumbbell
    steps:
      - stand tall, glutes and abdominals lightly braced, hold the weight at the chest by its edges (or the kettlebell by the horns)
      - circle it around the head close to the the curator, passing behind the neck
      - return to the chest, then circle the other way
    external_cue: draw a tight halo around the head with the weight
    common_fault: ribs flaring and the low back arching as the weight passes behind, or the head ducking out of the way
    fault_fix: lighter weight, ribs down, head still; the arms move around the head, not the head around the arms
    rep_unit: one full circle around the head
    side_mode: per_direction
    alternate: alternate direction each rep, or finish one direction then the other
    default_dose:
      sets: 1
      reps: 5
      note: product constant; light load, sub-fatiguing (065)
    basis: exercise/shoulder-prep-specific-vs-general-065
    basis_grade: D
  - drill_id: thoracic_rotation
    name_ko: 흉추 회전 (네발 자세)
    equipment: none
    steps:
      - kneel on all fours, then sit the hips back toward the heels to lock the low back
      - one hand on the floor under the shoulder, the other hand behind the head
      - turn the elbow down toward the supporting wrist
      - then rotate up, opening the elbow toward the ceiling, eyes following the elbow
      - hips stay still; finish the count and switch sides
    external_cue: point the elbow at the ceiling and follow it with the eyes
    common_fault: the hips shifting or rotating so the low back does the turn
    fault_fix: sit the hips further back toward the heels and keep them pinned; the range will look smaller but it is the upper back
    rep_unit: one rotation down and up to the open end and back
    side_mode: per_side
    default_dose:
      sets: 1
      reps: 6
      note: product constant; per side
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: C
  - drill_id: bird_dog
    name_ko: 버드독
    equipment: none
    steps:
      - on all fours, hands under shoulders, knees under hips, back flat
      - brace lightly, then reach one arm forward and the opposite leg back until both are level with the trunk
      - hold briefly (up to about 10 s) without the hips tilting
      - return hand and knee to the floor (or just above it) and switch to the other pair
    external_cue: reach the hand and the heel to opposite walls, a glass of water balanced on the low back
    common_fault: lifting the leg too high so the low back arches and the hip rotates open
    fault_fix: leg only to hip height, reach long rather than high; hips stay square to the floor
    rep_unit: one arm plus opposite-leg reach and return; the side is named by the reaching arm (right arm with left leg = one right-side rep)
    side_mode: per_side
    alternate: sides alternate each rep
    hold_s: [5, 10]
    default_dose:
      sets: 1
      reps: 5
      hold_s: 5
      note: product constant; per side; McGill material uses holds up to about 10 s
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: D
  - drill_id: cat_cow
    name_ko: 캣카우
    equipment: none
    steps:
      - on all fours, hands under shoulders, knees under hips
      - breathe out and round the whole back up, tucking the chin and the tailbone (cat)
      - breathe in and let the belly sink, lifting the chest and the tailbone, eyes forward (cow)
      - move slowly through a comfortable range, no end-range holds
    external_cue: push the floor away and round toward the ceiling, then let the chest slide forward and up
    common_fault: moving only the neck or only the low back, and forcing the ends of the range
    fault_fix: slower, spread the motion along the whole back, stop short of strain
    rep_unit: one cat plus one cow (one full cycle)
    side_mode: whole
    default_dose:
      sets: 1
      reps: 6
      note: product constant inside McGill's 5-8 cycles
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: D
  - drill_id: plate_pullover
    name_ko: 플레이트 풀오버
    equipment: light plate or dumbbell, flat bench
    steps:
      - lie on the bench, feet flat, hold the plate over the chest with both hands, elbows slightly bent
      - keep the elbow bend fixed and lower the plate in an arc behind the head
      - stop when the upper arms reach the ears or the ribs start to lift
      - pull the plate back over the chest along the same arc
    external_cue: draw a wide rainbow with the plate, ribs pinned to the bench
    common_fault: ribs flaring and the low back arching at the bottom, or the elbows bending so it turns into a triceps extension
    fault_fix: lighter plate, breathe out on the way down, keep the elbow angle locked and shorten the arc
    rep_unit: one lower behind the head and return
    side_mode: whole
    default_dose:
      sets: 1
      reps: 10
      note: product constant; light, sub-fatiguing in prep
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: C
  - drill_id: band_external_rotation
    name_ko: 밴드 외회전
    equipment: light band anchored at elbow height (cable interchangeable, 065)
    steps:
      - stand side-on to the anchor, band in the outside hand, elbow bent 90 deg and pinned to the side (a rolled towel between elbow and ribs)
      - start with the forearm across the belly
      - rotate the forearm out, away from the belly, keeping the elbow on the towel
      - return slowly; finish the count, turn round and do the other arm
    external_cue: swing the hand out like a door on its hinge, the elbow is the hinge
    common_fault: the elbow drifting away from the side and the trunk turning to make the range
    fault_fix: squeeze the towel, stop the rotation where the elbow would leave; lighter band
    rep_unit: one rotation out and back
    side_mode: per_side
    default_dose:
      sets: 2
      reps: 12
      note: inside 074's 8-16; prep 1-2 light sets per 065, strength dose lives in 074
    basis: exercise/shoulder-prehab-dose-074
    basis_grade: C
drill_rules:
  - rule: unit-always-shown
    trigger: any drill line in a plan, a brief or a chat answer
    action: render the count with the drill's side_mode template (count_display_ko); never a bare number for a per_side, per_direction or distance_or_time drill
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: D
  - rule: per-side-means-each-side
    trigger: side_mode per_side or per_side_per_direction
    action: the prescribed n is done on EACH side; logs store n per side, not the total; alternating sides does not halve the count
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: D
  - rule: one-cue-one-fault
    trigger: coaching text for a drill
    action: show the steps, then at most one external_cue and one common_fault with its fix; do not stack internal muscle cues
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: B
  - rule: hold-counts-as-rep
    trigger: a drill with hold_s (bird dog)
    action: one hold is one rep; the display names both ("한쪽 5회, 한 번에 5초 버티기")
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: D
  - rule: pain-is-not-a-cue-problem
    trigger: the user reports pain (not stretch or effort) during a drill
    action: stop the drill, no cue fix offered as the answer; a caution site follows 056 / 057 / 074 pain rules; red flags route (031)
    basis: exercise/harm-route-boundary-031
    basis_grade: D
  - rule: drill-is-not-a-lever
    trigger: the user asks which drill improves the lift or prevents injury
    action: say the warm-up as a whole helps and no single drill here is shown better than another (022, 065); pick by the position the session needs and by preference
    basis: exercise/dynamic-warmup-same-day-performance-022
    basis_grade: B
answer_rules:
  - question: does 10 reps mean each side?
    answer: for one-sided drills (world's greatest stretch, leg swing, thoracic rotation, bird dog, band external rotation) the number is per side; arm circles and halos are per direction; cat-cow, roll-down and pullover count the whole movement; bear crawl goes by distance or time
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: D
  - question: what counts as one leg swing?
    answer: one swing forward and back is one rep; do the count for each leg and, if both are planned, for front-back and side-to-side separately
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: D
  - question: is the pullover a lat exercise?
    answer: it works chest and lats, the chest more in the one EMG study; in a warm-up it is there to open the overhead position
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: C
  - question: should cat-cow be held as a stretch?
    answer: no, it is a slow movement through a comfortable range, about 5-8 cycles
    basis: exercise/drill-cue-rep-unit-evidence-740
    basis_grade: D
never_say:
  - 10 reps (bare, for a one-sided or two-direction drill)
  - this drill activates the glutes / lats so the lift will be stronger
  - the pullover isolates the lats
  - push through the pain to get the range
  - hold cat-cow at the end range to stretch the spine
refraction_notes:
  - note: >
      THE STEP LISTS ARE CURATED, NOT TESTED. Each drill's order follows the
      way it is commonly taught; no study compared orders, and the common
      fault picked is the one most often corrected in coaching text, not one
      observed in a sample.
    grade: D
  - note: >
      DOSES ARE PRODUCT NUMBERS. Only band external rotation borrows a
      trial-programme range (074's 8-16); the rest are short, sub-fatiguing
      prep counts chosen to fit a warm-up of a few minutes.
    grade: D
  - note: >
      A NOVICE NEEDS THE FAULT LINE MORE. A trained lifter usually needs only
      the unit and the cue; a beginner benefits from the fault and its fix
      on first exposure. The composer can drop the fault line after the user
      has logged the drill a few times.
    axis: training_status
    grade: D
claim: >
  Each of the eleven prep drills is written as ordered steps, one
  external-focus cue, one common fault with its fix, and a rep unit with a
  side mode: whole movement (roll-down, cat-cow, plate pullover), per side
  (world's greatest stretch, thoracic rotation, bird dog, band external
  rotation), per direction (arm circles, halo), per leg and per plane (leg
  swing), or distance / time (bear crawl, steps counted per side if counted).
  A per-side count is done on each side and logged per side; a bird-dog hold
  is one rep. The count is never shown without its unit. Pain during a drill
  stops it and routes to the pain rules rather than a cue fix, and no drill
  is sold as a lever on the lift.
reasoning: >
  740 shows that cue wording is the only part with outcome evidence
  (external focus, indirect), that three drills have position or muscle
  measurement, and that nothing defines a rep. The rep units chosen here
  follow how the drills are written in the practitioner sources 740 read
  (circles per direction, swings as a pendulum, cat-cow as a cycle, bird dog
  and lunge-rotation per side) and the CERT demand that dose be replicable.
  side_mode is an enum so the brief and the logger render the same unit.
  Bear crawl is distance or time because step counting is error-prone while
  moving; the per-side step count is the fallback. The pain rule and the
  not-a-lever rule keep the drill text inside 022 / 065 / 031. injury_history
  is soft: a caution site changes the dose rules of 074 / 057, not the cue.
---

# exercise/drill-cues-rep-units-741 -- 준비 운동 11가지: 동작 순서, 큐 하나, 흔한 실수 하나, "1회"의 단위

**한 줄 그림:** 모든 준비 동작은 순서대로 적은 단계, 결과를 말하는 큐 하나, 흔한 실수와 고치는 법 하나,
그리고 단위가 붙은 횟수로 내보낸다. 한쪽 동작은 "한쪽 n회", 방향이 있는 동작은 "방향별 n회", 베어 크롤은
거리나 시간이다.

## Rep units (engine-readable)

| Drill | 1 rep = | Side mode | Default (product) |
|---|---|---|---|
| roll-down | roll down and back up | whole | 5 |
| bear crawl | opposite hand + foot step; L+R = cycle | distance / time | 2 x 10 m or 20 s |
| arm circles | one full circle, both arms | per direction | 10 each way |
| world's greatest stretch | whole sequence on one side | per side | 3 a side |
| leg swing | one forward + back swing | per leg, per plane | 10 |
| halo | one circle around the head | per direction | 5 each way |
| thoracic rotation | rotate down, up and back | per side | 6 a side |
| bird dog | one reach and return (one hold) | per side | 5 a side, 5 s hold |
| cat-cow | one cat + one cow | whole | 6 |
| plate pullover | lower behind head and return | whole | 10 |
| band external rotation | rotate out and back | per side (arm) | 2 x 12 a side |

## 한국어 요약 (답변용)

- 횟수에는 항상 단위를 붙인다. 월드 그레이티스트 스트레칭, 레그 스윙, 흉추 회전, 버드독, 밴드 외회전은 "한쪽
  n회"이고 양쪽을 각각 n회 한다. 번갈아 해도 횟수가 반으로 줄지 않는다. 팔 돌리기와 헤일로는 "방향별 n회",
  캣카우·롤다운·풀오버는 동작 전체가 1회, 베어 크롤은 거리(10m)나 시간(20초)으로 센다.
- 롤다운: 숨을 내쉬며 턱을 당기고 머리부터 척추를 한 마디씩 말아 내려간다. 내려간 만큼에서 숨을 들이쉬고,
  아래부터 한 마디씩 쌓아 올라온다. 흔한 실수는 허리를 편 채 엉덩이만 접는 것. 무릎을 더 굽히고 천천히 한다.
- 베어 크롤: 무릎을 바닥에서 몇 cm만 띄우고, 반대쪽 손과 발을 함께 짧게 옮긴다. 엉덩이가 솟거나 좌우로
  흔들리면 보폭을 줄이고 느리게 한다.
- 팔 돌리기: 팔을 어깨 높이로 뻗고 작은 원에서 큰 원으로, 앞으로 다 하고 뒤로. 어깨가 귀로 올라가면 원을
  작게, 천천히.
- 월드 그레이티스트 스트레칭: 긴 런지 → 양손을 앞발 안쪽 바닥에 → 안쪽 팔꿈치를 앞발 쪽으로 내리기 → 가슴을
  열며 팔을 천장으로, 눈은 손을 따라간다 → 돌아와 반대쪽. 한 번의 전체 순서가 한쪽 1회. 뒷다리가 처지면 뒷다리를
  길게 펴고 엉덩이에 힘을 준다.
- 레그 스윙: 벽을 옆에 두고 다리를 시계추처럼 앞뒤로. 앞-뒤 한 번이 1회, 다리마다, 앞뒤와 옆으로를 따로 센다.
  상체가 흔들리면 스윙을 작게 한다.
- 헤일로: 가벼운 원판을 가슴 앞에서 머리 둘레로 바짝 붙여 한 바퀴, 방향을 바꿔 반복. 뒤로 넘길 때 허리가
  꺾이면 무게를 줄이고 갈비뼈를 내린다.
- 흉추 회전: 네발 자세에서 엉덩이를 발뒤꿈치 쪽으로 앉혀 허리를 잠그고, 한 손은 머리 뒤에. 팔꿈치를 아래로
  넣었다가 천장으로 열고, 눈이 팔꿈치를 따라간다. 엉덩이가 돌면 더 뒤로 앉힌다.
- 버드독: 네발 자세에서 한 팔과 반대 다리를 몸통 높이까지 뻗고 잠깐(5-10초) 버틴 뒤 돌아와 반대쪽. 한 번
  버티기가 1회. 다리를 너무 높이 들어 허리가 꺾이는 게 흔한 실수다. 다리는 엉덩이 높이까지만, 높이보다 길게.
- 캣카우: 내쉬며 등을 둥글게(캣), 들이쉬며 배를 내리고 가슴을 앞으로(카우). 캣 한 번 + 카우 한 번이 1회.
  끝 범위에서 버티지 않고 편한 범위에서 천천히 5-8번.
- 플레이트 풀오버: 벤치에 누워 팔꿈치 각도를 고정하고 원판을 머리 뒤로 호를 그리며 내렸다가 가슴 위로 돌아온다.
  갈비뼈가 들리거나 팔꿈치가 접히면 원판을 가볍게 하고 범위를 줄인다. 광배근 고립 운동이 아니다.
- 밴드 외회전: 팔꿈치를 90도로 옆구리에 붙이고(수건 끼우기) 팔뚝을 바깥으로 돌렸다가 천천히 돌아온다. 팔마다
  센다. 팔꿈치가 떨어지거나 몸통이 돌면 밴드를 약하게 하고 범위를 줄인다.
- 동작 중 늘어나는 느낌이 아니라 통증이 오면 멈춘다. 큐를 고쳐서 해결할 문제가 아니다. 어떤 준비 동작도 그것
  하나로 본운동 기록을 올리거나 부상을 막는다고 말하지 않는다.
