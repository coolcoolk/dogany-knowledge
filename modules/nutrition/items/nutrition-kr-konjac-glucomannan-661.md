---
# Volume-eating sprint 2026-10-07.
# KR-LOCALE row for konjac (곤약) in two forms that users conflate: (1) konjac
# as a FOOD -- 곤약밥, 곤약면, 실곤약, 곤약 in 조림 or 찌개, 곤약젤리 -- whose
# value on a cut is that it is nearly all water and fibre, i.e. a volume
# filler (the mechanism is nutrition/energy-density-satiety-660), and (2)
# glucomannan as a SUPPLEMENT (capsule, powder) sold for weight loss, where
# the trial evidence is mixed and the regulators disagree in tone.
# The choking rule is the one hard safety line here.
#
# Source access this pass: bibliographic and regulator hosts refused by the
# egress proxy; every source below was read as a web-search index rendering
# 2026-10-07 (abstract or article text as indexed). Rerun-needed in GAPS.md.
#
# konjac_rules feeds cooking item 662 (module not published); same field shape as
# 070's meal_rules plus never.
id: nutrition/kr-konjac-glucomannan-661
domain: nutrition
lane: "@obs-inferential"
grade: "C (glucomannan supplements for weight: one meta-analysis of RCTs found no significant effect, an earlier one a small effect, and the EU authorised a claim at 3 g a day before meals in an energy-restricted diet -- direction unsettled, size small at best); B (konjac food as a low-energy volume filler: follows from composition, about 96 percent water, plus the energy-density trials in 660); A (rule: konjac or glucomannan mini-cup jelly is banned in Korea for choking -- a regulatory fact, read through secondary reports); D (Korean composition figures for konjac noodles, read through a news report of a 국립농업과학원 analysis)"
locale: KR
as_of: 2004-2023
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/24533610/"  # Onakpoya I, Posadzki P, Ernst E. The efficacy of glucomannan supplementation in overweight and obesity: a systematic review and meta-analysis of randomized clinical trials. J Am Coll Nutr 2014;33(1):70-78. 9 RCTs, 8 pooled: mean difference -0.22 kg (95% CI -0.62 to 0.19), not significant; authors conclude RCT evidence does not show significant weight loss. Abstract read through a web-search index rendering 2026-10-07
  - "https://doi.org/10.2903/j.efsa.2010.1798"  # EFSA NDA Panel. Scientific Opinion on the substantiation of health claims related to konjac mannan (glucomannan) and reduction of body weight (and other claims). EFSA Journal 2010;8(10):1798. Cause-effect established for body-weight reduction in the context of an energy-restricted diet; conditions: at least 3 g a day in three doses of at least 1 g, with 1-2 glasses of water, before meals. Read through web-search index renderings and trade-press reports 2026-10-07; the EFSA PDF was not reachable (egress)
  - "https://www.medicaltimes.com/Main/view.html?ID=11998"  # 메디칼타임즈, report of 식품의약품안전청 measures on mini-cup jelly: provisional ban 2004-10-12 on mini-cup jellies 4.5 cm or less in diameter; sale resumed only for products passing a compression test of 7 N or less with choking warnings; mini-cup jellies containing 곤약 or 글루코만난 not permitted even when they pass. Read through a web-search index rendering 2026-10-07; the current 식품공전 text was not read, so whether the rule stands in this exact form today is unverified (secondary sources describe it as current)
  - "https://www.segye.com/newsView/20230315516342"  # 세계일보 2023-03-15, 곤약 article: about 5 kcal per 100 g; 국립농업과학원 figure for 국수형 곤약 per 100 g -- water 96.5 g, dietary fibre 2.9 g, protein 0.2 g; a clinic dietitian warns that a konjac-rice-only diet is nutritionally inadequate. Read through a web-search index rendering 2026-10-07; the national composition table row itself was not read
  - "source:nutrition/energy-density-satiety-660 -- why a near-zero-energy, high-water food can fill a plate on a cut"
  - "source:nutrition/protein-intake-002 -- a konjac meal still needs its protein"
  - "source:nutrition/fibre-doseresponse-013 -- fibre's associations; glucomannan is one fibre and does not inherit that row's grade"
  - "framework:GRADE -- supplement RCTs small and short with inconsistent pooled results; food use rests on composition plus 660; the jelly ban is regulatory"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [not_pregnant, none]
    - key: medication_list
      type: categorical
      role: hard
      unknown_policy: block_specifics
konjac_rules:
  - rule: konjac-is-a-filler
    when: user asks whether 곤약밥, 곤약면 or 실곤약 helps on a cut
    action: yes as a volume filler -- it adds bulk at almost no energy; use it to stretch a rice or noodle portion or bulk a 찌개, not to replace the whole meal
    never: [곤약이 지방을 태운다, negative calories, "곤약만 먹으면 빠져요"]
    basis: 세계일보 2023 (국립농업과학원 figures); nutrition/energy-density-satiety-660
    basis_grade: B
    kind: evidence
  - rule: half-swap-default
    when: suggesting konjac rice or noodles
    action: default to mixing -- replace about half of the 밥 or 면 with konjac -- and keep the protein portion; a fully konjac bowl is offered only if the user asks
    never: [곤약밥 only meals as a plan]
    basis: composition (protein 0.2 g per 100 g); dietitian caution in 세계일보 2023; convention on the ratio
    basis_grade: D
    kind: convention
  - rule: protein-still-needed
    when: a meal is built on konjac
    action: pair it with a protein portion (생선, 닭가슴살, 두부, 계란) as the meal's anchor
    never: [counting konjac toward protein]
    basis: 국립농업과학원 figure via 세계일보 2023; nutrition/protein-intake-002
    basis_grade: C
    kind: evidence
  - rule: supplement-not-promised
    when: user asks about glucomannan capsules or powder for weight loss
    action: say trials disagree -- one pooled analysis found no significant weight effect, the EU allows a claim at 3 g a day split before meals with 1-2 glasses of water inside a calorie-restricted diet; effect, if any, is small; food first
    never: [a kg figure, a product recommendation, a dose for a user whose pregnancy or medication status is unknown]
    basis: Onakpoya 2014; EFSA 2010
    basis_grade: C
    kind: evidence
  - rule: take-with-water
    when: a user already takes glucomannan powder or capsules
    action: the regulator's conditions of use include 1-2 glasses of water with each dose; mention it once
    never: [dry swallowing advice]
    basis: EFSA 2010 conditions of use
    basis_grade: B
    kind: evidence
  - rule: no-mini-cup-jelly
    when: konjac jelly or 곤약젤리 comes up for children, older adults or anyone with swallowing difficulty, or a small cup jelly in any context
    action: say konjac and glucomannan mini-cup jellies are banned in Korea because they caused choking deaths; pouch drinks and larger jellies are not that product but are still eaten in small bites, never sucked whole
    never: [recommending konjac jelly as a snack for a child or older adult]
    basis: 식약청 2004-2005 measures via 메디칼타임즈
    basis_grade: A
    kind: evidence
  - rule: log-konjac-by-label
    when: logging a packaged konjac product
    action: log from the package label; konjac rice products are often mixed with real rice and vary widely, so no generic default beyond about 5-10 kcal per 100 g for plain konjac
    never: [logging a konjac-rice blend as zero]
    basis: 세계일보 2023; convention
    basis_grade: D
    kind: convention
refraction_notes:
  - axis: primary_goal
    note: >
      For a user who is not cutting or who struggles to eat enough, konjac is
      not suggested; it fills without feeding.
    grade: C
  - axis: medication_list
    note: >
      Soluble fibre supplements can change how some drugs are absorbed. With
      the medication list unknown, give no supplement dose; konjac as food in
      a meal is not affected by this gate.
    grade: D
  - note: >
      THE SUPPLEMENT EVIDENCE IS GENUINELY SPLIT. The EU panel read the trials
      as showing an effect within a calorie-restricted diet; an independent
      meta-analysis four years later found none significant. Both are about
      capsules or powder taken before meals, not about eating 곤약면. Speak it
      as unsettled.
    grade: C
  - note: >
      SOURCE ACCESS. All four sources were read as search-index renderings;
      the 식품공전 text, the EFSA PDF and the national composition table row
      were not read directly this pass.
    grade: D
claim: >
  Konjac as a food is almost all water and fibre -- a 국립농업과학원 figure for
  noodle-type konjac is 96.5 g water, 2.9 g fibre and 0.2 g protein per 100 g,
  about 5 kcal -- so on a cut it is a volume filler: mixed half-and-half into
  rice or noodles, or added to a 찌개 or 조림, it adds bulk at almost no
  energy, by the same mechanism as other low-energy-density foods. It carries
  no protein, so the meal still needs its protein portion, and a
  konjac-only diet is inadequate. Glucomannan supplements are a separate
  question with split evidence: the EU authorised a weight-loss claim at 3 g
  a day in three doses before meals with water in an energy-restricted diet,
  while a 2014 meta-analysis of randomised trials found no significant
  weight effect (-0.22 kg). Konjac and glucomannan mini-cup jellies are
  banned in Korea after choking deaths.
reasoning: >
  Users ask about konjac in the food form far more than the supplement, and
  the food question has a simple answer from composition plus the
  energy-density trials (660): bulk without energy, no protein, not a meal on
  its own. The supplement question is carried at the observational band
  because the two best summaries point in different directions and the
  trials are short and small; it is flagged contested. The choking rule rests
  on a Korean regulatory measure seen through secondary reports, which is why
  the A applies to the rule's existence, not to its current exact wording.
  Not here: konjac and blood glucose or cholesterol (EFSA also reviewed
  these; not researched this pass), konjac and bowel effects, and any
  product-level advice.
---

# nutrition/kr-konjac-glucomannan-661 -- 곤약과 글루코만난

**One line:** 곤약은 '양을 늘리는 재료'로 쓰고 끼니 대신으로 쓰지 않는다. 글루코만난 보충제는
근거가 엇갈린다. 곤약 미니컵 젤리는 한국에서 금지된 제품이다.

- **Food.** Noodle-type konjac per 100 g: water 96.5 g, fibre 2.9 g, protein
  0.2 g, about 5 kcal. A filler, not a meal.
- **Supplement.** EU claim: 3 g a day in three doses before meals with water,
  inside an energy-restricted diet. A 2014 meta-analysis: -0.22 kg, not
  significant.
- **Choking.** Konjac or glucomannan mini-cup jellies are not permitted in Korea.

| Rule | When | Action |
|---|---|---|
| konjac-is-a-filler | 곤약밥/곤약면 on a cut | yes, as bulk |
| half-swap-default | suggesting konjac | about half the 밥 or 면, protein kept |
| protein-still-needed | konjac meal | add a protein anchor |
| supplement-not-promised | capsules/powder | evidence split; food first |
| take-with-water | already taking it | 1-2 glasses per dose |
| no-mini-cup-jelly | jelly, children, older adults | banned in Korea |
| log-konjac-by-label | packaged konjac | label, blends are not zero |

## 한국어 요약 (답변용)

- 곤약은 거의 물과 식이섬유다. 국립농업과학원 자료(기사 인용)로 국수형 곤약 100 g에 수분 96.5 g,
  식이섬유 2.9 g, 단백질 0.2 g, 열량은 5 kcal 안팎이다.
- 감량 중에는 '양 늘리기' 재료로 쓴다. 밥이나 면의 절반 정도를 곤약으로 바꾸거나 찌개·조림에
  넣으면 열량은 거의 그대로 두고 양을 늘릴 수 있다. 곤약이 지방을 태우는 것은 아니다.
- 단백질이 거의 없으니 생선, 닭가슴살, 두부, 계란 같은 단백질 반찬을 꼭 같이 둔다. 곤약밥만
  먹는 식단은 영양이 부족하다.
- 시판 곤약밥은 쌀이 섞인 제품이 많고 제품마다 다르다. 기록은 포장지 표시대로 하고, 0 kcal로
  두지 않는다.
- 글루코만난 보충제(캡슐·분말)는 근거가 엇갈린다. 유럽식품안전청은 열량을 줄인 식사와 함께
  하루 3 g을 식전 세 번에 나눠 물 1~2컵과 먹을 때 체중 감소 표시를 허용했지만, 2014년 무작위
  시험 메타분석에서는 의미 있는 차이가 없었다(-0.22 kg). 효과가 있더라도 작다. 이미 먹고
  있다면 물을 충분히 같이 마신다. 임신 여부나 복용 약을 모르면 용량은 말하지 않는다.
- 곤약·글루코만난이 든 미니컵 젤리는 질식 사고 때문에 한국에서 판매가 금지된 제품이다.
  아이나 어르신, 삼키기 어려운 사람에게 곤약 젤리를 간식으로 권하지 않고, 어떤 젤리든 통째로
  빨아 삼키지 않고 작게 나눠 먹는다.
