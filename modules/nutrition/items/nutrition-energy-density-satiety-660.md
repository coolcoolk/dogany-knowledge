---
# Volume-eating sprint 2026-10-07. The
# evidence row under cooking item 662 (module not published). It owns ONE finding:
# for a given meal, lowering the energy per gram of what is served (mostly by
# adding water and vegetables inside the food) lowers how much energy is eaten,
# and the body only partly makes it up. Satiety per kcal of protein is cited,
# not re-owned (protein rows 002/063/090 own amounts). Portion SIZE is item 070,
# not this one; the two interact (a big portion of a low-density food is the
# lever, a big portion of a dense food is the trap).
#
# Source access this pass: the egress proxy refused PubMed, PMC, Europe PMC,
# Crossref and every publisher host. Every figure below was read from a
# web-search index rendering of the abstract (search 2026-10-07), not from the
# record itself, and no full text was read. That is why the grade is held at
# B and not higher, and why the row is flagged rerun-needed in GAPS.md.
#
# meal_rules is structured data (same shape as 070): rule, when, action,
# basis, basis_grade, kind.
id: nutrition/energy-density-satiety-660
domain: nutrition
lane: "@obs-inferential"
grade: "B (direction: lower energy density of served food lowers energy intake, meta-analysis of 31 experimental studies with daily intake as outcome; water inside food beats water drunk with it; a low-density first course lowers the meal; one year-long RCT in women with obesity); C (size of the effect on body weight -- pooled weight effect small and mixed with observational studies; protein preloads raise fullness, meta-analysis of 5 studies; satiety index of single foods, one 1995 lab study)"
locale: universal
as_of: 1995-2022
contested: no
sources:
  - "https://doi.org/10.1186/s12966-022-01287-z"  # Robinson E, Khuttan M, McFarland-Lesser I, Patel Z, Jones A. Calorie reformulation: a systematic review and meta-analysis examining the effect of manipulating food energy density on daily energy intake. Int J Behav Nutr Phys Act 2022;19:48. PMC9026919. 31 experimental studies (27 adult, 4 child), 90 effects, intake measured over at least 1 day: lower energy density -> SMD -1.00 (95% CI -0.75 to -1.27), about -208 kcal a day pooled; adults about -160 kcal a day after accounting for compensation. Abstract figures read through a web-search index rendering 2026-10-07; record not reachable (egress)
  - "https://doi.org/10.1093/ajcn/85.6.1465"  # Ello-Martin JA, Roe LS, Ledikwe JH, Beach AM, Rolls BJ. Dietary energy density in the treatment of obesity: a year-long trial comparing 2 weight-loss diets. Am J Clin Nutr 2007;85(6):1465-1477. 97 women with obesity randomised to reduce fat (RF) or reduce fat and add water-rich foods, mainly fruit and vegetables (RF+FV); no calorie or fat-gram goals; completers (n=71) lost 7.9 +/- 0.9 kg (RF+FV) vs 6.4 +/- 0.9 kg (RF); RF+FV ate a greater weight of food at lower energy density and reported less hunger. Abstract read through web-search index renderings 2026-10-07
  - "https://doi.org/10.1093/ajcn/70.4.448"  # Rolls BJ, Bell EA, Thorwart ML. Water incorporated into a food but not served with a food decreases energy intake in lean women. Am J Clin Nutr 1999;70(4):448-455. 24 women; isoenergetic preloads of chicken-rice casserole, the casserole with a glass of water, or the same ingredients as chicken-rice soup; lunch intake 1209 +/- 125 kJ after soup vs 1657 and 1639 kJ after the casseroles (about 26 percent less); water drunk alongside did nothing; no compensation at dinner. Abstract read through a web-search index rendering 2026-10-07
  - "https://pubmed.ncbi.nlm.nih.gov/17574705/"  # Flood JE, Rolls BJ. Soup preloads in a variety of forms reduce meal energy intake. Appetite 2007;49(3):626-634. 60 normal-weight adults; broth and vegetables separate, chunky, chunky-pureed or pureed vegetable soup 15 min before lunch vs none: meal intake down 20 percent (134 +/- 25 kcal) including the soup; form of soup made no difference. Abstract read through a web-search index rendering 2026-10-07; PMID from the search result, record not reachable (egress)
  - "https://doi.org/10.1016/j.jada.2004.07.001"  # Rolls BJ, Roe LS, Meengs JS. Salad and satiety: energy density and portion size of a first-course salad affect energy intake at lunch. J Am Diet Assoc 2004;104(10):1570-1576. Low-energy-dense first-course salad cut total lunch energy 7 percent (small portion) and 12 percent (large portion) vs no first course; a high-energy-dense salad raised it. Abstract read through a web-search index rendering 2026-10-07; DOI not resolved (egress)
  - "https://doi.org/10.3390/nu8040229"  # Stelmach-Mardas M, Rodacki T, Dobrowolska-Iwanek J, et al. Link between food energy density and body weight changes in obese adults. Nutrients 2016;8(4):229. PMC4848697. 13 experimental and observational studies, 3,628 adults 18-66: low-energy-density eating associated with -0.53 kg (95% CI -0.88 to -0.19). Abstract read through a web-search index rendering 2026-10-07
  - "https://doi.org/10.1016/j.cmet.2019.05.008"  # Hall KD, Ayuketah A, Brychta R, et al. Ultra-processed diets cause excess calorie intake and weight gain: an inpatient randomized controlled trial of ad libitum food intake. Cell Metab 2019;30(1):67-77. 20 inpatients, 2 weeks each diet; ultra-processed +508 +/- 106 kcal a day vs unprocessed; meals matched on PRESENTED energy density (of the non-beverage food), macronutrients, sugar, sodium and fibre; +0.9 vs -0.9 kg. Abstract read through a web-search index rendering 2026-10-07. Cited for the limit it sets: matching density did not equalise intake, so density is one lever, not the whole story
  - "https://doi.org/10.1016/j.jand.2016.01.003"  # Dhillon J, Craig BA, Leidy HJ, et al. The effects of increased protein intake on fullness: a meta-analysis and its limitations. J Acad Nutr Diet 2016;116(6):968-983. Higher-protein preloads raised 2-4 h fullness more than lower-protein preloads (meta-analysis of 5 studies; directional vote count of 28). Abstract read through a web-search index rendering 2026-10-07; DOI not resolved (egress)
  - "https://pubmed.ncbi.nlm.nih.gov/7498104/"  # Holt SHA, Brand Miller JC, Petocz P, Farmakalidis E. A satiety index of common foods. Eur J Clin Nutr 1995;49(9):675-690. 38 foods at 1000 kJ (240 kcal), 11-13 subjects per food, white bread = 100: boiled potatoes about three times white bread; fat-rich bakery items (cake, croissant, doughnut) lowest. Abstract read through a web-search index rendering 2026-10-07; PubMed record not reachable (egress)
  - "source:nutrition/portion-size-effect-intake-070 -- the amount served sets the amount eaten; this row says WHAT is served at that size matters too"
  - "source:nutrition/kr-restaurant-dish-energy-ranking-022 -- measured Korean dish densities (찌개 61, 국 62, 탕 70 vs 튀김 310 kcal/100 g) and the per-serving trap"
  - "source:nutrition/fibre-doseresponse-013 -- fibre's long-term associations; this row does not claim fibre causes satiety by itself"
  - "source:nutrition/protein-intake-002 -- protein amounts on a cut; this row only says protein-forward plates are more filling per kcal"
  - "framework:GRADE -- experimental base for intake (lab and short free-living); one long RCT for weight; the weight effect size is small and partly observational"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
meal_rules:
  - rule: density-not-volume-alone
    when: suggesting a lighter meal on a cut
    action: lower kcal per gram of the plate (add vegetables, broth, water-rich foods inside the dish) while keeping the usual plate size, rather than shrinking a dense plate
    basis: Robinson 2022 (about -160 kcal a day in adults after compensation); Ello-Martin 2007 (more food by weight, less hunger, equal or better loss)
    basis_grade: B
    kind: evidence
  - rule: water-in-the-food
    when: user says drinking water before meals will fill them up
    action: say water cooked into the food (soup, stew, vegetables) filled people up in trials; the same water drunk alongside did not
    basis: Rolls 1999
    basis_grade: B
    kind: evidence
  - rule: low-density-first
    when: a meal has a broth, salad or vegetable side
    action: suggest eating that part first; a low-density first course cut total meal energy by about 7-20 percent in lab trials
    basis: Flood 2007 (soup, -20 percent); Rolls 2004 (salad, -7 to -12 percent)
    basis_grade: B
    kind: evidence
  - rule: dense-first-course-backfires
    when: the starter or side is creamy, fried, oily or heavily dressed
    action: do not call it a filler; a high-density first course raised total meal intake
    basis: Rolls 2004
    basis_grade: B
    kind: evidence
  - rule: protein-adds-fullness
    when: building a low-calorie plate
    action: anchor it on a protein portion; protein preloads raised fullness over 2-4 hours more than lower-protein ones
    basis: Dhillon 2016
    basis_grade: C
    kind: evidence
  - rule: no-weight-promise
    when: speaking about volume eating and weight
    action: say it makes the same calories more filling and tends to lower intake; never promise a kg figure; the pooled weight effect is about half a kilogram and the one long trial differed by 1.5 kg between two already-effective diets
    basis: Stelmach-Mardas 2016; Ello-Martin 2007
    basis_grade: C
    kind: evidence
refraction_notes:
  - axis: primary_goal
    note: >
      For a user who is not cutting, volume eating is not offered unprompted.
      For a user trying to gain or with a small appetite, low-density foods
      are the WRONG lever -- they fill before enough energy is in.
    grade: C
  - note: >
      THE MECHANISM IS WEIGHT AND VOLUME, NOT MAGIC FOODS. Across the
      Rolls-lab studies people tended to eat a fairly constant weight of food
      over a meal, so energy eaten fell when energy per gram fell. Nothing in
      this row says a particular vegetable "burns" calories or that any food
      is "negative calorie".
    grade: B
  - note: >
      LAB INTAKE IS NOT LONG-TERM WEIGHT. Most trials are single meals or a
      few days. The year-long trial was in women with obesity in the US and
      tested counselling, not served food. The weight effect is real in
      direction and small in pooled size.
    grade: C
  - note: >
      DENSITY IS NOT THE WHOLE STORY. In the 2019 inpatient trial meals matched
      on presented energy density still produced about 500 kcal a day more
      intake on the ultra-processed diet. Speed of eating, texture and
      palatability matter too; a low-density label does not make a food
      filling.
    grade: B
  - note: >
      SOURCE ACCESS. Every figure here was read from abstract renderings in
      search results, not from the PubMed records or full text (blocked this
      pass). Re-read at source before raising or quoting decimals.
    grade: D
claim: >
  Lowering the energy density of what is served -- mostly by building water
  and vegetables into the food -- lowers how much energy people eat, and they
  only partly make it up. Across 31 experiments measuring at least a day of
  intake, lower-density food cut daily intake by a large standardised amount,
  about 160 kcal a day in adults after compensation. Water counts when it is
  inside the food: the same chicken and rice eaten as a soup cut the next
  meal about a quarter, while the same water drunk with a casserole did
  nothing. A low-density first course (vegetable soup, a lightly dressed
  salad) lowered total meal energy by roughly 7-20 percent, while a dense one
  raised it. Over a year, women with obesity told to add water-rich foods to
  a lower-fat diet ate more food by weight, felt less hungry and lost at
  least as much (7.9 vs 6.4 kg in completers). Protein-forward preloads add
  fullness per kcal. The weight effect is small when pooled, and density
  does not explain everything (matched-density ultra-processed meals still
  drove about 500 kcal a day more intake).
reasoning: >
  The lever is well replicated at the meal and day level by one laboratory
  group and a 2022 meta-analysis that pooled experiments independently; that
  carries the direction at the randomised/pooled band. What it does to body
  weight over months rests on one year-long counselling trial and a small
  pooled estimate that mixes observational designs, so it is spoken as "tends
  to", never as a number for the user. The satiety index and the protein
  fullness meta-analysis are carried lower: one 1995 lab ranking and a
  five-study pool respectively. Not here: Korean-specific trials (none was
  found by search), konjac and glucomannan (item 661), the energy of specific
  Korean dishes (022), and any claim about fibre as the active ingredient.
  Source access was abstract renderings only this pass (proxy refused every
  bibliographic host); that caps the row and is recorded in GAPS.md.
---

# nutrition/energy-density-satiety-660 -- 에너지 밀도와 포만감

**One line:** 같은 칼로리라면 물과 채소가 음식 안에 많이 든 쪽이 더 배부르고, 사람들은
덜 먹는다. 다만 체중 효과는 작고, 칼로리 수치를 약속하지 않는다.

- **Intake.** Lower-density food lowered daily intake across 31 experiments
  (about 160 kcal a day in adults after compensation).
- **Water inside, not beside.** Soup made of the same chicken and rice cut the
  next meal about 26 percent; a glass of water with the casserole did nothing.
- **First course.** Vegetable soup before lunch: meal down 20 percent including
  the soup. Low-density salad: down 7-12 percent. A dense salad raised intake.
- **A year.** Adding water-rich foods to a lower-fat diet: more food by weight,
  less hunger, 7.9 vs 6.4 kg lost (completers).
- **Limits.** Pooled weight effect about half a kilogram; matched-density
  ultra-processed meals still drove about 500 kcal a day more.

| Rule | When | Action | Basis grade |
|---|---|---|---|
| density-not-volume-alone | lighter meal on a cut | lower kcal per gram, keep the plate size | B |
| water-in-the-food | "water fills me up" | water in soup/stew works; drunk alongside did not | B |
| low-density-first | broth/salad/veg present | eat it first | B |
| dense-first-course-backfires | creamy/fried starter | not a filler | B |
| protein-adds-fullness | building the plate | anchor on protein | C |
| no-weight-promise | weight talk | no kg figure | C |

## 한국어 요약 (답변용)

- 에너지 밀도는 음식 1 g에 든 열량이다. 같은 양을 먹어도 물과 채소가 많이 든 음식은 열량이
  낮다. 실험들에서 사람들은 한 끼에 대체로 비슷한 '양(무게)'을 먹었고, 그래서 밀도가 낮으면
  섭취 열량이 줄었다.
- 31개 실험을 모은 분석에서 밀도가 낮은 음식을 받은 사람들은 하루 섭취량이 줄었고, 성인은
  나중에 일부 더 먹은 것을 감안해도 하루 약 160 kcal 적었다.
- 물은 음식 안에 있어야 한다. 같은 닭고기와 밥을 수프로 먹었을 때 다음 끼니가 약 26% 줄었지만,
  같은 양의 물을 따로 마신 경우에는 차이가 없었다. "식전에 물 마시면 배부르다"보다 "국물과
  채소가 든 음식"이 근거가 있다.
- 채소 수프나 드레싱이 가벼운 샐러드를 먼저 먹으면 한 끼 전체 열량이 7~20% 줄었다. 반대로
  크림·기름·튀김이 들어간 전채는 오히려 전체를 늘렸다.
- 1년 연구에서 지방을 줄이면서 물 많은 음식(채소·과일)을 늘린 그룹은 더 많은 양을 먹고 덜
  배고팠으며, 체중 감량도 비슷하거나 조금 더 많았다(7.9 kg 대 6.4 kg, 끝까지 참여한 사람 기준).
- 단백질이 많은 음식도 같은 열량에서 포만감을 더 오래 준다(소규모 메타분석).
- 한계: 체중 효과는 모으면 평균 약 0.5 kg 정도로 작다. 밀도를 맞춘 초가공 식단도 하루 약
  500 kcal를 더 먹게 했으니, 밀도만으로 다 설명되지 않는다. "이걸 먹으면 몇 kg 빠진다"는 말은
  하지 않는다.
- 감량 중이 아니거나 살을 찌워야 하는 사용자에게는 반대다. 밀도 낮은 음식은 필요한 열량을
  채우기 전에 배를 부르게 한다.
