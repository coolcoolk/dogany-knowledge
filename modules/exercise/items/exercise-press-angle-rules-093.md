---
# Press-angle sprint 2026-10-07.
# The engine-readable half of 092: how the composer picks the bench angle for
# a chest pressing slot, when one of two or more weekly chest-press slots
# should be a low incline, how a shoulder caution site changes the pick, and
# how the answer path must speak "is incline easier on the shoulder". A
# routing rule, not a primary finding: each rule names the graded row it rests
# on and its own basis_grade; every angle number is a labelled constant.
#
# press_angle_rules plug into existing vocabulary: 056 rungs (history-old,
# history-recent, history-unknown, current-load-pain, current-other,
# red-flag), 064 selection_rules (grip, variant drops), 076 equipment_rules
# (strength-keep-named-lift, caution-site-machine-first) and 055's pain
# ceiling. Side-agnostic: a one-sided caution (left or right shoulder) uses
# the same rules plus unilateral-caution-decouple.
id: exercise/press-angle-rules-093
domain: exercise
grade: D (selection and answer rule over 092, 064, 076, 056 and 055; the upper-chest slot rests on a C-level single trial, the shoulder rules on D mechanism and practice; every angle is a product constant)
lane: "@gym-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/incline-press-angle-upper-chest-shoulder-evidence-092"  # incline biases upper chest (C), angle EMG (C), shoulder by angle not studied (D)
  - "exercise/shoulder-pressing-selection-cuff-work-064"  # grip <= ~1.5x bi-acromial, scapular retraction, drop highest-load variants, keep pressing loaded
  - "exercise/machine-first-selection-rules-076"  # strength-keep-named-lift; caution-site-machine-first
  - "exercise/caution-severity-ladder-056"  # rungs that decide which shoulder rules fire
  - "exercise/tendon-fascia-load-management-055"  # pain ceiling used to choose between angles at a loaded shoulder
  - "exercise/harm-route-boundary-031"  # red-flag shoulder pain is routed, not coached
  - "exercise/emg-not-hypertrophy-proxy-013"  # no rule here ranks growth by EMG
  - "exercise/effective-sets-fractional-008"  # synergist counting for the front deltoid
  - "exercise/machine-free-weight-equivalence-075"  # incline on machine, Smith or dumbbell ranks equal for growth
  - "a research sprint 2026-10-07: engine-readable press_angle_rules for program compose and for answering 'is incline easier on the shoulder'"
  - "framework:GRADE -- the upper-chest slot borrows 092's C (one small trial); the angle band borrows 092's C EMG trend (deltoid up, sternal down with angle) and is a constant; the shoulder-caution, unilateral and answer rules have no outcome study behind them (D)."
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
constants:
  low_incline_deg: [15, 30]       # product, from 092: chest-slot incline band
  low_incline_default_deg: 30     # product: setting to pick when the bench allows; nearest notch otherwise
  incline_max_chest_deg: 45       # product, from 092: above this the slot is a shoulder press, not a chest slot
  incline_slot_trigger: 2         # product: weekly horizontal chest-press slots at which one becomes the low incline
  incline_front_delt_credit: 0.5  # 008 convention: an incline press set counts 0.5 toward front deltoid (aggregate convention, not a measured weight)
press_angle_rules:
  - rule: two-slots-one-low-incline
    trigger: the week holds incline_slot_trigger or more horizontal chest-press slots and primary_goal is muscle size, physique or general fitness
    action: make one slot a press at low_incline_deg (default low_incline_default_deg) and keep at least one slot flat; the incline slot does not add chest sets, it replaces a flat one
    basis: exercise/incline-press-angle-upper-chest-shoulder-evidence-092
    basis_grade: C
  - rule: one-slot-flat-default
    trigger: only one chest-press slot this week
    action: flat (or low_incline_deg if the user names upper chest as a priority); never say an incline is required to grow the upper chest
    basis: exercise/incline-press-angle-upper-chest-shoulder-evidence-092
    basis_grade: D
  - rule: named-flat-lift-stays
    trigger: primary_goal names the flat bench press (powerlifting, a bench target or test)
    action: flat bench stays the primary chest slot (076 strength-keep-named-lift); the low incline fills a later accessory slot
    basis: exercise/machine-first-selection-rules-076
    basis_grade: B
  - rule: chest-slot-angle-cap
    trigger: any chest slot set to an incline
    action: angle within low_incline_deg; never above incline_max_chest_deg; a steeper press is logged as a shoulder-press slot, not a chest slot
    basis: exercise/incline-press-angle-upper-chest-shoulder-evidence-092
    basis_grade: C
  - rule: incline-equipment-free
    trigger: choosing the implement for the incline slot
    action: barbell, dumbbell, Smith or machine incline rank equal for growth; pick by availability and the 076 rules
    basis: exercise/machine-free-weight-equivalence-075
    basis_grade: C
  - rule: count-incline-sets
    trigger: weekly volume tally
    action: an incline press set counts 1 toward chest and incline_front_delt_credit toward front deltoid, same as a flat press; no extra upper-chest credit is computed
    basis: exercise/effective-sets-fractional-008
    basis_grade: D
  - rule: shoulder-angle-by-response
    trigger: shoulder at 056 rung history-old, history-recent, history-unknown or current-load-pain
    action: do not pick incline (or flat) as the shoulder-sparing press; pick the angle by the user's own response -- try the planned angle at a light working load, keep it if within the 055 ceiling, otherwise try the other angle (flat or low_incline_deg) before dropping the pattern; record which angle the user tolerates and reuse it
    basis: exercise/incline-press-angle-upper-chest-shoulder-evidence-092
    basis_grade: D
  - rule: shoulder-steep-first-out
    trigger: shoulder at rung history-recent, history-unknown or current-load-pain, or the user reports pain when the arm is raised overhead
    action: drop inclines above low_incline_deg first (they move toward overhead flexion and load the front deltoid more); keep flat and low incline as candidates
    basis: exercise/incline-press-angle-upper-chest-shoulder-evidence-092
    basis_grade: D
  - rule: shoulder-grip-and-scapula-over-angle
    trigger: shoulder at any caution rung, at any angle
    action: apply 064 bench-grip-max-1.5-biacromial and scapular retraction to flat and incline alike; when a press hurts, change grip width, range and implement before blaming the angle
    basis: exercise/shoulder-pressing-selection-cuff-work-064
    basis_grade: D
  - rule: shoulder-machine-or-dumbbell-incline
    trigger: shoulder at rung history-recent, history-unknown or current-load-pain and an incline slot is kept
    action: machine or dumbbell incline first (076 caution-site-machine-first); dumbbells may use a neutral or semi-neutral grip if that is what the user tolerates
    basis: exercise/machine-first-selection-rules-076
    basis_grade: D
  - rule: unilateral-caution-decouple
    trigger: the caution site is one shoulder (left or right)
    action: prefer dumbbells or an independent-arm machine for both chest slots so each side runs its own range and load; the caution side sets the range; do not add load to the good side to make up the difference
    basis: exercise/caution-severity-ladder-056
    basis_grade: D
  - rule: shoulder-route-not-coach
    trigger: shoulder at rung current-other or red-flag
    action: no angle rule applies; pain-triage first (064 route-not-coach)
    basis: exercise/harm-route-boundary-031
    basis_grade: D
answer_rules:
  - question: is incline easier (or safer) on the shoulder?
    answer: not established -- no study compares shoulder pain, injury or joint load between incline and flat; a steeper bench loads the front deltoid more and moves toward overhead; some people tolerate one and not the other; grip width and shoulder-blade position have more (model-level) support; try both at a light load and keep the one that stays within the pain rule
    basis: exercise/incline-press-angle-upper-chest-shoulder-evidence-092
    basis_grade: D
  - question: do I need incline to grow my upper chest?
    answer: no -- flat pressing grows the upper chest too; one small trial in beginners found incline biased growth toward the upper chest; with two or more chest presses a week, making one a low incline is a reasonable default
    basis: exercise/incline-press-angle-upper-chest-shoulder-evidence-092
    basis_grade: C
  - question: what angle is best?
    answer: no settled best; about 15-30 degrees, not past 45 -- steeper shifts work to the front deltoid and away from the middle and lower chest
    basis: exercise/incline-press-angle-upper-chest-shoulder-evidence-092
    basis_grade: C
never_say:
  - incline is easier on the shoulder / safer for the shoulder
  - flat bench is bad for the shoulders
  - you need incline press to build the upper chest
  - 45 degrees (or 30 degrees) is the proven best angle
  - incline isolates the upper chest
  - this angle has more EMG so it builds more muscle
refraction_notes:
  - note: >
      ONE OF TWO PRESSES AS A LOW INCLINE IS A DEFAULT, NOT A FINDING ABOUT
      ROTATION. The trial behind it compared incline-only, flat-only and a
      split, and the split did not beat flat for the upper chest. So the
      rule is a reasonable way to give the upper chest a direct slot while
      keeping a flat slot for the middle and lower chest, not a proven
      combination effect.
    grade: C
  - note: >
      AT A SHOULDER CAUTION SITE THE ANGLE IS PICKED BY RESPONSE. There is no
      outcome study saying either angle is gentler on the shoulder, so the
      engine treats both as candidates, removes steep inclines first, keeps
      the 064 grip and scapula rules, and keeps whichever angle the user
      presses within the 055 ceiling.
    grade: D
  - note: >
      A ONE-SIDED SHOULDER IS A CASE FOR INDEPENDENT ARMS. With a barbell
      both arms share one bar path and the good side tends to carry the
      bar; dumbbells or an independent-arm machine let the caution side set
      its own range. Practice reasoning, not tested.
    grade: D
claim: >
  When the week holds two or more horizontal chest presses and the goal is
  muscle size or physique, the composer makes one of them a low incline
  (about 15-30 degrees, default 30, never past 45) and keeps at least one
  flat; with one press, flat is the default unless the user names the upper
  chest. A flat bench the user wants to get stronger at stays the primary
  slot. Incline sets count like flat sets. At a shoulder caution site,
  neither angle is assumed to be shoulder-friendly: steep inclines go first,
  the 064 grip and scapula rules apply at every angle, machine or dumbbell
  versions come first, and the angle is chosen by which one the user presses
  within the pain rule; a one-sided shoulder favours dumbbells or
  independent-arm machines. Asked "is incline easier on the shoulder?", the
  answer is that it has not been shown, with the reasons and the try-both
  method.
reasoning: >
  092 supplies the only growth direction (incline biases the upper chest,
  one small trial) and the consistent EMG trend (front deltoid up, middle and
  lower chest down as the bench rises) that sets the band and the 45-degree
  cap; the band itself is a constant because the EMG peak is unsettled. The
  named-lift keep is 076's B-backed specificity rule. Every shoulder rule is
  D: there is no outcome study by angle, so the engine falls back to 064
  (grip, scapula, variant drops), 076 (machine-first at a caution site),
  056's rungs and 055's pain ceiling, and lets the user's own response pick
  the angle. The answer rules and never_say list exist because "incline is
  easier on the shoulder" circulates as fact and 092 found no study behind
  it. injury_history is hard with block_specifics: without the user's words
  on the shoulder's rung, the shoulder rules do not fire on a specific site.
---

# exercise/press-angle-rules-093 -- 프레스 각도 고르기 규칙

**한 줄 그림:** 가슴 프레스가 주 2회 이상이면 하나는 15-30도 인클라인, 하나는 플랫. 어깨가
걸리는 사람은 "인클라인이 어깨에 편하다"고 가정하지 않고, 직접 해 보고 덜 아픈 각도를 쓴다.

## The rules (engine-readable: `press_angle_rules`)

| Rule | When | Action | Basis |
|---|---|---|---|
| two-slots-one-low-incline | 2+ chest presses / week, size or physique goal | one slot at 15-30 degrees, keep one flat | 092 |
| one-slot-flat-default | one chest press | flat, or low incline if upper chest named | 092 |
| named-flat-lift-stays | goal names flat bench | flat stays primary; incline as accessory | 076 |
| chest-slot-angle-cap | any incline chest slot | 15-30, never above 45 | 092 |
| incline-equipment-free | choosing implement | barbell = dumbbell = Smith = machine | 075 |
| count-incline-sets | weekly tally | 1 chest, 0.5 front delt, like flat | 008 |
| shoulder-angle-by-response | shoulder caution rung | try angle light; keep what stays under 055 ceiling | 092, 055 |
| shoulder-steep-first-out | recent / unknown / current or overhead pain | drop >30 degree inclines first | 092 |
| shoulder-grip-and-scapula-over-angle | any caution rung | 064 grip and scapula at every angle | 064 |
| shoulder-machine-or-dumbbell-incline | recent / unknown / current | machine or dumbbell incline first | 076 |
| unilateral-caution-decouple | one shoulder | dumbbells / independent arms; bad side sets range | 056 |
| shoulder-route-not-coach | current-other, red-flag | triage first | 031 |

## 한국어 요약 (답변용)

- 가슴 프레스가 주에 두 번 이상이고 목표가 근육·몸매면 하나는 15-30도(가능하면 30도) 인클라인,
  하나는 플랫으로 둔다. 인클라인은 세트를 더하는 게 아니라 플랫 하나를 바꾸는 것이다.
- 프레스가 주 1회뿐이면 플랫이 기본이다. 윗가슴을 우선한다고 하면 낮은 인클라인으로 한다.
  "윗가슴은 인클라인 없이는 안 큰다"는 말은 하지 않는다.
- 벤치프레스 기록이 목표면 플랫이 주 운동으로 남고 인클라인은 보조 자리로 간다.
- 45도를 넘기면 가슴 운동이 아니라 숄더 프레스로 센다.
- 어깨가 걸리는 사람: 인클라인이든 플랫이든 "어깨에 편한 쪽"으로 미리 정하지 않는다. 가벼운
  무게로 해 보고 통증 기준 안에 드는 각도를 쓰고, 그 결과를 기억해 다음에도 쓴다. 최근 다쳤거나,
  언제 다쳤는지 모르거나, 지금 아프거나, 팔을 머리 위로 들 때 아프면 가파른 인클라인부터 뺀다.
  그립은 어깨너비 1.5배 이내, 날개뼈는 모으고, 머신이나 덤벨 버전을 먼저 쓴다.
- 한쪽 어깨만 문제면 덤벨이나 양팔이 따로 움직이는 머신으로 해서 아픈 쪽이 범위를 정하게 한다.
  성한 쪽에 무게를 더 얹어 메우지 않는다.
- "인클라인이 어깨에 더 편해요?"라는 질문에는: 연구로 확인된 적이 없다. 벤치를 세울수록 앞어깨
  부담이 커지고 머리 위로 미는 동작에 가까워진다. 사람마다 맞는 쪽이 다르니 둘 다 가볍게 해 보고
  덜 아픈 쪽을 쓰자고 답한다.
