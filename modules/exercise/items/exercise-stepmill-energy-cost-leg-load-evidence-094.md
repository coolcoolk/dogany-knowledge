---
# Stepmill-in-a-cut sprint 2026-10-07.
# The EVIDENCE row for one cardio mode inside the 062 / 063 frame: what a
# stair-climber (stepmill, stair treadmill ergometer) session costs in energy
# by body mass, what it does to the legs and the knee, and whether making it
# harder or making it longer matters for fat loss. 095 is the engine-readable
# stepmill_rules built on it.
#
# Scope guard: concurrent-training interference in general, the lift-first /
# separate-session rules, the mode ranking and the ~500 kcal/day deficit
# ceiling live in 062 / 063 and are NOT restated here. This row adds the
# numbers and facts those items left at "stepmill has no data": the
# per-kilogram energy cost, the exercise-compensation discount, the knee
# load, the local leg fatigue, and duration vs intensity for fat mass.
#
# kcal arithmetic: Compendium METs are multiples of 3.5 mL O2/kg/min, about
# 1 kcal/kg/h. Gross kcal = MET x kg x hours; NET (above what the person
# would have burned sitting) = (MET - 1) x kg x hours. For a deficit only
# the net cost counts. The per-kg values below are that arithmetic, not a
# measurement on this user.
id: exercise/stepmill-energy-cost-leg-load-evidence-094
domain: exercise
grade: B (Compendium energy cost of stair-machine and stair climbing, as a population average, and the per-kg arithmetic; interval vs continuous training make no difference to fat-mass or lean-mass change); C (exercise energy compensation -- people lose roughly 36-41% of the weight the exercise energy predicts when eating is not controlled; stair ascent loads the knee at about 3.2 times body weight; hard stepmill work is limited by local leg-muscle fatigue as well as the heart and lungs; individual resting rates sit about 20% below the 1-MET convention); D (stepmill interference with leg training, handrail and console-kcal effects, plantar fascia and calf load on a stepmill, every transfer of these into a trained lifter's cut)
lane: "@performance-lit"
locale: universal
as_of: 2005-2024
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/38242596/"  # Herrmann SD, Willis EA, Ainsworth BE, Barreira TV, Hastert M, Kracht CL, Schuna JM Jr, Cai Z, Quan M, Tudor-Locke C, Whitt-Glover MC, Jacobs DR Jr 2024, J Sport Health Sci 13(1):6-12, PMC10818145 -- 2024 Adult Compendium: 1 MET = 3.5 mL/kg/min, about 1 kcal/kg/h; 82% of activity values now measured; "a starting point for prescribing individual activities but does not reflect precise individual EE values"; recommends corrected METs when RMR is known. Activity values read on pacompendium.com: 02065 stair treadmill ergometer, general 9.3 MET; 17133 stair climbing, slow pace 4.5; 17131 stair climbing, general 6.8; 17134 stair climbing, fast pace, one step at a time 9.3; 17136 two steps at a time 7.5; 17070 descending stairs 3.5; for comparison 02048 / 02049 elliptical moderate / vigorous 5.0 / 9.0, 02071 rowing ergometer <100 W 5.0
  - "https://pubmed.ncbi.nlm.nih.gov/15831804/"  # Byrne NM, Hills AP, Hunter GR, Weinsier RL, Schutz Y 2005, J Appl Physiol 99(3):1112-1119 -- n=769 (642 women, 127 men), 18-74 y, 35-186 kg: measured resting VO2 2.6 +/- 0.4 mL/kg/min, 0.84 kcal/kg/h; the 3.5 mL convention overestimates resting VO2 by 35% and resting energy by 20% on average; body composition explained 62% of the variance (abstract read)
  - "https://pubmed.ncbi.nlm.nih.gov/31172175/"  # Martin CK, Johnson WD, Myers CA, et al. 2019, Am J Clin Nutr 110(3):583-592, PMC6735935 -- E-MECHANIC RCT, n=198 sedentary adults with overweight / obesity (72.5% women), 24 weeks supervised aerobic exercise at 8 or 20 kcal/kg/week vs control, food ad libitum: weight compensation 1.5 kg (8 KKW) and 2.7 kg (20 KKW); participants lost only 36-41% of predicted weight; energy intake +90.7 and +123.6 kcal/day vs -2.3 control; non-exercise activity and RMR changes did not differ; compensation came from eating more
  - "https://doi.org/10.3390/sports9110155"  # Steele J, Plotkin D, Van Every D, Rosa A, Zambrano H, Mendelovits B, Carrasquillo-Mercado M, Grgic J, Schoenfeld BJ 2021, Sports (Basel) 9(11):155, PMC8619923 -- 29 studies, 55 effects: interval vs moderate continuous training, fat mass SMD -0.02 (95% CI -0.07 to 0.04), fat-free mass -0.0004 (-0.05 to 0.05); 25 of 60 groups work-matched; intensity pattern has minimal influence on fat-mass or lean-mass change. Written partly in response to the RETRACTED Viana et al. 2019 Br J Sports Med meta-analysis (retracted December 2020; NOT used)
  - "https://doi.org/10.1080/00140139.2018.1473644"  # Halder A, Gao C, Miller M, Kuklane K 2018, Ergonomics 61(10):1382-1394 -- n=25 healthy adults (mean 35 y, VO2max 46.7 mL/kg/min) on a stair machine at step rates for 60%, 75% and 90% VO2max: leg EMG amplitude rose at all three, median frequency fell mostly at 90% (local muscle fatigue); at 90% tolerance averaged 4.32 min, limited jointly by local leg fatigue and cardiorespiratory strain (abstract read)
  - "https://pubmed.ncbi.nlm.nih.gov/20537336/"  # Kutzner I, Heinlein B, Graichen F, Bender A, Rohlmann A, Halder A, Beier A, Bergmann G 2010, J Biomech 43(11):2164-2173, doi:10.1016/j.jbiomech.2010.03.046 -- instrumented knee implants, n=5 (older adults after knee replacement): average peak resultant tibiofemoral force 316% body weight on stair ascent and 346% on stair descent, the highest of the daily activities measured (record and secondary report read; full text not read)
  - "https://pubmed.ncbi.nlm.nih.gov/31475628/"  # Willy RW et al. 2019, J Orthop Sports Phys Ther 49(9):CPG1-CPG95 -- patellofemoral pain CPG: pain worse with squatting, stairs, prolonged sitting, jumping, running (record, as cited in 057)
  - "https://doi.org/10.1136/bjsports-2018-099643"  # O'Driscoll R, Turicchi J, Beaulieu K, Scott S, Matu J, Deighton K, Finlayson G, Stubbs J 2020, Br J Sports Med 54(6):332-340 -- 60 studies, 40 wrist / arm devices, 104 comparisons: energy-expenditure estimates vary by activity, overall tend to underestimate, some devices overestimate during walking and stairs; heart-rate sensing helps but not consistently
  - "https://minds.wisconsin.edu/handle/1793/48743"  # Handrail assisted versus nonhandrail assisted StairMaster Gauntlet ergometry -- University of Wisconsin-La Crosse master's thesis: VO2, METs and kcal significantly higher without handrail support at every stage (record read; unpublished thesis). Howley ET, Colacino DL, Swensen TC 1992, Med Sci Sports Exerc 24(9):1055-1058 on handrail and stepping cost located by citation only, not read
  - "https://pubmed.ncbi.nlm.nih.gov/21694556/"  # Garber CE, Blissmer B, Deschenes MR, Franklin BA, Lamonte MJ, Lee IM, Nieman DC, Swain DP 2011, ACSM Position Stand, Med Sci Sports Exerc 43(7):1334-1359 (PMID 21694556) -- aerobic progression: progress intensity, duration and frequency gradually until the goal is reached (read through Kravitz's summary; no tested ordering of duration vs intensity is given)
  - "exercise/concurrent-cardio-interference-cut-062"  # within-warehouse: interference modifiers, the deficit ceiling, Gergley 2009 incline walking; stepmill has no interference data
  - "exercise/cut-cardio-placement-rule-063"  # within-warehouse: placement_rules, mode_preference, dose_bands, deficit_budget, step_up that this row feeds numbers into
  - "exercise/knee-pain-symptom-guided-loading-057"  # within-warehouse: the knee ceiling for a knee caution site
  - "exercise/plantar-heel-pain-lifter-foot-rules-088"  # within-warehouse: stepmill is in the "cut first, rebuild by symptoms" list for plantar heel pain
  - "exercise/tendon-fascia-load-management-055"  # within-warehouse: the pain ceiling for calf / Achilles load
  - "nutrition/energy-availability-threshold-010"  # within-warehouse: cardio energy cost lowers energy availability
  - "nutrition/weight-loss-rate-lean-mass-012"  # within-warehouse: the measured weekly trend outranks any kcal estimate
  - "framework:GRADE -- the energy cost is a population average from a measured compendium (stair-machine value from a small number of laboratory studies); the per-kg arithmetic is exact but inherits that average's spread, and individual resting rates sit about 20% under the convention. Interval vs continuous for fat mass rests on a 29-study meta-analysis with tight intervals in mostly untrained samples. Compensation comes from one RCT in sedentary adults with obesity eating freely, not in tracked dieters. Knee load comes from five implant patients; local fatigue from one acute 25-person study. No trial puts stepmill alongside resistance training, in a deficit, or in trained lifters."
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: scale
      unknown_policy: hedge
      rescale:
        per_unit_low: 1.2     # NET kcal per kg body weight per 20 min, easy stepping ((4.5 - 1) MET x 20/60 h)
        per_unit_high: 2.8    # NET kcal per kg per 20 min, hard continuous stepmill ((9.3 - 1) MET x 20/60 h)
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: injury_history
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: cardiovascular_condition
      type: categorical
      role: hard
      unknown_policy: block_specifics
energy_cost_per_20min:
  unit: kcal per kg body weight per 20 min
  formula_net: (MET - 1) x body_weight_kg x minutes / 60
  formula_gross: MET x body_weight_kg x minutes / 60
  levels:
    - level: easy
      compendium: 17133 stair climbing, slow pace
      met: 4.5
      net_per_kg: 1.17
      gross_per_kg: 1.5
    - level: moderate
      compendium: 17131 stair climbing, general
      met: 6.8
      net_per_kg: 1.93
      gross_per_kg: 2.27
    - level: hard
      compendium: 02065 stair treadmill ergometer, general (also 17134 fast pace, one step at a time)
      met: 9.3
      net_per_kg: 2.77
      gross_per_kg: 3.1
  worked_examples_net_kcal:
    - body_weight_kg: 60
      easy: 70
      moderate: 116
      hard: 166
    - body_weight_kg: 75
      easy: 88
      moderate: 145
      hard: 208
    - body_weight_kg: 90
      easy: 105
      moderate: 174
      hard: 249
  basis_grade: B
refraction_notes:
  - note: >
      THE NUMBER IS AN AVERAGE PERSON ON AN AVERAGE MACHINE. The Compendium
      says itself that it does not give an individual's precise energy cost.
      Resting rates in a large sample sat about a fifth under the 1-MET
      convention, body composition moved them most, and the stair-machine
      value is one general entry with no step-rate breakdown. Speak the kcal
      as "roughly", with a range, and let the measured weekly weight trend
      (012) overrule it.
    grade: C
  - note: >
      COUNT NET, NOT GROSS, AND NOT THE CONSOLE. For the deficit only the
      energy above sitting counts -- about one kcal per kg per hour less than
      the gross figure, which is 20-25 kcal for a 70 kg person in 20 minutes.
      Machine consoles and wrist devices were not validated for stepmill in
      anything read here; wrist devices in general err widely and in both
      directions on stairs. Leaning on the handrails lowered the oxygen cost
      in one thesis; a user who holds on hard is nearer the easy row.
    grade: D
  - note: >
      BURNED IS NOT LOST. When people eating freely added supervised
      exercise for six months, they lost only about 36-41% of the weight the
      exercise energy predicted, because they ate more; their non-exercise
      movement and resting rate did not change. A logged cut catches part of
      that, but appetite still rises. Never tell a user that a session's kcal
      equal the fat they will lose, and do not "eat back" the console figure.
    grade: C
  - note: >
      HARDER IS NOT BETTER FOR FAT LOSS, ONLY SHORTER. Across 29 studies,
      interval and moderate continuous training changed fat mass and lean
      mass the same. Intensity buys the same energy in fewer minutes, and at
      the hard end a stepmill is limited as much by tired legs as by
      breathing (one 25-person study: about 4 minutes at a 90% step rate).
      For a lifter that leg fatigue is the cost; minutes at an easy or
      moderate step rate are the cheaper lever when time allows.
    grade: B
  - note: >
      THE KNEE SEES ABOUT THREE BODY WEIGHTS PER STEP. In five people with
      instrumented knee implants, stair ascent loaded the knee at about 3.2
      times body weight, among the highest of everyday activities (descent
      higher still; a stepmill has no descent). Stairs are a classic
      aggravator in patellofemoral pain. Healthy knees tolerate this as
      ordinary loading; at a knee caution site it is counted as knee exposure
      under the 057 ceiling. Older implant patients, five people: direction,
      not a lifter's number.
    grade: C
  - note: >
      NO STEPMILL-PLUS-LIFTING TRIAL EXISTS. The stepmill is concentric
      (stepping up, no lowering phase), which is the proposed reason cycling
      interferes less than running, but it drives the quadriceps and glutes
      to local fatigue at hard step rates. Everything about how it interacts
      with leg training is 062's general evidence plus this mechanism.
    grade: D
claim: >
  A stair-climber session costs, as a population average, about 1.2 kcal per
  kg of body weight per 20 minutes above resting at an easy step rate, about
  1.9 at a moderate one and about 2.8 at a hard continuous one (Compendium
  4.5, 6.8 and 9.3 METs): roughly 90, 145 and 210 kcal for a 75 kg person.
  Those are averages; individual resting rates sit about 20% below the
  convention, devices and consoles err widely, and holding the rails lowers
  the cost. Burned energy is not the same as fat lost: in a six-month trial
  of freely eating adults, exercisers lost only 36-41% of the predicted
  weight because they ate more. Whether the work is done as intervals or
  continuously does not change fat-mass or lean-mass loss across 29 studies,
  so intensity mainly buys the same energy in fewer minutes. Hard stepmill
  work tires the leg muscles locally as well as the cardiorespiratory system,
  and stair ascent loads the knee at about three body weights. No study has
  tested a stepmill alongside resistance training or in a deficit.
reasoning: >
  The energy numbers are direct arithmetic on measured compendium values, so
  the arithmetic is firm and the spread around it is the uncertainty; two
  independent sources (Byrne 2005 on resting rates, the Compendium's own
  caveat) say an individual can sit well off the average, and the deficit
  logic in 062 / 063 needs the net, not the gross, figure. The compensation
  trial is the best randomised dose test of exercise energy against
  weight, but its participants ate freely, so it is a ceiling on how wrong a
  kcal count can be, not a measured discount for a logged cut. The
  interval-vs-continuous null is the most important fact for progression:
  for fat mass the lever is total energy, and intensity is a time-saver
  whose price for a lifter is leg fatigue, which Halder 2018 shows is real
  on a stair machine. Knee load and plantar or calf load are carried by
  biomechanics and the existing caution items, not by stepmill trials.
---

# exercise/stepmill-energy-cost-leg-load-evidence-094 -- 스텝밀 20분은 몇 kcal이고, 다리에는 무엇을 남기나

**한 줄 그림:** 스텝밀 20분은 체중 1kg당 쉬운 강도 약 1.2kcal, 보통 약 1.9kcal, 힘든 강도 약 2.8kcal(휴식 대비
순소모)다. 하지만 태운 만큼 빠지지는 않고, 세게 한다고 지방이 더 빠지지도 않는다. 세게 할수록 다리가 먼저 지친다.

## Energy cost per 20 min (net, above sitting)

| Level | Compendium | MET | kcal / kg / 20 min | 60 kg | 75 kg | 90 kg |
|---|---|---:|---:|---:|---:|---:|
| easy | stair climbing, slow | 4.5 | 1.17 | 70 | 88 | 105 |
| moderate | stair climbing, general | 6.8 | 1.93 | 116 | 145 | 174 |
| hard | stair treadmill ergometer | 9.3 | 2.77 | 166 | 208 | 249 |

Gross (including resting) is about 1 kcal per kg per hour higher. Population averages; the weekly weight
trend (012) overrules them.

## What else the evidence says

| Question | Answer | Strength of evidence |
|---|---|---|
| Intervals vs steady for fat loss | no difference in fat or lean mass | 29-study meta-analysis |
| Does burned = lost? | no; ~36-41% of predicted loss when eating freely | one 6-month RCT |
| Leg fatigue at hard step rates | local quad / glute fatigue, ~4 min at 90% | one acute study, n=25 |
| Knee load on stair ascent | ~3.2x body weight | 5 implant patients |
| Stepmill + lifting interference | no study | mechanism only |
| Console / watch kcal | not validated for stepmill; watches err widely | meta-analysis (devices in general) |

## 한국어 요약 (답변용)

- 스텝밀 20분 소모량은 체중에 비례한다. 앉아 있을 때보다 더 쓰는 열량(순소모)으로 체중 1kg당 쉬운 강도 약
  1.2kcal, 보통 약 1.9kcal, 힘든 강도 약 2.8kcal다. 75kg이면 대략 90 / 145 / 210kcal다.
- 이 숫자는 평균치다. 사람마다 안정 시 대사가 꽤 다르고, 기계 화면이나 시계의 칼로리는 스텝밀에서 검증된 적이
  없다. 손잡이에 체중을 실으면 소모가 줄어든다. 실제 몇 주간의 체중 추세가 있으면 그쪽을 믿는다.
- 태운 열량이 그대로 지방 감량이 되지는 않는다. 식사를 자유롭게 한 6개월 연구에서 운동으로 예상한 감량의
  36~41%만 빠졌다. 더 먹게 되기 때문이다. 기계에 뜬 칼로리만큼 더 먹지 않는다.
- 인터벌로 세게 하든 일정하게 하든 지방·근육 변화는 같았다(29개 연구). 강도를 올리면 같은 열량을 더 짧은
  시간에 쓸 뿐이다. 대신 스텝밀을 세게 하면 허벅지·엉덩이가 먼저 지친다. 웨이트를 하는 사람에게는 그게 비용이다.
- 계단을 오를 때 무릎에는 체중의 약 3배가 실린다. 건강한 무릎에는 평범한 부하지만, 무릎 앞쪽 통증이 있으면
  무릎 부하로 세고 통증 기준을 지킨다.
- 스텝밀과 웨이트를 함께 한 연구는 없다. 다리 운동과의 간섭은 일반 유산소 연구와 작동 원리로 추정한 것이다.
