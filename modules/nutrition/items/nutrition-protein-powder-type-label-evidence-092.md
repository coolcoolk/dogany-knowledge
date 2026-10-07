---
# Authored 2026-10-07. Evidence
# row behind the protein-powder shopping rules (093). It answers four
# questions a buyer meets: does the protein source (whey concentrate, whey
# isolate, soy or pea, blends) change what training produces; how far a
# label's protein figure can be trusted; what third-party seals do and do
# not test; and how much lactose a scoop carries against the dose people
# with lactose malabsorption tolerate. The Korean labelling regime and the
# price arithmetic live in 093; this row stays locale-neutral except for the
# one Korean product test (KCA 2023), which is the only measured
# label-vs-content data for products on the Korean shelf.
#
# Read 2026-10-07: abstracts on PubMed (Messina 2018, Lim 2021, Hevia-Larrain
# 2021, Babault 2015, Mathai 2017, Bandara 2020, Philips 2024, Geyer 2004,
# Park 2016, Oh 2022); the ADPI WPC and WPI standards (v4.0, 2023) at source;
# EFSA 2010 lactose opinion at its abstract page; the KCA 2023 test report at
# its own webzine page (full tables); Consumer Reports 2025 through two news
# reports; NSF, Informed Sport and Informed Protein through their own pages.
# No full text of any trial was read. Storhaug 2017 (global lactose
# malabsorption prevalence, Lancet Gastroenterol Hepatol) was located but is
# RETRACTED (2025) and is not used.
#
# powder_evidence is a structured ledger for 093 (claim, best_source,
# shown, not_shown, band). Plain text; nothing computes from it.
id: nutrition/protein-powder-type-label-evidence-092
domain: nutrition
lane: "@obs-inferential"
grade: "C (the ledger as a whole); B (protein source: soy or pea vs whey gives similar strength and lean-mass gains when total protein is adequate, meta-analysis of 9 trials and a 16-trial meta-analysis with a small animal-protein edge in percent lean mass under age 50); A (definitional: ADPI composition standards for WPC 80 and WPI); C (label accuracy: one Korean government test of 16 products, one self-funded Indian test, industry reports of amino spiking); B (lactose: EFSA opinion that most people with lactose maldigestion tolerate 12 g in one dose); D (third-party seals: programme self-descriptions)"
locale: universal
as_of: 2004-2025
contested: no
sources:
  - "https://doi.org/10.1123/ijsnem.2018-0071"  # Messina M, Lynch H, Dickinson JM, Reed KE. Int J Sport Nutr Exerc Metab 2018;28(6):674-685. PMID 29722584 -- meta-analysis, 9 trials, 266 participants, resistance training of 6 weeks or more; 5 trials whey vs soy, 4 soy vs beef, milk or dairy protein; strength rose with both, no between-group difference (bench P=.90, squat P=.64); lean body mass no difference (P=.96 whey vs soy; P=.80 soy vs other). Abstract read
  - "https://doi.org/10.3390/nu13020661"  # Lim MT, Pan BJ, Toh DWK, Sutanto CN, Kim JE. Nutrients 2021;13(2):661. PMID 33670701 -- systematic review of 18 RCTs, 16 meta-analysed; protein source did not change absolute lean mass or strength; animal protein favoured for percent lean mass, and in adults under 50 for absolute lean mass (+0.41 kg, 95% CI 0.08 to 0.74); total protein generally above the RDA. Abstract read
  - "https://doi.org/10.1007/s40279-021-01434-9"  # Hevia-Larrain V, Gualano B, Longobardi I, et al. Sports Med 2021;51(6):1317-1330. PMID 33599941, NCT03907059 -- 19 habitual vegan vs 19 omnivore untrained young men, 12 weeks twice-weekly training, protein topped up to 1.6 g/kg/day with soy isolate (vegan) or whey (omnivore); leg lean mass +1.2 kg in both, muscle and fibre area and leg-press 1RM no between-group difference. Abstract read
  - "https://doi.org/10.1186/s12970-014-0064-5"  # Babault N, Paizis C, Deley G, et al. J Int Soc Sports Nutr 2015;12(1):3. PMID 25628520, NCT02128516 -- 161 men 18-35, 12 weeks upper-limb training, 25 g pea vs 25 g whey vs placebo twice daily; biceps thickness rose over time, pea vs whey no difference, strength no group difference. Funded and co-authored by the pea-protein maker (Roquette). Abstract read
  - "https://doi.org/10.1017/S0007114517000125"  # Mathai JK, Liu Y, Stein HH. Br J Nutr 2017;117(4):490-499. PMID 28382889 -- DIAAS in pigs: ileal digestibility of most indispensable amino acids higher in WPI, WPC and milk protein concentrate than in pea protein concentrate, soy isolate or soy flour; PDCAAS-like values overestimate plant-protein quality. Abstract read; the per-protein DIAAS numbers were not read and are not carried
  - "https://adpi.org/wp-content/uploads/2023/07/WPC-Standard-v4.0_2023.pdf"  # American Dairy Products Institute, Whey Protein Concentrate Standard v4.0 (effective 2023-07-04), read at source 2026-10-07: WPC 80 protein 80.0-82.0 percent typical (79.5 minimum, dry basis), lactose 4.0-10.0 percent, fat 4.0-8.0 percent, moisture 3.5-5.0 percent; WPC 34 lactose 48.0-55.0 percent
  - "https://www.adpi.org/wp-content/uploads/2023/07/WPI-Standard-v4.0_2023.pdf"  # ADPI Whey Protein Isolate Standard v4.0 (effective 2023-07-04), read at source 2026-10-07: at least 90 percent protein dry basis (89.5 minimum), typical 90.0-92.0; lactose 0.5-1.0 percent; fat 0.5-1.0 (1.5 maximum); moisture 4.0-5.0 (6.0 maximum); protein by AOAC 991.20 (N x 6.38), i.e. a nitrogen method
  - "https://www.efsa.europa.eu/efsajournal/pub/1777"  # EFSA NDA Panel. Scientific Opinion on lactose thresholds in lactose intolerance and galactosaemia. EFSA J 2010;8(9):1777. doi:10.2903/j.efsa.2010.1777 -- most people with lactose maldigestion tolerate up to 12 g lactose in a single dose with no or minor symptoms, more if spread over the day; no single threshold fits everyone and some report symptoms under 6 g. Abstract page read
  - "https://doi.org/10.4166/kjg.2016.67.1.22"  # Park SH, Chang YW, Kim SJ, et al. Korean J Gastroenterol 2016;67(1):22-27. PMID 26809628 -- 35 Korean adults with milk-related symptoms; breath test with 550 mL milk (25 g lactose) positive in 31; lactose-free milk cut symptoms and hydrogen. Abstract read. Symptomatic recruits, not a prevalence sample; carried for the 25 g per 550 mL milk ratio and the Korean context only
  - "https://doi.org/10.1089/jmf.2022.K.0010"  # Oh CH, Kim JW, Park YM, et al. J Med Food 2022;25(10):1003-1010. PMID 36179067 -- Korean adults suspected of lactose intolerance; 570 mL chocolate milk (20 g lactose) breath test; 28 confirmed; flavoured lactose-free milk cut symptom score 4.18 to 0.61. Abstract read
  - "https://www.kca.go.kr/webzine/board/view?menuId=MENU00307&linkId=599&div=kca_2310"  # 한국소비자원 (Korea Consumer Agency) 소비자시대 2023-10, 단백질 보충 일반식품 16개 제품 시험 (8 powders, 8 drinks; bought 2023-02), read at source 2026-10-07: protein 4-29 g per serving; powder serving 30-60 g, 1-3 servings a day, 12-63 g protein a day at the label maximum; amino acid score 45-141, 14 of 16 at or above 85 (the health-functional-food criterion); no foreign matter, microbes or preservatives, aflatoxin M1, lead, cadmium within applicable limits; one WPC powder had undeclared soy and net weight 1,952 g vs 2,000 g; one WPI powder declared 45 g protein and measured 13 g (28 percent), fat 367 percent and sugars 550 percent of label; price per g protein 32-166 won for powders, 93-375 won for drinks
  - "https://doi.org/10.1097/MD.0000000000037724"  # Philips CA, Theruvath AH, Ravindran R, Chopra P. Medicine (Baltimore) 2024;103(14):e37724. PMID 38579036 -- self-funded analysis of 36 popular protein supplements sold in India: most did not meet the labelled protein, some exceeded it (suspected amino spiking); fungal toxins and pesticide residues in major brands; lead and arsenic detected; hepatotoxic herbal additives in some. Abstract read; the per-product numbers were seen only in press reports and are not carried
  - "https://doi.org/10.1016/j.toxrep.2020.08.001"  # Bandara SB, Towle KM, Monnot AD. Toxicol Rep 2020;7:1255-1262. PMID 33005567 -- risk assessment of published heavy-metal concentrations in protein powders at one or three servings a day: hazard index under 1 for every product, highest (near 1) in mass gainers and lowest in whey; modelled adult blood lead under 5 ug/dL, driven by background exposure. Consultancy authors, no declared conflict. Abstract read
  - "https://www.kpbs.org/news/health/2025/10/16/a-study-found-lead-in-popular-protein-powders-heres-why-you-shouldnt-panic"  # Consumer Reports, lead in 23 protein powders and shakes (2025-10), read through this news report 2026-10-07: over two-thirds above CR's 0.5 ug/day level (California Prop 65 MADL) in one serving; plant-based powders averaged about nine times dairy and twice beef; highest 7.7 and 6.3 ug per serving; FDA interim reference levels 2.2 ug/day (children) and 8.8 ug/day (women of childbearing age). The CR report itself was not read
  - "https://doi.org/10.1055/s-2004-819955"  # Geyer H, Parr MK, Mareck U, et al. Int J Sports Med 2004;25(2):124-129. PMID 14986195 -- 634 non-hormonal supplements from 13 countries (2000-2001): 94 (14.8 percent) contained undeclared anabolic-androgenic steroids; 21.1 percent from prohormone-selling companies vs 9.6 percent from others. Mixed supplement categories, not protein powders alone; old market. Abstract read
  - "https://sport.wetestyoutrust.com/"  # Informed Sport (LGC), read 2026-10-07: every batch tested for banned substances before release; the programme does not state that it verifies protein content
  - "https://protein.wetestyoutrust.com/"  # Informed Protein (LGC), read 2026-10-07: independent verification of label protein, free amino acid testing for amino spiking, targeted adulterant screen, facility audit
  - "https://www.nsfsport.com/"  # NSF Certified for Sport, read 2026-10-07: tested for 280+ banned substances; quality and purity testing; detail of label-claim verification not read on this page
  - "source:nutrition/protein-deficit-lean-mass-target-062 -- the daily total a powder exists to help reach"
  - "source:nutrition/protein-per-meal-ceiling-008 -- per-dose ceiling, so a bigger scoop is not a better scoop"
  - "source:nutrition/kr-convenience-protein-options-030 -- the whole-food and convenience alternatives on the Korean shelf"
  - "source:nutrition/pre-sleep-protein-matched-trials-091 -- whey vs casein at bedtime; no casein premium"
applicability:
  axes:
    - key: dietary_pattern
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: allergen_list
      type: categorical
      role: hard
      unknown_policy: hedge
powder_evidence:
  - claim: whey vs soy or pea for strength and muscle when total protein is adequate
    best_source: Messina 2018 (9 RCTs); Lim 2021 (16 RCTs meta-analysed); Hevia-Larrain 2021; Babault 2015
    shown: no difference in strength; no difference in absolute lean mass overall; a small animal-protein edge in lean mass under age 50 (+0.41 kg)
    not_shown: a difference that matters at intakes of about 1.6 g/kg or more; any trial in Korean lifters; blends tested against whey head to head
    band: B
  - claim: whey concentrate vs isolate for training outcomes
    best_source: ADPI standards (composition); no trial comparing WPC with WPI on muscle or strength was located
    shown: WPI carries about 10 percent more protein per gram and about a tenth of the lactose and fat
    not_shown: any outcome difference; per 20 g protein the two are the same protein
    band: D
  - claim: plant protein quality per gram
    best_source: Mathai 2017; KCA 2023 (amino acid score 45 for an almond protein drink)
    shown: lower ileal digestibility of indispensable amino acids for pea and soy than for whey and milk proteins; single-plant drinks can score low
    not_shown: that the gap survives a higher dose or a pea-rice blend in training outcomes
    band: C
  - claim: label protein can be trusted
    best_source: KCA 2023 (Korean shelf, 16 products); Philips 2024 (India, 36 products)
    shown: in Korea 1 of 8 powders measured 28 percent of its declared protein; elsewhere most products in one market missed the label and some exceeded it in a way consistent with free amino acid spiking
    not_shown: a representative audit of the Korean powder market; the KCA sample was 8 powders chosen from a consumer survey
    band: C
  - claim: what a Korean label lawfully promises
    best_source: MFDS 식품등의 표시기준 (actual protein at least 80 percent of label; see 093)
    shown: a product declaring 25 g per serving is compliant at 20 g
    not_shown: how often products sit near the floor
    band: A
  - claim: heavy metals in protein powders
    best_source: Bandara 2020 risk assessment; Consumer Reports 2025 (23 products)
    shown: plant-based powders carry more lead than dairy ones; at one to three servings modelled risk stayed below EPA hazard thresholds, lowest for whey
    not_shown: Korean-market metal data beyond the KCA lead and cadmium pass; long-term exposure outcomes
    band: C
  - claim: third-party seals
    best_source: programme pages (Informed Sport, Informed Protein, NSF)
    shown: banned-substance seals test for doping agents batch by batch; only protein-specific schemes say they check protein content and free amino acids
    not_shown: any independent study of seal-holding vs non-seal products on protein accuracy
    band: D
  - claim: lactose in a scoop vs tolerance
    best_source: ADPI WPC 80 and WPI standards; EFSA 2010
    shown: 30 g of WPC 80 ingredient carries about 1.2-3.0 g lactose, 30 g of WPI about 0.15-0.3 g; most people with maldigestion tolerate 12 g at once; a 250 mL glass of milk is about 11 g (Park 2016 ratio)
    not_shown: lactose in finished flavoured products (labels rarely state it); Korean prevalence from a representative sample
    band: B
refraction_notes:
  - note: >
      SOURCE MATTERS LESS THAN TOTAL. Every training trial that kept daily
      protein adequate found soy or pea as good as whey for strength, and the
      meta-analyses agree for absolute lean mass. The one signal against
      plant protein (Lim 2021, percent lean mass, under 50) is small and
      comes from trials whose totals differed. For a lifter already near
      their floor the protein type is a taste, gut and price choice.
    grade: B
  - note: >
      THE PLANT EVIDENCE IS MOSTLY SOY. Messina 2018 is soy by design;
      Hevia-Larrain 2021 used soy isolate; the one large pea trial (Babault
      2015) was funded and co-authored by the pea-protein maker and measured
      only the biceps. Pea-only and rice-only powders rest on thinner ground,
      and their lower digestibility per gram (Mathai 2017) is one reason
      blends exist.
    grade: C
  - note: >
      THE KOREAN LABEL TEST IS SMALL AND OLD. KCA 2023 bought 8 powders in
      February 2023. One failing product in eight is a warning that failure
      happens on the Korean shelf, not an estimate of how often. The
      products, prices and the failing brand may all have changed since.
    grade: C
  - note: >
      LEAD THRESHOLDS DIFFER BY A FACTOR OF 4 TO 17. Consumer Reports judges
      against 0.5 ug a day (a California labelling level); the FDA interim
      reference levels are 2.2 ug a day for children and 8.8 ug for women of
      childbearing age. "Two-thirds exceed" and "no added risk" (Bandara 2020)
      describe overlapping data against different lines. The plant-over-dairy
      ordering is the stable part.
    grade: C
  - note: >
      LACTOSE INTOLERANCE IS NOT MILK ALLERGY. Lactose intolerance is a dose
      problem and isolate or a water mix usually solves it; milk-protein
      allergy is an immune reaction to the protein itself, and both WPC and
      WPI contain it. An allergen_list entry for milk routes away from all
      dairy powders.
    grade: A
claim: >
  For building muscle the protein source in a powder matters little once daily
  protein is adequate: soy and pea matched whey for strength and lean mass in
  training trials and two meta-analyses (Messina 2018, 9 trials; Lim 2021, 16
  trials), apart from a small animal-protein edge in lean mass under 50. Whey
  concentrate and isolate are the same protein; by standard WPC 80 is about 80
  percent protein with 4-10 percent lactose and WPI about 90 percent with 0.5-1
  percent, so a 30 g scoop of concentrate carries roughly 1-3 g lactose, well
  under the 12 g that most people with lactose maldigestion tolerate at once
  (EFSA 2010), while mixing it with a glass of milk adds about 11 g. Label
  protein is not guaranteed: Korean rules accept 80 percent of the declared
  amount, and the Korea Consumer Agency's 2023 test found one of eight powders
  at 28 percent of its label. Free amino acids can inflate nitrogen-based
  protein tests. Plant powders carry more lead than dairy ones, though modelled
  risk at normal use stayed below hazard thresholds. Banned-substance seals
  test for doping agents, not protein content.
reasoning: >
  The source question has randomised trials pooled in two independent
  meta-analyses that agree on the main outcome, which earns the higher band
  for that row; the residual animal-protein signal is noted rather than
  spoken as a rule. The composition figures are industry standards, i.e.
  definitions, and the lactose threshold is an EFSA panel opinion over
  challenge studies. Label accuracy, contamination and the seals rest on one
  Korean government test of a small sample, one self-funded foreign test,
  advocacy testing read through news reports, and programme self-description,
  which keeps the ledger as a whole in the observational band. Nothing here
  ranks brands; the ledger exists so the shopping rules (093) can say which
  label fields carry information and which do not.
---

# nutrition/protein-powder-type-label-evidence-092

Most of what a protein-powder shelf sells as a difference is not one. Soy and
pea built as much strength and muscle as whey in training trials once people
ate enough protein in total, and whey concentrate and isolate are the same
protein at different purity. Per 20 g of protein they do the same job.

What does differ is lactose, lead and trust in the label. Concentrate carries
some lactose, about 1-3 g in a scoop, which most people with lactose
intolerance handle; the bigger dose is the milk people mix it with. Isolate
carries almost none. Plant powders carry more lead than dairy ones, by about
ninefold in one 2025 test, although a risk model at normal use found no added
risk. And the label is not a promise: Korean rules allow the real protein to be
20 percent under the label, and a 2023 government test found one powder in
eight with barely a quarter of what it declared.

Seals answer a narrower question than people assume. Informed Sport and NSF
exist to keep banned substances out of athletes; only protein-specific schemes
say they check that the protein is really there.

## Evidence ledger

| Claim | Best source | Shown | Band |
|---|---|---|---|
| soy or pea vs whey | Messina 2018, Lim 2021 | same strength and absolute lean mass | randomised, pooled |
| WPC vs WPI | ADPI standards | same protein; WPI more pure, less lactose | definitional only |
| plant quality per gram | Mathai 2017, KCA 2023 | lower digestibility; single-plant drink scored 45 | observational |
| label protein | KCA 2023, Philips 2024 | one Korean powder at 28 percent of label | observational |
| heavy metals | Bandara 2020, CR 2025 | plant higher than dairy; modelled risk low | observational |
| seals | programme pages | banned-substance seals do not check protein | practitioner |
| lactose | ADPI, EFSA 2010 | scoop 1-3 g (WPC) vs 12 g tolerated | panel opinion |

## 한국어 요약 (답변용)

- 하루 단백질 총량이 충분하면 유청(웨이)·대두·완두 단백질은 근력과 근육 증가에서 차이가 없었다
  (메타분석 9건·16건). 50세 미만에서 동물성 쪽이 제지방이 약 0.4 kg 더 늘었다는 작은 신호가
  있을 뿐이다. 그래서 종류는 맛·속 편함·가격으로 고르면 된다.
- WPC와 WPI는 같은 유청 단백질이다. 규격상 WPC80은 단백질 약 80%·유당 4-10%, WPI는 단백질
  약 90%·유당 0.5-1%다. 단백질 20 g 기준으로는 같은 일을 한다.
- 유당: WPC 한 스쿱(30 g)에 유당은 약 1-3 g이다. 유당 소화가 어려운 사람 대부분은 한 번에 12 g까지는
  증상이 없거나 가볍다(EFSA). 우유 250 mL에 섞으면 유당이 약 11 g 더해지니, 배가 불편하면 물에
  타거나 WPI로 바꾼다. 우유 단백질 알레르기는 다른 문제다. WPC·WPI 모두 피한다.
- 표시 단백질은 보증이 아니다. 국내 기준상 실제 단백질이 표시량의 80% 이상이면 적합이다(25 g 표시면
  20 g도 적합). 한국소비자원 2023년 시험에서 분말 8개 중 1개는 표시의 28%만 들어 있었다. 아미노산을
  섞어 질소 측정값을 부풀리는 사례도 해외에서 보고됐다.
- 식물성 분말은 유청보다 납이 많은 경향이 있다(2025년 미국 시험에서 평균 약 9배). 다만 하루 1-3회
  섭취 기준 위해 모델에서는 기준치 아래였다. 기준선이 기관마다 4-17배 달라 "위험하다"고 말하지 않는다.
- Informed Sport·NSF 같은 인증은 도핑 금지물질 검사가 중심이다. 단백질 함량까지 확인한다고 밝히는
  것은 단백질 전용 인증뿐이다.
