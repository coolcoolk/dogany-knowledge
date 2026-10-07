---
# Injury-caution follow-up 2026-10-07.
# Fills the muscle hole 056 left open: tissue_modifiers.muscle says "a new
# strain is current-other" and stops there. This row answers four questions
# for the pain-triage and split / caution code at the hamstring: does the
# user's description sound like tightness or a strain, is today a skip or a
# train-around day, how does the hamstring come back (isometric -> eccentric
# / hinge loading -> running -> sprinting), and which words mean refer, not
# coach. Population caveat stated up front: every rehabilitation trial here
# is in football players, sprinters or (Hickey) 43 men in running sports; none is in
# recreational lifters, and a lifter's strain in a heavy hinge was not
# studied on its own.
#
# hamstring_rules is structured data for the pain-triage and caution code,
# same style as 056 decision_ladder and 057 ladder_placement. Pain numbers
# are 0-10 ratings copied from the trial named in `basis`; day counts are
# trial medians, never a promise to the user.
id: exercise/hamstring-strain-triage-graded-return-079
domain: exercise
grade: B (lengthening-biased rehab returns faster than conventional rehab -- two RCTs, one group, elite athletes; exercising with pain up to 4/10 was no slower than pain-free and kept more strength -- one RCT; Nordic hamstring work roughly halves hamstring injuries and cuts recurrent ones -- meta-analysis of RCTs); C (slow pain-free walking predicts a longer course; most reinjuries come early after return; acute repair beats late repair for a tendon avulsion -- cohorts and observational reviews); D (the plain-language tightness vs strain triage, pain-free sprinting, the next-session rules and the lifter application)
lane: "@clinical-physio"
locale: universal
as_of: 2004-2023
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/23080315/"  # Mueller-Wohlfahrt HW et al. 2013, Br J Sports Med 47(6):342-350 -- Munich consensus on muscle injury terminology (expert opinion, level V). Table 3 read at full text (Europe PMC XML): type 1A fatigue-induced disorder = "dull, diffuse, tolerable pain ... Athlete reports of 'muscle tightness'", increasing with continued activity, MRI negative; type 1B DOMS = generalised pain hours after unaccustomed eccentric work, resolves within about a week; type 3A/3B partial tear = "sharp, needle-like or stabbing pain at time of injury ... often experiences a 'snap' followed by a sudden onset of localised pain", stretch-induced pain, haematoma (3B "often haematoma", possible fall); type 4 (sub)total tear / tendinous avulsion = snap, often fall, palpable gap, haematoma, loss of function. The authors note "strain" is the least consistently used term
  - "https://pubmed.ncbi.nlm.nih.gov/23645834/"  # Ekstrand J et al. 2013, Br J Sports Med 47(12):769-774 -- 31 European professional teams, 393 thigh muscle injuries classified by Munich: two thirds structural; functional disorders median lay-off 5-8 days; structural lay-off longer and rising with severity. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/18653619/"  # Warren P et al. 2010, Br J Sports Med 44(6):415-419 -- prospective, 59 elite Australian footballers with hamstring strain: taking more than 1 day to walk pain-free -> adjusted OR 4.0 (95% CI 1.3-12.6) for more than 3 weeks to return; recurrence 15.2%, more likely with a hamstring injury in the past 12 months (OR 19.6, wide CI). Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/26843538/"  # Jacobsen P et al. 2016, Br J Sports Med 50(7):431-439 -- 90 athletes, MRI-positive hamstring injury: initial + day-7 clinical exam explained 97% of variance in return time (+-5 days); days to walk pain-free, maximum pain at injury and pain on a single-leg bridge at day 7 among the predictors; MRI added nothing (8.6% alone). Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/29084725/"  # Whiteley R et al. 2018, Br J Sports Med 52(5):303-310 -- 131 MRI-confirmed acute hamstring injuries, daily exams: palpation pain, outer-range strength, active-knee-extension flexibility and reported pain in daily activity tracked rehabilitation progress; recovery non-linear. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/17170160/"  # Askling CM et al. 2007, Am J Sports Med 35(2):197-206 -- 18 elite sprinters, first-time strains: median 16 weeks (6-50) to pre-injury level; injury nearer the sit bone and involving the proximal free tendon took longer. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/23536466/"  # Askling CM et al. 2013, Br J Sports Med 47(15):953-959 -- RCT, 75 Swedish elite footballers, MRI-verified: lengthening (L) protocol mean 28 days to return vs conventional (C) 51 days; stretching-type injuries slower than sprinting-type (L 43 vs 23 days); one reinjury, in C. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/24620041/"  # Askling CM et al. 2014, Br J Sports Med 48(7):532-539 -- RCT, 56 elite sprinters and jumpers: L-protocol 49 vs C-protocol 86 days; free-tendon involvement 73 vs 31 days (L). Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/32005093/"  # Hickey JT et al. 2020, J Orthop Sports Phys Ther 50(2):91-103 -- RCT, 43 men with acute hamstring strain: pain-free vs pain-threshold rehab; median 15 vs 17 days to return-to-play clearance (no difference); pain-threshold group +15% isometric knee-flexor strength at clearance and better fascicle length at 2 months; 2 reinjuries per group at 6 months. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/35794049/"  # Hickey JT et al. 2022, J Sci Med Sport (doi 10.1016/j.jsams.2022.06.002) -- secondary analysis of the same RCT, accepted manuscript read at full text (ACU Research Bank): the two arms differed only in allowed exercise pain, 0 vs "<= 4" on a 0-10 scale; supervised twice weekly with a progressive running protocol; high-intensity eccentric loading (Nordic, single-leg slider) introduced once a bilateral slider was done through full range, median 5 (2-8) days after injury, while isometric testing still hurt (median 3.5/10); pain-free isometric testing reached at median 11 days; no reinjury during rehabilitation
  - "https://pubmed.ncbi.nlm.nih.gov/15089024/"  # Sherry MA, Best TM 2004, J Orthop Sports Phys Ther 34(3):116-125 -- RCT, 24 athletes: progressive agility and trunk stabilisation vs stretching + isolated hamstring strengthening; reinjury at 1 year 1/13 vs 7/10. Very small. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/36650032/"  # Paton BM et al. 2023, Br J Sports Med 57(5):278-291 -- London International Consensus part 3 (Delphi, 99/112 experts, 70% threshold): early rehab avoids high strain loads and rates; progress by capacity and symptoms with activity-dependent pain thresholds, EXCEPT pain-free criteria for sprinting (85.5%); no agreement on flexibility (40%) or strength (66.1%) benchmarks. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/36650033/"  # Plastow R et al. 2023, Br J Sports Med 57(5):266-277 -- London Consensus part 2: surgical indications include gapping at the tendinous injury (87.2%), loss of tension (70.7%), symptomatic displaced bony avulsion (72.8%), proximal free-tendon injury with functional compromise refractory to non-operative care (72.2%). Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/21563032/"  # Harris JD et al. 2011, Int J Sports Med 32(7):490-495 -- systematic review, 300 proximal hamstring ruptures, mean age 39.7: surgical better than non-surgical; repair within 4 weeks (acute) better than later on satisfaction, strength, return to sport, re-rupture and complications. Level I-IV, mostly case series. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/35549447/"  # Hillier-Smith R, Paton B 2022, Bone Jt Open 3(5):415-422 -- 35 studies, 1,530 repaired proximal avulsions, mean age 44.7: return to sport 84.5% at about 6.5 months; acute repair quicker return, fewer re-ruptures and less sciatic nerve dysfunction. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/28360143/"  # van der Horst N et al. 2017, Br J Sports Med 51(22):1583-1591 -- worldwide Delphi, 58 experts: return criteria = no pain on palpation, no pain in strength and flexibility testing, no pain during / after functional testing, similar flexibility, field-test performance, psychological readiness. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/27184543/"  # Wangensteen A et al. 2016, Am J Sports Med 44(8):2112-2121 -- case series, 180 athletes, 19 MRI-confirmed reinjuries within a year: 79% at the same location; median 24 days from return to reinjury; more than 50% within 25 days (about 4 weeks) of return. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/21825112/"  # Petersen J et al. 2011, Am J Sports Med 39(11):2296-2303 -- cluster RCT, 942 Danish footballers: 10-week progressive Nordic programme then weekly; overall RR 0.293, new RR 0.410, RECURRENT RR 0.137 (NNT 3 to prevent one recurrence). Abstract read; per-week set scheme not read
  - "https://pubmed.ncbi.nlm.nih.gov/25794868/"  # van der Horst N et al. 2015, Am J Sports Med 43(6):1316-1323 -- RCT, 579 amateur footballers, 25 Nordic sessions in 13 weeks: injury rate 0.25 vs 0.8 per 1000 h (OR 0.282); severity not reduced; compliance 91%. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/30808663/"  # van Dyk N et al. 2019, Br J Sports Med 53(21):1362-1370 -- 15 studies, 8,459 athletes: programmes including the Nordic RR 0.49 (RCTs only 0.52; low-bias only 0.55). Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/27288515/"  # Duhig S et al. 2016, Br J Sports Med 50(24):1536-1540 -- one AFL team, two seasons: high-speed running above the player's usual in the preceding week -> OR 6.44 for hamstring strain; total distance and session RPE trivial. Observational. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/24963588/"  # Reurink G et al. 2014, N Engl J Med 370(26):2546-2547 -- RCT (letter), platelet-rich plasma injection did not speed return after acute hamstring injury. Record read; carried only to say injections are not the lever
  - "exercise/injury-history-reinjury-risk-054"  # within-warehouse: hamstring history weight (recent RR 4.8 vs any 2.7, Green 2020)
  - "exercise/caution-severity-ladder-056"  # within-warehouse: the ladder this row places the hamstring on (muscle modifier)
  - "exercise/harm-route-boundary-031"  # within-warehouse: red flags are routed, not coached
  - "exercise/doms-timeline-mechanism-023"  # within-warehouse: soreness after unaccustomed eccentric work is DOMS, not injury
  - "exercise/low-back-pain-lifter-loading-059"  # within-warehouse: back-of-thigh pain with back pain or tingling goes to the back row
  - "exercise/ideal-sprinter-athletic-048"  # within-warehouse: lengthened hip-extension work (Maeo 2024) and hamstring burden in sprinters
  - "framework:GRADE -- that lengthening-biased loading and loading into mild pain do not slow return is RCT-level (small, mostly elite, one group for the lengthening trials); Nordic prevention is a meta-analysis of RCTs in field sports; walking-pain prognosis and early reinjury timing are cohort / case-series data; the tightness vs strain word map is expert-consensus classification (level V); pain-free sprinting is Delphi consensus; acute-vs-late avulsion repair rests on observational surgical series. No hamstring rehabilitation or prevention trial in recreational lifters was located."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
hamstring_rules:
  triage:
    - picture: tight, dull, spread-out ache at the back of the thigh that built up during or after training; no sudden moment; walks and bends normally; no bruise
      class: functional (tightness / fatigue)
      rung: mild
      today: train; warm up fully; keep hamstring work but stop a set that turns sharp or localised
      next_lower_session: unchanged
      basis: Mueller-Wohlfahrt 2013 type 1A; Ekstrand 2013 (functional lay-off median 5-8 days in pros)
      basis_grade: D
    - picture: general soreness at the back of both thighs one to three days after new or heavier Nordics, RDLs or hill running; tender to touch, stiff, eases as you warm up
      class: functional (DOMS)
      rung: mild
      today: train; lighter hamstring work is fine; no rest needed
      next_lower_session: unchanged
      basis: exercise/doms-timeline-mechanism-023; Mueller-Wohlfahrt 2013 type 1B
      basis_grade: C
    - picture: sudden sharp, stabbing or grabbing pain at one spot during a sprint, kick, lunge or hinge, often with a felt "pop" or "snap"; had to stop; walking, bending or stretching now hurts at that spot; a small bruise may appear in the next days
      class: structural-suspected (strain / partial tear)
      rung: current-other (muscle)
      today: skip all hamstring loading and running; upper body and pain-free quad or machine work are allowed
      next_lower_session: hamstring-free (no hinge, no leg curl, no running) until walking is pain-free; then the return stages below
      basis: Mueller-Wohlfahrt 2013 type 3A/3B; Warren 2010; 056 muscle modifier
      basis_grade: D
    - picture: back-of-thigh pain or tightness with low back pain, or with tingling, pins and needles or numbness running down the leg, and no clear moment of injury
      class: possibly spine-related
      rung: current-other
      today: no hamstring stretching or heavy hinge; route to the low-back row (059) and pain-triage
      next_lower_session: per 059
      basis: Mueller-Wohlfahrt 2013 type 2A; exercise/low-back-pain-lifter-loading-059
      basis_grade: D
    - picture: pop or tearing at the top of the thigh or the sit bone, often from a slip into the splits or a forced bend with the knee straight; large bruising spreading down the back of the thigh; cannot walk normally, cannot sit on that side, a dent or gap felt, weak knee bending; or numbness / weakness in the leg or foot
      class: red-flag (possible tendon avulsion or complete tear)
      rung: red-flag
      today: stop; refer promptly to a sports doctor or orthopaedics; do not wait out a week of rest first
      next_lower_session: none at the site until cleared
      basis: Mueller-Wohlfahrt 2013 type 4; Plastow 2023; Harris 2011; Hillier-Smith 2022 (repair within 4 weeks did better)
      basis_grade: C
  refer_also:
    - cue: still cannot walk without pain about a week after a suspected strain
      basis: Warren 2010 (>1 day to walk pain-free -> longer course); Jacobsen 2016; one-week cut is a product constant
      basis_grade: D
    - cue: pain getting worse day to day instead of better, or a second strain at the same spot
      basis: Wangensteen 2016 (reinjury same location, often more extensive)
      basis_grade: C
  prognosis_signals:
    - signal: more than 1 day before walking is pain-free
      meaning: expect a longer course (more than 3 weeks in elite players, OR 4.0)
      basis_grade: C
    - signal: pain close to the sit bone, or a stretching-type injury (slow overstretch rather than sprinting)
      meaning: expect a longer course (Askling: stretching-type 43 vs sprinting-type 23 days on the L-protocol)
      basis_grade: C
  return_stages:
    - stage: 1
      name: isometric
      enter_when: walking is pain-free or nearly so
      content: isometric knee bends (heel digs) and bridges held at mid-range, both legs then one; walking; upper body and quad work as usual
      exercise_pain_max: 4
      basis: Hickey 2020 / 2022 (pain-threshold arm, <= 4/10)
      basis_grade: B
    - stage: 2
      name: submaximal eccentric and lengthened hip work
      enter_when: stage 1 moves done without pain above the ceiling
      content: two-leg slider or long-lever bridge walk-outs; lengthening-biased hip work (Askling extender, diver, glider; light RDL with a slow lower); no fast or ballistic stretching
      exercise_pain_max: 4
      basis: Askling 2013 / 2014 (L-protocol); Hickey 2022 (bilateral slider first)
      basis_grade: B
    - stage: 3
      name: heavy eccentric and hinge loading
      enter_when: the two-leg slider can be done through full range
      content: Nordic hamstring curls and single-leg slider; RDL load progressed session to session
      exercise_pain_max: 4
      basis: Hickey 2022 (introduced at median day 5, while isometric testing still hurt ~3.5/10, no reinjury)
      basis_grade: B
    - stage: 4
      name: running then sprinting
      enter_when: stage 3 tolerated; running added from early rehab in the trial protocols and built up
      content: jog -> stride -> faster running in steps; avoid a jump in fast-running volume above what the user did recently
      exercise_pain_max: 4
      sprint_pain_max: 0
      basis: Paton 2023 (pain-free criteria for sprinting, 85.5% agreement); Duhig 2016 (spikes in high-speed running preceded strains)
      basis_grade: D
    - stage: 5
      name: return and secondary prevention
      enter_when: no pain when pressing on the spot, no pain on a hard knee bend or a straight-leg stretch, flexibility about equal to the other side, full-speed running pain-free
      content: back to normal lower sessions; keep Nordics (or another heavy eccentric hamstring move) at least weekly; no sudden spike in sprinting or heavy hinges for the first month back
      basis: van der Horst 2017 (return criteria); Petersen 2011 (recurrent RR 0.137); Wangensteen 2016 (over half of reinjuries within ~4 weeks of return)
      basis_grade: B
  monitoring:
    scale: 0-10 numeric rating
    exercise_pain_max: 4
    sprint_pain_max: 0
    next_day: no worse than before the session; otherwise repeat the stage
    breach_action: next session repeats the current stage at lower load or range; a sharp, localised pain like the original moment is a stop and re-triage, not a breach
    basis: Hickey 2020 / 2022 (exercise ceiling); next-day rule is a product constant
    basis_grade: B (exercise ceiling); D (next-day rule)
  typical_course_days:
    functional_median: 5-8 (professional football, Ekstrand 2013)
    strain_rtp_median: 15-17 (43 men, Hickey 2020; sport level not read); 23-51 (elite football, Askling 2013, by protocol and type)
    note: trial medians, not a promise; never quoted to the user as their date
    basis_grade: C
refraction_notes:
  - note: >
      TIGHTNESS AND STRAIN SOUND DIFFERENT. The muscle-injury consensus
      describes fatigue-type tightness as a dull, diffuse, tolerable ache that
      builds with activity, and a tear as a sudden, sharp or stabbing pain at
      one spot, often with a "snap", that hurts on stretching and may bruise.
      The engine asks for these plain words (when did it start, sudden or
      gradual, one spot or spread, walking and bending, bruise) and maps them;
      it never names a grade of tear. This mapping is expert classification,
      not a tested questionnaire.
    grade: D
  - note: >
      TIGHTNESS IS A TRAIN DAY. Functional muscle disorders cost professional
      players a median of 5-8 days against much longer for structural ones,
      and DOMS settles within about a week by itself. A dull, spread-out ache
      without a sudden moment, with normal walking and no bruise, keeps the
      session; only a set that turns sharp or localised stops.
    grade: D
  - note: >
      A SUDDEN SHARP PAIN IS A SKIP DAY FOR THE HAMSTRING, NOT FOR THE WEEK.
      A suspected strain closes hamstring loading and running today and puts
      the next lower session on hamstring-free work, under 056's
      current-other. Upper body and pain-free quad work continue. Loading
      restarts once walking is pain-free, which in the trials was within days
      for most strains.
    grade: D
  - note: >
      WALKING PAIN TELLS THE LENGTH. In elite players, needing more than a
      day to walk pain-free made a course longer than three weeks four times
      as likely, and a clinical exam at day 7 predicted return within about
      five days while MRI added nothing. The engine uses "can you walk
      without pain?" as its main day-to-day check, and pain still on walking
      after about a week as a referral cue (the week is a product constant).
    grade: C
  - note: >
      LOADING INTO MILD PAIN IS FINE. In a 43-man trial, rehab allowed pain up
      to 4 out of 10 during exercise returned players as fast as pain-free
      rehab and kept more knee-flexor strength and muscle fascicle length.
      Heavy eccentric work (Nordics) started at a median of five days, while
      testing still hurt, with no reinjury during rehab. Sprinting is the
      exception: experts agree it should be pain-free.
    grade: B
  - note: >
      LENGTHENED WORK FIRST. Two trials from one Swedish group found a
      programme built on lengthening exercises (hip-dominant movements with
      the hamstring long) returned elite footballers in 28 instead of 51 days
      and sprinters in 49 instead of 86. The return stages lean on
      lengthened hip work and slow RDLs early, not on stretching and leg
      curls alone. Elite samples; recreational lifters are by analogy.
    grade: B
  - note: >
      KEEP THE NORDICS AFTER RETURN. Nordic programmes cut hamstring injuries
      by about half across field-sport trials, and in one large trial cut
      recurrent injuries far more (rate ratio about 0.14). Reinjuries cluster
      early: in one series more than half came within about four weeks of
      return, mostly at the same spot. So the plan keeps heavy eccentric
      hamstring work at least weekly and avoids sudden spikes in sprinting
      or heavy hinges in the first month back.
    grade: B
  - note: >
      SOME WORDS MEAN REFER, NOT REHAB. A pop at the top of the thigh or the
      sit bone, often from a slip into the splits, with large spreading
      bruising, trouble walking or sitting, a felt gap or a weak knee bend,
      can be a tendon avulsion. Surgical series find repair within about four
      weeks does better than later repair, so these words route straight to
      a doctor instead of a wait-and-see week. Numbness or weakness in the
      leg goes the same way.
    grade: C
claim: >
  At the back of the thigh, how the pain started separates tightness from a
  strain. A dull, spread-out ache that built up with training, with normal
  walking and no bruise, is a functional disorder or DOMS: train, and stop
  only a set that turns sharp. A sudden sharp or stabbing pain at one spot,
  often with a pop, that makes walking, bending or stretching hurt, is a
  suspected strain: skip hamstring loading and running today and keep the
  next lower session hamstring-free until walking is pain-free. Needing more
  than a day to walk pain-free predicted a course longer than three weeks.
  The return runs in stages: isometrics, then submaximal eccentric and
  lengthened hip work, then Nordics and progressively loaded RDLs, then
  running, with exercise pain up to 4/10 allowed (no slower than pain-free
  rehab, more strength kept) and sprinting only when pain-free. Lengthening-
  biased programmes returned elite athletes markedly faster than
  conventional ones. After return, weekly Nordic work cuts recurrence and the
  first month back avoids spikes, because more than half of reinjuries came
  within about four weeks. A pop near the sit bone with large bruising,
  trouble walking or sitting, a felt gap, leg numbness or weakness is a
  referral, not a rehab plan: early repair of a tendon avulsion does better
  than late.
reasoning: >
  The strongest rows carry the return direction. Askling 2013 and 2014 are
  RCTs with MRI-confirmed injuries and large effects on return time, but from
  one group in elite athletes; Hickey 2020 is a single small RCT, read with
  its 2022 secondary analysis at full text for the exact 0 vs <= 4/10 rule and
  the day-5 Nordic start. Prevention is the best-evidenced piece (van Dyk
  2019 meta-analysis; Petersen 2011 with a large recurrent-injury effect),
  all in field sports. The triage word map is the weakest link: the Munich
  table is level-V expert classification, and no study tests a lay
  questionnaire that separates tightness from a strain, so the engine maps
  words only to triage classes and never names a tear grade. Walking-pain
  prognosis (Warren 2010, Jacobsen 2016) and early reinjury timing
  (Wangensteen 2016, 19 reinjuries) are small observational samples, which
  caps them below the trial rows. Avulsion urgency comes from observational
  surgical series and a Delphi, so it is graded as a referral cue, not a
  treatment claim. injury_history is hard with block_specifics: without the
  user's words on how the pain began, the stage and ceiling are withheld and
  the 056 triage route applies. Age is soft because older age raises
  hamstring risk (054, Green 2020) and the avulsion series are in people
  around 40-45.
---

# exercise/hamstring-strain-triage-graded-return-079 -- 햄스트링: 뭉침인지 부상인지, 쉬는 날인지, 어떻게 돌아오는지

**한 줄 그림:** 허벅지 뒤가 서서히 묵직하게 뭉친 건 운동하는 날이다. 어느 순간 한 지점이 찌르듯
아팠다면 오늘은 햄스트링을 쉬고, 걸을 때 안 아파지면 단계적으로 다시 부하를 준다.

## Triage by the user's words (engine-readable)

| User's words | Class | Rung (056) | Today | Next lower session |
|---|---|---|---|---|
| dull, spread-out tightness that built up; walks and bends normally; no bruise | functional | mild | train; stop a set that turns sharp | unchanged |
| soreness 1-3 days after new Nordics / RDLs / hills | DOMS (023) | mild | train | unchanged |
| sudden sharp / stabbing pain at one spot, often a pop; walking, bending or stretching hurts | suspected strain | current-other (muscle) | skip hamstring loading and running | hamstring-free until walking is pain-free, then return stages |
| thigh pain with back pain, or tingling / numbness down the leg, no clear moment | possibly spine-related | current-other | no hamstring stretch, no heavy hinge | per 059 |
| pop at the sit bone or top of the thigh, large spreading bruise, can't walk or sit normally, felt gap, weak knee bend, leg numbness or weakness | possible avulsion / complete tear | red-flag | stop; refer promptly | none until cleared |

Also refer: still painful to walk about a week after a suspected strain (a
product constant), pain getting worse day to day, or a second strain at the
same spot.

## Return stages (engine-readable)

| Stage | Enter when | Content | Pain ceiling |
|---|---|---|---|
| 1 isometric | walking pain-free or nearly | heel digs, bridges held mid-range | exercise at most 4/10 |
| 2 submaximal eccentric + lengthened hip | stage 1 within ceiling | two-leg slider, long-lever bridge, extender / diver / glider, light slow RDL | at most 4/10 |
| 3 heavy eccentric + hinge | two-leg slider through full range | Nordics, single-leg slider, RDL load progressed | at most 4/10 |
| 4 running then sprinting | stage 3 tolerated | jog -> strides -> faster, no spike in fast running | running at most 4/10; sprinting 0 |
| 5 return + prevention | no pain on pressing, hard knee bend or stretch; flexibility about equal; full-speed running pain-free | normal sessions; Nordics at least weekly; no spikes in the first month back | -- |

Next day no worse than before the session, or the next session repeats the
stage lighter. A sharp pain like the original moment is a stop and
re-triage, not a breach.

## 한국어 요약 (답변용)

- 허벅지 뒤가 운동하면서 서서히 묵직하게 뭉쳤고, 걷거나 숙일 때 문제없고 멍이 없으면 근육 피로성
  뭉침이다. 운동해도 된다. 세트 중에 한 지점이 날카롭게 아파지면 그 세트만 멈춘다.
- 노르딕이나 RDL을 새로 하거나 무게를 올린 뒤 1-3일 양쪽이 뻐근한 건 지연성 근육통이다. 쉴 필요
  없다(023).
- 전력 질주, 킥, 런지, 힌지 중에 한 지점이 갑자기 찌르듯 아프고 '뚝' 하는 느낌이 있었고, 지금 걷거나
  숙이거나 늘릴 때 그 자리가 아프면 근육 손상을 의심한다. 오늘은 햄스트링 운동과 달리기를 쉬고, 상체와
  안 아픈 앞허벅지 운동은 해도 된다. 다음 하체 날은 걸을 때 안 아플 때까지 햄스트링을 빼고 짠다.
- 걸을 때 안 아파지기까지 하루를 넘기면 회복이 3주 넘게 걸릴 가능성이 4배쯤 높았다(프로 선수 연구).
  그래서 "걸을 때 아파요?"를 매일 확인한다. 일주일쯤 지나도 걷기가 아프면 진료를 권한다. 일주일은
  제품이 정한 기준이다.
- 복귀는 단계로 간다. 버티기(등척성) → 가벼운 신장성 운동과 엉덩이 주도로 햄스트링을 길게 쓰는 동작,
  천천히 내리는 가벼운 RDL → 노르딕과 무게를 올리는 RDL → 조깅부터 빠른 달리기 순서다.
- 운동 중 통증은 10점 중 4점까지 괜찮다. 43명 연구에서 4점까지 허용한 쪽이 통증 없이만 한 쪽만큼
  빨리 복귀했고 근력은 더 남았다. 전력 질주만은 통증이 없어야 한다는 게 전문가 합의다.
- 다음 날 운동 전보다 나빠졌으면 그 단계를 가볍게 한 번 더 한다. 처음 다칠 때처럼 날카롭게 아프면
  멈추고 다시 확인한다.
- 복귀한 뒤에도 노르딕 같은 신장성 햄스트링 운동을 주 1회 이상 이어간다. 노르딕 프로그램은
  햄스트링 부상을 절반쯤 줄였고, 재부상은 훨씬 더 줄였다. 재부상의 절반 넘게는 복귀 후 4주 안에
  같은 자리에서 생겼으니, 복귀 첫 달은 질주나 무거운 힌지를 갑자기 늘리지 않는다.
- 엉덩이 아래 뼈(좌골) 쪽이나 허벅지 맨 위에서 '뚝' 하고, 멍이 허벅지 뒤로 넓게 번지고, 걷거나 앉기
  힘들고, 움푹 꺼진 데가 만져지거나 무릎 굽히는 힘이 빠졌다면 힘줄이 떨어졌을 수 있다. 다리가 저리거나
  힘이 빠지는 것도 마찬가지다. 운동으로 버티지 말고 바로 진료를 권한다. 힘줄 봉합은 4주 안에 할수록
  결과가 좋았다.
- 연구는 대부분 축구 선수와 육상 선수 대상이다. 헬스 하는 사람에게는 방향을 가져와 쓰는 것이고,
  날짜는 그 사람의 예정일로 말하지 않는다.
