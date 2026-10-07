---
# Stress / training-load sprint 2026-10-07. The session brief and the daily retro need to know
# whether a stressful week outside the gym should change the plan inside it.
# This row carries the EVIDENCE half: what perceived and life-event stress do to
# strength gains, to recovery after a hard session, to injury odds and to
# turning up at all. Companion rows: mental-health item 071 (module not published) (how
# to ask without turning the question into an assessment) and
# exercise/stress-training-load-rules-084 (the stress_rules the engine reads).
# Population caveat stated up front: the strength and recovery rows are
# undergraduates in university weight-training classes, from one research group,
# and two of the three papers analyse the SAME 31 people. No study in trained
# recreational lifters was located.
id: exercise/life-stress-adaptation-recovery-083
domain: exercise
grade: C (higher life / perceived stress goes with smaller strength gains and slower recovery after a hard session -- small observational samples, one group); B (an acute demanding cognitive task lowers resistance-exercise volume in the same session -- RCT meta-analyses, low GRADE certainty); C (stress predicts less exercise and more injury restriction)
lane: "@performance-lit"
locale: universal
as_of: 2003-2026
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/18545186/"  # Bartholomew JB, Stults-Kolehmainen MA, Elrod CC, Todd JS 2008, J Strength Cond Res 22(4):1215-1221 -- 135 undergraduates in 12-week weight-training classes (2x/week); median split on stressful life events (college APES): low-stress group gained significantly more bench press and squat 1RM; social support unrelated. Effect magnitudes not given in the abstract and not read at full text
  - "https://pubmed.ncbi.nlm.nih.gov/22688829/"  # Stults-Kolehmainen MA, Bartholomew JB 2012, Med Sci Sports Exerc 44(11):2220-2227 -- n=31 undergraduate resistance-training students; leg press 10RM + 6 sets; life-event stress (USQ) and perceived stress (PSS) moderated recovery of maximal isometric force over the first 60 min, adjusted for fitness, workload and training experience; neither moderated energy, fatigue or soreness at 60 min
  - "https://pubmed.ncbi.nlm.nih.gov/24343323/"  # Stults-Kolehmainen MA, Bartholomew JB, Sinha R 2014, J Strength Cond Res 28(7):2007-2017 -- SAME n=31 cohort followed ~24-hourly to 96 h; life-event stress moderated recovery of isometric force (linear p=0.027, squared p=0.031) and of perceived energy, fatigue and soreness; perceived stress moderated force (p<0.001) and energy recovery; "in all analyses, higher stress was associated with worse recovery"
  - "https://pubmed.ncbi.nlm.nih.gov/24030837/"  # Stults-Kolehmainen MA, Sinha R 2014, Sports Med 44(1):81-121 -- systematic review, 168 studies, 55 prospective: 76.4% found stress predicts less physical activity / more sedentary time; 18.2% found MORE activity under stress; habitually active people exercise more in the face of stress, beginners less
  - "https://pubmed.ncbi.nlm.nih.gov/27406221/"  # Ivarsson A et al. 2017, Sports Med 47(2):353-365 -- 48 studies, 161 effect sizes: stress RESPONSE r=0.27 (80% CI 0.20-0.33) and history of stressors r=0.13 (0.11-0.15) with injury rates; stress response mediates history -> injury; 7 prevention studies all favour treatment
  - "https://pubmed.ncbi.nlm.nih.gov/26049791/"  # Mann JB, Bryant KR, Johnstone B, Ivey PA, Sayers SP 2016, J Strength Cond Res 30(1):20-25 -- 101 Division I football players; odds of an injury restriction in high-ACADEMIC-stress weeks OR 1.78 (p=0.0088) vs low-academic-stress weeks
  - "https://pubmed.ncbi.nlm.nih.gov/42168782/"  # Solon-Junior LJF ... Marcora SM, de Lima-Junior D 2026, Eur J Sport Sci 26(6):e70194 -- RCT-only meta-analysis, 11 studies / 14 comparisons / >205 participants: a demanding cognitive task before resistance exercise lowered volume g=-0.39; multi-joint g=-0.45, single-joint g=-0.20 (p=0.09); authors call the evidence low quality
  - "https://pubmed.ncbi.nlm.nih.gov/36509089/"  # Alix-Fages C, Grgic J et al. 2023, Motor Control 27(2):442-461 -- 7 studies: mental fatigue cut repetitions to failure, upper body SMD -0.41 (-0.70 to -0.12), lower body -0.39 (-0.75 to -0.04), I2=0%
  - "https://pubmed.ncbi.nlm.nih.gov/29345524/"  # Kellmann M et al. 2018, Int J Sports Physiol Perform 13(2):240-245 -- recovery consensus statement: the stress side of the stress-recovery balance includes "other life demands", not only training load (expert consensus, D)
  - "exercise/autoregulation-vs-percentage-prescription-030"  # within-warehouse: adjusting load by daily readiness has no measured strength advantage
  - "exercise/recovery-kinetics-session-spacing-025"  # within-warehouse: recovery is driven by proximity to failure and volume -- the levers a stress rule pulls
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # within-warehouse: the better-evidenced neighbour; stress weeks are often short-sleep weeks
  - "sleep-recovery/subjective-monitoring-vs-objective-markers-011"  # within-warehouse: self-report tracks training response better than objective markers
  - "mental-health item 019 (module not published)"  # within-warehouse: why the acute mental-fatigue row is NOT a willpower budget
  - "framework:GRADE -- the strength-gain and recovery rows are observational (stress was measured, not assigned), small, undergraduate, from one laboratory group, and two papers share one 31-person cohort: C at best, direction only. The acute cognitive-task rows are randomized crossover trials pooled twice, but the newest pooling calls its own certainty low: B for direction, nothing for magnitude. No trial has tested whether LOWERING training load in a stressful week preserves gains or prevents injury (GAPS.md)."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      ONE COHORT, NOT TWO. The 60-minute paper (2012) and the 96-hour paper
      (2014) analyse the same 31 undergraduates after the same leg-press bout.
      Together with the 2008 strength-gain study they are three papers from one
      research group, all in university weight-training classes. Speak them as
      one small consistent signal, never as replication.
    grade: C
  - note: >
      DIRECTION, NO DOSE. Every study here splits or models stress as a
      continuous score; none gives a threshold at which stress starts to cost
      gains, and the 2008 study used a median split. So "higher stress, smaller
      gains, slower recovery" is carryable; "above X stress, cut Y percent" is
      not, and any such number in product code is a product constant.
    grade: C
  - note: >
      RECOVERY OF FORCE, NOT ONLY FEELING. In the 96-hour data the slower
      recovery shows up in measured isometric force, not only in soreness or
      energy, and it holds after adjusting for fitness, workload and training
      experience. In the first hour, stress moved force but not feelings -- so a
      person under stress can feel normal and still be under-recovered.
    grade: C
  - note: >
      ACUTE MENTAL FATIGUE IS A DIFFERENT THING FROM LIFE STRESS. The RCT rows
      are a demanding lab task (Stroop and similar) done right before lifting,
      and they cost reps in that session (pooled around g -0.4, multi-joint
      lifts more). They say nothing about weeks of life stress, and they are not
      ego depletion: they measure same-session volume, not a willpower reserve
      (019). Practical reach: after a draining workday, today's reps may come up
      short; that is a session expectation, not a reason to skip.
    grade: B
  - note: >
      STRESS ALSO CHANGES WHETHER PEOPLE TRAIN. Most prospective studies find
      stress predicts less exercise, but habitually active people tend to keep
      or raise their exercise under stress while beginners drop off. For an
      established lifter the realistic risk of a stressful week is a missed or
      cut-short session, which is why the companion rule makes the lighter
      session the easy one to start, not the one to argue about.
    grade: C
  - note: >
      INJURY ODDS RISE WITH THE STRESS RESPONSE. Across 48 studies the person's
      stress response correlates with injury rate about r 0.27, and the count
      of stressors about r 0.13; in one football team, exam weeks nearly doubled
      the odds of an injury restriction. Athletes in team sport, observational;
      direction only for a lifter.
    grade: C
claim: >
  Stress outside training costs training, in a small and consistent but thinly
  measured way. In 135 undergraduates over 12 weeks of weight training, those
  above the median for stressful life events gained significantly less bench
  press and squat strength than those below it (Bartholomew 2008). In 31
  undergraduates after a heavy leg-press session, higher life-event and
  perceived stress slowed the recovery of measured isometric force in the first
  hour and across 96 hours, and slowed the recovery of energy, fatigue and
  soreness over the four days, after adjustment for fitness, workload and
  training experience (Stults-Kolehmainen 2012, 2014 -- the same cohort). Stress
  also predicts training less: 76 percent of 55 prospective studies found less
  physical activity under stress, though habitually active people tend to keep
  exercising (Stults-Kolehmainen and Sinha 2014). The stress response correlates
  with injury rates (r 0.27 across 48 studies; Ivarsson 2017) and exam weeks
  nearly doubled injury restrictions in one football team (Mann 2016).
  Separately and on firmer, randomized ground, a demanding cognitive task just
  before lifting reduces the reps done in that session (g about -0.4, low
  certainty; Solon-Junior 2026, Alix-Fages 2023). What is NOT known: any stress
  threshold, any dose of adjustment, and whether lightening the load in a
  stressful week protects gains or prevents injury -- no trial has tested it.
reasoning: >
  The question the engine asks is "should a stressful week change the plan".
  The evidence answers the first half -- stress is a real load on adaptation and
  recovery, not only a mood -- and leaves the second half open. The strength and
  recovery data are graded C because stress was measured rather than assigned,
  the samples are small undergraduate classes, and the two recovery papers are
  one cohort. The mental-fatigue rows are graded B for direction because they
  are randomized, but they describe a same-session effect of a lab task and are
  kept apart from the life-stress rows. The behavioural and injury rows come
  from systematic reviews of observational studies and are C. Because no trial
  tests stress-guided lightening, and because autoregulated prescription shows
  no strength advantage over a fixed plan (030), the rules in 084 are written as
  conservative product rules over this row (keep the session, trim proximity to
  failure and volume, do not chase a PR), not as a proven intervention.
---

# exercise/life-stress-adaptation-recovery-083 -- 생활 스트레스가 근력 향상과 회복에 미치는 영향

**한 줄 그림:** 바깥 스트레스가 큰 기간에는 같은 운동을 해도 근력이 덜 오르고 회복이 느리다는
신호가 있다. 다만 연구가 작고, "얼마나 줄이면 되는지"는 아무도 시험하지 않았다.

## What the evidence carries

| Row | What was found | Population | Strength |
|---|---|---|---|
| Strength gains (Bartholomew 2008) | high life-event stress -> smaller bench and squat 1RM gains over 12 weeks | 135 undergraduates, weight-training class | C |
| Recovery (Stults-Kolehmainen 2012, 2014) | high stress -> slower force recovery at 60 min and to 96 h; slower energy / fatigue / soreness recovery over 4 days | 31 undergraduates, ONE cohort | C |
| Acute mental fatigue (2023, 2026 meta-analyses) | draining cognitive task before lifting -> fewer reps that session, multi-joint more | small randomized crossovers | B (direction) |
| Turning up (2014 review) | stress -> less exercise for most; habitual exercisers often keep going | 55 prospective studies | C |
| Injury (Ivarsson 2017; Mann 2016) | stress response r 0.27 with injury; exam weeks OR 1.78 for injury restriction | athletes, observational | C |
| Does lightening in a stressful week help? | not tested | -- | gap |

## 한국어 요약 (답변용)

- 일·시험·이사·가족 일처럼 생활 스트레스가 큰 기간에는 같은 프로그램을 해도 근력이 덜 오르고, 힘든
  운동 뒤 힘이 돌아오는 속도도 느리다는 연구가 있다. 다만 대학 웨이트 수업 학생을 대상으로 한 작은
  연구들이고, 회복 연구 두 편은 같은 31명을 분석한 것이다. 방향만 믿고 숫자는 믿지 않는다.
- 스트레스가 크면 몸이 괜찮게 느껴져도 힘의 회복은 덜 됐을 수 있다. 첫 1시간에는 느낌은 그대로인데
  측정한 힘만 느리게 돌아왔다.
- 머리를 많이 쓴 날 바로 운동하면 그날 반복 수가 조금 줄어든다(무작위 연구, 확실성 낮음). 이건 그날
  기대치를 낮출 이유지, 운동을 건너뛸 이유는 아니다. "의지력이 바닥났다"는 설명과는 다르다.
- 스트레스가 크면 대부분 운동을 덜 하게 되지만, 꾸준히 운동해 온 사람은 오히려 유지하는 편이다.
- 스트레스 반응이 클수록 부상도 조금 늘어나는 경향이 있다(운동선수 관찰 연구).
- 스트레스가 큰 주에 강도를 낮추면 근력 향상이 지켜지는지, 부상이 줄어드는지는 시험한 연구가 없다.
  그래서 강도 조절 규칙(084)은 제품이 정한 보수적인 규칙이다. 답할 때도 그렇게 말한다.
