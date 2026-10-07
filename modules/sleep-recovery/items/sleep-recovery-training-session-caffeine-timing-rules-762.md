---
# Caffeine timing for training vs sleep sprint 2026-10-07 (block 760..764, numbers are this branch's
# claim). The engine-readable answer to "can I have caffeine before THIS
# session", for any session hour -- the gap the dawn rules (exercise 073,
# sleep-recovery 083) leave for midday, afternoon and evening sessions. It
# joins three rows the warehouse already grades: the ergogenic dose and
# 60-minute timing (exercise 069, ISSN 2021), the dose x hours-before-bed
# cutoff (070, spoken per 083 cutoff-speak-one-number), and the Korean
# serving bands (761). A routing rule, not a primary finding; same posture
# as 072, 081, 083. Every boundary not copied from a source is labelled a
# product constant.
#
# caffeine_rules / session_caffeine_plan are structured data for the brief /
# session-prep code. The plan is a LOOKUP, not a calculation the model does:
# intake time = session start minus intake_lead_min; hours_to_bed = usual
# bedtime minus intake time; the engine picks the LARGEST 070 row whose
# spoken cutoff is <= hours_to_bed, capped at single_dose_ceiling_mg. No mg
# is ever produced that is not a row value. Session start and bedtime come
# from the stated plan / stated usual bedtime (data reality as in 083: no
# caffeine data is inferred). These rules sit UNDER 072's brief_guards and
# 083's caffeine_guards (one caffeine line per brief, never suggest caffeine
# to a non-user, safety gate first).
id: sleep-recovery/training-session-caffeine-timing-rules-762
domain: sleep-recovery
grade: D (synthesis rule over 069, 070, 083, 760 and 761; each rule's basis_grade is the strength of its own row; the row-picking lookup, the 60-minute lead and the worked thresholds are product judgement)
lane: "@clinical"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/early-morning-caffeine-food-069"  # ISSN 2021: 3-6 mg/kg, 60 min pre-exercise the most common timing, gum faster, minimum effective dose may be about 2 mg/kg; EFSA 200 mg single-dose ceiling
  - "sleep-recovery/caffeine-bedtime-cutoff-070"  # dose x hours-before-bed rows
  - "sleep-recovery/caffeine-morning-brief-rules-083"  # cutoff-speak-one-number (9 h / 13 h / 14 h), safety-gate, caffeine_guards
  - "sleep-recovery/caffeine-half-life-clearance-760"  # peak about 30 min; clearance modifiers that move a user to the conservative column
  - "sleep-recovery/kr-coffee-serving-caffeine-761"  # which Korean drink fits which row
  - "sleep-recovery/caffeine-tolerance-short-night-082"  # habitual users: usual amount works; evening 3-6 mg/kg cut athletes' sleep efficiency (Kocak 2025)
  - "exercise/early-morning-session-brief-rules-073"  # dawn-caffeine-if-user and afternoon-caffeine-cutoff, which this block extends to every session hour
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # why the night's sleep outranks one session's caffeine
  - "sleep-recovery/brief-sleep-training-rules-072"  # brief_guards
  - "framework:GRADE -- inherits 069 (B: ergogenic dose and timing convention), 070 (B / C: cutoffs), 760 (B: peak time) and 761 (C: serving mg). The intake lead of 60 min, the lookup order and the choice to cap at 200 mg whatever the gap are product constants (D)."
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: caffeine_sensitivity
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [not_pregnant, none]
    - key: cardiovascular_condition
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [none]
    - key: medication_list
      type: categorical
      role: hard
      unknown_policy: block_specifics
constants:
  intake_lead_min: 60              # ISSN 2021 most common timing (069); 760: blood peak about 30 min, so 30-60 is the window
  single_dose_ceiling_mg: 200      # 069 / EFSA 2015 safety ceiling; also the cap whatever the gap to bed
  spoken_cutoff_h:                 # 083 cutoff-speak-one-number, from 070
    up_to_100_mg: 9
    about_200_mg: 13
    about_400_mg: 14
session_caffeine_plan:
  - hours_to_bed_min: 13
    allowed_row: about 200 mg
    kr_examples: 커피전문점 아메리카노 1잔 or 프리워크아웃 1스쿱 (label 200 mg or less)
    note: cap at single_dose_ceiling_mg; the 400 mg row is never offered as a pre-session dose
    basis_grade: B
  - hours_to_bed_min: 9
    allowed_row: up to about 100 mg
    kr_examples: 커피믹스 1봉, 캔커피 250 mL, 1샷 아메리카노
    note: below the ISSN minimum effective dose for most adults (about 2 mg/kg); speak as a smaller, uncertain lift
    basis_grade: C
  - hours_to_bed_min: 0
    allowed_row: none
    kr_examples: 디카페인 or no caffeine
    note: the session goes ahead without caffeine; tonight's sleep is worth more to the next sessions than this one's caffeine
    basis_grade: B
caffeine_rules:
  - rule: session-caffeine-plan
    needs: [caffeine_user, session_start, usual_bedtime]
    when: a caffeine user plans caffeine before a session that is not a 05:00-06:00 dawn session (dawn is 073 / 083)
    level: note
    say: take it about an hour before; for this session and your bedtime, the most that still leaves your sleep alone is the session_caffeine_plan row for hours_to_bed, named as the matching drink from 761
    never_say: an mg figure that is not a row value; a dose above single_dose_ceiling_mg; a cutoff in clock time without the user's bedtime
    product_constant: true
    basis: sleep-recovery/caffeine-bedtime-cutoff-070
    basis_grade: B
  - rule: evening-session-no-caffeine
    needs: [caffeine_user, session_start, usual_bedtime]
    when: hours_to_bed is under 9 and the user plans caffeine or a pre-workout
    level: hedge
    say: this close to bed even a small coffee costs some sleep, and you may not feel it; train without it or use decaf. If you really want caffeine on evening days, move the session earlier rather than the bedtime later
    never_say: that the session will be poor without caffeine; that a smaller scoop solves it; that the user should go to bed later
    product_constant: true
    basis: sleep-recovery/caffeine-bedtime-cutoff-070
    basis_grade: B
  - rule: midday-session-small-serve
    needs: [caffeine_user, session_start, usual_bedtime]
    when: hours_to_bed is 9 to under 13
    level: note
    say: a small serve (a coffee mix, a single shot, a small can) fits; a full coffee-shop Americano or a pre-workout scoop reaches into tonight
    never_say: that the small serve gives the full ergogenic effect
    product_constant: true
    basis: sleep-recovery/kr-coffee-serving-caffeine-761
    basis_grade: C
  - rule: preworkout-label-check
    needs: [caffeine_user]
    when: the user mentions a pre-workout product or a scoop count
    level: note
    say: check the 총카페인 on the tub; two scoops or a stim product above 200 mg goes past the single-dose ceiling and into the 400 mg row
    never_say: a guessed mg for a named product; advice to double a scoop
    product_constant: false
    basis: exercise/early-morning-caffeine-food-069
    basis_grade: B
  - rule: daily-total-includes-session
    needs: [caffeine_user, usual_caffeine]
    when: the user already had coffee earlier the same day and plans a pre-session serve
    level: note
    say: the latest serve sets tonight's cutoff, and earlier coffee is still partly in your system; count the pre-session serve as the day's last
    never_say: a computed remaining mg; that earlier coffee has worn off
    product_constant: true
    basis: sleep-recovery/caffeine-half-life-clearance-760
    basis_grade: B
  - rule: slow-clearance-shift
    needs: [caffeine_user]
    when: 760 slow-clearance-conservative fires (hormonal contraception, recent smoking quit, liver disease, medication) or caffeine_sensitivity is high
    level: hedge
    say: use the plan one row smaller than the hours allow, or no caffeine for evening sessions
    never_say: a dose number when a hard gate is unresolved
    product_constant: true
    basis: sleep-recovery/caffeine-half-life-clearance-760
    basis_grade: C
caffeine_guards:
  - guard: never suggest starting caffeine to someone who has not said they use it (083 / 073); this plan only times an existing habit
    basis_grade: D
  - guard: the plan never moves the bedtime; it moves or drops the caffeine
    basis_grade: B
  - guard: safety-gate from 083 runs first; under it, direction only (earlier and smaller is better for sleep), no row values
    basis_grade: B
  - guard: one caffeine line per brief across 072, 073, 081, 083 and this block; the highest level wins
    basis_grade: D
refraction_notes:
  - note: >
      THE PLAN IS 070 READ BACKWARDS. 070 gives hours-before-bed per dose; a
      training user knows the session hour and the bedtime. Subtracting the
      one-hour lead and picking the largest row that fits is a lookup over
      graded rows, not a new finding. With a 23:00 bedtime: a 07:00 session
      (caffeine 06:00, 17 h) allows the 200 mg row; a 12:00 session (11:00,
      12 h) allows only the small-coffee row; an 18:00 session (17:00, 6 h)
      allows none.
    grade: D
  - note: >
      THE SMALL ROW IS A SLEEP ALLOWANCE, NOT AN ERGOGENIC DOSE. About 100 mg
      is roughly 1.4 mg/kg at 70 kg, under the ISSN's 3-6 mg/kg range and its
      suggested minimum of about 2 mg/kg. It may lift alertness; the
      warehouse holds no trial showing it lifts strength. Speak it that way.
    grade: C
  - note: >
      EVENING TRAINING IS WHERE THE CONFLICT IS REAL. The ISSN convention
      (3-6 mg/kg, an hour before) puts an evening lifter's dose inside 070's
      disruptive window almost by definition, and in athletes taking 3-6
      mg/kg between 16:00 and 19:45 sleep efficiency fell (082, Kocak 2025).
      Morning and evening training give similar gains (exercise 068 / 073),
      so the choice is the user's, but the plan does not pretend both fit.
    grade: B
claim: >
  For any session that is not at dawn, the brief can time caffeine with one
  lookup: take it about an hour before the session; count the hours from
  then to the stated bedtime; at 13 hours or more the about-200 mg row fits
  (a coffee-shop Americano or one pre-workout scoop, capped at 200 mg); at 9
  to 13 hours only the small row fits (a coffee mix, a single shot, a small
  can) and is spoken as a smaller, uncertain lift; under 9 hours the session
  goes without caffeine or with decaf, and the fix is moving the session,
  never the bedtime. Earlier coffee the same day still counts; slow
  clearance or high sensitivity moves the plan one row down; stated non-users
  are never offered caffeine; and the 083 safety gate runs first.
reasoning: >
  Each threshold is a spoken cutoff already in the warehouse (083's 9, 13
  and 14 hours over 070's rows) and each serving is a 761 band, so the plan
  adds no number of its own except the 60-minute lead (the ISSN's most
  common timing, consistent with the 30-minute blood peak in 760) and the
  200 mg cap (069). The lookup is deterministic, which fits REFRACTION.md:
  the model compares two stated times to fixed rows and never computes a
  dose. The direction that evening pre-workout caffeine costs sleep is B
  (070's trial rows, 082's athlete meta-analysis); the boundaries are D.
  Not contested: this row adds no primary claim of its own.
---

# sleep-recovery/training-session-caffeine-timing-rules-762 -- 운동 시간과 취침 시간으로 정하는 카페인

**한 줄 그림:** 운동 한 시간 전에 마신다고 치고, 그때부터 잠들 때까지 몇 시간 남는지 보고 마실 수 있는 양을
고른다. 9시간이 안 남으면 카페인 없이 운동한다.

## The lookup

| Hours from caffeine to bed | Allowed serve | Korean example |
|---:|---|---|
| 13 or more | up to about 200 mg (cap 200) | 커피전문점 아메리카노 1잔, 프리워크아웃 1스쿱 |
| 9 to under 13 | up to about 100 mg | 커피믹스 1봉, 1샷, 캔커피 250 mL |
| under 9 | none | 디카페인, 또는 없이 |

Worked, 23:00 bedtime: 07:00 session -> 17 h -> 200 mg row; 12:00 session ->
12 h -> small row; 18:00 session -> 6 h -> none.

| Rule | When | Level | Basis |
|---|---|---|---|
| session-caffeine-plan | caffeine before a non-dawn session | note | 070 |
| evening-session-no-caffeine | under 9 h to bed | hedge | 070 |
| midday-session-small-serve | 9 to 13 h | note | 761 |
| preworkout-label-check | pre-workout mentioned | note | 069 |
| daily-total-includes-session | coffee earlier today too | note | 760 |
| slow-clearance-shift | slow clearance or high sensitivity | hedge | 760 |

## 한국어 요약 (답변용)

- 운동 전 카페인은 보통 운동 약 1시간 전에 마신다. 그 시각부터 평소 잠드는 시각까지 몇 시간 남는지로 양을
  정한다.
- 13시간 이상 남으면 커피전문점 아메리카노 한 잔이나 프리워크아웃 한 스쿱(200mg 이하)까지 괜찮다. 이보다
  많이는 권하지 않는다.
- 9~13시간이면 커피믹스, 1샷, 작은 캔커피 정도만. 이 정도 양은 운동 효과가 확실하다고 보기 어렵다.
- 9시간이 안 남는 저녁 운동은 카페인 없이 하거나 디카페인을 쓴다. 본인이 못 느껴도 잠은 줄어든다. 꼭
  카페인을 쓰고 싶다면 잠을 늦추지 말고 운동 시간을 앞당긴다.
- 낮에 이미 커피를 마셨다면 그것도 아직 몸에 남아 있다. 운동 전 한 잔을 그날 마지막 잔으로 친다.
- 피임약 복용, 최근 금연, 간 질환, 일부 약, 카페인에 예민한 경우는 한 단계 적게 잡는다. 임신 중이거나 심장
  질환이 있으면 mg 숫자는 말하지 않는다.
- 카페인을 안 마시는 사람에게는 권하지 않는다.
