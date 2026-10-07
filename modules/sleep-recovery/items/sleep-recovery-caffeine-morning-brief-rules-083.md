---
# Caffeine / early-training sprint 2026-10-07. The engine-readable synthesis of 082 with
# 069 / 070 / 071 for the morning brief: what the brief says about caffeine
# on a training morning -- dose for a habitual user, a skipped usual coffee,
# caffeine after a short night, the afternoon top-up, a run of short nights,
# and which bedtime cutoff to speak. A routing rule, not a primary finding;
# same posture as 072, 081 and exercise 073. Each rule names the graded row
# it rests on; every hour, mg and count not copied from a source is labelled
# a product constant.
#
# caffeine_rules is structured data for the brief / session-prep code.
# DATA REALITY (2026-10-07): hk-ingest stores sleep_min only (016). Caffeine
# is never inferred from data: caffeine_user, usual_caffeine (amount and
# times) and today's last caffeine come only from what the user said in chat
# or a check-in. Bedtime is the stated usual bedtime. Dose in mg/kg uses
# body_weight_kg; unknown weight uses 70 kg and hedges.
#
# These rules sit UNDER 072's brief_guards (one sleep line per brief, never
# cancel on sleep alone, no readiness score) and BESIDE exercise 073's
# dawn-caffeine-if-user and afternoon-caffeine-cutoff, which they refine, not
# replace: 073 says when and how much on a dawn morning; this block adds what
# a daily habit and a short night change. When a rule here and a 072 / 073 /
# 081 line fire on the same morning, one caffeine line is spoken -- the
# higher level wins (flag > hedge > note).
# Source re-audit 2026-10-07: one source line linking 085 (nap rules); no rule, constant or grade change.
id: sleep-recovery/caffeine-morning-brief-rules-083
domain: sleep-recovery
grade: D (synthesis rule over 082, 070, 069, 071 and 072; each rule's basis_grade is the strength of its own row, every boundary is product judgement)
lane: "@clinical"
locale: universal
as_of: 2026
contested: no
sources:
  - "sleep-recovery/caffeine-tolerance-short-night-082"  # habitual intake, partial tolerance, withdrawal relief, daily habit vs sleep, one vs several short nights
  - "sleep-recovery/caffeine-bedtime-cutoff-070"  # dose x hours-before-bed table (product_hours, conservative_hours)
  - "exercise/early-morning-caffeine-food-069"  # dawn dose 3-6 mg/kg, 200 mg single-dose ceiling, pregnancy / cardiovascular gate
  - "exercise/early-morning-session-brief-rules-073"  # dawn-caffeine-if-user and afternoon-caffeine-cutoff, refined here
  - "sleep-recovery/early-morning-session-071"  # morning-caffeine-ok
  - "sleep-recovery/brief-sleep-training-rules-072"  # brief_guards, repeated-short-nights, nap-repay, caffeine-late
  - "sleep-recovery/short-night-rules-081"  # the stated-cause short night block; one line per brief across both
  - "sleep-recovery/nap-force-null-shuttle-signal-009"  # nap as the first alternative to an afternoon top-up
  - "sleep-recovery/nap-brief-rules-085"  # nap-before-caffeine and coffee-nap: which nap, and the coffee nap against 070
  - "framework:GRADE -- directions are inherited from 082 (B for habitual intake not cancelling the effect and above-6-mg/kg adding nothing, and for caffeine losing its effect over a run of restricted nights; C for partial tolerance, withdrawal relief, daily-habit sleep and the one-short-night protection; D for the afternoon loop) and 070 (B/C for the cutoffs). The boundaries -- 360 min as a short night (072 / 073), 3 of the last 7 nights (072), 8 h before bed as a daily-habit line (the tested schedule, not a threshold), 6 mg/kg ceiling, 200 mg single-dose ceiling (069) -- are product constants or source edges."
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
  short_night_min: 360            # product, same line as 072 / 073
  repeated_nights: [3, 7]         # product, 072's 3 of the last 7
  dose_ceiling_mg_per_kg: 6       # 082, Carvalho 2022: no detectable added effect above 6 mg/kg
  single_dose_ceiling_mg: 200     # 069, EFSA 2015 safety ceiling, not an ergogenic target
  daily_habit_last_dose_h: 8      # 082, Weibel 2021 tested schedule (last 150 mg dose 8 h before bed); not a threshold
caffeine_rules:
  - rule: habit-no-bigger-dose
    needs: [caffeine_user, usual_caffeine]
    when: the user takes caffeine daily and asks whether they need more before training, or states a pre-session dose above their usual amount
    level: note
    say: a daily habit does not cancel the pre-session effect; your usual amount works, and going above about 6 mg per kg adds nothing measurable
    never_say: that tolerance means a bigger dose; a dose above single_dose_ceiling_mg as advice
    product_constant: false
    basis: sleep-recovery/caffeine-tolerance-short-night-082
    basis_grade: B
  - rule: no-washout-needed
    needs: [caffeine_user]
    when: the user asks about cycling off caffeine or a washout before a test or competition
    level: note
    say: stopping beforehand is optional, not required; the effect held in trials whether or not people abstained first. Daily use trims it a little over weeks, it does not remove it
    never_say: a set number of days off; that daily users get no benefit
    product_constant: false
    basis: sleep-recovery/caffeine-tolerance-short-night-082
    basis_grade: B
  - rule: skipped-usual-coffee
    needs: [caffeine_user, usual_caffeine]
    when: a daily user says they skipped or ran out of their usual morning caffeine and feels flat or has a headache before a session
    level: note
    say: in daily users much of the morning lift from coffee is relief from overnight withdrawal; the flat start is that, not lost fitness. Your usual amount is fine if you want it; no extra
    never_say: that the session will be bad; that the headache is nothing if it is severe or unusual
    product_constant: false
    basis: sleep-recovery/caffeine-tolerance-short-night-082
    basis_grade: C
  - rule: short-night-usual-dose
    needs: [caffeine_user, sleep_min]
    when: sleep_min is below short_night_min, the session is in the morning, and the user takes caffeine before training
    level: note
    say: your usual pre-session caffeine is reasonable after a short night and may hold up some sharpness; a bigger dose did no better in the one trial
    never_say: that caffeine replaces the lost sleep; to double the dose
    product_constant: true
    basis: sleep-recovery/caffeine-tolerance-short-night-082
    basis_grade: C
  - rule: short-night-afternoon-topup
    needs: [sleep_min, usual_bedtime]
    when: sleep_min is below short_night_min and the user mentions or plans extra caffeine after midday
    level: hedge
    say: the morning dose is far from bed; an afternoon top-up is the one that reaches tonight's sleep and sets up another short night. A nap first; if caffeine, keep it before bedtime minus the 070 hours for its dose
    never_say: that all afternoon caffeine is forbidden; a cutoff in clock time without the user's bedtime
    product_constant: true
    basis: sleep-recovery/caffeine-bedtime-cutoff-070
    basis_grade: B
  - rule: run-of-short-nights
    needs: [sleep_min]
    when: sleep_min is below short_night_min on 3 or more of the last 7 nights and the user says they are leaning on caffeine to get through
    level: flag
    say: caffeine covers one short night, but in the trials it stopped helping after about three in a row and recovery was slower; the fix is the schedule, not more caffeine
    never_say: a dose to push through; that the user is dependent
    product_constant: true
    basis: sleep-recovery/caffeine-tolerance-short-night-082
    basis_grade: B
  - rule: daily-habit-sleep-ok
    needs: [usual_caffeine, usual_bedtime]
    when: the user asks whether their daily coffee habit is hurting their sleep, and all usual caffeine is at least daily_habit_last_dose_h before bedtime with no single serve over the 070 about-100 mg row
    level: none
    say: a morning-and-midday habit ending about 8 h before bed did not change measured or felt sleep in a controlled trial; a late serve is what to watch
    never_say: that the habit has no effect at all; that more is fine
    product_constant: false
    basis: sleep-recovery/caffeine-tolerance-short-night-082
    basis_grade: C
  - rule: cutoff-speak-one-number
    needs: [usual_bedtime]
    when: any caffeine bedtime cutoff is spoken in a brief (this block, 072 caffeine-late, 073 afternoon-caffeine-cutoff)
    level: none
    say: use 070's rows; for up to about 100 mg speak the conservative_hours (9 h), which agrees with 073's 8.8 h; for about 200 mg or an unknown dose, 13 h; for 400 mg or more, 14 h
    never_say: two different cutoffs for the same serve in one brief; the 4 h low-dose figure as a target
    product_constant: true
    basis: sleep-recovery/caffeine-bedtime-cutoff-070
    basis_grade: D
  - rule: safety-gate
    needs: [pregnancy_status, cardiovascular_condition, medication_list]
    when: pregnancy_status, cardiovascular_condition or medication_list is outside its allowed set, unknown or refused, or the user mentions hormonal contraception
    level: none
    say: speak direction only (earlier is better for sleep, the usual amount is enough) and the conservative cutoff column; no mg or mg/kg number
    never_say: a dose number; that caffeine is safe for them
    product_constant: true
    basis: exercise/early-morning-caffeine-food-069
    basis_grade: B
caffeine_guards:
  - guard: never suggest caffeine to someone who has not said they use it (073); these rules only refine an existing habit
    basis_grade: D
  - guard: one caffeine line per brief across 072, 073, 081 and this block; pick the highest level
    basis_grade: D
  - guard: never frame caffeine as a substitute for sleep or a way to repay a short night
    basis_grade: B
  - guard: never advise waking earlier to fit caffeine in (073 no-earlier-alarm)
    basis_grade: B
  - guard: palpitations, chest pain, fainting or severe headache route out of the brief to a clinician, not into dose advice
    basis_grade: D
refraction_notes:
  - note: >
      THE DIRECTIONS ARE GRADED, THE LINES ARE NOT. That a daily habit does
      not cancel the pre-session dose, and that caffeine stops covering a run
      of restricted nights, rest on a meta-analysis and a laboratory RCT. The
      360-minute night, the 3-of-7 pattern, the 8-hour daily-habit line and
      the choice of 9 h as the spoken low-dose cutoff are the plan's
      boundaries. Speak them as the plan's rules.
    grade: D
  - note: >
      ONE CUTOFF PER SERVE. 070 says 4 h for up to 100 mg (trial) with 9 h as
      the cautious column; 069 / 073 carry 8.8 h for a coffee. Speaking both
      would confuse; the brief speaks the cautious 9 h, which is the number
      the two rows share, and keeps the 4 h trial result for explanations
      only. Merging the two rule sets is left to an audit (GAPS).
    grade: D
  - note: >
      SHORT NIGHT: USUAL DOSE, NOT MORE; MORNING, NOT AFTERNOON. One short
      night is the case caffeine helps with best and the low dose did as well
      as the high one; the cost of a short night comes from the afternoon
      top-up, which moves the next bedtime's sleep, and from repeating the
      pattern, where the trials show caffeine stops helping.
    grade: C
claim: >
  On a training morning the brief can use six graded directions about
  caffeine, each with product boundaries: a daily habit does not call for a
  bigger pre-session dose or a washout, and above about 6 mg/kg adds nothing;
  a skipped usual coffee explains a flat start without meaning lost fitness;
  after one short night the usual dose is reasonable and more is not better;
  after a short night the afternoon top-up, not the dawn dose, is what reaches
  tonight's sleep, so a nap comes first; when short nights repeat (3 of 7)
  and the user leans on caffeine, the brief flags the schedule because
  caffeine stops helping after about three nights; and a morning-weighted
  habit ending about 8 hours before bed is not the sleep problem. One cutoff
  number per serve is spoken (070's cautious 9 h for up to 100 mg, 13 h for
  200 mg or unknown, 14 h for 400 mg). Caffeine is never suggested to a
  non-user, never framed as a sleep substitute, and dose numbers are withheld
  under the pregnancy, cardiovascular and medication gates.
reasoning: >
  Each rule lifts its direction from a graded row and keeps that row's
  grade as basis_grade. 082 supplies the tolerance and short-night rows;
  070 supplies the cutoffs and 069 the dose ceiling and safety gate. The
  structural choices -- sitting under 072's guards, one caffeine line per
  brief, refining rather than replacing 073 -- follow how 081 joined 072. The
  cutoff-speak-one-number rule exists because the warehouse already carries
  two low-dose cutoffs (070's 4 h trial row, 069 / 073's 8.8 h regression
  figure); the brief picks the cautious figure both rows contain, which is a
  product decision (D), not a re-grade of either. The medication axis is a
  hard gate because caffeine clearance is changed by several drugs and by
  hormonal contraception, which no row here quantifies. Not contested: this
  row adds no primary claim of its own.
---

# sleep-recovery/caffeine-morning-brief-rules-083 -- 아침 브리프용 카페인 규칙

**한 줄 그림:** 매일 마셔도 양을 늘릴 필요는 없다. 짧게 잔 날은 평소 양으로 아침에만 마시고, 오후의 추가
한 잔과 며칠 이어지는 수면 부족을 짚는다.

## The rule set

| Rule | When | Level | Basis |
|---|---|---|---|
| habit-no-bigger-dose | daily user asks for more | note | 082 |
| no-washout-needed | asks about cycling off | note | 082 |
| skipped-usual-coffee | daily user skipped it, feels flat | note | 082 |
| short-night-usual-dose | under 6 h, morning session, caffeine user | note | 082 |
| short-night-afternoon-topup | under 6 h, extra caffeine after midday | hedge | 070 |
| run-of-short-nights | under 6 h on 3 of 7, leaning on caffeine | flag | 082 |
| daily-habit-sleep-ok | habit ends 8 h or more before bed | none | 082 |
| cutoff-speak-one-number | any cutoff spoken | none | 070 |
| safety-gate | pregnancy, heart condition, medication, contraception | none | 069 |

Guards: never suggest caffeine to a non-user; one caffeine line per brief;
never a sleep substitute; never an earlier alarm; symptoms route to a
clinician.

## 한국어 요약 (답변용)

- 매일 커피를 마시는 사람도 운동 전 평소 양이면 충분하다. 내성 때문에 양을 늘릴 필요가 없고, 체중 1kg당
  6mg을 넘겨도 효과가 더 커지지 않는다.
- 시합이나 테스트 전에 카페인을 끊을지는 선택이다. 미리 끊지 않아도 효과는 있었다. 매일 먹으면 몇 주에 걸쳐
  효과가 조금 줄 뿐 없어지지는 않는다.
- 평소 마시던 아침 커피를 걸렀는데 몸이 처지면, 금단 증상이 풀리지 않은 탓이 크다. 체력이 떨어진 게
  아니다. 평소 양을 마시면 되고 더 마실 필요는 없다.
- 6시간 못 잔 날 아침 운동 전에는 평소 양이면 된다. 한 연구에서 많이 먹은 쪽이 더 낫지 않았다.
- 짧게 잔 날 오후에 한 잔 더 마시면 오늘 밤잠이 줄고 내일도 짧게 잘 수 있다. 낮잠을 먼저 권하고, 마신다면
  잠들기 전 시간(070 표)을 지킨다.
- 일주일에 사흘 넘게 6시간 미만으로 자면서 카페인으로 버티고 있다면 일정을 바꿔야 한다. 연구에서 카페인
  효과는 사흘쯤 지나 사라졌다.
- 아침·점심에 마시고 마지막 잔이 잠들기 8시간 전이면 하루 습관 자체가 잠을 해친다는 근거는 약하다.
  조심할 것은 늦게 마신 한 잔이다.
- 취침 전 기준은 한 가지만 말한다. 100mg 정도는 9시간, 200mg이거나 양을 모르면 13시간, 400mg 이상은
  14시간이다.
- 임신 중이거나 심장 질환이 있거나 약을 먹고 있거나 피임약을 쓰면 mg 숫자는 말하지 않는다. 카페인을
  안 마시는 사람에게 권하지 않는다. 가슴 두근거림, 흉통, 실신, 심한 두통은 병원으로 안내한다.
