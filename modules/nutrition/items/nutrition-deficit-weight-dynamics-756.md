---
# Goal-calorie sprint 2026-10-08 (
# block 755..759). Owns the DEFICIT-TO-WEIGHT arithmetic: what a daily deficit
# does to body weight over weeks and months, why the 3500 kcal per pound
# (7700 kcal per kg) rule over-predicts, why the first weeks over-report, and
# what the guidelines prescribe. Rate-for-muscle stays with 012; protein with
# 062. Abstracts re-read via PubMed E-utilities on 2026-10-08 (Hall 2008, Hall
# 2011, Thomas 2013, Kreitzman 1992, Fothergill 2016). The Hall 2011 rule of
# thumb (100 kJ/day per kg) is from the paper body as quoted by search results;
# the PMC full text was behind a captcha this pass. The 2013 AHA/ACC/TOS
# guideline text was read in the Circulation PDF; KSSO 2020 and 2022 in Europe
# PMC full text.
id: nutrition/deficit-weight-dynamics-756
domain: nutrition
lane: "@obs-inferential"
grade: B (model-based but validated against supervised feeding studies; guideline deficit sizes are strong recommendations)
locale: universal
as_of: 1992-2023
contested: no
sources:
  - "https://doi.org/10.1016/S0140-6736(11)60812-X"  # Hall KD, Sacks G, Chandramohan D, Chow CC, Wang YC, Gortmaker SL, Swinburn BA. Quantification of the effect of energy imbalance on bodyweight. Lancet 2011;378(9793):826-837. PMID 21872751, PMC3880593 -- half-time of the weight response about 1 year; greater adiposity, larger and slower loss; body text rule of thumb 100 kJ/day per ~1 kg eventual change (10 kcal/day per lb), half in ~1 year, 95% in ~3 years (body text via search extract)
  - "https://doi.org/10.1038/sj.ijo.0803720"  # Hall KD. What is the required energy deficit per unit weight loss? Int J Obes 2008;32(3):573-576. PMID 17848938 -- the 3500 kcal/lb rule roughly fits people with more than ~30 kg body fat and OVERESTIMATES the deficit needed per unit loss for leaner people
  - "https://doi.org/10.1038/ijo.2013.51"  # Thomas DM, Martin CK, Lettieri S, et al. Can a weight loss of one pound a week be achieved with a 3500-kcal deficit? Int J Obes 2013;37(12):1611-1613. PMID 23628852 -- in seven supervised or measured-intake experiments the static rule grossly overestimated actual loss
  - "https://doi.org/10.1093/ajcn/56.1.292S"  # Kreitzman SN, Coxon AY, Szaz KF. Glycogen storage: illusions of easy weight loss, excessive weight regain, and distortions in estimates of body composition. Am J Clin Nutr 1992;56(1 Suppl):292S-293S. PMID 1615908 -- glycogen stored with 3-4 parts water; early dieting weight change and carbohydrate-reload regain reflect it
  - "https://doi.org/10.1002/oby.21538"  # Fothergill E, Guo J, Howard L, et al. Persistent metabolic adaptation 6 years after "The Biggest Loser" competition. Obesity 2016;24(8):1612-1619. PMID 27136388 -- n=14, extreme loss (58 kg in 30 wk): RMR -610 kcal/day at the end; adaptation -499 kcal/day after 6 years
  - "https://doi.org/10.1161/01.cir.0000437739.71477.ee"  # Jensen MD, Ryan DH, Apovian CM, et al. 2013 AHA/ACC/TOS guideline for the management of overweight and obesity in adults. Circulation 2014;129(25 Suppl 2):S102-S138. PMID 24222017 (JACC copy PMID 24239920) -- 1200-1500 kcal/d women, 1500-1800 men, or a 500 or 750 kcal/d (or 30%) deficit; initial goal 5-10% in 6 months; ~8 kg average in 6 months; most equilibrate after 6 months; VLCD <800 kcal/d only with medical supervision
  - "https://doi.org/10.7570/jomes23016"  # Kim KK, Haam JH, Kim BT, et al. Evaluation and treatment of obesity and its comorbidities: 2022 update of clinical practice guidelines for obesity by the Korean Society for the Study of Obesity. J Obes Metab Syndr 2023;32(1):1-24. PMID 36945077 -- individualise the restriction; low energy diet 500-1,000 kcal/day less, 0.5-1.0 kg/week expected, maximum effect within 6 months; VLED (<=800 kcal/day) only under trained supervision
  - "https://doi.org/10.7570/jomes21022"  # Kim BY, Kang SM, Kang JH, et al. 2020 Korean Society for the Study of Obesity guidelines for the management of obesity in Korea. J Obes Metab Syndr 2021;30(2):81-92. PMID 34045368 -- same 500-1,000 kcal and 0.5-1.0 kg/week figures
  - "nutrition/weight-loss-rate-lean-mass-012"  # the 0.5-1 percent per week rate for lean-mass retention; its own base is thin
  - "nutrition/protein-deficit-lean-mass-target-062"  # a ~500 kcal/day deficit already stopped RT lean-mass gains (Murphy and Koehler 2022)
  - "nutrition/diet-breaks-refeeds-026"  # the break-week weight rise is water and glycogen, not fat
  - "nutrition/maintenance-estimate-calibration-755"  # the starting maintenance estimate the deficit is subtracted from
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: ask
    - key: body_fat_pct
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE 7700 KCAL PER KG RULE IS A FIRST-WEEKS ROUGH SCALE, NOT A FORECAST.
      Supervised experiments show the static rule over-predicts loss, and more
      so the longer it is applied, because expenditure falls as weight falls.
      The validated rule of thumb is about 1 kg of eventual change per 100 kJ
      (about 24 kcal) of sustained daily change, half reached in about a year
      and most in about three. Never project a straight line from a weekly
      deficit to a goal date months away.
    grade: B
  - note: >
      LEANER PEOPLE LOSE MORE WEIGHT PER KCAL, AND MORE OF IT IS LEAN. The
      3500 kcal per pound figure roughly fits people carrying more than about
      30 kg of fat. For leaner people a larger share of the loss is lean
      tissue, which holds less energy, so the same deficit moves the scale
      more and costs more muscle. This is the mechanism behind sizing a lean
      lifter's deficit from a rate target (012) rather than from a fixed kcal
      number.
    grade: B
  - note: >
      THE FIRST WEEKS OVER-REPORT. Glycogen is stored with three to four parts
      water, so the first days of a deficit (and of a lower-carbohydrate diet
      most of all) drop weight that is not fat, and a return to higher
      carbohydrate brings it back. A large first-week loss must not be read as
      the diet's rate, nor a rise after a break as fat regain (026).
    grade: B
  - note: >
      SLOWING IS EXPECTED, NOT FAILURE. Both guidelines expect the largest
      effect within about six months, after which most people equilibrate and
      need the plan re-set if more loss is wanted. A slowing trend at the same
      logged intake is physics before it is an adherence problem.
    grade: B
  - note: >
      METABOLIC ADAPTATION IS REAL BUT THE FAMOUS NUMBER IS AN EXTREME. The
      Biggest Loser follow-up (14 people, 58 kg lost in 30 weeks) found resting
      expenditure about 500 kcal/day below what body size predicts six years
      later. That is a ceiling case of very fast, very large loss. Do not
      quote it as what a moderate deficit does; do use it as one reason not
      to chase a large deficit.
    grade: C
  - note: >
      THE KOREAN GUIDELINE'S 0.5-1.0 KG A WEEK IS A STATIC-RULE FIGURE. KSSO's
      500-1,000 kcal deficit with 0.5-1.0 kg/week expected is the 7700 kcal
      per kg arithmetic. It is a fair description of the early months for an
      adult with obesity. For a lean adult, 1 kg a week is well above the
      0.5-1 percent of body weight per week that 012 sets for keeping muscle
      (0.35-0.7 kg at 70 kg). Speak the guideline range to its population and
      the percent rule to lean or training users.
    grade: C
claim: >
  A daily energy deficit does not convert to weight loss at a fixed 7700 kcal
  per kg (3500 kcal per pound). Validated dynamic models show the weight
  response slows as expenditure falls: about 1 kg of eventual change per 100
  kJ (24 kcal) of sustained daily change, half of it reached in about a year.
  The static rule fits people with a lot of body fat and over-predicts loss
  for leaner people, and in supervised experiments it grossly over-predicted
  actual loss. The first days of a deficit also drop glycogen-bound water, so
  early weeks over-report fat loss. Guidelines for adults with overweight or
  obesity prescribe a 500-750 kcal/day deficit (AHA/ACC/TOS) or a 500-1,000
  kcal/day reduction (Korean Society for the Study of Obesity), or intakes of
  1200-1500 kcal/day for women and 1500-1800 for men, with an initial goal of
  5-10 percent of body weight in six months. Weight loss usually plateaus
  around six months. Diets under 800 kcal/day are for medically supervised
  settings only.
reasoning: >
  The dynamic-model claims are mechanistic models fitted to and tested
  against supervised feeding and measured-intake data, from one research
  group and its collaborators; the CALERIE validation (755) is a further test
  on independent trial data, by the same group. The direction (the static rule
  over-predicts over time) is not disputed in the sources located. The
  deficit sizes are strong guideline recommendations for adults with
  overweight or obesity; they say nothing about lean or training users,
  which is why the rate-based sizing of 012 stays separate. The glycogen-water
  point rests on a short physiological report and standard physiology. The
  adaptation note is held at C because the cited magnitude comes from 14
  people at an extreme. The whole item is B: the arithmetic is well
  supported for groups, and any single user's curve will scatter around it.
---

# nutrition/deficit-weight-dynamics-756 -- 적자 칼로리가 체중으로 바뀌는 방식

**한 줄 그림:** 하루 500 kcal 적자가 매주 같은 속도로 체중을 빼 주지는 않는다. 첫 주는 물 때문에
많이 빠져 보이고, 몇 달 지나면 같은 식사로도 속도가 줄어든다.

The popular rule says 7700 kcal of deficit is one kilogram, so 500 kcal a day is
about half a kilo a week, forever. Supervised feeding studies show this is wrong
in a predictable way. As weight falls, expenditure falls too, and the loss slows.
The validated rule of thumb is roughly one kilogram of eventual change per 24 kcal
of sustained daily change, with half of that reached in about a year.

Body fat matters. The static rule roughly fits people with a lot of fat. Leaner
people lose more weight for the same deficit, and more of it is lean tissue, so
for them the target is better set as a rate (012) than as a calorie gap.

The first week misleads in the other direction. Stored carbohydrate holds three to
four times its weight in water, so early loss is partly water and comes back when
carbohydrate returns.

For adults with overweight or obesity, the American and Korean guidelines give the
same frame: a deficit of about 500-750 (KR: 500-1,000) kcal a day, or set intakes
of 1200-1500 kcal for women and 1500-1800 for men, aiming at 5-10 percent of body
weight in six months, with a plateau expected around then. Diets under 800 kcal a
day belong under medical supervision.

## 한국어 요약 (답변용)

- "7700 kcal = 1 kg" 계산은 초반 몇 주의 대략적인 눈금일 뿐이다. 체중이 줄면 쓰는 에너지도 줄어서
  같은 식단을 이어가도 감량 속도가 느려진다. 목표일을 직선으로 계산해 약속하지 않는다.
- 체지방이 적은 사람은 같은 적자로 체중이 더 빨리 빠지고, 그만큼 근육도 더 빠진다. 그래서 마른
  편이거나 운동하는 사람은 칼로리 숫자보다 **주당 체중의 0.5~1%** 속도로 적자를 잡는다(012).
- 첫 주에 크게 빠진 체중은 상당 부분 글리코겐과 함께 빠진 물이다. 이 숫자를 식단의 속도로 읽지
  않는다. 탄수화물을 다시 먹고 조금 오른 체중도 지방이 다시 찐 게 아니다.
- 대한비만학회(2022)는 하루 500~1,000 kcal를 줄이면 주 0.5~1.0 kg 감량을 기대한다고 쓴다. 비만인
  성인의 초반 몇 달에 맞는 숫자다. 체중 70 kg의 마른 사람에게 주 1 kg은 근육을 지키는 속도(주
  0.35~0.7 kg)보다 빠르다.
- 첫 목표는 6개월에 체중의 5~10%가 미국·한국 지침의 공통 권고다. 6개월 무렵 정체는 흔하고 예상된
  일이다. 실패가 아니라 다시 계획을 맞출 시점이다.
- 하루 800 kcal 이하 초저열량식은 의료진 관리 아래에서만 한다. 앱에서 목표로 제시하지 않는다.
