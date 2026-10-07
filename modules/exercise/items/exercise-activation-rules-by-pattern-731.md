---
# Activation sprint 2026-10-07.
# The engine-readable half of 730: whether the session builder puts a short
# activation / stabilizer primer in front of a heavy free-weight compound,
# which drills it may offer per movement pattern, how much, where in the
# warm-up, and what it must never do (fatigue the lift's own muscles). A
# routing rule, not a primary finding: each rule names the graded row it
# rests on and its own basis_grade; every number is a labelled product
# constant or a value copied from a named row.
#
# activation_rules plug into existing vocabulary: 056 rungs, 065 prep_policy
# (shoulder-primer at a shoulder caution rung), 078 knee_prep (knee caution
# site), 080 ramp_rules (the specific ramp), 081 trunk placement, 091 short
# session trimming. The patterns are the five the composer already tags:
# horizontal_press, vertical_press, squat, hinge, row. Where 065 or 078
# already decides the prep for a caution site, that row governs and this one
# defers to it.
id: exercise/activation-rules-by-pattern-731
domain: exercise
grade: D (selection and placement rule over 730, 065, 078, 080 and 081; the ramp-first rule rests on borrowed review-level evidence, the no-pre-fatigue rule on small consistent crossovers, the drill menus, the load trigger and every dose are product judgement)
lane: "@gym-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/activation-priming-by-pattern-evidence-730"  # glute activation mixed vs control warm-up (C); pre-fatigue lowers the compound (C); no primer tested for press, row, trunk (D)
  - "exercise/shoulder-prep-specific-vs-general-065"  # prep_policy: specific ramp for all; shoulder-primer only at a shoulder caution rung; no-cuff-fatigue-before-pressing
  - "exercise/warmup-ramp-sets-heavy-compounds-080"  # ramp_rules: the specific ramp before heavy compounds
  - "exercise/knee-prep-hip-adductor-abductor-078"  # knee_prep at a knee caution site
  - "exercise/core-functional-accessory-carry-081"  # fatiguing trunk work after the main lifts; light bracing / dead bug as warm-up is fine
  - "exercise/serratus-anterior-integration-019"  # serratus drills as a pre-set cue (practitioner)
  - "exercise/caution-severity-ladder-056"  # rungs
  - "exercise/short-session-rules-091"  # what drops first when time is short
  - "exercise/emg-not-hypertrophy-proxy-013"  # EMG activation is not an outcome
  - "a research sprint 2026-10-07: engine-readable activation_rules -- pattern to drills, load trigger, dose, placement, fatigue boundary"
  - "framework:GRADE -- ramp-first borrows 065 / 080's review-level evidence; no-pre-fatigue borrows 730's small consistent crossovers at 10RM to failure (C); the drill menus, the heavy-load trigger, the one-set dose, the placement before the ramp and the drop-first order have no outcome trial behind them (D)."
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
  primer_drills_max: 2             # product: drills per pattern per session, total across the warm-up
  primer_sets_per_drill: 1         # product: one set (065's shoulder primer allows 1-2 at a caution rung; 065 governs there)
  primer_reps: [8, 12]             # product; Crow 2012 / Comyns 2015 glute series used about 10 per exercise
  primer_effort: far from failure (5+ reps in reserve, light band / plate / body weight)  # product; 730 fatigue boundary
  primer_minutes_max: 3            # product: the primer's whole time budget
  heavy_trigger_reps_max: 6        # product: working sets of <= 6 reps (or >= 80% 1RM) count as heavy for this rule
  heavy_trigger_pct_1rm: 80        # product: same trigger expressed as load
  primer_before_ramp: true         # product: primer, then ramp; never between the top ramp set and the first working set (Comyns 2015 jump drop 0.5-6 min after a glute series)
inputs:
  - pattern            # horizontal_press | vertical_press | squat | hinge | row -- of the first heavy compound of the session
  - working_reps       # target reps of its working sets
  - site_rungs         # 056 rung per caution site (shoulder, knee, low back, elbow)
  - user_primer_pref   # on | off | unknown -- the user likes a primer / asked for one
  - minutes_available  # session time budget (091)
activation_rules:
  - rule: ramp-first-always
    trigger: any heavy or moderate compound slot
    action: the warm-up for the lift is its own ramp (080 ramp_rules); no primer replaces a ramp set, and the ramp is built first
    basis: exercise/warmup-ramp-sets-heavy-compounds-080; exercise/shoulder-prep-specific-vs-general-065
    basis_grade: B
  - rule: primer-default-off
    trigger: no caution rung on the pattern's site (no-rung or mild) and user_primer_pref is off or unknown
    action: no primer; the ramp is the activation; do not add drills to fill the warm-up
    basis: exercise/activation-priming-by-pattern-evidence-730
    basis_grade: C
  - rule: primer-on-by-preference
    trigger: user_primer_pref on, or the user reports a drill helps them find a position (shoulder blades set, hips engaged)
    action: offer up to primer_drills_max drills from the pattern's menu below, primer_sets_per_drill set of primer_reps each, at primer_effort, before the ramp; label it as a feel / cue choice, not a strength or injury tool
    basis: exercise/activation-priming-by-pattern-evidence-730; exercise/serratus-anterior-integration-019
    basis_grade: D
  - rule: caution-site-defers
    trigger: shoulder at a 065 shoulder-primer rung (history-old, history-recent, history-unknown, current-load-pain) before a press or row; knee at a 078 knee_prep rung before a squat or hinge
    action: 065 shoulder-primer or 078 knee_prep is the primer; this rule adds nothing on top and counts it against primer_drills_max
    basis: exercise/shoulder-prep-specific-vs-general-065; exercise/knee-prep-hip-adductor-abductor-078
    basis_grade: C
  - rule: no-pre-fatigue-of-the-lift
    trigger: any primer before a heavy slot (working_reps <= heavy_trigger_reps_max or load >= heavy_trigger_pct_1rm)
    action: the primer never trains the lift's prime mover or key synergist hard -- no fly / pec deck, triceps, leg extension, hamstring curl, back extension, biceps or rear-delt sets near failure before the compound; any such set moves after the compound
    basis: exercise/activation-priming-by-pattern-evidence-730 (Gentil 2007, Soares 2016, Augustsson 2003)
    basis_grade: C
  - rule: stabilisers-fresh-before-heavy
    trigger: heavy slot (as above)
    action: no fatiguing trunk, cuff or scapular work before it (no plank or ab wheel to failure before a squat or deadlift, no hard external-rotation or face-pull sets before a heavy press); light bracing or a dead bug is fine; hard versions go after the main lifts
    basis: exercise/core-functional-accessory-carry-081; exercise/shoulder-prep-specific-vs-general-065; Ebaugh 2006 via 730
    basis_grade: D
  - rule: primer-before-ramp
    trigger: any primer
    action: primer first, then the ramp sets, then the working sets; never insert a drill between the top ramp set and the first working set
    basis: Comyns 2015 via 730 (jump height down 0.5-6 min after a glute series); product placement
    basis_grade: D
  - rule: no-primer-in-the-work-block
    trigger: user wants the drill as strength work (serratus, glute, cuff, rear delt)
    action: put it in the accessory block as progressive sets (065 cuff-strength-not-in-prep; 078 programme dose), not in the warm-up
    basis: exercise/shoulder-prep-specific-vs-general-065; exercise/knee-prep-hip-adductor-abductor-078
    basis_grade: C
  - rule: drop-first-when-short
    trigger: minutes_available below the plan's full session (091)
    action: the primer is the first warm-up piece cut; ramp sets are trimmed only after it (080 ramp_rules), never before it
    basis: exercise/short-session-rules-091; exercise/activation-priming-by-pattern-evidence-730
    basis_grade: D
  - rule: once-per-pattern
    trigger: a second compound of the same pattern in the session
    action: no second primer; the first lift was the warm-up
    basis: product judgement
    basis_grade: D
pattern_menus:
  # Choice menus, unranked: no drill is evidenced over another (730). The
  # engine offers at most primer_drills_max; "avoid before" lists the
  # pre-fatigue cases the no-pre-fatigue rule blocks.
  - pattern: horizontal_press
    drills: [serratus punch / push-up plus, light plate pullover, scapular push-up, very light fly (one set of 12 at about 30-40% of a fly 10RM)]
    avoid_before: [pec deck or fly near failure, triceps pushdown or dips near failure, hard external-rotation sets]
    basis_grade: D
  - pattern: vertical_press
    drills: [wall slide / serratus upward-rotation reach, light band external rotation, light face pull]
    avoid_before: [lateral raises or rear-delt sets near failure, triceps near failure, hard cuff sets]
    basis_grade: D
  - pattern: squat
    drills: [body-weight squat to the working depth, glute bridge, band lateral walk]
    avoid_before: [leg extension near failure, hard hip abduction, plank or ab wheel to failure]
    note: a band at the knees during WORKING squats is not a valgus fix (Forman 2023 via 730); at a knee caution site 078 knee_prep is the primer
    basis_grade: D
  - pattern: hinge
    drills: [hip hinge with a dowel, glute bridge, dead bug or bird dog (light bracing)]
    avoid_before: [hamstring curl or back extension near failure, plank or ab wheel to failure, heavy carries]
    basis_grade: D
  - pattern: row
    drills: [band pull-apart, scapular retraction / prone Y with no load]
    avoid_before: [biceps curls or rear-delt sets near failure, heavy grip work]
    note: when the row follows a press or the hinge in the same session, the earlier lifts already warmed the area; no primer
    basis_grade: D
answer_patterns:
  - question: should I do activation drills before bench / squat / deadlift?
    answer: not needed; the few lighter sets of the lift itself are the warm-up with evidence; if a drill helps you feel set up, one light set of one or two drills before those sets is fine
    basis: exercise/activation-priming-by-pattern-evidence-730
    basis_grade: C
  - question: does glute activation make my squat or deadlift stronger?
    answer: not shown; against a normal warm-up it did not raise force and sometimes lowered glute activity for a few minutes; keep it light and early if you like it
    basis: exercise/activation-priming-by-pattern-evidence-730
    basis_grade: C
  - question: should I pre-exhaust my chest with flies before benching?
    answer: hard flies or triceps work before the bench cut bench reps and shift work to the triceps; do the hard isolation after the bench
    basis: exercise/activation-priming-by-pattern-evidence-730
    basis_grade: C
  - question: do serratus punches / pullovers protect my shoulder before pressing?
    answer: no study tests that; they are a setup cue at most; if your shoulder has a history, the short cuff and shoulder-blade primer in the plan covers it, and the real protection is progressive cuff strength work later in the session
    basis: exercise/shoulder-prep-specific-vs-general-065; exercise/activation-priming-by-pattern-evidence-730
    basis_grade: D
  - question: should I do core work before heavy squats?
    answer: light bracing practice or a dead bug is fine; save planks and ab-wheel sets for after the main lifts
    basis: exercise/core-functional-accessory-carry-081
    basis_grade: D
never_say:
  - activation drills prevent injury
  - you must activate your glutes before squatting
  - your glutes are not firing (as a diagnosis from a warm-up)
  - this drill switches on the muscle so the lift gets stronger
  - pre-exhaust before the compound to make the target muscle work more
  - skip the ramp sets if you did your activation
refraction_notes:
  - note: >
      THE LIFT IS ITS OWN PRIMER. For every heavy squat, hinge, press or
      row, the plan's warm-up is the lift itself in lighter ramp sets. An
      activation drill is added only if the user wants one or a caution
      site calls for 065 / 078's primer, and it never takes a ramp set's
      place.
    grade: B
  - note: >
      ONE OR TWO DRILLS, ONE LIGHT SET, BEFORE THE RAMP. When a primer is
      used it is short (about three minutes), far from failure, and done
      before the ramp sets so a few minutes pass before the heavy work. The
      numbers are product choices; no trial sets a primer dose.
    grade: D
  - note: >
      NEVER TIRE THE LIFT'S OWN MUSCLES FIRST. Hard flies or triceps before
      the bench and leg extensions to failure before a leg press lowered
      the big lift. Hard isolation, core and cuff sets go after the
      compound.
    grade: C
claim: >
  The session builder treats the specific ramp as the warm-up for every heavy
  free-weight compound and adds an activation primer only when the user wants
  one or a caution site calls for 065's shoulder primer or 078's knee prep.
  A primer is at most two drills from the pattern's menu (horizontal press:
  serratus punch, light plate pullover, scapular push-up, a very light fly;
  vertical press: wall slide, light band external rotation, light face pull;
  squat: body-weight squat, glute bridge, band walk; hinge: dowel hinge, glute
  bridge, dead bug or bird dog; row: band pull-apart, unloaded prone Y), one
  light set of 8-12 each, far from failure, about three minutes, placed before
  the ramp. Before a heavy slot (working sets of six reps or fewer, or 80% 1RM
  or more) nothing in the warm-up may train the lift's prime mover or key
  synergist hard, and fatiguing core, cuff or scapular work moves after the
  main lifts. The primer is the first warm-up piece cut when time is short, is
  not repeated for a second lift of the same pattern, and is never presented
  as protective or strength-raising.
reasoning: >
  730 grades the evidence: the ramp carries the warm-up effect (borrowed B),
  glute activation is mixed against a proper control (C), pre-fatigue of the
  lift's own muscles costs the lift (C, small but consistent), and nothing
  tests a serratus, pullover, fly, bracing or scapular primer (D). So the
  default is off and the primer is a preference, which keeps the plan honest
  and the warm-up short. The load trigger (six reps or fewer, or 80% 1RM)
  marks where pre-fatigue matters most; the trials behind the fatigue rule
  used 10RM to failure, so the trigger and the far-from-failure dose are
  product choices that stay well clear of the tested harm. Placing the primer
  before the ramp uses Comyns 2015's transient jump drop as a direction and
  costs nothing. 065 and 078 already own the shoulder and knee caution sites,
  so this row defers to them rather than stacking a second primer. The menus
  are unranked because no drill has evidence over another; the light fly is
  allowed only as a feel drill well below the pec-deck dose that cut bench
  performance.
---

# exercise/activation-rules-by-pattern-731 -- 동작별 활성화 드릴 규칙: 기본은 램프, 드릴은 선택, 같은 근육은 미리 지치게 하지 않는다

**한 줄 그림:** 무거운 복합 운동의 준비는 그 운동의 램프 세트다. 활성화 드릴은 사용자가 원하거나 다친 부위가
있을 때만, 1-2개를 가볍게 한 세트씩, 램프 앞에 3분 안으로 한다. 본운동 근육을 미리 세게 지치게 하지 않는다.

## Activation rules (engine-readable)

| Rule | When | What the plan does | Basis |
|---|---|---|---|
| ramp-first-always | every compound | the lift's own ramp is the warm-up | 080, 065 |
| primer-default-off | no caution rung, no preference | no drills | 730 |
| primer-on-by-preference | user wants one | 1-2 drills x 1 set x 8-12, light, before the ramp | 730, 019 |
| caution-site-defers | shoulder / knee caution rung | 065 shoulder-primer or 078 knee_prep instead | 065, 078 |
| no-pre-fatigue-of-the-lift | heavy slot (<= 6 reps or >= 80% 1RM) | no hard prime-mover or synergist sets first | 730 |
| stabilisers-fresh-before-heavy | heavy slot | hard core / cuff / scapular work after | 081, 065 |
| primer-before-ramp | any primer | primer, ramp, work; nothing between top ramp and work | 730 |
| drop-first-when-short | short session | cut the primer before any ramp set | 091 |
| once-per-pattern | second lift, same pattern | no second primer | product |

| Pattern | Drill menu (unranked) | Avoid before |
|---|---|---|
| horizontal press | serratus punch, light plate pullover, scapular push-up, very light fly | fly / pec deck or triceps near failure |
| vertical press | wall slide, light band ER, light face pull | lateral / rear-delt or triceps near failure |
| squat | body-weight squat, glute bridge, band walk | leg extension near failure, core to failure |
| hinge | dowel hinge, glute bridge, dead bug / bird dog | hamstring curl or back extension near failure |
| row | band pull-apart, unloaded prone Y | biceps or rear-delt near failure |

## 한국어 요약 (답변용)

- 무거운 스쿼트·힙힌지(데드리프트)·벤치·오버헤드 프레스·로우 전에는 그 운동을 가볍게 올려 가는 램프
  세트가 준비운동이다. 활성화 드릴은 기본으로 넣지 않고, 램프 세트를 대신하지도 않는다.
- 드릴이 자세 잡는 데 도움이 된다는 사람에게는 1-2개를 골라 가볍게 한 세트(8-12회)씩, 램프 세트 앞에,
  전부 3분 안으로 한다. 벤치 전: 전거근 펀치, 가벼운 플레이트 풀오버, 스캐풀라 푸시업, 아주 가벼운 플라이.
  오버헤드 전: 월 슬라이드, 가벼운 밴드 외회전, 가벼운 페이스풀. 스쿼트 전: 맨몸 스쿼트, 글루트 브릿지,
  밴드 워크. 데드리프트 전: 막대 힙힌지, 글루트 브릿지, 데드버그·버드독. 로우 전: 밴드 풀어파트,
  무게 없는 프론 Y. 어느 게 더 낫다는 근거는 없다.
- 어깨나 무릎에 주의 단계가 있으면 어깨 준비(065)나 무릎 준비(078)가 그 자리를 맡고, 드릴을 더 쌓지 않는다.
- 6회 이하나 1RM 80% 이상의 무거운 세트 전에는 본운동 근육을 세게 쓰지 않는다. 플라이·펙덱·삼두, 레그
  익스텐션, 레그 컬, 백 익스텐션, 이두·후면 삼각근을 실패 가까이 하는 건 본운동 뒤로 보낸다. 플랭크나 ab
  휠을 끝까지 하거나 회전근개를 세게 하는 것도 뒤로 보낸다. 가벼운 브레이싱이나 데드버그는 괜찮다.
- 드릴은 램프 세트 앞에 둔다. 마지막 램프 세트와 첫 본 세트 사이에 드릴을 끼우지 않는다.
- 시간이 부족하면 드릴을 가장 먼저 뺀다. 같은 동작 패턴 운동을 두 번째로 할 때는 드릴을 다시 하지 않는다.
- 드릴이 부상을 막는다거나 근육을 "깨워서" 무게가 오른다고 말하지 않는다. 연구된 적이 없다.
- 드릴 수, 세트·횟수, 3분, 6회·80% 기준은 제품에서 정한 값이고 측정된 기준이 아니다.
