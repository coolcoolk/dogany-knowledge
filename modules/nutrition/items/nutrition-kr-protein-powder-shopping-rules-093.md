---
# Authored 2026-10-07. KR-LOCALE
# engine-readable synthesis for the shopping module when it shows protein
# powder (단백질 보충제) candidates and when it times a rebuy. The evidence is
# in 092 (source, label accuracy, seals, lactose); the daily target is 062 /
# 063; whole-food and convenience alternatives are 030. This row adds only
# the Korean labelling regime (건강기능식품 vs 기능성 표시 일반식품 vs plain
# 일반식품; the 80 percent protein tolerance), the price-per-20 g-protein
# arithmetic, the label-plausibility checks, and rebuy timing.
#
# Read 2026-10-07: MFDS 「한눈에 보는 영양표시 가이드라인」 (민원인 안내서
# 0997-04, 2024-12) at source for the tolerance, the protein daily value and
# the 강조표시 criteria; the KCA 2023 report at source (16 products, prices);
# MFDS card news 2026-05-20 and the RDA webzine 2025-10 for the three
# labelling classes; news reports for the 2020-12 기능성 표시 일반식품 regime
# and for MFDS 2023 해외직구 testing. The 건강기능식품 공전 protein monograph
# itself (daily intake, claim wording) was NOT read at source; the amino
# acid score 85 criterion is carried as stated by KCA 2023.
#
# protein_powder_rules, product_fields and rebuy are structured data for the
# shopping module; field shape follows 080 (rule, surface, trigger, action,
# never, constants, basis, basis_grade, kind). Every constant is a product
# constant unless its basis says otherwise. Prices are a 2023-02 snapshot
# and are never shown as current; the module computes from the live listing.
# No program code was changed.
id: nutrition/kr-protein-powder-shopping-rules-093
domain: nutrition
lane: "@meal-craft"
grade: "D (synthesis: the protein_powder_rules as a set; each rule carries its own basis_grade); A (definitional: MFDS labelling tolerance, actual protein at least 80 percent of label; protein daily value 55 g; the price and days-of-supply arithmetic); C (Korean shelf data: KCA 2023 test of 8 powders and 8 drinks, prices of February 2023); D (rebuy lead times and switching margin, product constants)"
locale: KR
as_of: 2010-2026
contested: no
sources:
  - "https://business.jangseong.go.kr/file/wsboard/data/www_notice/1742287310.pdf"  # 식품의약품안전처, 한눈에 보는 영양표시 가이드라인 (민원인 안내서, 등록번호 안내서-0997-04, 2024-12), a municipal re-post of the MFDS guidance PDF, read 2026-10-07: tolerance -- calories, sodium, sugars, fat, trans fat, saturated fat, cholesterol actual value under 120 percent of label; carbohydrate, fibre, protein, vitamins, minerals actual value at least 80 percent of label (식품등의 표시기준 별지1 1.아.4)); protein shown to the nearest 1 g, under 0.5 g as 0; daily value protein 55 g; 단백질 함유(급원) at 10 percent DV per 100 g, 5 percent per 100 mL, 5 percent per 100 kcal or 10 percent per reference serving, 고(풍부) twice that
  - "https://www.kca.go.kr/webzine/board/view?menuId=MENU00307&linkId=599&div=kca_2310"  # 한국소비자원 소비자시대 2023-10, 단백질 보충 일반식품 16개 제품 시험, read at source 2026-10-07: price per g of measured protein, powders 32 (NS포대유청 WPC, 2 kg), 33 (뉴욕웨이 WPC, 2 kg), 68 and 72 (two isolate brands, ~1-1.9 kg), 102, 102, 132, 166 won; drinks 93-375 won; prices bought 2023-02 and confirmed with sellers; the quoted health-functional-food criterion is amino acid score 85 or more; 14 of 16 general-food products met it; tolerance quoted as 식약처 고시 제2022-86호
  - "https://mfds.go.kr/brd/m_768/view.do?seq=3693"  # MFDS 카드뉴스 건강기능식품 이야기 (2026-05-20), read 2026-10-07: three classes -- general food (no function claim), 기능성 표시 일반식품 ('~기능성에 도움을 줄 수 있다고 알려진 ~가 들어 있음' plus '건강기능식품이 아님'), 건강기능식품 ('~에 도움을 줄 수 있음', mark or the words 건강기능식품); 고시형 and 개별인정형 ingredients
  - "https://rda.go.kr/webzine/2025/10/sub_20.html"  # 농촌진흥청 webzine 2025-10, 건강기능식품 vs 기능성 표시식품, read 2026-10-07: same three-way distinction; neither may claim to treat disease
  - "https://mobile.newsis.com/view/NISX20201228_0001285986"  # 뉴시스 2020-12-28, MFDS 일반식품 기능성 표시제 시행 2020-12-29: functional ingredient from a GMP maker, product from a HACCP plant, 6-monthly content testing, the not-a-health-functional-food warning on the main panel; tablets and capsules excluded. News report; the 고시 text was not read
  - "https://www.segye.com/newsView/20240605506894"  # 세계일보 2024-06-05, MFDS 2023 testing of 1,600 해외직구 foods marketed for an effect: 281 (17.6 percent) with hazardous ingredients; muscle-building products mainly anabolic steroids (15) and SARMs (2); MFDS says direct-purchase food safety cannot be guaranteed. Protein powders were not singled out. News report
  - "source:nutrition/protein-powder-type-label-evidence-092 -- source equivalence, label accuracy, seals, lactose and lead; every evidence claim here routes there"
  - "source:nutrition/protein-deficit-lean-mass-target-062 -- the daily floor that decides whether a powder is needed at all"
  - "source:nutrition/meal-protein-nudge-rules-063 -- per-meal dose and the renal gate, reused here"
  - "source:nutrition/protein-per-meal-ceiling-008 -- why a 40-60 g serving is not better than 20-30 g"
  - "source:nutrition/kr-convenience-protein-options-030 -- whole-food comparators on the Korean shelf"
  - "source:nutrition/metabolizable-energy-atwater-015 -- a shake is food and is logged as energy"
  - "source:spending-saving item 082 (module not published) -- the return window for an online order that arrives wrong"
  - "source:skincare-hygiene item 085 (module not published) -- sibling shopping-module rule set; same claim-tier discipline"
applicability:
  axes:
    - key: dietary_pattern
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: allergen_list
      type: categorical
      role: hard
      unknown_policy: hedge
    - key: renal_condition
      type: categorical
      role: hard
      unknown_policy: hedge
      gate:
        allowed: [none, healthy]
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: hedge
protein_powder_rules:
  - rule: need-before-product
    surface: shopping
    trigger: user asks which protein powder to buy, or the module is about to show powder candidates
    action: first check the logged daily protein against the user's floor (062/063); if the floor is usually met from food, say a powder is optional convenience, then still show candidates if asked
    never: [a powder as required for gains, "보충제 안 먹으면 근손실"]
    constants: none
    basis: nutrition/protein-deficit-lean-mass-target-062; nutrition/pre-sleep-protein-matched-trials-091 (no bonus on a met day)
    basis_grade: B
    kind: gate
  - rule: renal-and-allergen-gate
    surface: shopping
    trigger: renal_condition stated and not none or healthy, or allergen_list contains milk or soy
    action: renal -- show no powder candidates and route to a clinician (same as 063 renal-gate); milk allergy -- exclude every whey, casein, milk-protein and 산양유 product (WPI is not milk-free); soy allergy -- exclude soy and blends listing 대두, and read the allergen box (KCA found undeclared soy in a WPC)
    never: [WPI offered to a milk-allergic user as lactose-free so fine]
    constants: none
    basis: nutrition/meal-protein-nudge-rules-063; nutrition/protein-powder-type-label-evidence-092 (allergy vs intolerance; KCA 2023 undeclared soy)
    basis_grade: A
    kind: gate
  - rule: compare-per-20g-protein
    surface: shopping
    trigger: two or more powder candidates are shown
    action: compute won_per_20g_protein = price / (servings_per_container x protein_g_per_serving) x 20 and rank on it; never rank on price per container or per scoop, because Korean serving sizes run 30-60 g
    never: [a ranking by price per kg of powder, price per 1회 섭취량 as the headline]
    constants: 20 g reference dose (product constant, sits in 063's per-meal band for most adults); servings_per_container = net_g / serving_g when the label gives none
    basis: KCA 2023 (serving 30-60 g, 1-3 servings a day; price per g protein 32-375 won)
    basis_grade: A
    kind: computation
  - rule: price-reference-band
    surface: shopping
    trigger: user asks whether a powder is expensive
    action: compare its won_per_20g_protein with the live candidate set; the KCA 2023 snapshot may be quoted only as a dated reference (2023-02 prices -- bulk WPC about 640-660 won per 20 g protein, branded isolate about 1,360-1,440, other powders up to about 3,300, ready-to-drink 1,860-7,500)
    never: [the 2023 figures shown as today's price]
    constants: snapshot date 2023-02
    basis: KCA 2023 price table (won per g x 20)
    basis_grade: C
    kind: reference
  - rule: type-by-gut-and-diet
    surface: shopping
    trigger: user asks WPC vs WPI vs plant (식물성, 완두, 대두, 혼합)
    action: say they build muscle alike at adequate daily protein; default to the cheapest per 20 g that the user tolerates; WPI only when concentrate causes gut symptoms or lactose matters; plant or blend for vegan, milk-allergic or dairy-avoiding users, preferring soy or a pea-rice blend over a single low-score plant protein
    never: [WPI described as faster-absorbing and so better for muscle, plant protein called inferior for a user who meets the daily total]
    constants: none
    basis: nutrition/protein-powder-type-label-evidence-092 (Messina 2018, Lim 2021, Mathai 2017, KCA amino acid score 45 for an almond drink)
    basis_grade: B
    kind: convention
  - rule: lactose-first-move
    surface: shopping
    trigger: user reports bloating, gas or loose stool after a shake, or says 유당불내증
    action: first suggest mixing with water instead of milk (250 mL milk adds about 11 g lactose against 1-3 g in a WPC scoop), then a WPI or lactose-free product; only then plant
    never: [a diagnosis, "유청은 몸에 안 맞는 사람"]
    constants: EFSA 12 g single-dose tolerance (panel opinion); scoop and milk lactose from 092
    basis: nutrition/protein-powder-type-label-evidence-092 (ADPI WPC 80 lactose 4-10 percent, EFSA 2010, Park 2016 ratio)
    basis_grade: B
    kind: convention
  - rule: label-plausibility
    surface: shopping
    trigger: a candidate's label protein per serving is known with its serving weight
    action: compute protein_ratio = protein_g_per_serving / serving_g; flag "label protein looks higher than the ingredient allows" when the ratio exceeds 0.90 for any whey product or 0.82 for a product sold as WPC or 농축유청; flag "free amino acids may count toward protein" when glycine, taurine, glutamine, arginine or creatine sit among the first five ingredients of a product with a protein headline
    never: [an accusation of fraud, a brand named as cheating]
    constants: 0.90 and 0.82 ceilings from the ADPI WPI and WPC 80 typical protein (dry basis, before moisture and flavouring, so real products sit lower); first-five window (product constant)
    basis: ADPI standards (092); Philips 2024 and Informed Protein (amino spiking, 092)
    basis_grade: C
    kind: check
  - rule: expect-80-percent
    surface: shopping
    trigger: the module states how much protein a serving gives, or the user counts a scoop in their log
    action: log the label value (it is the legal declaration), but in a shopping comparison note that a compliant product may hold 80 percent of it; never treat two products within 20 percent of each other on label protein as clearly different
    never: [label protein described as a guaranteed amount]
    constants: 0.80 tolerance (MFDS 식품등의 표시기준, legal)
    basis: MFDS 한눈에 보는 영양표시 가이드라인 2024-12
    basis_grade: A
    kind: computation
  - rule: hff-mark-is-not-a-rank
    surface: shopping
    trigger: a candidate carries the 건강기능식품 mark or words, or the user asks whether a 건강기능식품 powder is better
    action: say the mark means a regulated ingredient monograph (amino acid score 85 or more, GMP manufacture) and a permitted claim, not more muscle per 20 g; most whey general foods meet the same score (14 of 16 in KCA 2023); rank 건강기능식품 and 일반식품 on the same price-per-20 g basis
    never: [건강기능식품 described as proven for muscle, a general food penalised for lacking the mark]
    constants: amino acid score 85 (as stated by KCA 2023)
    basis: KCA 2023; MFDS card news 2026-05-20
    basis_grade: C
    kind: convention
  - rule: claim-class-read
    surface: shopping
    trigger: a listing or label makes a function claim (근육, 근력, 체지방, 면역 etc.)
    action: classify -- '~에 도움을 줄 수 있음' with the mark is a 건강기능식품 claim; '~에 도움을 줄 수 있다고 알려진 ~가 들어 있음' with '건강기능식품이 아님' is a 기능성 표시 일반식품 (the claim is about the ingredient, not the product); a function claim on a plain general food with neither is not a lawful Korean claim and is shown as unverified seller text
    never: [repeating a seller's muscle or fat-loss claim as fact]
    constants: none
    basis: MFDS card news 2026-05-20; RDA webzine 2025-10; 뉴시스 2020-12-28
    basis_grade: A
    kind: check
  - rule: seal-scope
    surface: shopping
    trigger: a candidate shows Informed Sport, Informed Choice, NSF Certified for Sport or a similar seal, or the user is a drug-tested athlete
    action: say a banned-substance seal lowers doping-contamination risk batch by batch and matters most for tested athletes; it does not verify protein content unless the scheme says so (Informed Protein does); for tested athletes prefer sealed products
    never: [a seal described as proof of label protein or of quality]
    constants: none
    basis: nutrition/protein-powder-type-label-evidence-092 (programme pages; Geyer 2004)
    basis_grade: D
    kind: convention
  - rule: overseas-direct-purchase
    surface: shopping
    trigger: candidate is a 해외직구 listing, or the product adds anything beyond protein (테스토, 부스터, fat burner, 근육 강화 블렌드)
    action: plain protein from a known maker is low risk; products marketed for muscle or hormones are where MFDS found steroids and SARMs, so show them without a recommendation and point to the 식품안전나라 해외직구 위해식품 list; a direct purchase also carries no Korean label-tolerance check
    never: [a recommendation of a booster or anabolic blend]
    constants: none
    basis: MFDS 2023 해외직구 testing (세계일보 2024-06-05); Geyer 2004
    basis_grade: C
    kind: gate
  - rule: plant-lead-cap
    surface: shopping
    trigger: user takes a plant or mass-gainer powder two or more servings a day, or asks about heavy metals
    action: say plant powders tend to carry more lead than whey and that modelled risk at one to three servings stayed below hazard thresholds; suggest one plant serving a day with the rest from food or a dairy powder where diet allows; no alarm language
    never: [a named brand called toxic, a heavy-metal danger headline]
    constants: one plant serving a day (product constant)
    basis: nutrition/protein-powder-type-label-evidence-092 (Bandara 2020, CR 2025)
    basis_grade: C
    kind: convention
  - rule: drink-vs-powder
    surface: shopping
    trigger: user compares 단백질 음료 (RTD) with powder
    action: show both per 20 g protein; drinks cost about 3 to 12 times the cheapest powder per gram of protein in the 2023 snapshot and some carry only 4-12 g protein, and sugars reached 20.9 g in one; offer a drink as a convenience line, not a value one
    never: [a low-protein drink counted as a protein serving]
    constants: none
    basis: KCA 2023
    basis_grade: C
    kind: reference
product_fields:
  - field: protein g per serving and serving g
    verifiable: label (legal declaration, 80 percent tolerance)
    use: compute won_per_20g_protein and protein_ratio
    basis: MFDS tolerance; ADPI ceilings (092)
  - field: net weight and price
    verifiable: full
    use: price per 20 g protein; days of supply
    basis: arithmetic
  - field: 식품유형 and the 건강기능식품 mark or the 건강기능식품이 아님 line
    verifiable: full
    use: claim-class-read; never a quality rank
    basis: MFDS card news 2026-05-20
  - field: protein source on the ingredient list (농축유청단백, 분리유청단백, 분리대두단백, 완두단백, 혼합)
    verifiable: full
    use: type-by-gut-and-diet; allergen gate; WPC ceiling check
    basis: 092
  - field: allergen box (우유, 대두, 밀 etc.)
    verifiable: label (one KCA product missed soy)
    use: hard exclude for listed allergens
    basis: KCA 2023
  - field: sugars g per serving
    verifiable: label (120 percent tolerance)
    use: tie-break for a user in a cut; the KCA range was 0.2-8.6 g for powders
    basis: KCA 2023
  - field: third-party seal
    verifiable: check on the scheme's own database
    use: seal-scope
    basis: 092
  - field: 소비기한 or 유통기한 of the lot sold
    verifiable: often seller-stated online
    use: rebuy max-quantity check
    basis: product constant
  - field: marketing lines such as 단백질 함량 1위, 흡수율, 근육 생성
    verifiable: none
    use: ignored for ranking
    basis: claim-class-read
rebuy:
  - field: days_of_supply
    formula: floor(net_g / (serving_g x servings_per_day))
    example: 2,000 g at 30 g once a day lasts 66 days; at twice a day 33 days
    basis_grade: A (arithmetic)
  - field: servings_per_day
    formula: the user's logged shake frequency over the last 14 days; if fewer than 7 logged days, ask once or use the label's 1회 섭취량 x 1
    example: none
    basis_grade: D (product constant)
  - field: reorder_point
    formula: remind when days_left <= lead_days + 7, lead_days 3 for domestic online, 14 for 해외직구
    example: domestic 2 kg at once a day, remind on day 56
    basis_grade: D (product constant)
  - field: max_units
    formula: buy no more containers than floor(days_to_best_before / days_of_supply); a bulk discount past that is not a saving
    example: 소비기한 300 days away and 66 days per tub, at most 4 tubs
    basis_grade: D (product constant)
  - field: switch_margin
    formula: on rebuy keep the current product unless a candidate passing every gate is at least 15 percent cheaper per 20 g protein, or the user reported gut symptoms or taste fatigue
    example: current 900 won per 20 g, switch only below 765 won
    basis_grade: D (product constant; a habit margin, not a precision claim)
  - field: stop_rebuy_prompt
    formula: if logged food protein met the floor on at least 5 of the last 7 days without the shake, say so once at the reorder point and let the user decide
    example: none
    basis_grade: C (091 no-bonus-on-a-met-day)
refraction_notes:
  - note: >
      THE PRICE BAND IS OLD AND SMALL. The only official Korean price data is
      the KCA purchase of February 2023, eight powders and eight drinks, with
      price computed on measured, not label, protein. It shows the spread
      (about tenfold) and the order (bulk WPC cheapest, drinks dearest); it
      does not give today's price of any product.
    grade: C
  - note: >
      THE 80 PERCENT LINE IS THE LAW, NOT THE MARKET. A compliant product
      may hold 80 percent of its label; how many sit near that floor is
      unknown. One of eight KCA powders sat far below it. The rules
      therefore treat label protein as a declaration to log and a ceiling to
      compare, not as a measured amount.
    grade: A
  - note: >
      THE PLAUSIBILITY CEILINGS ARE GENEROUS. ADPI typical protein is on a
      dry basis; a finished powder with moisture, flavour and sweetener sits
      lower, so a whey product declaring 27 g in a 30 g scoop (0.90) is
      already at the edge. The flag is a prompt to look, not a finding.
    grade: C
  - note: >
      THE HEALTH-FUNCTIONAL-FOOD MONOGRAPH WAS NOT READ. The amino acid score
      criterion is as KCA states it; the daily-intake figure and the exact
      permitted protein claim wording in the 건강기능식품 공전 were not read
      at source, so no rule quotes them.
    grade: D
claim: >
  On the Korean shelf most protein powders are general foods (일반식품); a few
  are 건강기능식품, whose protein monograph requires an amino acid score of 85
  or more, a bar most whey general foods also clear (14 of 16 in the 2023 KCA
  test). The mark is a regulatory class, not more muscle per gram. Korean
  labelling allows actual protein down to 80 percent of the declared value,
  and serving sizes run from 30 to 60 g, so the comparable unit is price per
  20 g of protein: in KCA's February 2023 purchase it ran from about 640 won
  for bulk WPC to about 7,500 won for a protein drink. Choose the cheapest per
  20 g that the user's gut and diet tolerate (092: whey, soy and pea build
  alike at adequate intake), check that label protein is physically
  plausible, read function claims by their Korean class, treat
  banned-substance seals as doping protection only, and time a rebuy from
  days of supply, delivery lead time and the best-before date rather than
  from bulk discounts.
reasoning: >
  The tolerance, daily value, claim classes and the arithmetic are
  definitional and earn the top band row by row. The price band and label
  failure rate rest on one small Korean government test from 2023, held in
  the observational band and always dated. The type, lactose and lead rules
  route to 092's evidence. The reorder buffer, the switching margin, the
  first-five-ingredient window and the one-plant-serving cap are product
  constants chosen for a quiet shopping module, labelled as such, and they
  carry the practitioner band. The set as a whole is a synthesis, so the
  item's lead letter is the synthesis band.
---

# nutrition/kr-protein-powder-shopping-rules-093

Buying protein powder in Korea comes down to one number and a few checks. The
number is price per 20 g of protein, because one product's scoop is 30 g and
another's is 60 g, and a per-tub or per-scoop price hides that. In the Korea
Consumer Agency's 2023 purchase the spread was about tenfold, from roughly 640
won per 20 g for a bulk concentrate to several thousand won for a protein
drink.

The checks are about what the label can and cannot promise. Korean rules let
the real protein run 20 percent under the label, so two products within a
fifth of each other are not clearly different. A whey label claiming more
protein per scoop than whey isolate itself contains deserves a second look, as
does a protein headline sitting on top of cheap free amino acids. The
건강기능식품 mark means a regulated ingredient and a permitted claim, not a
better powder for muscle, and most plain whey products meet the same quality
score. A muscle or fat-loss claim on a product with neither the mark nor the
"건강기능식품이 아님" line is not a lawful Korean claim.

Type follows the gut and the diet: the cheapest powder the user tolerates,
isolate or water instead of milk when lactose bites, soy or a blend when dairy
is out. Rebuying is arithmetic: days of supply from the tub size and the
user's real shake habit, a reminder a week plus delivery time before it runs
out, no more tubs than will be used before the best-before date, and no
switching for small savings.

## Engine rules (shopping module)

| Rule | When | Effect | Basis band |
|---|---|---|---|
| need-before-product | asks what to buy | check the daily floor first; powder optional if met | randomised |
| renal-and-allergen-gate | renal, milk or soy allergy | no candidates or exclude by allergen | definitional |
| compare-per-20g-protein | two or more candidates | rank on won per 20 g protein | definitional |
| price-reference-band | asks if expensive | compare live; 2023 snapshot dated only | observational |
| type-by-gut-and-diet | WPC vs WPI vs plant | cheapest tolerated; alike at adequate intake | randomised |
| lactose-first-move | gut symptoms | water before milk, then WPI | panel opinion |
| label-plausibility | label known | flag above 0.90 (whey) or 0.82 (WPC); amino acids in top five | observational |
| expect-80-percent | protein compared | label may be 20 percent high, legally | definitional |
| hff-mark-is-not-a-rank | 건강기능식품 mark | regulatory class, same ranking basis | observational |
| claim-class-read | function claim | classify by Korean claim class | definitional |
| seal-scope | seal shown or tested athlete | doping protection, not protein check | practitioner |
| overseas-direct-purchase | 직구 or booster blend | no recommendation for muscle or hormone blends | observational |
| plant-lead-cap | 2+ plant servings | one plant serving a day, no alarm | observational |
| drink-vs-powder | RTD vs powder | drinks are convenience, not value | observational |

## Rebuy timing

| Field | Formula | Example |
|---|---|---|
| days_of_supply | net g / (serving g x servings a day) | 2 kg, 30 g once a day = 66 days |
| reorder_point | days left at or under lead + 7 | domestic: remind on day 56 |
| max_units | days to best-before / days of supply | 300 days, 66 per tub = 4 tubs |
| switch_margin | 15 percent cheaper per 20 g, or gut or taste | 900 won -> switch below 765 |
| stop_rebuy_prompt | food met the floor 5 of 7 days | say once, user decides |

## 한국어 요약 (답변용)

- 먼저 필요부터 본다. 음식으로 하루 단백질 목표를 대체로 채우고 있으면 보충제는 편의용 선택지다.
  신장 질환이 있으면 보충제를 권하지 않고 의료진에게 연결한다. 우유 알레르기면 WPI도 안 된다.
- 비교 단위는 "단백질 20 g당 가격"이다. 제품마다 1회 섭취량이 30-60 g으로 달라서 통 가격이나
  스쿱 가격으로는 비교가 안 된다. 계산: 가격 ÷ (총 섭취횟수 × 1회 단백질 g) × 20.
- 참고로 한국소비자원 2023년 2월 구입가 기준 단백질 20 g당 대용량 WPC 약 640-660원, 아이솔레이트
  브랜드 약 1,360-1,440원, 단백질 음료 약 1,860-7,500원이었다. 지금 가격이 아니니 날짜와 함께만 말한다.
- 표시 단백질은 법적으로 80%까지 허용된다. 표시량 차이가 20% 안쪽인 두 제품은 확실히 다르다고 말하지
  않는다. 유청 제품이 스쿱 무게의 90%(WPC는 82%)를 넘는 단백질을 표시하면 "원료가 낼 수 있는 양보다
  높아 보인다"고 표시한다. 원재료 앞쪽 5개 안에 글리신·타우린·글루타민·아르기닌·크레아틴이 있으면
  유리 아미노산이 단백질 수치에 섞였을 수 있다고 알린다. 특정 브랜드를 사기라고 하지 않는다.
- 건강기능식품 마크는 원료 기준(아미노산 스코어 85 이상 등)과 허용된 표현을 뜻할 뿐, 근육에 더 좋다는
  뜻이 아니다. 일반식품 유청 제품도 대부분 같은 기준을 넘는다(2023년 16개 중 14개). "건강기능식품이
  아닙니다" 문구가 있으면 원료에 대한 이야기이고, 마크도 그 문구도 없이 근육·체지방 효능을 말하면
  판매자 문구로만 보여준다.
- 종류는 속 편함과 식단으로 고른다. 견딜 수 있는 것 중 20 g당 가장 싼 것. 배가 불편하면 우유 대신
  물, 그다음 WPI. 비건이거나 유제품을 피하면 대두나 완두·쌀 혼합. 식물성 분말은 납이 더 많은 경향이
  있어 하루 1회 정도를 권하되 겁주지 않는다.
- Informed Sport·NSF 같은 인증은 도핑 금지물질 방지용이다. 도핑 검사를 받는 선수라면 인증 제품을
  고르고, 단백질 함량 보증으로 말하지는 않는다. 해외직구 "근육 강화·테스토 부스터" 제품은 식약처 검사에서
  스테로이드가 나온 범주라 권하지 않는다.
- 재구매: 남은 일수 = 총 중량 ÷ (1회 g × 하루 횟수). 남은 일수가 배송일 + 7일 이하가 되면 알린다
  (국내 3일, 직구 14일). 소비기한 안에 다 먹을 만큼만 산다. 20 g당 15% 이상 싸지 않으면 바꾸라고 하지
  않는다. 최근 7일 중 5일 이상 음식만으로 목표를 채웠다면 재구매 시점에 한 번만 알려주고 결정은
  사용자에게 맡긴다.
