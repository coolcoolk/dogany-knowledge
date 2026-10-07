---
# Nap timing sprint 2026-10-07.
# The engine-readable synthesis of 084 with 009 / 072 / 082 / 083 / 070 for
# the brief: which nap to suggest after a short night, how far before
# training it must end, nap versus caffeine and the coffee nap, a nap before
# an evening session, and how late a nap can sit before bedtime. A routing
# rule, not a primary finding; same posture as 072, 081 and 083. Each rule
# names the graded row it rests on; every minute and hour not copied from a
# source is labelled a product constant.
#
# nap_rules is structured data for the brief / session-prep code.
# DATA REALITY (2026-10-07): hk-ingest stores sleep_min only (016), summed
# per wake day with naps included. The MORNING brief's sleep_min is the
# night only (the nap has not happened yet); a later-day line must not
# re-count a logged nap as night sleep. Whether the day allows a nap
# (nap_possible), the session time and the usual bedtime come from the
# plan or from what the user said; nap_possible is never assumed true.
#
# These rules sit UNDER 072's brief_guards (one sleep line per brief, never
# cancel on sleep alone, no readiness score) and REFINE 072's nap-repay and
# nap-not-a-strength-tool, which they do not replace: 072's 30 to under 60
# min nap with more than 1 h before training stays the long-gap option;
# this block adds the short nap for a closer session, the 90-min caution,
# the coffee nap and a nap-to-bedtime line. When a rule here and a 072 /
# 081 / 083 line fire on the same day, one nap line is spoken -- the higher
# level wins (flag > hedge > note).
id: sleep-recovery/nap-brief-rules-085
domain: sleep-recovery
grade: D (synthesis rule over 084, 009, 072, 082, 083 and 070; each rule's basis_grade is the strength of its own row, every boundary is product judgement)
lane: "@clinical"
locale: universal
as_of: 2026
contested: no
sources:
  - "sleep-recovery/nap-length-timing-short-night-084"  # nap length, inertia, 90 min, evening-lift null, coffee nap, night-sleep cost
  - "sleep-recovery/nap-force-null-shuttle-signal-009"  # 30 to under 60 min, more than 1 h before the test; force null
  - "sleep-recovery/brief-sleep-training-rules-072"  # brief_guards, nap-repay, nap-not-a-strength-tool, refined here
  - "sleep-recovery/caffeine-morning-brief-rules-083"  # short-night-afternoon-topup (nap first), caffeine_guards
  - "sleep-recovery/caffeine-tolerance-short-night-082"  # one short night vs a run of them
  - "sleep-recovery/caffeine-bedtime-cutoff-070"  # coffee-nap caffeine still counts against bedtime
  - "sleep-recovery/short-night-rules-081"  # the stated-cause short night block; one line per brief across both
  - "sleep-recovery/regularity-appetite-brief-rules-016"  # naps inside sleep_min; earlier bedtime or nap preferred to a lie-in
  - "framework:GRADE -- directions are inherited from 084 (C for the 10-20 min default after a short night, the 90 min caution, the evening-lift strength null, the coffee nap, late naps and the night; B for inertia being worst in the first 15-30 min and for an evening nap spending sleep pressure), 009 (B force null, C nap parameters) and 070 (B/C cutoffs). The boundaries -- 360 min as a short night (072), 10-20 min asleep and a 25 min alarm, the 30 min and 60 min wake buffers, 90 min as a long nap, a nap ending by 16:00 and at least 6 h before usual bedtime -- are product constants or source edges."
applicability:
  axes:
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: caffeine_sensitivity
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
constants:
  short_night_min: 360              # product, same line as 072 / 083
  short_nap_asleep_min: [10, 20]    # 084, Brooks & Lack 2006: 10 min best, 20 min helps; 30 min inertia
  short_nap_alarm_min: 25           # product: up to 20 min asleep plus about 5 min to fall asleep
  long_nap_asleep_min: [30, 60]     # 009 / 072, Mesas 2023 band
  short_nap_wake_buffer_min: 30     # product, from 084's inertia window (worst first 15-30 min)
  long_nap_wake_buffer_min: 60      # 009 / 072 (more than 1 h from waking to the test)
  full_cycle_nap_min: 90            # 084, Romdhani 2021: did worse than 20 min before a sprint test
  nap_latest_end_clock: "16:00"     # product; no trial sets a clock cutoff (084)
  nap_latest_end_h_before_bed: 6    # product; direction from Werth 1996 (an early-evening nap delays sleep)
  repeated_nights: [3, 7]           # product, 072's 3 of the last 7
nap_rules:
  - rule: short-night-short-nap
    needs: [sleep_min, nap_possible]
    when: sleep_min is below short_night_min, nap_possible is true, and the next session (or a drive) is less than 2 h after the nap could start, or no session time is known
    level: note
    say: a 10 to 20 minute nap in the early afternoon is the one that helps straight away without grogginess; set the alarm for about 25 minutes so you have time to fall asleep; leave about 30 minutes before training or driving
    never_say: that a nap makes up the lost night; a nap length longer than 20 min for this case
    product_constant: true
    basis: sleep-recovery/nap-length-timing-short-night-084
    basis_grade: C
  - rule: short-night-long-gap-nap
    needs: [sleep_min, nap_possible, session_time]
    when: sleep_min is below short_night_min, nap_possible is true, and the session is at least 2 h after the nap could start
    level: note
    say: either a 10 to 20 minute nap, or 30 to under 60 minutes if you wake from it at least an hour before training; the longer one leaves you groggy at first
    never_say: that the longer nap will make you stronger
    product_constant: true
    basis: sleep-recovery/nap-force-null-shuttle-signal-009
    basis_grade: C
  - rule: no-full-cycle-before-session
    needs: [session_time]
    when: the user plans or asks about a nap of about full_cycle_nap_min or longer on a day with a session after it
    level: hedge
    say: a 90 minute nap before training did worse than a 20 minute one in a small trial and left people sleepier; on a training day keep it short, and save a long nap for a free day
    never_say: that 90 minutes avoids grogginess because it is a full cycle
    product_constant: false
    basis: sleep-recovery/nap-length-timing-short-night-084
    basis_grade: C
  - rule: evening-session-nap
    needs: [session_time]
    when: the session starts 16:00 or later, sleep was short or the user feels flat, and nap_possible is true
    level: note
    say: an early-afternoon nap helps you feel more alert and in better mood for the evening session; it did not change strength in the trials, so keep the plan's loads as they are
    never_say: that the nap will raise the lift; to push for a heavier top set because you napped
    product_constant: true
    basis: sleep-recovery/nap-length-timing-short-night-084
    basis_grade: C
  - rule: nap-before-caffeine
    needs: [sleep_min]
    when: sleep_min is below short_night_min and the user asks whether to nap or have coffee in the afternoon
    level: note
    say: after a short night a short nap comes first; it helped in the trials where caffeine alone did not, and it does not reach tonight's sleep the way afternoon caffeine does
    never_say: that caffeine is bad; that one is always better than the other
    product_constant: false
    basis: sleep-recovery/nap-length-timing-short-night-084
    basis_grade: C
  - rule: coffee-nap
    needs: [caffeine_user, usual_bedtime]
    when: the user already takes caffeine and asks about having coffee right before a short nap, and the planned time is at least the 070 conservative_hours for the dose before usual_bedtime
    level: note
    say: caffeine taken just before a 15 to 20 minute nap worked better than either alone in small trials, because it starts acting about as you wake; it still counts against bedtime like any other cup
    never_say: a coffee nap to a non-user; a dose number under the 083 safety-gate; that the nap cancels the caffeine
    product_constant: false
    basis: sleep-recovery/nap-length-timing-short-night-084
    basis_grade: C
  - rule: coffee-nap-too-late
    needs: [caffeine_user, usual_bedtime]
    when: a coffee nap is planned inside the 070 conservative_hours for its dose before usual_bedtime (unknown dose = about 200 mg row)
    level: hedge
    say: at this time the caffeine is likely to cost tonight's sleep; take the nap without the coffee
    never_say: two different cutoffs for the same serve (083 cutoff-speak-one-number)
    product_constant: true
    basis: sleep-recovery/caffeine-bedtime-cutoff-070
    basis_grade: B
  - rule: late-nap
    needs: [usual_bedtime]
    when: the user plans or reports a nap ending after nap_latest_end_clock or less than nap_latest_end_h_before_bed before usual_bedtime
    level: hedge
    say: a nap this late uses up sleep pressure and can make tonight start later; if you need it, keep it short, or go to bed a little earlier instead
    never_say: a measured cutoff; that any late nap will ruin the night
    product_constant: true
    basis: sleep-recovery/nap-length-timing-short-night-084
    basis_grade: B
  - rule: daily-naps-poor-nights
    needs: [sleep_min]
    when: the user naps most days and also reports trouble falling or staying asleep at night
    level: hedge
    say: frequent and late naps go with more broken night sleep; try dropping or shortening the late ones for a week and see whether nights improve
    never_say: that naps are the cause; a diagnosis
    product_constant: true
    basis: sleep-recovery/nap-length-timing-short-night-084
    basis_grade: C
  - rule: could-not-sleep
    needs: []
    when: the user says they lay down to nap but did not really fall asleep
    level: note
    say: dozing or resting quietly still helped in the trials; it was not wasted
    never_say: that they must fall asleep for it to count
    product_constant: false
    basis: sleep-recovery/nap-length-timing-short-night-084
    basis_grade: C
  - rule: run-of-short-nights-nap
    needs: [sleep_min]
    when: sleep_min is below short_night_min on 3 or more of the last 7 nights and the user relies on daily naps to get through
    level: flag
    say: a nap covers one short night; when they repeat, the schedule is the fix, not more naps
    never_say: a nap plan as the answer to repeated short nights
    product_constant: true
    basis: sleep-recovery/brief-sleep-training-rules-072
    basis_grade: C
nap_guards:
  - guard: one nap line per brief across 072, 081, 083 and this block; pick the highest level; 083's short-night-afternoon-topup and this block's nap-before-caffeine are one line, not two
    basis_grade: D
  - guard: never suggest a nap unless nap_possible is true or the user raised it; never assume the user can nap at work
    basis_grade: D
  - guard: never frame a nap as raising strength or repaying the full night (009 force null, 072 nap-not-a-strength-tool)
    basis_grade: B
  - guard: no driving, heavy lifting or a maximal attempt in the first short_nap_wake_buffer_min after any nap, or long_nap_wake_buffer_min after a 30 min or longer nap
    basis_grade: B
  - guard: sleepiness while driving routes to stopping somewhere safe, not to a brief line; a stopped driver may take caffeine and a short nap if they already use caffeine
    basis_grade: C
  - guard: a logged nap is not night sleep; the morning brief's short-night decision uses the night only
    basis_grade: D
  - guard: daytime sleepiness that needs a nap every day despite enough night sleep, sudden sleep attacks or snoring with gasping route to a clinician (072 guard), not into nap advice
    basis_grade: B
refraction_notes:
  - note: >
      THE DIRECTIONS ARE GRADED, THE LINES ARE NOT. Short beats long right
      before training, a long nap needs an hour, a 90-minute nap is not the
      pre-session choice, the nap before an evening lift helps feel not
      force, a coffee nap works but still counts against bedtime, and late
      naps cost the night: each rests on a small trial or review. The
      25-minute alarm, the 30- and 60-minute buffers, the 16:00 and
      6-hours-before-bed lines and the 3-of-7 pattern are the plan's
      boundaries. Speak them as the plan's rules.
    grade: D
  - note: >
      072 STAYS, THIS REFINES IT. 072's nap-repay names 30 to under 60
      minutes ending more than an hour before training, and says no shorter
      nap was offered for want of a trial. 084 adds that trial (Brooks &
      Lack 2006), so this block offers the short nap first when the session
      is close and keeps 072's long nap as the option when there is time.
      072 itself was not edited; merging the two lines is left to an audit
      (GAPS).
    grade: D
  - note: >
      THE NAP-TO-BEDTIME LINE HAS A DIRECTION, NOT A NUMBER. An early-evening
      nap measurably spent sleep pressure for the night, and late naps went
      with poorer nights; nobody tested where the line is. 16:00 and 6 hours
      before bed are conservative product picks and are spoken as a hedge,
      never as a rule the user broke.
    grade: D
claim: >
  After a short night the brief can use six graded directions about napping,
  each with product boundaries: offer a 10 to 20 minute early-afternoon nap
  (alarm about 25 minutes) ending at least 30 minutes before training or
  driving, and keep 072's 30 to under 60 minute nap only when it can end an
  hour before; discourage a 90-minute nap on a training day; before an
  evening session say the nap helps alertness and mood, not strength; after
  a short night put the nap before afternoon caffeine; allow a coffee nap
  only for an existing caffeine user and only when the cup clears 070's
  cutoff for tonight; and hedge a nap ending after 16:00 or within 6 hours
  of bedtime, or daily naps with poor nights. Repeated short nights are
  flagged as a schedule problem, not a nap problem. The block sits under
  072's guards, speaks one nap line per brief, never presents a nap as a
  strength aid or a full repayment, and routes driving sleepiness and
  unexplained daytime sleepiness out of the brief.
reasoning: >
  Each rule lifts its direction from a graded row and keeps that row's grade
  as basis_grade. 084 supplies the duration, inertia, 90-minute, evening-lift,
  coffee-nap and night-sleep rows; 009 the long-nap band and force null; 070
  the cutoffs; 072 the repeated-nights flag and the guards. Splitting the
  short-night nap by the gap to the session is the one structural choice:
  the inertia evidence says the cost of a longer nap is the first 15-30
  minutes after it, so the session time decides which nap is safe, not the
  sleep number. The coffee nap is gated to existing users because 073 and
  083 never introduce caffeine; its cutoff reuses 083's one-number rule.
  The late-nap line is a hedge, not a flag, because the direction is
  physiological (B) but the cutoff is invented (D). Not contested: this row
  adds no primary claim of its own.
---

# sleep-recovery/nap-brief-rules-085 -- 브리프용 낮잠 규칙

**한 줄 그림:** 짧게 잔 날은 이른 오후에 10~20분 낮잠. 운동이 가까우면 짧게, 시간이 있으면 길게 자고
1시간 여유. 커피보다 낮잠이 먼저이고, 늦은 낮잠은 오늘 밤을 깎는다.

## The rule set

| Rule | When | Level | Basis |
|---|---|---|---|
| short-night-short-nap | under 6 h, nap possible, session close or unknown | note | 084 |
| short-night-long-gap-nap | under 6 h, session 2 h or more after the nap | note | 009 |
| no-full-cycle-before-session | 90 min nap on a training day | hedge | 084 |
| evening-session-nap | session 16:00 or later | note | 084 |
| nap-before-caffeine | under 6 h, nap or coffee? | note | 084 |
| coffee-nap | caffeine user, clears 070 cutoff | note | 084 |
| coffee-nap-too-late | inside 070 cutoff | hedge | 070 |
| late-nap | ends after 16:00 or under 6 h before bed | hedge | 084 |
| daily-naps-poor-nights | naps most days, poor nights | hedge | 084 |
| could-not-sleep | lay down, did not sleep | note | 084 |
| run-of-short-nights-nap | under 6 h on 3 of 7, leaning on naps | flag | 072 |

Guards: one nap line per brief; no nap unless possible or raised; never a
strength aid or full repayment; no driving or max attempt straight after;
driving sleepiness and unexplained daytime sleepiness route out.

## 한국어 요약 (답변용)

- 6시간 못 잔 날 낮잠을 잘 수 있으면 이른 오후에 10~20분 잔다. 잠드는 시간까지 넣어 알람은 25분쯤.
  깬 뒤 운동이나 운전까지 30분은 둔다.
- 운동까지 2시간 넘게 남았으면 30분에서 1시간 미만으로 자도 된다. 대신 깬 뒤 1시간은 비운다. 처음엔
  더 멍하다.
- 운동하는 날 90분 낮잠은 권하지 않는다. 작은 연구에서 20분보다 결과가 나빴고 더 졸렸다. 긴 낮잠은
  쉬는 날에.
- 저녁 운동 전 낮잠은 각성과 기분을 올리지만 힘은 올리지 않는다. 계획한 무게는 그대로 간다.
- 짧게 잔 날 오후엔 커피보다 낮잠이 먼저다. 커피를 원래 마시는 사람이 잠들기 전 기준 시간(070) 안에
  들어오지 않으면 '커피 마시고 바로 15~20분 낮잠'도 괜찮다. 그 카페인도 밤잠에 영향을 준다.
- 16시 넘어서 끝나거나 잠들기 6시간 안에 끝나는 낮잠은 오늘 밤 잠들기를 늦출 수 있다. 이 기준은 정한
  연구가 없는 계획상의 선이다.
- 거의 매일 낮잠을 자는데 밤잠이 나쁘면 늦은 낮잠부터 일주일쯤 줄여 본다.
- 잠들지 못하고 누워만 있었어도 도움이 됐다.
- 일주일에 사흘 넘게 짧게 자고 낮잠으로 버티면 일정을 고쳐야 한다. 운전 중 졸리면 먼저 안전한 곳에
  멈춘다. 밤에 충분히 자도 매일 낮잠이 필요하거나 갑자기 잠들거나 코골이와 숨 막힘이 있으면 병원으로
  안내한다.
