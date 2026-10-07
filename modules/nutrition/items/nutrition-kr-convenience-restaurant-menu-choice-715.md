---
# Eating-out / convenience sprint 2026-10-07.
# KR-LOCALE choice row: what to pick, on a cut, at a 편의점 or an everyday
# restaurant (김밥, 도시락, 국밥 / 탕, 면, 분식). The warehouse already holds the
# numbers: 030 (MFDS K-FIND protein per 100 kcal and sodium for convenience
# products and analysed dishes), 022 (2012-13 MFDS restaurant volumes, class
# medians), 072 (general 외식 rules), 080 (회식). What it lacked was the
# CHOICE layer that turns those tables into "build the meal like this" for the
# four places a Korean office worker actually eats lunch alone. This row adds
# that layer and one new data point (the 2023 Korea Consumer Agency 도시락
# test), and does not restate 030's or 022's tables.
#
# NO NEW COMPOSITION VALUES WERE READ THIS PASS. K-FIND, foodsafetykorea.go.kr
# and every publisher / news page were blocked by the egress proxy on
# 2026-10-07; only search-index records could be seen. Every kcal / protein /
# sodium figure below is copied from 030 or 022 (read at source by those
# passes) or is arithmetic on them, except the 도시락 ranges, which come from
# search-index summaries of news reports of the KCA test and are graded D.
# 김밥 rolls and 분식 dishes (떡볶이, 라볶이, 순대, 튀김) have NO tabled value in
# this warehouse; their rules are structural. See GAPS.
#
# menu_choice_rules is structured data for the diet card's "뭐 먹지 / 대신 뭐
# 먹을까" path and the meal log. Same field shape as 080's eating_out_rules:
# rule, surface, trigger, action, never, constants, basis, basis_grade, kind.
# combos is worked arithmetic on 030 rows (data, not advice by itself).
# The YAML-subset reader returns scalars as strings. No program code changed.
id: nutrition/kr-convenience-restaurant-menu-choice-715
domain: nutrition
lane: "@meal-craft"
grade: "D (synthesis: the menu_choice_rules as a set; each rule carries its own basis_grade); C (the per-item numbers, inherited from 030 K-FIND rows and 022 restaurant class medians, single analyses or label medians); D (2023 Korea Consumer Agency 도시락 ranges, seen only through search-index summaries of news reports)"
locale: KR
as_of: 2012-2026
contested: no
sources:
  - "source:nutrition/kr-convenience-protein-options-030 -- every convenience-store figure here (삼각김밥 190 kcal / 5 g protein / 444 mg sodium; 컵라면 326 / 7 / 1460; 닭가슴살 120 / 25 / 379; 고단백 음료 110 / 20 / 130; 구운란 132 / 11.5 / 155; 포장 두부 252 / 23.3 / 23; 그릭요거트 181 / 11 / 35, median packages) and its rank_key, protein_tier and sodium_tier"
  - "source:nutrition/kr-restaurant-dish-energy-ranking-022 -- restaurant class medians per serving: one-bowl rice meal 700 kcal and 26 g protein; 면류 636 kcal, 3.4 g protein per 100 kcal, 2193 mg sodium (16 of 30 at or above 2000 mg); 탕류 456 kcal, 12.7 g per 100 kcal, 1786 mg; 국류 1980 mg; 찌개류 1962 mg; restaurant 설렁탕 420 kcal, 60 g protein; the rice-line and no-rice-line logging rules; no broth credit"
  - "https://www.kca.go.kr/"  # 한국소비자원 (Korea Consumer Agency) quality and safety comparison test of convenience-store 도시락, press release 2023-06-28, as summarised in search-index records of Seoul Shinmun (m.seoul.co.kr/news/2023/06/28/20230628500129) and Newsis (NISX20230628_0002355924): sodium 1101-1721 mg per product (55-86 percent of the 2000 mg label reference); energy 30-52 percent of 2000 kcal; protein 36-71 percent of the label reference; 44 percent of surveyed consumers said they eat a 도시락 together with a cup ramen. The release itself and the news pages were blocked 2026-10-07; product count, brands and per-product values NOT seen. One summary conflated the product as 김밥; the headline and two other summaries say 도시락
  - "source:nutrition/kr-eating-out-fat-loss-072 -- decide-before-eating, leave-the-broth (logging convention), frequency-is-the-lever; not restated"
  - "source:nutrition/kr-hoesik-cut-rules-080 -- the 회식 / 술자리 case; this row defers to it for any evening with colleagues and drinks"
  - "source:nutrition/meal-protein-nudge-rules-063 -- the per-meal protein nudge whose dose the anchor rule fills"
  - "source:nutrition/protein-deficit-lean-mass-target-062 -- the deficit-phase protein band the choices help reach; not set here"
  - "source:nutrition/kr-mixed-dish-logging-unit-020 -- log a restaurant dish by its name and measured entry; shared-dish convention"
  - "source:nutrition/energy-density-satiety-660 -- why a soup, vegetable or tofu side adds volume for few kcal"
  - "source:nutrition/sodium-bp-evidence-cut-716 -- the sodium evidence and the 2,300 mg Korean reference behind the sodium display rule; this row does not grade sodium outcomes itself"
  - "framework:VC-E craft -- the numbers are government data read by earlier passes; protein per 100 kcal as the choice key, the anchor-plus-starch pattern, the sodium display thresholds and the copy are conventions labelled with their basis_grade"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: dietary_pattern
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: allergen_list
      type: categorical
      role: hard
      unknown_policy: hedge
    - key: cardiovascular_condition
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: renal_condition
      type: categorical
      role: soft
      unknown_policy: hedge
combos:
  - key: two_triangle_kimbap
    items: [triangle_kimbap, triangle_kimbap]
    kcal: 380
    protein_g: 10
    sodium_mg: 888
    protein_g_per_100kcal: 2.6
    role: baseline
  - key: cup_ramyeon_plus_triangle
    items: [cup_ramyeon, triangle_kimbap]
    kcal: 516
    protein_g: 12
    sodium_mg: 1904
    protein_g_per_100kcal: 2.3
    role: baseline
  - key: triangle_plus_chicken_breast
    items: [triangle_kimbap, chicken_breast_rte]
    kcal: 310
    protein_g: 30
    sodium_mg: 823
    protein_g_per_100kcal: 9.7
    role: option
  - key: triangle_plus_protein_drink
    items: [triangle_kimbap, rtd_protein_drink]
    kcal: 300
    protein_g: 25
    sodium_mg: 574
    protein_g_per_100kcal: 8.3
    role: option
  - key: triangle_plus_roasted_eggs
    items: [triangle_kimbap, egg_roasted]
    kcal: 322
    protein_g: 16.5
    sodium_mg: 599
    protein_g_per_100kcal: 5.1
    role: option
    note: "one median 구운란 package (132 kcal, 11.5 g protein); eggs per package not recorded in 030"
  - key: tofu_plus_triangle
    items: [tofu_pack, triangle_kimbap]
    kcal: 442
    protein_g: 28.3
    sodium_mg: 467
    protein_g_per_100kcal: 6.4
    role: option
    note: "vegan-compatible only if the 삼각김밥 filling is; read the pack"
menu_choice_rules:
  - rule: protein-anchor-first
    surface: diet_card
    trigger: user asks what to eat at a 편의점, or logs a starch-only convenience meal on a cut
    action: build the meal as one lean- or mid-tier protein item from 030 (닭가슴살, 고단백 음료, 구운란, 두부) plus at most one starch item, instead of two starch items or a cup ramen; show the combo arithmetic once (e.g. 삼각김밥 + 닭가슴살 about 310 kcal and 30 g protein against 삼각김밥 + 컵라면 about 516 kcal and 12 g)
    never: [a list of more than two options, "삼각김밥은 먹지 마세요", a brand name as a recommendation]
    constants: one swap suggestion per meal; combos from the combos table only
    basis: nutrition/kr-convenience-protein-options-030 (median package values); nutrition/meal-protein-nudge-rules-063
    basis_grade: C
    kind: convention
  - rule: rank-by-protein-per-kcal
    surface: diet_card
    trigger: comparing two or more options the user names
    action: compare by protein g per 100 kcal (030 rank_key) and say it in plain words ("같은 칼로리에 단백질이 몇 배"); starch meals sit at 2-4 g per 100 kcal, a lean item at 15 or more
    never: [a health score, a single 'best food']
    constants: tiers as 030 swap_rules.protein_tier
    basis: nutrition/kr-convenience-protein-options-030
    basis_grade: C
    kind: convention
  - rule: dosirak-is-a-full-meal
    surface: diet_card
    trigger: a 편의점 도시락 is logged or considered
    action: treat it as a complete meal; read the pack's kcal and protein and log those; if the shelf has several, pick the one with the most protein per kcal on the label; do not add a cup ramen -- 44 percent of surveyed buyers pair them, which adds about 326 kcal and 1460 mg sodium to a box already at 1100-1700 mg
    never: [a 도시락 kcal or protein default when the product is readable, the KCA ranges as one product's value]
    constants: none
    basis: Korea Consumer Agency 2023 도시락 test via news summaries (sodium 1101-1721 mg, energy 30-52 percent and protein 36-71 percent of label references); nutrition/kr-convenience-protein-options-030 (cup ramen median)
    basis_grade: D
    kind: convention
  - rule: dosirak-fallback
    surface: diet_card
    trigger: a 도시락 is logged without pack values
    action: log it as estimated at the one-bowl rice meal median (700 kcal, 26 g protein; 022) and mark the line estimated; the KCA ranges (about 600-1040 kcal) bracket that value
    never: [a precise figure without the label]
    constants: 700 kcal, 26 g protein, estimated
    basis: nutrition/kr-restaurant-dish-energy-ranking-022 (class-median-fallback); KCA 2023 energy share 30-52 percent of 2000 kcal
    basis_grade: D
    kind: convention
  - rule: gukbap-tang-is-a-protein-choice
    surface: diet_card
    trigger: choosing a lunch at a 국밥 / 탕 / 백반 restaurant on a cut
    action: a clear meat- or white-fish 탕 (설렁탕, 대구탕 type) gives the most protein per kcal of the restaurant classes (탕 median 12.7 g per 100 kcal against 3.4-3.6 for noodle and one-bowl rice meals); the rice is a separate line (022 rice-line) and the 공기밥 amount is the energy lever; 감자탕, 곰탕 and 꼬리곰탕 carry 30-52 g fat, so the protein advantage holds but the energy advantage does not
    never: [국밥 as automatically light, a broth-left kcal credit]
    constants: rice line one 공기 = 300 kcal, adjust in thirds (022)
    basis: nutrition/kr-restaurant-dish-energy-ranking-022 (dish_class_table, swap more-protein-per-kcal)
    basis_grade: B
    kind: evidence
  - rule: noodle-low-protein-high-salt
    surface: diet_card
    trigger: a noodle meal (라면, 칼국수, 짬뽕, 냉면, 우동) is chosen or logged on a cut
    action: say once that a noodle dish is about 640 kcal with little protein (median 3.4 g per 100 kcal) and usually at or above 2000 mg sodium; offer one lever -- add a protein side (egg, tofu) or leave most of the 국물 -- not both
    never: [a ban, a number for sodium saved by leaving the broth]
    constants: none
    basis: nutrition/kr-restaurant-dish-energy-ranking-022 (면류 n=30, 16 at or above 2000 mg; no broth split measured)
    basis_grade: B
    kind: evidence
  - rule: bunsik-structural
    surface: diet_card
    trigger: 떡볶이, 라볶이, 튀김, 순대 or a 분식 combo
    action: name it as a mostly starch-and-fat meal low in protein; the levers are portion (share, one 인분 split, skip the 튀김 add-on) and adding a protein item; log by name from the logger's dish entry and mark it estimated; quote no kcal from this row
    never: [a kcal or sodium figure for 분식 from this item, "분식은 다이어트의 적"]
    constants: none
    basis: nutrition/kr-restaurant-dish-energy-ranking-022 (튀김류 3.9 g protein per 100 kcal, 310 kcal per 100 g, restaurant class, not 분식-specific); no measured 분식 values read (GAPS)
    basis_grade: D
    kind: convention
  - rule: kimbap-roll-pair
    surface: diet_card
    trigger: a 김밥 roll (줄) is chosen or logged
    action: treat one roll as a rice meal low in protein per kcal; pair it with a protein item rather than a second roll or 라면; log by the logger's named entry; quote no roll kcal from this row
    never: [a 김밥 kcal from the 삼각김밥 row, a filling ranking]
    constants: none
    basis: nutrition/kr-convenience-protein-options-030 (삼각김밥 2.6 g per 100 kcal as the nearest measured relative); 022 excluded 김밥 from its one-bowl median; no roll values read (GAPS)
    basis_grade: D
    kind: convention
  - rule: sodium-as-label-share
    surface: diet_card
    trigger: a logged meal holds a 면, 국, 탕, 찌개, 도시락 or cup ramen
    action: show the meal's sodium, when known, as a share of the 2000 mg label reference; flag a single meal at 1000 mg or more once, plainly; the daily line is the 2,300 mg Korean chronic-disease reference (716)
    never: [a health warning from one meal, a low-sodium target below the reference, sodium advice framed as fat loss]
    constants: meal flag at 1000 mg (product constant, half the label reference); daily reference 2,300 mg
    basis: nutrition/kr-convenience-protein-options-030 (sodium_tier, label parity); nutrition/sodium-bp-evidence-cut-716
    basis_grade: D
    kind: convention
  - rule: sodium-condition-hedge
    surface: both
    trigger: cardiovascular_condition or renal_condition is present, or a user mentions blood-pressure medication
    action: keep the same label-share display, add no personal sodium or potassium target, and point to the user's clinician for one; never suggest a potassium salt substitute
    never: [저염 소금 추천, a sodium number as treatment]
    constants: none
    basis: nutrition/sodium-bp-evidence-cut-716 (substitute evidence is from a trial with its own exclusions)
    basis_grade: D
    kind: convention
  - rule: one-place-one-lever
    surface: diet_card
    trigger: any of the rules above fires
    action: give one lever per meal (protein anchor, rice amount, broth, or portion), in the user's chosen place; the place is not questioned
    never: [편의점 음식은 건강에 나빠요, 외식을 줄이세요 for a single meal, 치팅]
    constants: one lever per meal
    basis: nutrition/kr-eating-out-fat-loss-072 (frequency, not the single meal, is the lever); nutrition/kr-hoesik-cut-rules-080 (no-moralizing)
    basis_grade: D
    kind: convention
  - rule: hoesik-defers
    surface: diet_card
    trigger: the meal is a 회식, 술자리 or dinner with drinks
    action: route to nutrition/kr-hoesik-cut-rules-080 and do not apply this row's lunch rules
    never: []
    constants: none
    basis: nutrition/kr-hoesik-cut-rules-080
    basis_grade: D
    kind: convention
refraction_notes:
  - axis: primary_goal
    note: >
      For a user who is not cutting, the anchor and noodle rules do not fire
      unprompted; the sodium display still applies as information.
    grade: D
  - axis: dietary_pattern
    note: >
      Vegetarian or vegan users get 두부, 두유, 구운란 (vegetarian) and the tofu
      combo; 닭가슴살 and meat-broth 탕 rows drop out. A vegan high-protein
      convenience option other than 포장 두부 is not in 030.
    grade: D
  - note: >
      THE STARCH-ONLY CONVENIENCE MEAL IS THE COMMON CASE. Two 삼각김밥 or a
      삼각김밥 with a cup ramen gives 10-12 g protein for 380-520 kcal. Swapping
      one starch item for a lean protein item roughly triples protein at the
      same or lower energy. This is arithmetic on median labelled packages; a
      given product can sit well off the median (030 IQRs).
    grade: C
  - note: >
      THE 도시락 NUMBERS ARE SECOND-HAND. The KCA test was seen only through
      search-index summaries of news reports; how many products, which brands
      and each product's values were not seen. Use the ranges as context, never
      as one box's value, and read the pack.
    grade: D
  - note: >
      BROTH IS A LEVER WITHOUT A NUMBER. No measurement in the warehouse splits
      a Korean soup's sodium between broth and solids. Leaving the 국물 is
      offered as a sodium lever in words only.
    grade: D
claim: >
  On a cut, the everyday Korean lunch is best chosen by protein per calorie
  first and sodium second, and the levers differ by place. At a 편의점 the
  common meal is starch only (two 삼각김밥, or 삼각김밥 with a cup ramen: about
  10-12 g protein for 380-520 kcal by median package values); replacing one
  starch item with a lean protein item (닭가슴살, a protein drink, eggs, tofu)
  gives about 25-30 g protein for about 300 kcal. A 도시락 is already a full
  meal (in a 2023 consumer-agency test, about 30-52 percent of daily energy and
  1100-1700 mg sodium per box); read the pack and do not add a cup ramen. At a
  국밥 or 탕 restaurant, a clear meat or white-fish 탕 carries the most protein
  per calorie of the measured restaurant classes and the rice amount is the
  energy lever; noodle dishes are about 640 kcal with little protein and
  usually 2000 mg sodium or more. 김밥 rolls and 분식 have no measured value in
  this warehouse, so they get structural advice only (pair with protein, share
  the portion). Sodium is shown as a share of the 2000 mg label reference with
  a single-meal flag, never as a scare, and the 회식 case goes to item 080.
reasoning: >
  Items 030 and 022 hold the composition data, read at source by earlier
  passes, but neither says how to build a lunch from it; 072 gives general
  eating-out rules without numbers and 080 covers the evening event. The
  choice key (protein per 100 kcal) is the diet engine's existing density term
  and is a convention; the combo arithmetic is exact on 030's median packages,
  so its weight is the weight of those rows (label medians, wide IQRs). The
  restaurant rules lean on 022's class medians, which are wide orderings and
  survive the dataset's limits, so the 탕-versus-noodle rule keeps 022's B. The
  도시락 figures could not be read at source this pass (every Korean
  government and news host was blocked by the network proxy) and are held at
  D with the read path stated. 김밥 and 분식 are the most-asked items and have
  no number here; the honest output is structural advice plus a GAPS entry,
  not a borrowed figure. Deliberately not here: a 분식 or 김밥 kcal, a broth
  credit, brand recommendations, and any rule that rewards skipping lunch.
---

# nutrition/kr-convenience-restaurant-menu-choice-715 -- 감량 중 편의점·식당 메뉴 고르기

**One line:** 같은 칼로리면 단백질이 많은 쪽, 그다음 나트륨. 편의점에서는 탄수화물 두 개 대신 단백질
하나 + 탄수화물 하나, 식당에서는 맑은 탕 + 밥 양 조절, 면은 단백질이 적고 짜다.

What this row adds to 030 (편의점 단백질 표), 022 (외식 요리 열량), 072 (외식 규칙), 080 (회식):

- **Convenience combos.** Median packages from 030: 삼각김밥 ×2 = 380 kcal / 10 g protein;
  삼각김밥 + 컵라면 = 516 kcal / 12 g / 1904 mg sodium; 삼각김밥 + 닭가슴살 = 310 kcal / 30 g;
  삼각김밥 + 고단백 음료 = 300 kcal / 25 g.
- **도시락.** A full meal: 1101-1721 mg sodium, 30-52 % of 2000 kcal, protein 36-71 % of
  the label reference (KCA 2023, seen via news summaries only). Read the product; no cup ramen on top.
- **국밥 / 탕 vs 면.** 탕 median 12.7 g protein per 100 kcal; noodles 3.4 and about 640 kcal,
  usually ≥2000 mg sodium (022). Rice is its own line.
- **김밥, 분식.** No measured value here; structural advice only.

| Rule | Surface | Trigger | Action |
|---|---|---|---|
| protein-anchor-first | diet card | 편의점 meal | one protein item + at most one starch item |
| rank-by-protein-per-kcal | diet card | comparing options | g protein per 100 kcal, plain words |
| dosirak-is-a-full-meal | diet card | 도시락 | read pack; no cup ramen added |
| dosirak-fallback | diet card | 도시락 without label | 700 kcal / 26 g, estimated |
| gukbap-tang-is-a-protein-choice | diet card | 국밥/탕 lunch | clear 탕, rice line is the lever |
| noodle-low-protein-high-salt | diet card | noodle meal | one lever: protein side or leave broth |
| bunsik-structural | diet card | 떡볶이 etc. | share, add protein, no kcal quoted |
| kimbap-roll-pair | diet card | 김밥 roll | pair with protein, no kcal quoted |
| sodium-as-label-share | diet card | salty meal | share of 2000 mg; flag ≥1000 mg once |
| sodium-condition-hedge | both | CV / renal condition | no personal target; no salt substitute |
| one-place-one-lever | diet card | any | one lever per meal, no judging the place |
| hoesik-defers | diet card | 회식 | route to 080 |

## 한국어 요약 (답변용)

- 감량 중 메뉴는 "같은 칼로리에 단백질이 얼마나 있나"를 먼저 보고, 그다음 나트륨을 본다.
  탄수화물 위주 식사는 100 kcal당 단백질 2~4 g, 닭가슴살·고단백 음료는 15 g 이상이다.
- 편의점: 삼각김밥 두 개(약 380 kcal, 단백질 10 g)나 삼각김밥 + 컵라면(약 516 kcal, 12 g,
  나트륨 약 1,900 mg) 대신 삼각김밥 하나 + 닭가슴살(약 310 kcal, 30 g)이나 고단백 음료(약
  300 kcal, 25 g)로 바꾸면 비슷하거나 적은 칼로리로 단백질이 두세 배가 된다. 식약처 데이터의 제품
  중앙값 기준이라 제품마다 차이가 크니 포장 표시를 본다.
- 도시락은 그 자체로 한 끼다. 한국소비자원 2023년 시험에서 한 개에 나트륨 1,101~1,721 mg,
  열량은 하루 기준의 30~52%였다(보도 요약으로만 확인). 포장의 열량·단백질을 기록하고, 여러
  개 중에서는 칼로리 대비 단백질이 많은 것을 고른다. 컵라면을 같이 먹으면 약 326 kcal와 나트륨
  약 1,460 mg이 더해진다.
- 국밥·탕집: 설렁탕·대구탕 같은 맑은 고기·흰살생선 탕이 외식 요리 중 칼로리 대비 단백질이 가장
  많다(탕류 100 kcal당 12.7 g, 면·덮밥류 3.4~3.6 g). 밥은 따로 기록하고 공기밥 양이 칼로리를
  좌우한다. 감자탕·곰탕·꼬리곰탕은 지방이 많아 단백질은 많지만 가볍지는 않다.
- 면 요리는 한 그릇 약 640 kcal에 단백질이 적고, 절반 이상이 나트륨 2,000 mg 이상이었다. 고른다면
  달걀·두부 같은 단백질을 하나 곁들이거나 국물을 남기는 것 중 하나만 권한다. 국물을 남겨 줄어드는
  나트륨 양은 측정 자료가 없어 숫자로 말하지 않는다.
- 김밥 한 줄과 떡볶이·라볶이·튀김·순대 같은 분식은 이 창고에 측정값이 없다. 열량 숫자는 말하지
  않고, 나눠 먹기·튀김 추가 빼기·단백질 식품 곁들이기 같은 방법만 제안한다.
- 나트륨은 표시 기준 2,000 mg 대비 몇 %인지로 보여 주고, 한 끼 1,000 mg 이상이면 한 번만
  짚는다. 하루 기준선은 한국인 영양소 섭취기준의 2,300 mg이다. 한 끼로 건강 경고를 하지 않는다.
- 고혈압·심혈관·신장 질환이 있거나 혈압약을 먹는다면 개인 나트륨 목표나 저염 소금(칼륨 대체염)은
  권하지 않고 담당 의료진과 정하도록 안내한다.
- 한 끼에 방법은 하나만. 편의점이나 분식을 고른 것 자체를 문제 삼지 않는다. 회식은 080 규칙을 따른다.
