---
# Late-social-night sprint 2026-10-07 (a research sprint
# training). The engine-readable synthesis of 080 for the morning brief: after
# a late night with a cause the user has named (late social event, drinking,
# sleeping away from home), what the brief says about this morning's session
# -- keep, keep with a cap, swap the session kind, or offer rest. A routing
# rule, not a primary finding; same posture as 072 and exercise 056. Each rule
# names the graded row it rests on; every hour, minute and g/kg boundary not
# copied from a source is labelled a product constant.
#
# short_night_rules is structured data for the brief / session-prep code.
# DATA REALITY (2026-10-07): hk-ingest stores sleep_min only (asleep minutes
# summed per WAKE day); onset and wake clock times are not stored (016). The
# CAUSE of a late night is never inferred from data: it fires only from
# what the user said (night_context, stated in chat or a check-in), and the
# drink amount and last-drink time likewise come only from the user. Drinks
# are converted to grams with nutrition 032 and to g/kg with body_weight_kg;
# unknown weight uses 70 kg and hedges. Session kind comes from the plan
# (strength / power / conditioning / technical / easy / max-test).
#
# These rules sit UNDER 072's brief_guards (one sleep line per brief, never
# cancel on sleep alone, missing sleep_min means no sleep line). A plain short
# night with no stated cause stays with 072 short-night-morning and
# short-night-later; this block only fires when the user has named a cause or
# a drinking amount. When both blocks fire, the higher level wins and one
# line is spoken.
id: sleep-recovery/short-night-rules-081
domain: sleep-recovery
grade: D (synthesis rule over 080, 004, 072 and nutrition 031/032; each rule's basis_grade is the strength of its own row, every boundary is product judgement)
lane: "@clinical"
locale: universal
as_of: 2026
contested: no
sources:
  - "sleep-recovery/late-night-next-morning-training-080"  # the morning-after evidence: strength holds, power and hard conditioning slip, attention impaired, residual alcohol, first-night effect, consecutive nights
  - "sleep-recovery/brief-sleep-training-rules-072"  # plain short-night lines and the brief_guards this block sits under
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # late bedtime with usual wake time; AM sessions largely spared
  - "sleep-recovery/regularity-appetite-brief-rules-016"  # data reality (sleep_min only), late-lie-in and evening-appetite lines that may follow a late night
  - "sleep-recovery/adult-injury-risk-not-established-006"  # why no rule speaks an injury figure
  - "nutrition/alcohol-training-recovery-dose-031"  # g/kg dose bands (light < 0.25, moderate 0.25-0.75, heavy >= 0.75); no-moralizing rule
  - "nutrition/kr-alcohol-units-drinking-pattern-032"  # soju / beer to grams
  - "exercise/autoregulation-vs-percentage-prescription-030"  # loads from the warm-up
  - "exercise/caution-severity-ladder-056"  # routing posture for symptoms that leave training advice
  - "https://pubmed.ncbi.nlm.nih.gov/20304569/"  # Jones AW 2010 Forensic Sci Int 200:1-20 -- ethanol elimination about 15 mg/100 mL/h average (range 10-35); the arithmetic behind the residual-alcohol window
  - "framework:GRADE -- directions are inherited from 080 (C for the morning-after performance pattern, B for hangover attention and elimination rate, C for first night, D for injury) and 004 (B). The boundaries -- 0.75 g/kg as heavy (031's band edge), the 10-hour residual window, 240 minutes as a very short night, two consecutive nights, two days of carry-over -- are product constants or band edges, not tested thresholds."
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: sex
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: medication_list
      type: categorical
      role: hard
      unknown_policy: block_specifics
decision_levels:
  - decision: keep
    meaning: session as planned; only a new max or test is moved
  - decision: keep-capped
    meaning: session as planned with the top end capped (no max or test, top sets at about RPE 8 or one fewer top set), loads read from the warm-up
  - decision: swap
    meaning: same day, different session kind (power / hard conditioning / technical -> strength or easy aerobic)
  - decision: rest-offered
    meaning: the brief offers rest or an easy walk first and says the session is the user's call; it never cancels and never frames rest as a penalty
short_night_rules:
  - rule: late-bed-usual-wake
    needs: [night_context, sleep_min]
    when: night_context is late-social (no drinking, or light band under 0.25 g/kg) and sleep_min is 240 or more and the session is before 12:00
    decision: keep
    say: a late night with your usual wake-up is the kind of short night that costs least, and morning is the least affected time; train as planned, leave any new max for another day
    never_say: that the session should be skipped; a performance percentage
    product_constant: true
    basis: sleep-recovery/sleep-loss-performance-decrement-004
    basis_grade: B
  - rule: very-short-night
    needs: [sleep_min]
    when: night_context is stated and sleep_min is below 240 (or the user says they did not sleep)
    decision: keep-capped
    say: one very short night did little to strength in the lifting studies; keep the session, cap the top end, and set loads from how the warm-up moves
    never_say: that strength will be down by a set amount; that training now is risky
    product_constant: true
    basis: sleep-recovery/late-night-next-morning-training-080
    basis_grade: C
  - rule: residual-alcohol-window
    needs: [drinks_stated, last_drink_time, session_start]
    when: stated drinking is in the heavy band (0.75 g/kg or more) and the session starts less than 10 h after the last drink
    decision: rest-offered
    say: after a heavy night ending this late, some alcohol can still be in your blood this morning; do not drive there; if you train, keep it to machines or light steady work and skip heavy overhead, Olympic-style and balance work
    never_say: a blood alcohol number or a time when the user will be sober; that one drink of water or coffee clears it
    product_constant: true
    basis: https://pubmed.ncbi.nlm.nih.gov/20304569/
    basis_grade: B
  - rule: hangover-strength-day
    needs: [drinks_stated, session_kind]
    when: stated drinking is in the heavy band, residual-alcohol-window does not fire, and session_kind is strength
    decision: keep-capped
    say: maximal strength held the morning after heavy drinking in the studies; it will feel harder than it is, so set loads from the warm-up and skip any max
    never_say: that the session is wasted; that muscle is lost
    product_constant: false
    basis: sleep-recovery/late-night-next-morning-training-080
    basis_grade: C
  - rule: hangover-power-or-conditioning
    needs: [drinks_stated, session_kind]
    when: stated drinking is in the heavy band and session_kind is power, conditioning (intervals, time trial, sprint) or max-test
    decision: swap
    say: jump power and hard conditioning are what dropped the morning after (about 11 percent shorter in one cycling test); move today's intervals or test and do strength or easy aerobic work instead
    never_say: the 11 percent as the user's own loss; that easy cardio sweats the alcohol out
    product_constant: false
    basis: sleep-recovery/late-night-next-morning-training-080
    basis_grade: C
  - rule: hangover-technical
    needs: [drinks_stated, session_kind]
    when: stated drinking is in the heavy band, or sleep_min is below 240 after a stated late night, and session_kind is technical (Olympic lifts, climbing, sparring, skiing, trail running)
    decision: swap
    say: the clearest morning-after cost is attention and reaction speed, which is what technical and fall-prone work needs; pick the simpler variant or a strength day
    never_say: an injury multiplier; that the user will get hurt
    product_constant: false
    basis: sleep-recovery/late-night-next-morning-training-080
    basis_grade: B
  - rule: moderate-drinking
    needs: [drinks_stated]
    when: stated drinking is in the light or moderate band (under 0.75 g/kg)
    decision: keep
    say: no performance line; if the user asks, the clearer cost of this amount is sleep quality (031)
    never_say: that the amount is harmless or helpful
    product_constant: false
    basis: nutrition/alcohol-training-recovery-dose-031
    basis_grade: B
  - rule: slept-away-first-night
    needs: [night_context]
    when: night_context is slept-away and it was the first night in that place
    decision: keep
    say: the first night in a new bed is usually shorter and lighter and settles by the second; treat today like any short night
    never_say: that the user's sleep is disordered; a tracker reading as fact when the device was off or worn differently
    product_constant: false
    basis: sleep-recovery/late-night-next-morning-training-080
    basis_grade: C
  - rule: second-late-night
    needs: [night_context, sleep_min]
    when: a stated late night (any cause) follows another night with sleep_min below 360 and the session is a heavy compound day
    decision: keep-capped
    say: one short night barely touches strength, two in a row start to cut the big lifts; lighten the top sets today
    never_say: that the week is ruined
    product_constant: true
    basis: sleep-recovery/late-night-next-morning-training-080
    basis_grade: C
  - rule: no-carry-over
    needs: [drinks_stated]
    when: a heavy-band night was 2 or more days ago
    decision: keep
    say: no line; performance was back to baseline by the second day
    never_say: a delayed penalty, an extra rest day or punishment cardio
    product_constant: true
    basis: sleep-recovery/late-night-next-morning-training-080
    basis_grade: C
  - rule: unwell-routes-out
    needs: [symptoms_stated]
    when: the user reports vomiting, being unable to keep fluids down, chest pain, fainting, or confusion after drinking
    decision: rest-offered
    say: today is a rest and fluids day; if symptoms are severe or not settling, that is a medical question, not a training one
    never_say: a training substitute; a hangover remedy
    product_constant: false
    basis: exercise/caution-severity-ladder-056
    basis_grade: D
rule_guards:
  - guard: the cause of a late night and any drinking amount come only from the user's own words; never infer drinking from sleep_min, heart rate, spending or location
    basis_grade: D
  - guard: one line per brief across this block and 072/016; the highest decision wins (rest-offered > swap > keep-capped > keep); unwell-routes-out overrides all
    basis_grade: D
  - guard: rest is offered, never imposed; no rule cancels the session on sleep or drinking alone, and rest is never framed as penalty or 반성
    basis_grade: D
  - guard: no blood alcohol estimate, no "sober by" time, no injury multiplier, no performance percentage as a personal prediction
    basis_grade: B
  - guard: medication_list unknown or containing an alcohol-interacting drug withholds every drinking-specific line except do-not-drive and unwell-routes-out
    basis_grade: D
  - guard: no moralizing tone (031 no-moralizing); report the measured pattern and one practical change
    basis_grade: D
refraction_notes:
  - note: >
      THE DEFAULT IS KEEP. Of the eleven rules, the only ones that move a
      session away from the plan are tied to heavy drinking, a technical
      session, or feeling unwell. A late night alone, a strange bed or a
      moderate amount of drinking leaves the session in place.
    grade: B
  - note: >
      SWAP BEATS SKIP. The morning-after evidence finds strength held and
      power and hard conditioning down, so the useful move is changing the
      session kind for the day, not losing the day.
    grade: C
  - note: >
      THE 10-HOUR WINDOW IS ARITHMETIC, NOT A MEASUREMENT. At the average
      elimination rate of about 15 mg/100 mL per hour, a peak typical of a
      heavy night (around 100-150 mg/100 mL) takes roughly 7-10 hours to
      clear, and slower eliminators take longer. The window is the plan's
      rule built from that arithmetic; it is spoken as "alcohol can still be
      in your blood", never as a computed level.
    grade: D
  - note: >
      THE BOUNDARIES ARE THE PLAN'S. 0.75 g/kg is 031's heavy-band edge; 240
      minutes, two consecutive nights and two days are product constants.
      Speak them as this plan's rules.
    grade: D
claim: >
  After a late night the user has named, the morning brief chooses one of
  four decisions -- keep, keep-capped, swap, rest-offered -- from the cause,
  the stated drinking amount and timing, last night's sleep_min and the
  planned session kind. A late night with the usual wake time, a first night
  in a strange bed, or light-to-moderate drinking keeps the session (only a
  new max moves). A very short night (under 4 h) or a second short night
  before a heavy compound day caps the top end. Heavy drinking (0.75 g/kg or
  more) keeps a strength session with loads read from the warm-up, swaps
  power, interval, test and technical sessions for strength or easy work,
  and -- when the session starts less than 10 h after the last drink --
  offers rest first and says not to drive, because alcohol can still be in
  the blood. Nothing carries past the second day. Rest is offered, never
  imposed; no blood alcohol figure, injury multiplier or personal
  performance percentage is spoken; the cause is taken only from the user's
  own words.
reasoning: >
  Each rule is the operational shadow of one statement in 080 (or 004, 031,
  056) and keeps that row's grade as basis_grade so the module can phrase it
  at the right strength. The decision ladder exists because the evidence is
  about which part of a session suffers, not about whether to train: strength
  held in every morning-after study, explosive and severe-intensity work did
  not, and attention is the best-pooled cost -- hence swap for power,
  conditioning and technical days and keep-capped for strength. The only
  rest-first rule rests on elimination arithmetic and a safety consequence
  (driving, falls), not on performance. Data are deliberately narrow:
  sleep_min is the only measured input; cause, amount and timing are stated,
  which keeps the brief from guessing that the user drank and keeps it
  within 031's no-moralizing posture. Sitting under 072's guards prevents two
  sleep lines in one brief.
---

# sleep-recovery/short-night-rules-081 -- 늦은 밤 다음 날 아침 운동 규칙 (브리프용)

**한 줄 그림:** 늦게 잤다는 이유만으로는 운동을 빼지 않는다. 과음한 날은 운동 종류를 바꾸고,
술이 남아 있을 수 있는 아침에만 쉬자고 먼저 제안한다.

## The rules

| Rule | Fires when | Decision | Basis |
|---|---|---|---|
| late-bed-usual-wake | late social night, little or no alcohol, 4 h+ sleep, AM session | keep | 004 |
| very-short-night | stated late night, under 4 h | keep-capped | 080 |
| residual-alcohol-window | heavy drinking, session under 10 h after last drink | rest-offered | Jones 2010 |
| hangover-strength-day | heavy drinking, strength session | keep-capped | 080 |
| hangover-power-or-conditioning | heavy drinking, power / intervals / test | swap | 080 |
| hangover-technical | heavy drinking or under 4 h, technical session | swap | 080 |
| moderate-drinking | under 0.75 g/kg | keep | 031 |
| slept-away-first-night | first night in a new place | keep | 080 |
| second-late-night | second short night before heavy compound day | keep-capped | 080 |
| no-carry-over | heavy night 2+ days ago | keep | 080 |
| unwell-routes-out | vomiting, can't keep fluids, chest pain, fainting, confusion | rest-offered | 056 |

Guards: cause and amount from the user's words only; one line per brief with
072/016; rest offered, never imposed; no blood alcohol, injury or percentage
figure; medication gate; no moralizing.

## 한국어 요약 (답변용)

- 회식·모임으로 늦게 잤어도 평소 시각에 일어났고 술을 거의 안 마셨다면 아침 운동은 그대로 한다.
  신기록 시도만 미룬다.
- 4시간도 못 잤으면 운동은 하되 탑세트를 낮추고(최대 시도 없음), 워밍업 느낌으로 무게를 정한다.
- 과음(체중 1kg당 0.75g 이상, 70kg이면 소주 1병 넘게)한 다음 날: 근력 운동은 그대로 하되 무게를
  욕심내지 않는다. 점프·인터벌·기록 측정·역도·클라이밍·스파링은 근력 운동이나 가벼운 유산소로
  바꾼다.
- 마지막 잔에서 운동까지 10시간이 안 되면 술이 아직 남아 있을 수 있다. 운전해서 가지 말고, 쉬자고
  먼저 제안한다. 한다면 머신이나 가벼운 운동만. 혈중 농도나 "몇 시면 깬다"는 말하지 않는다.
- 소주 몇 잔 정도(0.75g/kg 미만)는 운동 경고를 하지 않는다. 물어보면 수면 질 쪽 영향만 말한다.
- 낯선 곳에서 잔 첫날 밤은 짧고 얕은 게 보통이다. 그냥 짧게 잔 날처럼 다룬다.
- 짧은 밤이 이틀 연속이면 무거운 스쿼트·데드리프트 날의 탑세트를 낮춘다.
- 과음 후 이틀이 지나면 아무 말도 하지 않는다. 벌칙 유산소나 추가 휴식은 없다.
- 토하거나 물도 못 넘기거나, 가슴 통증·실신·혼란이 있으면 운동 얘기가 아니라 쉬고 수분 섭취,
  심하면 진료로 안내한다.
- 술을 마셨는지는 사용자가 말한 것만 쓴다. 수면 기록이나 심박으로 추측하지 않는다. 훈계하지 않는다.
