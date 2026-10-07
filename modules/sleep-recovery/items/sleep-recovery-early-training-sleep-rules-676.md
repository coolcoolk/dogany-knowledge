---
# Early-training bedtime sprint 2026-10-07 (numbers are this branch's claim, renumber at
# merge). The engine-readable synthesis of 675 with 071 / 072 / 081 / 085 /
# 016 / 007 for the EVENING brief before a 05:00-06:00 session, plus the
# few morning and weekend lines that only make sense from that angle: when
# to start winding down, what the lights should do, how a weekend lie-in
# changes the eve of the first training day, and what to say when the user
# lies awake at the early bedtime or says they feel fine. A routing rule,
# not a primary finding; same posture as 072, 081 and 085. Each rule names
# the graded row it rests on; every clock time and minute not copied from a
# source is labelled a product constant.
#
# early_training_sleep_rules is structured data for the brief code.
# DATA REALITY (2026-10-07): hk-ingest stores sleep_min only (asleep minutes
# summed per wake day, naps included; 016). Tomorrow's session_start comes
# from the plan; usual_wake_training (the alarm on training days) and
# usual_bedtime are stated once by the user and stored as profile facts.
# Rules that need onset_wake_times (actual wake clock time) cannot fire
# until those are stored; they are declared so the next build knows what to
# keep, never so the brief guesses a wake time. Nothing here is inferred
# from phone use, location or heart rate.
#
# These rules sit UNDER 072's brief_guards (one sleep line per brief, never
# cancel on sleep alone, no readiness score, missing sleep_min means no
# line). They own the EVENING brief; the morning lines stay in 072 / 081 /
# 083 / 085 and exercise 073. 072 repeated-short-nights stays the flag; this
# block only adds the copy that goes with it when the user says they feel
# fine. Caffeine timing stays in 070 / 083 and is not restated.
id: sleep-recovery/early-training-sleep-rules-676
domain: sleep-recovery
grade: D (synthesis rule over 675, 071, 072, 016, 012 and 007; each rule's basis_grade is the strength of its own row, every clock time and window is product judgement)
lane: "@clinical"
locale: universal
as_of: 2026
contested: no
sources:
  - "sleep-recovery/early-training-bedtime-wake-regularity-675"  # wake-time shift, evening room light, light consensus, warm water, unnoticed deficit, individual need
  - "sleep-recovery/early-morning-session-071"  # bedtime-anchor (lights-out about 7.5 h before wake-up), chronic-short-sleep
  - "sleep-recovery/brief-sleep-training-rules-072"  # brief_guards; repeated-short-nights flag; early-alarm-pattern
  - "sleep-recovery/short-night-rules-081"  # the late-night-with-a-cause morning block; one line across both
  - "sleep-recovery/nap-brief-rules-085"  # the nap repays the short night; earlier bedtime or nap preferred to a lie-in
  - "sleep-recovery/regularity-appetite-brief-rules-016"  # late-lie-in (120 min) and irregular-week; data reality (sleep_min only)
  - "sleep-recovery/regularity-vs-duration-014"  # weekend catch-up contested, not forbidden
  - "sleep-recovery/evening-light-mechanism-vs-intervention-012"  # no blue-light-glasses advice
  - "sleep-recovery/cbti-strong-sleep-hygiene-weak-007"  # lying awake repeatedly routes to CBT-I, not more hygiene
  - "sleep-recovery/caffeine-morning-brief-rules-083"  # caffeine lines live there
  - "exercise/early-morning-session-brief-rules-073"  # the 04:30 morning brief this evening brief pairs with
  - "framework:GRADE -- directions are inherited from 675 (B: later wake delays the clock, evening room light delays melatonin, chronic restriction goes unnoticed; C: warm water before bed, daylight; D: consensus light thresholds, individual need), 071 (D anchor, C chronic pattern) and 007 (A: CBT-I strong, hygiene alone weak). The constants -- lights-out = wake minus 7.5 h, the evening brief 90 min before lights-out, wind-down 60 min, lights lowered from 3 h before (Brown 2022's figure, used as a cue time), the 120-min weekend shift (016's line), lights-out moved no more than 30 min, 3 nights of lying awake, 30 min awake in bed -- are product constants or source edges."
applicability:
  axes:
    - key: chronotype
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
constants:
  early_start_window: ["05:00", "06:00"]   # sessions this block serves (071); a 06:01-07:00 start uses the same rules with its own wake time
  anchor_offset_min: 450                    # lights-out = usual_wake_training - 450 (071 bedtime-anchor, product)
  evening_brief_lead_min: 90                # evening brief sent 90 min before lights-out (product)
  wind_down_min: 60                         # screens and work down 60 min before lights-out (product)
  dim_lights_lead_min: 180                  # Brown 2022: evening light low from at least 3 h before bedtime (consensus, used as a cue time)
  warm_water_lead_min: [60, 120]            # Haghayegh 2019 via 675
  weekend_shift_min: 120                    # same line as 016 late-lie-in (product)
  max_bedtime_pullforward_min: 30           # never move lights-out earlier than usual by more than this in one step (product)
  awake_in_bed_min: 30                      # stated lying awake this long counts as a night lying awake (product)
early_training_sleep_rules:
  - rule: eve-bedtime-line
    needs: [session_start_tomorrow, usual_wake_training]
    when: tomorrow's session starts 05:00-06:00 and the evening brief is due
    level: note
    say: one line with tonight's lights-out (usual_wake_training minus 7.5 h, e.g. 21:00 for 04:30) and the wind-down start 60 min before it; offered as the plan's anchor, not an order
    never_say: a required bedtime; a sleep score; that the user will perform badly if they miss it
    product_constant: true
    basis: sleep-recovery/early-morning-session-071
    basis_grade: D
  - rule: eve-lights-down
    needs: [session_start_tomorrow, usual_wake_training]
    when: eve-bedtime-line fires and the user has not muted light lines
    level: note
    say: after dinner, lower and warmer lights and a dark bedroom; bright screens late push sleep later
    never_say: a lux number; blue-light glasses or night-mode as the fix; that screens are forbidden
    product_constant: true
    basis: sleep-recovery/early-training-bedtime-wake-regularity-675
    basis_grade: B
  - rule: eve-after-weekend-shift
    needs: [session_start_tomorrow, usual_wake_training, onset_wake_times]
    when: tomorrow starts 05:00-06:00 and today's (or the day off's) wake time was 120 min or more later than usual_wake_training
    level: hedge
    say: after a later wake-up today, sleep may come later than the anchor tonight; keep the alarm, go to bed at the usual time and do not go earlier to compensate; if it was a short night, the nap and the next night repay it
    never_say: that the weekend was a mistake; that the user should not have slept in; a minute figure for the clock shift
    product_constant: true
    basis: sleep-recovery/early-training-bedtime-wake-regularity-675
    basis_grade: B
  - rule: weekend-wake-anchor
    needs: [onset_wake_times, usual_wake_training]
    when: the user asks how to make early weeks easier, or eve-after-weekend-shift has fired on 2 of the last 3 weeks
    level: note
    say: on days off, waking within about 2 h of the training alarm and getting daylight early keeps the first early night easier; if the week ran short, an earlier bedtime or a nap repays it better than a long lie-in
    never_say: that lie-ins are harmful (014 marks catch-up contested); a mortality or weight figure
    product_constant: true
    basis: sleep-recovery/early-training-bedtime-wake-regularity-675
    basis_grade: B
  - rule: daylight-after-session
    needs: [session_start]
    when: the user asks how to fall asleep earlier, or eve-after-weekend-shift fired yesterday
    level: note
    say: get outdoor daylight in the morning after the session (the walk or commute counts); bright days and dim evenings are what pull sleep earlier
    never_say: a lux or minute dose; that gym lighting at 04:30 resets the clock
    product_constant: false
    basis: sleep-recovery/early-training-bedtime-wake-regularity-675
    basis_grade: C
  - rule: warm-shower-option
    needs: []
    when: the user asks for a wind-down step, or lying-awake-early has fired once
    level: none
    say: a warm shower or bath 1-2 h before lights-out, even 10 min, helped people fall asleep a few minutes sooner
    never_say: that it treats insomnia; a water temperature as a requirement
    product_constant: false
    basis: sleep-recovery/early-training-bedtime-wake-regularity-675
    basis_grade: C
  - rule: lying-awake-early
    needs: [awake_in_bed_stated]
    when: the user says they lay awake 30 min or more after the early lights-out on 1-2 of the last 7 nights
    level: note
    say: an early bedtime can come before the body is sleepy, especially after a later wake-up; keep the alarm fixed, keep lights-out where it is rather than moving it earlier, and if awake a long time, get up in dim light and come back when sleepy
    never_say: that the user has insomnia; a sleeping pill or melatonin dose (008 routes melatonin)
    product_constant: true
    basis: sleep-recovery/early-training-bedtime-wake-regularity-675
    basis_grade: B
  - rule: lying-awake-persistent
    needs: [awake_in_bed_stated]
    when: lying awake 30 min or more on 3 or more nights a week for 2 or more weeks, or the user says it is a long-standing problem
    level: flag
    say: this is worth more than a bedtime tweak; the treatment with the strongest evidence is CBT-I, and a clinician or a CBT-I program is the route
    never_say: a diagnosis; more sleep-hygiene tips as the answer
    product_constant: true
    basis: sleep-recovery/cbti-strong-sleep-hygiene-weak-007
    basis_grade: A
  - rule: feels-fine-pattern
    needs: [sleep_min]
    when: 072 repeated-short-nights fires and the user says they feel fine or questions the flag
    level: flag
    say: in a two-week lab study, people on 6 h nights kept losing ground while feeling only a little sleepy; the record, not the feeling, is the better test of whether the early schedule fits
    never_say: that the user is impaired; a performance percentage; a health risk figure
    product_constant: false
    basis: sleep-recovery/early-training-bedtime-wake-regularity-675
    basis_grade: B
  - rule: individual-need
    needs: [sleep_baseline_hours]
    when: the user says they do well on less than 7 h without daytime sleepiness, and 072 repeated-short-nights does not fire
    level: none
    say: 7 h is a population floor, not a personal target; if days feel alert and training progresses, the brief will not push more
    never_say: that under 7 h is always harmful; that the user is a short sleeper
    product_constant: false
    basis: sleep-recovery/hour-target-is-a-threshold-consensus-013
    basis_grade: B
  - rule: bedtime-pullforward-cap
    needs: [usual_bedtime, usual_wake_training]
    when: usual_bedtime is later than the anchor and the user wants to move toward it
    level: note
    say: move lights-out earlier by about 30 min at a time over several days, alarm fixed, rather than jumping straight to the anchor
    never_say: that the user must reach the anchor this week
    product_constant: true
    basis: sleep-recovery/early-training-bedtime-wake-regularity-675
    basis_grade: D
  - rule: no-eve-line
    needs: [session_start_tomorrow]
    when: no session tomorrow, or tomorrow's session starts after 07:00, or the user muted evening lines
    level: none
    say: no evening sleep line; 016 weekly lines may still fire on their own cadence
    never_say: a bedtime
    product_constant: true
    basis: sleep-recovery/brief-sleep-training-rules-072
    basis_grade: D
rule_guards:
  - guard: one sleep line in the evening brief; the highest level wins (flag > hedge > note > none); lying-awake-persistent overrides all
    basis_grade: D
  - guard: the evening brief speaks lights-out as the plan's anchor, never a curfew; missing it is never framed as failure and no morning line refers back to it
    basis_grade: D
  - guard: no lux, melanopic or minute-of-clock-shift figure reaches the user; the numbers stay as cue times in the engine
    basis_grade: D
  - guard: wake times are never inferred; rules needing onset_wake_times do not fire until those are stored
    basis_grade: D
  - guard: no supplement, melatonin or medication advice from this block; melatonin questions route to 008, insomnia to 007
    basis_grade: B
  - guard: the evening line is suppressed after the user's lights-out time (no late-night nudges that themselves keep the user awake)
    basis_grade: D
refraction_notes:
  - note: >
      THE EVENING BRIEF IS WHERE A 05:00 SESSION IS PROTECTED. The morning
      brief can only react to last night; the one decision that changes
      tonight's sleep is when the evening winds down. So this block speaks
      once, about 90 minutes before lights-out, and says two things: when,
      and lights down.
    grade: D
  - note: >
      DO NOT CHASE THE ANCHOR AFTER A LATE WAKE-UP. After a weekend lie-in
      the clock is later than the wall, so going to bed even earlier to
      compensate means more time awake in bed. Keep the alarm fixed and the
      usual lights-out; the morning daylight and the next night do the
      rest.
    grade: B
  - note: >
      LYING AWAKE IS A ROUTE, NOT A NUDGE, WHEN IT PERSISTS. Once or twice
      after a weekend it is expected and gets one practical line. Most
      nights for weeks is the insomnia pattern, where hygiene tips are
      advised against as a standalone treatment and CBT-I is strongly
      recommended.
    grade: A
  - note: >
      THE CLOCK TIMES ARE THE PLAN'S. 7.5 hours before the alarm, 90 and 60
      minutes before lights-out, 3 hours of dim light, 2 hours of weekend
      shift and 30-minute steps are product constants or a consensus figure
      used as a cue. Speak them as this plan's rules.
    grade: D
claim: >
  For a 05:00-06:00 lifter the evening brief, sent about 90 minutes before
  lights-out on the eve of a session, says one thing: tonight's lights-out
  (the training alarm minus 7.5 hours, so about 21:00 for a 04:30 alarm) with
  the wind-down starting an hour before, and lights lowered after dinner.
  After a day off with a wake-up 2 hours or more later than the training
  alarm, it says sleep may come later tonight and to keep the alarm and the
  usual bedtime rather than going to bed earlier. On request it offers
  weekend wake-ups within about 2 hours of the alarm, outdoor daylight after
  the session and a warm shower 1-2 hours before bed. Lying awake once or
  twice gets a keep-the-alarm line; lying awake most nights for weeks routes
  to CBT-I. When short nights repeat and the user feels fine, the brief
  explains that chronic short sleep is under-felt and keeps the flag. Every
  clock time is a product constant; no lux figure, curfew or blame is
  spoken.
reasoning: >
  Each rule is the operational shadow of one statement in 675 (or 071, 013,
  007) and keeps that row's grade as basis_grade. The block exists because
  every existing sleep rule set (072, 081, 083, 085, exercise 073) speaks in
  the morning, after the night is over; the only point where the user can
  still change tonight's sleep is the evening. The wake-time evidence drives
  the two least intuitive rules: do not move bedtime earlier after a
  lie-in (the clock is later, so the extra time is spent awake) and move
  toward the anchor in steps. The light rules translate a lab result and a
  consensus into one behaviour (lights down after dinner) and deliberately
  keep numbers out of the user's view, because the thresholds are a
  consensus and 012 shows the consumer product version does not deliver.
  The lying-awake split follows 007's line between hygiene and CBT-I. Rules
  that need wake clock times are declared and inert until those are stored,
  the same discipline as 016.
---

# sleep-recovery/early-training-sleep-rules-676 -- 새벽 운동 전날 밤 브리프 규칙

**한 줄 그림:** 새벽 운동은 전날 저녁 브리프가 지킨다. 불 끄는 시각 하나, 조명 낮추기 하나만 말하고,
주말에 늦게 일어난 날은 더 일찍 자라고 하지 않는다.

## The rules

| Rule | Fires when | Level | Basis |
|---|---|---|---|
| eve-bedtime-line | session 05:00-06:00 tomorrow | note | 071 |
| eve-lights-down | with the bedtime line | note | 675 |
| eve-after-weekend-shift | woke 120+ min later than the training alarm today | hedge | 675 |
| weekend-wake-anchor | user asks, or the shift fired 2 of 3 weeks | note | 675 |
| daylight-after-session | user asks how to fall asleep earlier | note | 675 |
| warm-shower-option | user asks for a wind-down step | none | 675 |
| lying-awake-early | awake 30+ min at lights-out, 1-2 nights | note | 675 |
| lying-awake-persistent | 3+ nights a week for 2+ weeks | flag | 007 |
| feels-fine-pattern | 072 repeated-short-nights + "I feel fine" | flag | 675 |
| individual-need | does well under 7 h, no flag | none | 013 |
| bedtime-pullforward-cap | moving toward the anchor | note | 675 |
| no-eve-line | no early session tomorrow | none | 072 |

Example: alarm 04:30 -> lights-out 21:00, evening brief 19:30, wind-down 20:00,
lights lowered after dinner (about 18:00).

Guards: one line; anchor, not curfew; no lux or clock-shift figure; wake times
never inferred; no melatonin or medication advice; nothing after lights-out.

## 한국어 요약 (답변용)

- 내일 새벽 5~6시 운동이 있으면, 불 끄기 약 90분 전에 저녁 브리프 한 줄: 오늘 불 끄는 시각(알람 7.5시간 전,
  4시 30분 알람이면 9시)과 1시간 전부터 마무리 시작. 지켜야 할 통금이 아니라 계획의 기준이다.
- 저녁 먹은 뒤에는 조명을 낮추고 따뜻한 색으로, 침실은 어둡게. 밝은 화면은 잠을 늦춘다. 룩스 숫자나 블루라이트
  안경 얘기는 하지 않는다.
- 쉬는 날 평소 알람보다 2시간 이상 늦게 일어났다면: 오늘 밤엔 잠이 늦게 올 수 있다. 알람은 그대로, 취침도
  평소대로. 더 일찍 눕지 않는다. 늦잠을 탓하지 않는다.
- 물어보면: 쉬는 날에도 알람과 2시간 안쪽으로 일어나기, 운동 뒤 바깥 햇빛, 자기 1~2시간 전 따뜻한 샤워.
- 일찍 누웠는데 30분 넘게 잠이 안 온 밤이 한두 번이면 정상이다. 알람 고정, 취침 시각을 더 당기지 않기, 오래
  깨어 있으면 어두운 곳에서 잠깐 일어났다가 졸릴 때 다시 눕기.
- 일주일에 3일 이상, 2주 넘게 그렇다면 생활 팁이 아니라 CBT-I(불면 인지행동치료)로 안내한다.
- 짧은 잠이 반복되는데 "괜찮다"고 하면: 6시간 수면 2주 실험에서 사람들은 조금 졸린 정도로 느꼈지만 저하는
  계속 쌓였다. 느낌보다 기록을 본다.
- 7시간 미만이어도 낮에 멀쩡하고 운동이 늘면 더 자라고 밀지 않는다.
- 늦게 자던 사람은 한 번에 기준 시각으로 당기지 말고 30분씩 며칠에 걸쳐 앞당긴다.
- 시각 기준(7.5시간, 90·60분, 3시간, 2시간, 30분)은 모두 제품 규칙이다.
