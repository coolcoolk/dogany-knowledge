---
# Authored 2026-10-07 (protein distribution re-audit). Protein before sleep is
# the timing claim a lifter on a cut meets most often ("casein before bed").
# nutrition/protein-timing-total-matched-024 owns the around-the-session timing
# claim and carries a short bedtime rule; this item takes the pre-sleep evidence
# apart because trials published since 2017 changed what can be said, and
# because a cut raises two questions the older work never asked (hunger and
# metabolic rate the next morning). Primaries read 2026-10-07 at abstract level on PubMed
# (Res 2012, Snijders 2015 and 2019, Joy 2018, Antonio 2017, Valenzuela 2023,
# Chen 2022, Pourabbas 2021, Chapman 2023, Klemp 2025, Ormsbee 2022, Kinsey
# 2014, Madzima 2018, Dela Cruz 2021, Reis 2021, Zhou 2024, Aussieker 2026);
# none of these was read at full text. Zhou 2024's publisher page returned 403,
# so only its abstract is used.
#
# pre_sleep_rules is structured data for a diet module (last-call line, card
# copy). Values are plain text; the module copies them, it does not compute from
# them.
id: nutrition/pre-sleep-protein-matched-trials-091
domain: nutrition
lane: "@obs-inferential"
grade: C
locale: universal
as_of: 2012-2026
contested: yes
sources:
  - "https://doi.org/10.1249/MSS.0b013e31824cc363"  # Res PT, Groen B, Pennings B, et al. Med Sci Sports Exerc 2012;44(8):1560-1569. PMID 22330017 -- 16 young men, evening resistance exercise, 40 g casein vs placebo 30 min before sleep: whole-body net protein balance +61 vs -11 umol/kg over 7.5 h, mixed-muscle synthesis about 22 percent higher (P=0.05, borderline). The acute mechanism
  - "https://doi.org/10.3945/jn.114.208371"  # Snijders T, Res PT, Smeets JS, et al. J Nutr 2015;145(6):1178-1184. PMID 25926415, NCT02222415 -- 44 young men, 12 weeks of training, 27.5 g protein (plus 15 g carbohydrate) every night vs a NON-CALORIC placebo: quadriceps area +8.4 vs +4.8 cm2, strength up more; daily totals not matched
  - "https://doi.org/10.1186/s12970-018-0228-9"  # Joy JM, Vogel RM, Shane Broughton K, et al. J Int Soc Sports Nutr 2018;15(1):24. PMID 29764464, NCT03352583 -- 13 men, 10 weeks, 35 g casein daytime vs before bed on isocaloric 1.8 g/kg diets: lean tissue, muscle area, leg and bench press all up in both, no difference between groups (preliminary)
  - "https://doi.org/10.70252/QWHA8703"  # Antonio J, Ellerbroek A, Peacock C, Silver T. Int J Exerc Sci 2017;10(3):479-486. PMID 28515842 -- 26 men and women training for over a year, 54 g casein in the morning vs within 90 min of sleep for 8 weeks; both groups ate more protein; no within- or between-group difference in any body-composition or performance measure; no unsupplemented control
  - "https://doi.org/10.1080/15502783.2023.2166366"  # Valenzuela PL, Alejo LB, Montalvo-Perez A, et al. J Int Soc Sports Nutr 2023;20(1):2166366. PMID 36686220 -- 24 professional U23 cyclists, 6-day training camp: 40 g casein before sleep vs in the afternoon vs 40 g carbohydrate before sleep; protein intake above 2.5 g/kg in all; no between-group difference in fatigue, body composition or time trials
  - "https://doi.org/10.3390/nu14112289"  # Chen Y, Liang Y, Guo H, et al. Nutrients 2022;14(11):2289. PMID 35684089 -- 42 untrained men aged 18-24, 6 weeks of training: 25 g whey plus 4000 IU vitamin D3 before bedtime vs after waking, vs a 5 g maltodextrin control; both supplement groups gained muscle mass over control, bedtime and waking did not differ (vitamin D confounds the contrast with control)
  - "https://doi.org/10.3390/nu13030948"  # Pourabbas M, Bagheri R, Hooshmand Moghadam B, et al. Nutrients 2021;13(3):948. PMID 33804259 -- 30 resistance-trained men (15 months of training), 6 weeks: 30 g milk protein after each session AND 30 g before sleep vs isoenergetic maltodextrin; lean mass, strength and power rose more with milk (bioimpedance); two doses and a carbohydrate control, so the pre-sleep dose cannot be isolated
  - "https://doi.org/10.3389/fnut.2023.1262044"  # Chapman S, Roberts J, Roberts AJ, et al. Front Nutr 2023;10:1262044. PMID 38144428, NCT05998590 -- 122 British Army recruits, 12 weeks: no supplement, carbohydrate placebo, 20 g or 60 g protein on weekday evenings (20:00-21:00); protein intake 1.17, 1.31, 1.71, 2.16 g/kg/day; no effect on strength or power tests or on fat-free mass change (CON 4, PLA 4, MOD 3, HIGH 5 percent, P=0.959)
  - "https://doi.org/10.1080/15502783.2025.2519511"  # Klemp AO, Ormsbee MJ, Yeh M, et al. J Int Soc Sports Nutr 2025;22(1):2519511. PMID 40539259, NCT05922475 -- 30 untrained older men (66 years), 12 weeks, 40 g protein after training vs before sleep vs training alone; all gained muscle thickness and strength, no group difference; baseline protein 1.0 g/kg/day or more
  - "https://doi.org/10.1080/15502783.2022.2036451"  # Ormsbee MJ, Saracino PG, Morrissey MC, et al. J Int Soc Sports Nutr 2022;19(1):164-178. PMID 35599912 -- 18 resistance-trained men, one evening session: 40 g casein vs non-caloric placebo before sleep; no difference in next-morning squat or bench 1RM, creatine kinase or CRP; hunger lower with protein but P=0.07 (d=0.95)
  - "https://doi.org/10.1017/S0007114514001068"  # Kinsey AW, Eddy WR, Madzima TA, et al. Br J Nutr 2014;112(3):320-327. PMID 24833598 -- 44 sedentary overweight or obese women, whey vs casein vs carbohydrate placebo 30 min before sleep: no group-by-time interaction; satiety up and desire to eat down after protein AND placebo alike (insulin up too)
  - "https://doi.org/10.3390/nu10091273"  # Madzima TA, Melanson JT, Black JR, Nepocatych S. Nutrients 2018;10(9):1273. PMID 30201853 -- 9 active women, crossover: 48 g casein likely raised next-morning resting metabolic rate by 4.0 +/- 4.8 percent vs a non-energetic placebo, trivial effect on training volume; 24 g casein and whey at either dose showed no clear effect (magnitude-based inference, not significance tests)
  - "https://doi.org/10.3390/nu13061872"  # Dela Cruz J, Kahan D. Nutrients 2021;13(6):1872. PMID 34070862 -- systematic review, 11 studies of 24-48 g casein before sleep: limited to no effect on energy expenditure, lipolysis or appetite, with limited data
  - "https://doi.org/10.3389/fnut.2019.00017"  # Snijders T, Trommelen J, Kouw IWK, et al. Front Nutr 2019;6:17. PMID 30895177 -- review by authors of the original trials: pre-sleep protein raises overnight synthesis, does not reduce breakfast appetite or change resting energy expenditure, and benefits muscle and strength in training young men
  - "https://doi.org/10.1016/j.jsams.2020.07.016"  # Reis CEG, Loureiro LMR, Roschel H, da Costa THM. J Sci Med Sport 2021;24(2):177-182. PMID 32811763 -- systematic review, 9 studies; possible muscle benefit in young men, none shown in older men; conclusions limited by uneven protein intakes between groups
  - "https://doi.org/10.1123/ijsnem.2023-0118"  # Zhou HH, Liao Y, Zhou X, et al. Int J Sport Nutr Exerc Metab 2024;34(1):54-64. PMID 38039960, PROSPERO CRD42022358766 -- network meta-analysis, 116 trials, 4,711 participants, search to May 2023; vs placebo, protein at night gave +2.85 kg handgrip and +12.12 kg leg-press strength (moderate certainty); the authors call for trials that compare timing directly. ABSTRACT ONLY
  - "https://doi.org/10.1123/ijsnem.2025-0205"  # Aussieker T, Kredig N, Wasserfurth P, et al. Int J Sport Nutr Exerc Metab 2026;36(5):481-490. PMID 42413910 -- 9 resistance-trained adults, double-blind crossover after a lifting session: 40 g whey vs 40 g casein vs maltodextrin 30 min before bed; whey shortened sleep-onset latency (9 vs 19 min) and raised sleep efficiency (96 vs 93 percent) vs control, casein did not separate from control, and the abstract reports no significant whey-casein difference; no difference in gut symptoms or next-day performance
  - "source:nutrition/protein-timing-total-matched-024 -- owns the around-the-session timing claim and the bedtime fill-slot rule this item supports"
  - "source:nutrition/meal-protein-nudge-rules-063 -- its pre-sleep-option rule rests on the same trials"
  - "source:nutrition/protein-deficit-lean-mass-target-062 -- the daily total the bedtime slot exists to help reach"
  - "source:nutrition/metabolizable-energy-atwater-015 -- a bedtime snack is energy and is logged as energy"
  - "source:sleep-recovery/late-night-next-morning-training-080 -- the sleep side of late evening habits"
applicability:
  axes:
    - key: age_years
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
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
pre_sleep_rules:
  - rule: fill-slot-only
    when: the day's protein is below the user's floor and the evening has no protein-containing meal
    effect: may offer 25-40 g of milk protein, whey, yogurt or similar before bed as one convenient slot; it counts in full toward the day's total; never described as better than the same protein earlier in the day
    basis: Joy 2018, Antonio 2017, Valenzuela 2023 and Chen 2022 (same dose at another time of day, no difference)
    basis_grade: C
  - rule: no-bonus-on-a-met-day
    when: the day's protein total is already at or above the user's floor
    effect: no pre-sleep protein line and no extra-gains claim
    basis: Chapman 2023 (20 or 60 g on weekday evenings on top of the diet, no effect in 122 recruits), Klemp 2025 (older men), Joy 2018
    basis_grade: C
  - rule: not-an-appetite-tool
    when: program is cut and the user asks whether protein before bed cuts next-morning hunger or cravings
    effect: say the studies found no protein-specific effect on next-morning appetite; allow it as a snack on its energy cost, not as a hunger fix
    basis: Kinsey 2014 (protein and placebo improved appetite alike), Dela Cruz 2021 (11 studies), Ormsbee 2022 (hunger lower, P=0.07, 18 men)
    basis_grade: C
  - rule: not-a-metabolism-tool
    when: user asks whether protein before bed raises metabolism or burns extra calories overnight
    effect: not established; one 9-woman crossover found about +4 percent morning resting metabolic rate at 48 g casein and reviews found no change; no calorie credit is given in the energy budget
    basis: Madzima 2018, Snijders 2019, Dela Cruz 2021
    basis_grade: C
  - rule: log-its-energy
    when: a pre-sleep shake or snack is logged
    effect: counts toward the day's energy and protein in full
    basis: Atwater arithmetic (nutrition/metabolizable-energy-atwater-015)
    basis_grade: A (definitional)
  - rule: sleep-claim-withheld
    when: user asks whether a pre-bed protein drink helps sleep, or reports poor sleep after one
    effect: no sleep benefit is claimed; one 9-person crossover found whey, but not casein, separated from an isocaloric control on sleep onset after evening lifting (the two proteins did not differ significantly) and has not been replicated; the late-meal comfort and reflux margin stays a comfort rule (024)
    basis: Aussieker 2026
    basis_grade: D
  - rule: population-guard
    when: user is 65 or over, or the user is a woman asking whether pre-sleep protein adds muscle
    effect: say the muscle-gain trials were in young men, the one trial in older men found nothing (Klemp 2025), and women appear mainly in short one-night studies and as a minority of two mixed-sex trials that found no effect; do not extend the young-male result
    basis: Snijders 2015, Klemp 2025, Kinsey 2014, Madzima 2018, Antonio 2017, Chapman 2023
    basis_grade: D
refraction_notes:
  - note: >
      THE POSITIVE TRIALS DID NOT MATCH TOTALS. Snijders 2015 compared a
      protein drink with a calorie-free placebo, Pourabbas 2021 gave two 30 g
      milk-protein doses (after training and before sleep) against
      maltodextrin, and Chen 2022 compared two supplements with a 5 g
      maltodextrin control and added vitamin D. In each the protein group
      simply ate more protein. Reading them as a bedtime effect needs a
      matched comparison, and the matched comparisons found nothing.
    grade: C
  - note: >
      THE MATCHED TRIALS ARE SMALL AND SHORT. Joy 2018 has 13 men, Antonio
      2017 has 26 with no unsupplemented control, Valenzuela 2023 has 24
      cyclists over 6 days eating above 2.5 g/kg, and Chen 2022 has 42
      untrained men over 6 weeks with vitamin D added. Four nulls of this size
      cannot exclude a modest timing effect; they do remove the evidence that
      one exists. The reviews (Reis 2021 and Snijders 2019) reach different
      conclusions from the same trials, which is the contested flag.
    grade: C
  - note: >
      THE NETWORK META-ANALYSIS DOES NOT SETTLE IT. Zhou 2024 ranks protein at
      night best for strength, but its estimates are each timing against
      placebo, so they mix the timing with the extra protein, and its authors
      ask for trials that compare timing directly. Only the abstract was read;
      how many trials sit in the night node is not known here.
    grade: C
  - note: >
      IN A CUT THE QUESTIONS ARE HUNGER AND METABOLISM, AND THE ANSWER IS
      THIN. The one-night study in overweight women found no protein-specific
      appetite effect, and the one in active women found, at one dose in 9
      women, a small rise in morning metabolic rate that the reviews do not
      confirm. No trial of pre-sleep protein on lean mass or fat loss during
      a calorie deficit was located. The fill-slot use stands on convenience,
      not on a measured benefit in dieters.
    grade: C
  - note: >
      SEX, AGE AND TRAINING STATUS LIMIT THE POSITIVES. The muscle-gain
      positives are in young men. The one 12-week trial in older men, with the
      same 40 g, found training alone did as well. Women appear in one-night
      appetite and metabolism studies (Kinsey 2014, Madzima 2018) and as a
      minority of two mixed-sex trials (Antonio 2017, Chapman 2023) whose
      abstracts report no sex-specific results and no effect.
    grade: D
  - note: >
      THE SLEEP RESULT IS A PILOT. Aussieker 2026 (9 people, crossover) found
      whey, but not casein, separated from an isocaloric control on sleep
      latency and efficiency, which cuts against the usual assumption that
      slow casein is the bedtime protein; the abstract reports no significant
      difference between the two proteins. It has not been replicated and is
      not spoken as a finding; it is recorded so that a sleep module can pick
      it up.
    grade: D
claim: >
  Protein before sleep (about 25-40 g) raises overnight muscle protein
  synthesis in young men after evening training. A 12-week trial that added it
  to usual intake against a calorie-free placebo found more strength and muscle
  (Snijders 2015, n=44), as did a 6-week trial that gave milk protein after
  training and before sleep against a carbohydrate control (Pourabbas 2021,
  n=30). Every comparison that gave the same dose at another time of day, with
  protein matched, found no difference (Joy 2018, n=13; Antonio 2017, n=26
  trained; Valenzuela 2023, n=24 cyclists; Chen 2022, n=42 untrained men), and
  added evening protein did nothing for strength or lean mass in recruits whose
  usual intake was about 1.2-1.3 g/kg (Chapman 2023, n=122) or in older men
  (Klemp 2025). A network meta-analysis ranks night protein best for strength, but against
  placebo, not against the same protein at another time. In people dieting,
  one-night studies show no protein-specific effect on next-morning appetite
  and an inconsistent effect on resting metabolic rate; no trial of pre-sleep
  protein on lean mass during a cut was located. For a diet card, a bedtime
  portion is a convenient place to reach the day's protein total, counted as
  food, and not a timing bonus.
reasoning: >
  The overnight synthesis finding is a measured mechanism and is not in
  dispute. What is disputed is whether it turns into extra growth that would
  not have happened had the same protein been eaten earlier. The trials that
  say yes did not hold the daily total constant, so they cannot answer that
  question; the trials that did hold it constant say no, but are small, and one
  has no unsupplemented arm. Two review groups read the same literature in
  opposite directions, and a network meta-analysis whose estimates are against
  placebo points the same way as the unmatched trials. That is a contested
  claim resting on small randomised trials, and the lower letter reflects that
  no adequately sized matched trial exists. The cut-specific statements
  (hunger, metabolic rate, lean mass) are held at the same band because the
  evidence is one-night studies and one small crossover, with no trial in
  dieters on the outcome a lifter cares about. Nothing here argues
  against a bedtime shake; it argues against calling it more than a slot.
---

# nutrition/pre-sleep-protein-matched-trials-091

The reason people eat protein before bed is solid as far as it goes: protein
taken just before sleep is digested overnight and measurably raises muscle
protein synthesis after an evening workout. The leap from that to "it builds
more muscle" is where the evidence gets thin. The trials that found bigger
gains compared a protein drink with a calorie-free or carbohydrate drink, so
the protein group was eating more protein all day. When researchers gave the
same dose at a different time of day and kept the total equal, the groups did
the same.

That does not show bedtime protein is useless, only that no trial has shown it
better than the same protein earlier. The matched trials are small, a network
meta-analysis ranks night protein best for strength against placebo, and two
review groups disagree. The claim is therefore held as contested.

On a cut the question changes to hunger and metabolism. The one-night studies in
women found protein before bed did not curb next-morning appetite any more than
a placebo snack, and a small rise in morning metabolic rate at one dose in nine
women has not been confirmed. A bedtime shake is useful when the day's protein
is short and evening is the only slot left. It is logged as food, and it is
not sold as anything else.

## Engine rules (diet card)

| Rule | When | Effect | Basis band |
|---|---|---|---|
| fill-slot-only | day short, no evening protein | may offer 25-40 g as a slot | observational |
| no-bonus-on-a-met-day | day at or above floor | no pre-sleep line | observational |
| not-an-appetite-tool | cut, asks about hunger | no protein-specific effect found | observational |
| not-a-metabolism-tool | asks about metabolism | not established, no calorie credit | observational |
| log-its-energy | snack logged | counts in full | definitional |
| sleep-claim-withheld | asks about sleep | no benefit claimed | practitioner |
| population-guard | 65 or over, or a woman asking about muscle | do not extend the young-male result | practitioner |

## 한국어 요약 (답변용)

- 자기 전 단백질(약 25-40 g)이 밤사이 근단백질 합성을 높인다는 것은 측정된 사실이다. 하지만 "그래서
  근육이 더 붙는다"는 것은 다른 문제다.
- 더 큰 증가를 보인 시험들은 대조군이 열량 없는 위약이나 탄수화물이었다. 단백질 군이 하루 단백질을 더
  먹은 효과다. 같은 양을 낮에 먹게 하고 총량을 맞춘 시험 네 건(13명, 26명, 24명, 42명)에서는 차이가 없었다.
  다만 모두 작은 시험이어서 "효과가 없다"가 아니라 "더 낫다는 근거가 없다"로 말한다.
- 그래서 하루 총량이 모자라고 저녁에 단백질이 없을 때 자기 전 25-40 g은 총량을 채우는 편한 자리 중
  하나다. 총량을 이미 채운 날에는 따로 권하지 않고, 다른 시간에 먹는 것보다 낫다고 말하지 않는다.
- 감량 중 다음 날 아침 허기를 줄이는지는 연구들이 단백질만의 효과를 찾지 못했다. 신진대사를 올린다는
  근거(여성 9명, 48 g 카제인에서 약 4%)도 확정이 아니다. 열량으로 더하고, 기록은 음식으로 한다.
- 근육 증가 시험은 젊은 남성 중심이다. 65세 이상 남성 12주 시험에서는 차이가 없었고, 여성은 하룻밤
  연구와 남녀 혼합 시험의 일부로만 들어 있다. 젊은 남성 결과를 그대로 옮기지 않는다.
- 수면에 좋다는 말은 하지 않는다. 9명 교차시험에서 유청은 대조 음료보다 잠드는 시간을 줄였지만 카제인은
  그렇지 않았고(둘 사이 차이는 유의하지 않았다), 재현되지 않았다. 자기 직전 식사는 속 편함의 문제로 따로 본다.
