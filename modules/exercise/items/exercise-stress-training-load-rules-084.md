---
# Stress / training-load sprint 2026-10-07. The engine-readable synthesis of 083 (what
# outside stress does to gains and recovery) and
# mental-health item 071 (module not published) (how the input is
# obtained). It is a routing rule, not a primary finding: each rule names the
# graded row it rests on, and every number (sets factor, RIR floor, expiry,
# the 3-week renegotiation point) is labelled as a product constant. Same
# posture as 031, 032 and 056.
#
# stress_rules and ask_policy are structured data for the session brief
# (health-brief / rx-calc), the daily retro (session-retro) and the e1RM /
# miss-streak predicates. Values are DIRECTIONS and product constants. The
# YAML-subset reader returns scalars as strings ("0.67", "7") -- cast them.
# No program code changed in this task.
id: exercise/stress-training-load-rules-084
domain: exercise
grade: D (synthesis rule over 083 and mental-health 071; the direction "keep load, trim volume and proximity to failure" is C-backed, every number is product judgement, and no trial tests stress-guided lightening)
lane: "@gym-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/life-stress-adaptation-recovery-083"  # stress slows gains and force recovery (C); acute mental fatigue cuts same-session reps (B); stress predicts injury and dropping out (C)
  - "mental-health item 071 (module not published)"  # where and how the input may be obtained; stored as a session choice, never a score
  - "https://pubmed.ncbi.nlm.nih.gov/33629972/"  # Spiering BA, Mujika I, Sharp MA, Foulis SA 2021, J Strength Cond Res 35(5):1449-1458 -- narrative review written for periods of "personal, family, or business conflicts": strength and size held up to 32 weeks on as little as 1 session/week and 1 set/exercise in younger people IF relative load is kept; older people may need 2 sessions and 2-3 sets; intensity is the key variable
  - "exercise/recovery-kinetics-session-spacing-025"  # proximity to failure and volume drive recovery time -- the two levers this rule pulls
  - "exercise/autoregulation-vs-percentage-prescription-030"  # adjusting by readiness has no measured strength dividend -- so the lighter session is a hedge, not a gain
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # short sleep in the same week compounds; early waking costs more than late bedtime
  - "sleep-recovery/subjective-monitoring-vs-objective-markers-011"  # the person's report beats device readiness scores; no consumer stress score is validated (GAPS.md)
  - "mental-health item 027 (module not published)"  # a "feel bad" report gets load relief, not questions
  - "mental-health item 024 (module not published)"  # no lightening on inferred state
  - "mental-health item 025 (module not published)"  # offer once, no streak or missed-day language, renegotiate rather than push
  - "exercise/deload-planned-vs-reactive-060"  # within-warehouse (v37): its life-stress-or-travel trigger moves a planned deload INTO a hard week; this row lightens the session itself; how the two combine in the same week is not yet specified (GAPS.md) (linked v40)
  - "framework:GRADE -- the DIRECTION of each lever is supported: keeping relative load preserves strength through low-volume periods (narrative review, C); proximity to failure and volume set recovery time (C); stress slows recovery (C). The lightened-session numbers, the 7-day expiry, the once-a-week ask and the 3-week renegotiation point are product constants with no direct evidence. No study compares lightening against training as planned in a stressful week."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
ask_policy:
  surface: session-brief
  never_surfaces: [daily-retro, feel-bad-reply, inferred-tone]
  max_unprompted_asks_per_days: 7
  trigger: a concrete calendar fact (deadline, exam, travel, move, evening events most days) or the person's own words
  answer_options: [lighter, as-planned]
  no_answer: as-planned
  store_as: session_choice
  store_never: [stress_score, mood, trend]
  forbidden_terms_ko: [스트레스 지수, 정신건강, 우울, 불안, 번아웃, 상담, 멘탈 관리]
  basis: mental-health item 071 (module not published)
  basis_grade: D
stress_rules:
  - signal: heavy-week-chosen
    words: the person chose "lighter" in the brief, or said unprompted that this is a heavy week (마감, 시험, 이사, 출장, 일이 몰림)
    applies_to: [brief, rx, retro]
    session: lighter
    load: keep last working load; no increase today
    sets_factor: 0.67
    min_sets: 1
    rir_floor: 3
    to_failure: false
    pr_or_test: false
    e1rm: raise_only
    miss_streak: skip
    expires_days: 7
    basis: exercise/life-stress-adaptation-recovery-083
    basis_grade: C
  - signal: draining-day
    words: the person says today was mentally draining (야근, 시험 친 날, 하루 종일 회의) and does not ask for a lighter session
    applies_to: [brief, rx, retro]
    session: as-planned
    load: as planned
    sets_factor: 1
    min_sets: 1
    rir_floor: plan
    to_failure: plan
    pr_or_test: false
    e1rm: raise_only
    miss_streak: skip
    expires_days: 1
    basis: exercise/life-stress-adaptation-recovery-083
    basis_grade: B
  - signal: heavy-week-plus-short-sleep
    words: heavy-week-chosen AND logged sleep well under the person's own baseline on the session day, especially an early alarm
    applies_to: [brief, rx]
    session: lighter
    load: keep last working load; no increase today
    sets_factor: 0.67
    min_sets: 1
    rir_floor: 3
    to_failure: false
    pr_or_test: false
    e1rm: raise_only
    miss_streak: skip
    expires_days: 1
    basis: sleep-recovery/sleep-loss-performance-decrement-004
    basis_grade: B
  - signal: feel-bad-report
    words: the person says they feel bad, are not doing well, or the week is rough in a personal rather than scheduling sense
    applies_to: [brief]
    session: offer-relief
    load: no change unless the person picks lighter or skip
    sets_factor: 1
    min_sets: 1
    rir_floor: plan
    to_failure: plan
    pr_or_test: plan
    e1rm: raise_only
    miss_streak: skip
    expires_days: 1
    basis: mental-health item 027 (module not published)
    basis_grade: D
  - signal: lighter-three-weeks-running
    words: heavy-week-chosen in three consecutive weeks (product constant)
    applies_to: [brief]
    session: offer-renegotiate
    load: as planned
    sets_factor: 1
    min_sets: 1
    rir_floor: plan
    to_failure: plan
    pr_or_test: plan
    e1rm: unchanged
    miss_streak: unchanged
    expires_days: 0
    basis: mental-health item 025 (module not published)
    basis_grade: D
  - signal: none
    words: no answer, no words, or only indirect cues (short replies, wearable stress or readiness number, HRV)
    applies_to: [brief, rx, retro]
    session: as-planned
    load: as planned
    sets_factor: 1
    min_sets: 1
    rir_floor: plan
    to_failure: plan
    pr_or_test: plan
    e1rm: unchanged
    miss_streak: unchanged
    expires_days: 0
    basis: mental-health item 024 (module not published)
    basis_grade: D
refraction_notes:
  - note: >
      KEEP THE LOAD, CUT THE REST. A lighter session keeps the last working
      load (relative intensity) and trims sets and proximity to failure. That
      is the direction the maintenance literature supports -- strength held for
      months on far less volume when relative load is kept -- and the two
      levers that set recovery time are proximity to failure and volume (025).
      Dropping the weight while keeping the sets would cut the one thing that
      protects strength and keep the thing that costs recovery. The factor
      0.67, the floor of 3 reps in reserve and one set minimum are the plan's
      numbers, not measured thresholds.
    grade: C
  - note: >
      LIGHTER, NOT SKIPPED, BY DEFAULT -- BUT SKIP IS THE PERSON'S CALL.
      Habitual exercisers tend to keep training under stress while beginners
      drop out (083), and a shorter session is the cheap one to start. The
      rule offers lighter, never pressures; a skip the person chooses is
      accepted without comment and does not count as a miss.
    grade: D
  - note: >
      A STRESS DAY MUST NOT DRAG THE NUMBERS. A lighter or draining-day session
      is treated like the product's existing 컨디션 저조 rule: e1RM raise_only
      (it may raise the estimate, never lower it) and it neither counts toward
      nor resets the two-miss deload streak. Short reps on a draining day are
      the expected same-session effect of mental fatigue (B), not a signal that
      the load is wrong.
    grade: D
  - note: >
      THE RETRO COUNTS AGAINST THE LIGHTER PLAN AND NEVER SAYS STRESS. When the
      session was lightened by choice, the daily retro compares the log with the
      lightened plan and tags it "(가볍게)" -- no "N세트 빠짐" against the
      original plan, no stress word, no streak, no question. The retro is a
      glance card; it carries no ask.
    grade: D
  - note: >
      EXPIRY, NOT HISTORY. A heavy-week choice lasts 7 days (product constant)
      or until the named event ends, then the plan returns to normal by itself.
      Nothing is trended. After three consecutive lighter weeks the brief may
      offer, once, to make the plan itself smaller (fewer days, shorter days);
      it does not comment on the person.
    grade: D
  - note: >
      NO INFERRED TRIGGERS. Message tone, reply length, a wearable stress or
      readiness score and HRV never trigger lightening or an ask. Tone is item
      024's refusal; no consumer stress score has been validated against an
      affect outcome (mental-health GAPS), and HRV guidance has no
      resistance-training case (sleep-recovery 011).
    grade: D
claim: >
  When the person says this is a heavy week (or picks "lighter" when the
  session brief asks once, with a calendar reason), the session stays on the
  calendar and gets lighter in a specific way: the last working load is kept, no
  increase today, working sets are cut to about two-thirds (at least one), every
  set stops at least three reps short of failure, and there is no PR, test or
  remeasure. The lightened session cannot lower the e1RM estimate and does not
  count in the two-miss deload streak; the daily retro compares it with the
  lightened plan, tags it as lighter and never mentions stress. A draining
  single day keeps the plan but expects fewer reps and does not count short sets
  as misses. A "feel bad" report gets an offer to lighten, move or drop the
  session, not questions. The choice expires after seven days; after three
  lighter weeks in a row the brief offers once to make the plan itself smaller.
  Nothing else triggers this: not tone, not a device score. The direction
  (keep load, trim volume and proximity to failure) is evidence-backed; the
  numbers are product constants, and whether lightening protects gains in a
  stressful week has never been tested.
reasoning: >
  083 establishes that outside stress slows recovery of force and strength
  gains (C) and that a draining day costs same-session reps (B), but supplies no
  dose. The lever choice therefore comes from neighbouring rows: Spiering 2021
  says strength is maintained through low-volume periods if relative load is
  kept, and 025 says proximity to failure and volume are what set recovery
  time. Together they point one way -- keep the bar weight, remove sets and
  the last hard reps -- which also avoids teaching the e1RM and the miss streak
  that the person got weaker. The e1RM and miss-streak handling reuses the
  product's 2026-09-30 condition rule rather than inventing a new predicate.
  030 caps the ambition: readiness-adjusted training shows no strength
  dividend, so this is a hedge for recovery and adherence, not a performance
  method. The asking and storage rules are mental-health 071's, and the refusals (no tone,
  no device score, no streak language) are 024, 025, 027 and the open GAPS
  rows restated. Graded D because every number is product judgement.
---

# exercise/stress-training-load-rules-084 -- 바쁜 주·스트레스 큰 주의 운동 조절 규칙

**한 줄 그림:** 바쁜 주라고 하면 운동은 그대로 두고, 무게는 지키고, 세트와 막판 반복만 줄인다.
그날 기록이 추정치나 디로드 판단을 끌어내리지 않게 한다.

## What the engine reads from this row

| Signal | Session | Load | Sets | RIR floor | e1RM | Miss streak | Expires |
|---|---|---|---:|---:|---|---|---:|
| heavy-week-chosen | lighter | keep, no increase | x0.67 (min 1) | 3 | raise_only | skip | 7 d |
| draining-day | as planned | as planned | x1 | plan | raise_only | skip | 1 d |
| heavy-week-plus-short-sleep | lighter | keep, no increase | x0.67 (min 1) | 3 | raise_only | skip | 1 d |
| feel-bad-report | offer lighter / move / drop | -- | -- | -- | raise_only | skip | 1 d |
| lighter-three-weeks-running | offer smaller plan once | -- | -- | -- | -- | -- | -- |
| none (incl. tone, device score) | as planned | -- | -- | -- | unchanged | unchanged | -- |

Field notes for the build: `sets_factor` multiplies working sets and rounds
to the nearest whole set (4 -> 3, 3 -> 2, 2 -> 1). `rir_floor: plan` keeps the program's own
target. `e1rm: raise_only` maps onto `e1rm_rx_rules` `condition` (the
same treatment as the 컨디션 저조 ruling); a new flag value such as
`stress_light` would be added to `flag_excluded` by the code maintainer, not here.
`miss_streak: skip` means the session neither extends nor resets the run read
by `derive_miss_streak`. Every number in the table is a product constant.

## 한국어 요약 (답변용)

- 바쁜 주(마감, 시험, 이사, 출장)라고 하거나 브리프에서 "가볍게"를 고르면, 운동은 그대로 하되
  가볍게 한다. 무게는 지난번 작업 무게 그대로(올리지 않음), 세트는 3분의 2 정도로(최소 1세트), 모든
  세트는 실패 3회 전에 멈추고, 최고 기록 시도나 재측정은 하지 않는다.
- 무게를 지키는 이유: 운동량을 크게 줄여도 무게(강도)만 유지하면 근력은 몇 달 유지된다는 정리가
  있다. 회복을 늦추는 건 세트 수와 실패에 가까운 반복이라 그걸 줄인다. 다만 3분의 2, 3회 여유, 7일
  같은 숫자는 제품이 정한 규칙이다.
- 머리를 많이 쓴 날은 계획대로 하되 반복이 몇 개 덜 나올 수 있다고 미리 말해 둔다. 덜 나온 세트는
  실패로 세지 않는다.
- 가볍게 한 날이나 힘든 날의 기록은 1RM 추정치를 끌어내리지 않고(올리는 건 허용), "두 번 미달이면
  디로드" 계산에도 넣지 않는다. 기존의 컨디션 저조 규칙과 같은 처리다.
- 하루 회고에는 가볍게 한 계획과 비교해 "(가볍게)"로만 적는다. 원래 계획 대비 "빠짐", 스트레스라는
  말, 연속 기록, 질문은 넣지 않는다.
- 기분이 안 좋다고 하면 묻지 않고, 오늘 운동을 가볍게 하거나 옮기거나 빼는 걸 한 번 제안한다. 쉬는
  것도 본인 선택이고 실패로 세지 않는다.
- 선택은 7일 뒤 저절로 끝난다. 3주 연속 가볍게 했다면 계획 자체를 줄이자고 한 번만 제안한다.
- 답장 말투, 워치의 스트레스·준비도 점수, HRV로는 절대 조절하지 않는다.
- 스트레스 주에 가볍게 하는 게 실제로 근력을 지키는지는 시험된 적이 없다. 회복과 꾸준함을 위한
  보수적 규칙이라고 말한다.
