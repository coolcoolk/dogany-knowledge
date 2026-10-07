---
# NEAT / daily-activity sprint 2026-10-08.
# The evidence row behind the goal-consult calorie step: how far a user's
# daily activity can be known from (a) a smartwatch "active energy" figure,
# (b) a step count, (c) a job / activity question, and (d) the user's own
# weight trend against the food log. 751 holds the engine rules (neat_rules).
# Exercise-session kcal (stepmill, console figures, compensation) is already
# owned by exercise 094 / 095 and is linked, not repeated.
#
# READ PATH, stated plainly: abstracts read through the Europe PMC REST API
# 2026-10-08; FULL TEXT read (Europe PMC fullTextXML) for Fuller 2020
# (PMC7509623), Lee 2026 (PMC13120158) and Kostrna 2026 (PMC13419227); the
# FAO/WHO/UNU 2004 adult chapter read on fao.org; Han 2023 (Korean PACT
# validation) read as the koreascience abstract record only. PubMed web pages
# returned a cookie wall; the 2025 KDRI energy chapter was NOT read.
#
# Derived arithmetic (steps -> kcal) is labelled as such: cadence-to-MET
# anchor from CADENCE-Adults (measured), MET-to-kcal convention from the 2024
# Compendium as already cited in exercise 094. No program code changed.
id: nutrition/neat-estimation-watch-steps-evidence-750
domain: nutrition
lane: "@obs-inferential"
grade: "B (consumer wrist devices do not measure energy expenditure accurately: no brand accurate across 158 publications, Apple Watch pooled MAPE about 28 percent, every subgroup above the 10 percent threshold); B (step counts from the same devices are close in the laboratory, within about 10 percent, and drift in free living); C (direction and size of watch kcal error differ by brand, model and activity -- over-reading on cycling and resistance work, near on running in one Galaxy study, under-reading of free-living activity energy in older devices -- so no per-brand correction factor exists); C (NEAT varies widely between people and falls when people diet: overfeeding NEAT change -98 to +692 kcal/day, 16 people; 2 h/day more sitting in obese vs lean, 20 people; activity energy fell under 25 percent calorie restriction, DLW, 48 people); B (self-report activity questionnaires overstate activity, IPAQ-SF on average by 84 percent); C (a Korean 24-h activity classification table predicted DLW total energy within 10 percent for about 55-59 percent of 141 adults); D (steps-to-kcal arithmetic, about 0.3-0.6 kcal per kg body weight per 1000 steps above rest)"
locale: universal
as_of: 1999-2026
contested: no
sources:
  - "https://doi.org/10.2196/18694"  # Fuller D, Colwell E, Low J, et al. Reliability and validity of commercially available wearable devices for measuring steps, energy expenditure, and heart rate: systematic review. JMIR Mhealth Uhealth 2020;8(9):e18694. PMID 32897239, PMC7509623 (full text read). 158 publications, 9 brands. Steps, controlled settings: 805 comparisons, 45.2% within +/-3%, mean -9% (median -2%); free living: 69 comparisons, 42% within +/-10%, mean +5% (median +6%). Energy expenditure: "no brand of wearable was within +/-3% measurement error more than 13% of the time"; Garmin under-estimated 69% (37/51) and Withings 74% (34/46) of the time; Apple over-estimated 58% (18/31), Polar 69% (9/13); free-living EE 18% of comparisons within +/-10%, mean -3%, median -11%. "For energy expenditure, no brand was accurate."
  - "https://doi.org/10.1088/1361-6579/adca82"  # Choe JP, Kang M. Apple watch accuracy in monitoring health metrics: a systematic review and meta-analysis. Physiol Meas 2025;46(4). PMID 40199339. 56 studies, 270 effect sizes; EE mean bias 0.30 kcal/min (LoA -2.09 to 2.69); steps -1.83 steps/min (LoA -9.08 to 5.41); "all subgroups for EE exceeded the 10% validity threshold". Pooled MAPE 27.96% EE, 8.17% steps, 4.43% HR as reported by the University of Mississippi release (abstract read; MAPE figures from the release, not the paper)
  - "https://doi.org/10.1136/bjsports-2018-099643"  # O'Driscoll R, et al. Br J Sports Med 2020;54(6):332-340. PMID 30194221. 60 studies, 104 effect sizes, wrist / arm monitors vs calorimetry or DLW: accuracy varies by activity type, I2 above 75% for many devices; heart-rate sensing reduces error in most activity types (abstract read; already cited in exercise 094)
  - "https://doi.org/10.1007/s40279-024-02077-2"  # Doherty C, Baldwin M, Keogh A, Caulfield B, Argent R. Keeping pace with wearables: a living umbrella review. Sports Med 2024;54(11):2907-2926. PMID 39080098, PMC11560992. 24 systematic reviews, 249 validation studies: about 11% of released devices validated for any outcome; energy expenditure mean bias -3% with error from -21.27 to +14.76%; step-count MAPE -9 to 12% (abstract read)
  - "https://doi.org/10.1123/jmpb.2019-0035"  # Evenson KR, Spade CL. Review of validity and reliability of Garmin activity trackers. J Meas Phys Behav 2020;3(2):170-185. PMID 32601613, PMC7323940. 32 adult validity studies: steps good-to-excellent and acceptable MAPE across 16 studies; energy expenditure across 12 studies "wide variability ... MAPE that exceeded acceptable limits" (abstract read)
  - "https://doi.org/10.3390/s26082526"  # Lee TH, Jun DU, Bae JY, Roh HT, Cho SY. Comparative validity of smartwatch-derived heart rate and energy expenditure during endurance and resistance exercise. Sensors 2026;26(8):2526. PMID 42076635, PMC13120158 (full text read). 62 healthy Korean men, 26.6 y, 73.3 kg, Apple / Galaxy / Fitbit / Garmin vs indirect calorimetry. Endurance (Table 1): calorimetry 203.75 kcal; Apple 232.87, Galaxy 221.50, Fitbit 246.19, Garmin 265.87 (devices read 9-30% high). Resistance (Table 2): calorimetry 140.79; Apple 299.10, Galaxy 258.10, Fitbit 145.95 (SD 64.67), Garmin 304.71; resistance EE r = 0.10-0.34, ICC under 0.45. NOTE: the paper's text calls the endurance Bland-Altman bias "underestimation" while its own tables show device values above calorimetry (bias computed as criterion minus device); this item reads the tables. Calorimetry during lifting misses part of the anaerobic cost, so the true over-read is somewhat smaller than the table ratio
  - "https://doi.org/10.1371/journal.pone.0353261"  # Kostrna J, Oparina E, Palacios C, et al. Body fat, skin tone, and the accuracy of smartwatch caloric expenditure estimates. PLoS One 2026;21(7):e0353261. PMID 42525581, PMC13419227 (full text read). 58 Hispanic adults, 10-min recumbent cycling intervals, COSMED K5: mean bias Apple Series 8 +21.6 kcal (APE 35.7%), Garmin Forerunner 955 +68.6 (77.6%), Samsung Galaxy Watch 5 +56.8 (66.5%), Fitbit Sense 2 +3.1 after removing 7 implausible readings (+128.6 with them); error rose with body-fat percentage for every brand
  - "https://doi.org/10.2196/83090"  # Ferreira ARP, Inoue A, Barbosa RLM, et al. Validity of Galaxy Watch for estimating energy expenditure during intermittent running. JMIR Form Res 2026;10:e83090. PMID 41849635, PMC12998609. 148 adults, 27 min walk-run intervals: K5 213.6 kcal, Galaxy Watch 6 219.5, Galaxy Watch 7 202.7 (no significant difference); MAPE 10.1-12.6%; limits of agreement -61.9 to +65.8 kcal (abstract read)
  - "https://doi.org/10.2196/13938"  # Murakami H, Kawakami R, Nakae S, et al. Accuracy of 12 wearable devices for estimating physical activity energy expenditure using a metabolic chamber and the doubly labeled water method. JMIR Mhealth Uhealth 2019;7(8):e13938. PMID 31376273, PMC6696858. 19 Japanese adults, 15 free-living days: DLW activity energy 728 kcal/day; all devices except two Omron models significantly under-estimated it; only two devices correlated with DLW (r about 0.46-0.48). Devices 2014-era (Fitbit Flex, Garmin Vivofit, Jawbone, Misfit, Withings and Japanese research monitors), no current Apple / Galaxy watch (abstract read)
  - "https://doi.org/10.1186/s12966-019-0769-6"  # Tudor-Locke C, Aguiar EJ, Han H, et al. Walking cadence (steps/min) and intensity in 21-40 year olds: CADENCE-adults. Int J Behav Nutr Phys Act 2019;16:8. PMID 30654810. 76 adults, portable calorimetry: 100 steps/min heuristic for 3 METs (PPV 91.4%), 130 steps/min for 6 METs (abstract read)
  - "https://doi.org/10.1126/science.283.5399.212"  # Levine JA, Eberhardt NL, Jensen MD. Role of nonexercise activity thermogenesis in resistance to fat gain in humans. Science 1999;283(5399):212-214. PMID 9880251. 16 nonobese adults overfed 1000 kcal/day for 8 weeks; two-thirds of the rise in daily expenditure was NEAT; NEAT change predicted fat gain (r = 0.77); NEAT change -98 to +692 kcal/day (range from index records; abstract read)
  - "https://doi.org/10.1126/science.1106561"  # Levine JA, Lanningham-Foster LM, McCrady SK, et al. Interindividual variation in posture allocation: possible role in human obesity. Science 2005;307(5709):584-586. PMID 15681386. 10 lean, 10 mildly obese sedentary adults, posture sensed every half-second for 10 days: obese seated about 2 h/day longer; posture unchanged by weight change; about 350 kcal/day modelled difference (abstract read)
  - "https://doi.org/10.1371/journal.pone.0004377"  # Redman LM, Heilbronn LK, Martin CK, et al. Metabolic and behavioral compensations in response to caloric restriction. PLoS One 2009;4(2):e4377. PMID 19198647, PMC2634841. CALERIE, 48 overweight adults, 6 months, DLW: daily expenditure down 454 kcal/day at 3 months under 25% restriction; physical activity (TDEE adjusted for sleeping metabolic rate) reduced at 3 and 6 months; not in the restriction-plus-exercise arm (abstract read)
  - "https://doi.org/10.1186/1479-5868-8-115"  # Lee PH, Macfarlane DJ, Lam TH, Stewart SM. Validity of the IPAQ-SF: a systematic review. Int J Behav Nutr Phys Act 2011;8:115. PMID 22018588. 23 validation studies: correlation with objective standards 0.09-0.39; overestimated activity by 36-173 percent in most studies, on average by 84 percent (abstract read)
  - "https://doi.org/10.4163/jnh.2023.56.4.391"  # Han HJ, Jun HY, Park J, Ishikawa-Takata K, Kim EK. 한국 성인과 노인을 대상으로 이중표식수법을 이용한 신체활동분류표 타당도 평가. J Nutr Health 2023;56(4):391-403. 141 Korean adults (mean 50.5 y): PACT-estimated vs DLW total energy, bias +17.3 kcal/day men, -4.5 women; within +/-10% for 58.6% of men and 54.9% of women; Spearman r = 0.769 (koreascience abstract record read)
  - "https://www.fao.org/4/Y5686E/y5686e07.htm"  # FAO/WHO/UNU. Human energy requirements, Food and Nutrition Technical Report Series 1, 2004, ch. 5 (read on fao.org): sedentary or light activity lifestyle PAL 1.40-1.69 (urban male office workers who only occasionally do physically demanding activity); active or moderately active 1.70-1.99 (masons, construction workers, or a sedentary job plus regular exercise); vigorous 2.00-2.40 (non-mechanised agricultural labour); PAL above 2.40 difficult to maintain long term
  - "https://doi.org/10.1016/s0140-6736(11)60812-x"  # Hall KD, Sacks G, Chandramohan D, et al. Quantification of the effect of energy imbalance on bodyweight. Lancet 2011;378(9793):826-837. PMID 21872751, PMC3880593. Body-weight response to a change in intake is slow (half time about a year); expenditure adapts as weight changes (abstract read)
  - "source:exercise/stepmill-energy-cost-leg-load-evidence-094 -- Compendium MET-to-kcal convention (1 MET about 1 kcal/kg/h), measured resting rate about 20% below it (Byrne 2005), exercise compensation (Martin 2019), console kcal not counted"
  - "source:exercise/stepmill-cardio-slot-rules-095 -- no-eat-back and the exercise-session kcal display; this item does not restate them"
  - "nutrition/self-report-underreporting-007 -- the food log under-reports, so a back-calculated maintenance is in the user's logged-kcal units, not true kcal"
  - "nutrition/body-measure-reading-rules-029 -- the confirmed-trend rule any weight-trend calibration must respect"
  - "nutrition/weekend-drift-073 -- like-day comparison of weight"
  - "nutrition/unlogged-day-not-zero-019 -- unlogged days are unknown, not zero, which limits back-calculation"
  - "framework:GRADE -- device inaccuracy for energy rests on several systematic reviews and a meta-analysis agreeing in direction (not accurate) while disagreeing in sign by brand and activity, so the inaccuracy is graded high and any brand correction low. NEAT variability rests on small metabolic studies. The Korean table rests on one validation. The steps arithmetic is a derivation from a measured cadence anchor."
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: scale
      unknown_policy: ask
      rescale:
        per_unit_low: 0.3     # NET kcal per kg body weight per 1000 steps, about 100 steps/min (3 MET, 2 MET above rest, 10 min)
        per_unit_high: 0.6    # NET kcal per kg per 1000 steps, brisk walking near 130 steps/min (about 6 MET, 7.7 min)
    - key: activity_level
      type: categorical
      role: soft
      unknown_policy: ask
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
steps_to_kcal:
  unit: NET kcal per kg body weight per 1000 steps (above resting)
  low: 0.3
  high: 0.6
  derivation: "100 steps/min = about 3 MET (CADENCE-Adults); 1000 steps = 10 min; (3 - 1) MET x 1 kcal/kg/h x 10/60 h = 0.33. 130 steps/min = about 6 MET; 1000 steps = 7.7 min; (6 - 1) x 7.7/60 = 0.64. Rounded to 0.3-0.6."
  worked_example: "75 kg: about 25-45 kcal per 1000 steps above rest; 4000 extra steps a day about 100-180 kcal"
  caveats: [the step count itself is within about 10 percent at best, slow shuffling steps cost less per step and are under-counted by wrist devices, the MET convention overstates resting cost by about 20 percent, people compensate]
  grade: D
refraction_notes:
  - note: >
      THE WATCH KCAL IS THE WEAKEST NUMBER ON THE WRIST. The same devices that
      count steps within about 10 percent and heart rate within a few percent
      miss energy by about 28 percent on average (Apple Watch meta-analysis),
      and no brand was accurate across 158 publications. The heart rate is
      good; the conversion from heart rate and motion to kcal is where it
      breaks, and it breaks differently per person.
    grade: B
  - note: >
      NO BRAND CORRECTION FACTOR. The sign flips with the device and the
      activity: on cycling Garmin and Galaxy read 50-70 kcal high over a 10-
      minute test and Apple about 20; on running two Galaxy models were within
      about 10-12 percent; on lifting Apple, Galaxy and Garmin read about
      twice the calorimeter (Korean men, 2026); older devices under-read whole
      days of free-living activity against doubly labelled water. Error also
      grew with body fat. A fixed "Apple minus X percent" would replace a
      known error with a hidden one.
    grade: C
  - axis: activity_level
    note: >
      A STATED ACTIVITY LEVEL IS A STARTING BAND, NOT A MEASUREMENT. Self-report
      questionnaires overstate activity (IPAQ-SF by 84 percent on average), and
      even a Korean 24-hour activity table built for the purpose put total
      energy within 10 percent of doubly labelled water for only a little over
      half of people. Ask what the job and the commute physically involve, map
      to a band, and let the weight trend correct it.
    grade: B
  - note: >
      NEAT MOVES WHEN INTAKE MOVES. Between people, daily non-exercise movement
      differs by hundreds of kcal (about 2 hours more sitting a day in one
      study); within a person it rose by up to about 700 kcal a day on
      overfeeding and fell under calorie restriction. A maintenance number set
      before a diet drifts down during it, which is one reason the weight trend
      outranks any start-of-diet estimate.
    grade: C
  - note: >
      STEPS ARE THE USEFUL WEARABLE SIGNAL FOR NEAT. Not because steps convert
      neatly to kcal, but because the count is reasonably accurate and comparable
      week to week on one device. A falling weekly step mean during a cut is a
      visible sign of the NEAT drop above.
    grade: C
claim: >
  For setting a calorie target, a smartwatch's "active energy" figure is the
  least trustworthy activity number a user has. Systematic reviews of 158 and
  60 studies and a 56-study Apple Watch meta-analysis agree that consumer
  wrist devices do not measure energy expenditure accurately (Apple pooled
  error about 28 percent, every subgroup above 10 percent), while the same
  devices count steps within about 10 percent and measure heart rate well.
  The sign of the energy error depends on brand, model, activity and body
  fat -- over-reading cycling and roughly doubling resistance training in
  recent Apple, Galaxy and Garmin tests, near on running for Galaxy, and
  under-reading whole free-living days in older devices -- so no correction
  factor exists. Daily non-exercise activity (NEAT) differs by hundreds of
  kcal between people and falls during dieting, and self-reported activity
  levels overstate it. The defensible order is: the user's own weight trend
  against the food log once 2-3 weeks of data exist, then a job-and-commute
  activity band for the starting estimate, with the step count as a relative
  week-to-week NEAT signal (about 0.3-0.6 kcal per kg per 1000 steps above
  rest, arithmetic), and the watch kcal used only as a same-device trend,
  never added to the food budget at face value.
reasoning: >
  The goal consult's calorie step needs an activity term, and users arrive
  with three competing numbers: a watch "active kcal", a step count, and their
  own sense of how active their job is. The evidence ranks them clearly on
  accuracy for steps vs energy (consistent across independent reviews and
  brands), so that ranking is graded high. The finer brand comparisons rest on
  single small laboratory studies with conflicting signs, which is exactly why
  the item grades them low and refuses a correction factor. The Lee 2026 paper
  is used through its tables because its text labels the bias direction the
  opposite way. Step-to-kcal conversion is offered only as derived arithmetic
  for the "what if I walk more" question, with its caveats attached. The
  weight-trend calibration is placed first because it is the only measure in
  reach that integrates true expenditure, while 007 keeps it honest: the result
  is maintenance in the user's logged units. Deliberately not here: a resting
  metabolic rate equation (none is in the warehouse; GAPS), the 2025 KDRI
  activity coefficients (not read), and exercise-session kcal (exercise 094 /
  095).
---

# nutrition/neat-estimation-watch-steps-evidence-750 -- 활동량 추정: 워치 칼로리 vs 걸음 수 vs 직업 질문

**One line:** 워치의 '활동 칼로리'는 손목 위에서 가장 약한 숫자다. 걸음 수와 심박은 꽤 맞지만,
칼로리는 평균 약 28% 어긋나고 방향도 기기·운동마다 다르다. 목표 칼로리는 체중 추세가 정한다.

| Number | Accuracy | Use for calorie target | Basis |
|---|---|---|---|
| Weight trend vs food log (2-3+ weeks) | integrates true expenditure; in logged-kcal units | first, once data exist | Hall 2011; 007, 029 |
| Job + commute activity band | self-report overstates; KR table within 10% for ~55-59% | starting band | FAO 2004; Lee 2011; Han 2023 |
| Step count (one device) | within ~10% lab; drifts free-living | relative NEAT signal | Fuller 2020; Choe 2025 |
| Watch active kcal | no brand accurate; Apple MAPE ~28% | same-device trend only | Fuller 2020; Choe 2025; O'Driscoll 2020 |

- **Brand tests, not a ranking.** Cycling: Garmin +69, Galaxy W5 +57, Apple S8 +22 kcal over a 10-min test (Kostrna 2026).
  Running: Galaxy W6/W7 within ~10-12% (Ferreira 2026). Lifting: Apple 299, Galaxy 258, Garmin 305 vs 141 kcal
  calorimeter (Lee 2026, Korean men). Whole days, older devices: under-read DLW activity energy (Murakami 2019).
- **NEAT.** Overfeeding NEAT change −98 to +692 kcal/day (Levine 1999); ~2 h/day more sitting in obese vs lean
  (Levine 2005); activity fell under 25% restriction (Redman 2009).
- **Steps arithmetic (derived).** ~0.3-0.6 kcal/kg per 1000 steps above rest → 75 kg: ~25-45 kcal per 1000 steps.

## 한국어 요약 (답변용)

- 워치(애플워치, 갤럭시워치, 가민 등)의 칼로리 수치는 정확하지 않다. 158편의 연구를 모은 리뷰에서
  칼로리를 정확히 재는 브랜드는 없었고, 애플워치 메타분석에서는 평균 오차가 약 28%였다. 반면 같은
  기기의 걸음 수는 약 10% 안팎, 심박은 몇 % 안팎으로 꽤 맞다.
- 오차 방향은 기기와 운동 종류에 따라 다르다. 실내 자전거에서는 가민·갤럭시가 10분 검사에서 50~70 kcal
  많게, 애플은 약 20 kcal 많게 나왔다. 달리기에서는 갤럭시워치 6·7이 약 10~12% 오차였다. 한국 남성
  62명의 근력운동에서는 애플·갤럭시·가민이 실제의 약 두 배로 계산했다. 체지방이 많을수록 오차도
  커졌다. 그래서 "애플은 몇 % 빼면 된다" 같은 보정값은 없다.
- 운동이 아닌 일상 활동량(NEAT)은 사람마다 하루 수백 kcal씩 차이 나고, 다이어트 중에는 줄어든다.
  처음에 정한 유지 칼로리가 감량 중에 조금씩 내려가는 이유 중 하나다.
- "얼마나 활동적이세요?" 같은 자기 평가는 실제보다 높게 나오는 경향이 있다(설문은 평균 84% 과대).
  직업에서 앉아 있는지, 서서 걷는지, 몸을 쓰는지와 출퇴근 걷기를 묻고, 그걸로 시작 범위만 잡는다.
- 걸음 수는 칼로리로 바꾸기보다 같은 기기에서 주 평균이 오르내리는지를 보는 신호로 쓴다. 대략
  계산하면 1,000보에 체중 1 kg당 0.3~0.6 kcal(휴식 대비 추가분)이고, 75 kg이면 약 25~45 kcal다.
  어림셈이지 측정값이 아니다.
- 가장 믿을 만한 기준은 2~3주 이상 쌓인 체중 추세와 식단 기록이다. 다만 기록은 실제보다 적게
  잡히는 경향이 있어서, 이렇게 계산한 유지 칼로리는 '내 기록 기준' 숫자다.
- 워치 칼로리만큼 더 먹는 방식(먹어서 채우기)은 권하지 않는다. 운동 칼로리는 운동 항목의 규칙을 따른다.
