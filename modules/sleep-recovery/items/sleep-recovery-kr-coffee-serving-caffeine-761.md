---
# Caffeine timing for training vs sleep sprint 2026-10-07 (block 760..764, numbers are this branch's
# claim). 070's cutoff table is written in mg; Korean users speak in drinks
# (아메리카노 한 잔, 커피믹스 한 봉, 캔커피, 에너지음료, 프리워크아웃 한 스쿱). This item maps
# the common Korean servings onto 070's dose rows using Korean government
# survey data, so the brief can pick a row from what the user said.
#
# SOURCE ACCESS (2026-10-07): korea.kr, mfds.go.kr, kca.go.kr and the news
# hosts were refused by the network policy (403 at the proxy). Every figure
# below was read as a search-index rendering of the agency release or of a
# news article quoting it; no release PDF or table was opened. The surveys
# are dated (2012, 2016, 2019) and chain recipes, shot counts and cup sizes
# change, so the mg figures are staleness-gated (reverify_by) and only the
# BAND each serving falls into is used by the engine.
#
# kr_servings is structured data for the brief / caffeine code: each row is
# a serving the user may name, its surveyed mg, and the 070 row it maps to
# (070 dose_band). When the serving is unknown or the size is large, the
# row falls back to 070's unknown-dose rule (about 200 mg). Rubric:
# sleep-recovery @clinical (VC-A).
id: sleep-recovery/kr-coffee-serving-caffeine-761
domain: sleep-recovery
grade: C (surveyed caffeine per Korean serving -- coffee-shop coffee about 132 mg per 400 mL on average, chain Americano 91-196 mg in one survey and up to about 300 mg for the highest products in another, coffee mix about 55 mg a stick, liquid / canned coffee about 88 mg per 250 mL, energy drinks about 58 mg a can on average); B (MFDS daily maximum intake guidance -- adults 400 mg, pregnant women 300 mg, children and adolescents 2.5 mg/kg); D (the serving-to-070-row mapping and the unknown-size fallback)
lane: "@clinical"
locale: KR
as_of: 2012-2026
reverify_by: 2027-04-30
contested: no
sources:
  - "https://www.dailypharm.com/user/news/124525"  # news report of the MFDS caffeine intake assessment (2015-2017 KNHANES, released about 2020): mean intake 65.7 mg/day per person (adults 78.0 mg), 17.6% of the maximum; per-serving means of the 2019 product survey -- coffee-shop coffee 132.0 mg (400 mL), liquid coffee 88.2 mg (250 mL), roasted coffee 91.5 mg (7 g), coffee mix (조제커피) 55.8 mg (12 g), instant 54.5 mg (2 g). Search-index rendering only
  - "https://impfood.mfds.go.kr/CFBBB02F02/getCntntsDetail?cntntsSn=281601"  # MFDS 식품안전나라 content '우리나라 카페인 섭취 안전한 수준 - 카페인 섭취량 평가 결과': maximum daily intake guidance adults 400 mg or less, pregnant women 300 mg or less, children and adolescents 2.5 mg per kg or less. Search-index rendering only
  - "https://www.korea.kr/briefing/pressReleaseView.do?newsId=155854487"  # KFDA (식품의약품안전청) press release, 2012, '국내 유통 중인 에너지 음료 등 카페인 함량 조사결과 발표': coffee-shop coffee had the highest mean caffeine of the categories surveyed; reported (news quotation) Americano mean 124.99 mg per serving and top coffee-shop products 217.26-307.75 mg. Title and summary only; per-product table not read
  - "https://www.hankyung.com/article/2012080578711"  # news report of the Korea Consumer Agency (한국소비자원) 2012 survey of 9 coffee chains (27 outlets): Americano caffeine 91-196 mg per cup, about 2-fold between brands, driven by shot count (3 brands 1 shot of about 30 mL, 6 brands 2 shots of about 60 mL); lowest 91 mg (Ediya, Tom N Toms), highest 196 mg (Pascucci). Search-index rendering only
  - "https://www.kca.go.kr/kca/sub.do?menukey=5084&mode=view&no=1001982085"  # Korea Consumer Agency release, about 2016 (as rendered): energy drinks mean 58.1 mg per can, highest product 162.4 mg. Search-index rendering only; the canned-coffee column was garbled and is not used
  - "https://www.imaeil.com/page/view/2026052813371998612"  # news report of the Korea Consumer Agency 2026-05 test of franchise matcha / green tea lattes and milk teas (6 chains): 45-172 mg per cup; two milk teas (172 mg, 148 mg) above the agency's reference iced Americano of 132 mg. Search-index rendering only
  - "https://www.bizhankook.com/bk/article/23400"  # news explainer of the Korean labelling rule: a liquid with 0.15 mg/mL or more caffeine is labelled 고카페인 함유 with total caffeine in mg (37.5 mg in a 250 mL can); coffee-shop caffeine display for chains of 100+ outlets described by MFDS as a recommendation. Search-index rendering only; the 식품등의 표시기준 text itself was not read
  - "sleep-recovery/caffeine-bedtime-cutoff-070"  # the dose rows (up to about 100 mg / about 200 mg / about 400 mg) these servings map to
  - "sleep-recovery/caffeine-morning-brief-rules-083"  # cutoff-speak-one-number: which hour figure the brief speaks per row
  - "sleep-recovery/caffeine-half-life-clearance-760"  # why the rows' hours are long
  - "exercise/early-morning-caffeine-food-069"  # 200 mg single-dose ceiling
  - "framework:GRADE -- the per-serving figures are government laboratory surveys (objective measurement) but each is a snapshot of products that change, read second-hand through search renderings, with different serving bases (400 mL vs per cup) and years (2012-2019); downgraded to C for indirectness to today's menu and imprecision. The MFDS intake guidance is a regulator's position aligned with EFSA / Health Canada (B as guidance, not as a sleep threshold). The mapping to 070 rows is product judgement (D)."
applicability:
  axes:
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [not_pregnant, none]
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: caffeine_sensitivity
      type: categorical
      role: soft
      unknown_policy: hedge
kr_servings:
  - serving: 커피믹스 1봉 (instant coffee mix stick)
    mg_typical: 55
    mg_range: "about 50-60 (2019 MFDS means 55.8 per 12 g mix, 54.5 per 2 g instant)"
    maps_to_070: up to about 100 mg
    basis_grade: C
  - serving: 캔커피 / 컵커피 / 편의점 RTD 커피 (liquid coffee, about 250 mL)
    mg_typical: 88
    mg_range: "mean 88.2 per 250 mL (2019); bottle sizes above 250 mL scale up"
    maps_to_070: up to about 100 mg (250 mL or less); about 200 mg above 300 mL
    basis_grade: C
  - serving: 1샷 아메리카노 (single-shot chain Americano, regular size)
    mg_typical: 100
    mg_range: "91 at the 1-shot brands (KCA 2012)"
    maps_to_070: up to about 100 mg
    basis_grade: C
  - serving: 2샷 아메리카노 / 일반 커피전문점 아메리카노 (regular size, shot count unknown)
    mg_typical: 150
    mg_range: "132 mean per 400 mL (MFDS 2019); 168-196 at 2-shot brands (KCA 2012); up to about 300 for the highest products (KFDA 2012)"
    maps_to_070: about 200 mg
    basis_grade: C
  - serving: 대용량 / 벤티 / 24oz 이상 아메리카노 or 샷 추가 (large size or extra shot)
    mg_typical: null
    mg_range: "not surveyed in any source read; more shots means more caffeine (KCA 2012)"
    maps_to_070: about 200 mg; about 400 mg if the user says 3 or more shots or two large cups
    basis_grade: D
  - serving: 에너지음료 1캔 (energy drink can)
    mg_typical: 58
    mg_range: "mean 58.1, highest 162.4 per can (KCA about 2016); read the 총카페인 label"
    maps_to_070: up to about 100 mg unless the label says more
    basis_grade: C
  - serving: 밀크티 / 말차·녹차 라떼 (franchise tea latte)
    mg_typical: null
    mg_range: "45-172 per cup (KCA 2026); milk teas can exceed an Americano"
    maps_to_070: about 200 mg for milk tea; up to about 100 mg for green tea / matcha latte
    basis_grade: C
  - serving: 디카페인 아메리카노 (decaf)
    mg_typical: null
    mg_range: "low single to low double digits; not zero (decaf cold brews reported 3-15 mg in a 2025 news-reported test, not read)"
    maps_to_070: below every row; no cutoff spoken
    basis_grade: D
  - serving: 프리워크아웃 1스쿱 (pre-workout scoop)
    mg_typical: null
    mg_range: "product-specific; read the label (no survey of Korean pre-workout products located)"
    maps_to_070: by label mg; unknown label -> about 200 mg; 2 scoops -> about 400 mg
    basis_grade: D
constants:
  kr_daily_max_adult_mg: 400       # MFDS guidance; a safety ceiling, not a sleep threshold
  kr_daily_max_pregnant_mg: 300    # MFDS guidance; this item still gates pregnancy to direction only
  kr_daily_max_youth_mg_per_kg: 2.5
  high_caffeine_label_mg_per_ml: 0.15
caffeine_rules:
  - rule: serving-to-row
    needs: [stated serving]
    when: the user names a drink rather than mg
    level: none
    say: map the drink to its kr_servings row and use that row's 070 cutoff as spoken by 083 cutoff-speak-one-number
    never_say: the row's mg as an exact figure for the user's cup; a brand comparison
    product_constant: true
    basis_grade: D
  - rule: shop-coffee-is-not-small
    needs: [stated serving]
    when: the user calls a coffee-shop Americano "just one coffee" or "a small coffee"
    level: note
    say: a regular coffee-shop Americano is usually two shots and sits nearer the pre-workout row than the small-coffee row; a coffee mix or a single shot is the small one
    never_say: an exact mg for a named brand; that the user drinks too much
    product_constant: false
    basis_grade: C
  - rule: unknown-size-as-200
    needs: []
    when: the drink, size or shot count is unknown
    level: none
    say: treat it as the about-200 mg row (070's unknown-dose rule)
    never_say: the 100 mg row for an unknown coffee-shop drink
    product_constant: true
    basis_grade: D
  - rule: label-first
    needs: [stated product]
    when: the user names a packaged drink or a pre-workout
    level: note
    say: check the 총카페인 함량 on the label; Korean drinks over 0.15 mg per mL must show it, and a pre-workout scoop varies by brand
    never_say: a guessed mg for a named product
    product_constant: false
    basis_grade: C
  - rule: daily-total-is-not-sleep-cutoff
    needs: []
    when: the user cites the 400 mg daily limit to justify an evening drink
    level: note
    say: 400 mg a day is a safety ceiling for the whole day; sleep depends on how much and how close to bed, so a drink well under 400 mg can still cost sleep
    never_say: that staying under 400 mg protects sleep
    product_constant: false
    basis_grade: B
refraction_notes:
  - note: >
      THE KOREAN CUP IS BIGGER THAN "ONE COFFEE". 070's smallest row is about
      100 mg, labelled "one small coffee". A coffee mix stick (about 55 mg),
      a 250 mL canned coffee (about 88 mg) or a single-shot Americano (about
      91 mg in 2012) fits it. A regular two-shot chain Americano does not:
      the 2012 survey found 168-196 mg at the two-shot brands, the 2019 MFDS
      mean was 132 mg per 400 mL, and the highest coffee-shop products were
      around 300 mg. So the default coffee-shop Americano maps to 070's
      about-200 mg row.
    grade: C
  - note: >
      THE NUMBERS ARE OLD; THE SPREAD IS THE DURABLE PART. No survey read
      covers the current low-price chains' large cups (24 oz and up), extra
      shots or today's recipes. What holds across surveys is that shot count
      drives caffeine and that brand-to-brand spread is about two-fold. The
      engine therefore uses bands, not brand mg, and re-verification is due
      by reverify_by.
    grade: C
  - note: >
      THE DAILY LIMIT IS A DIFFERENT QUESTION. MFDS guidance (adults 400 mg,
      pregnancy 300 mg, youth 2.5 mg/kg) is about safety over a day. The
      average Korean adult takes about 78 mg a day, far below it. Sleep
      disruption is a matter of dose and hours before bed (070) and starts
      far below 400 mg.
    grade: B
claim: >
  Korean servings carry very different caffeine loads. In government
  surveys a coffee mix stick held about 55 mg, a 250 mL canned or bottled
  coffee about 88 mg, an energy drink about 58 mg on average (up to 162 mg),
  a coffee-shop coffee about 132 mg per 400 mL on average, chain Americanos
  91-196 mg depending mainly on one vs two shots, and the strongest
  coffee-shop products about 300 mg; some franchise milk teas exceed an
  Americano. Mapped onto 070: a coffee mix, a small canned coffee, a
  single-shot Americano or a typical energy drink is the up-to-100 mg row; a
  regular coffee-shop Americano, a milk tea, an unknown drink or one
  pre-workout scoop is the about-200 mg row; three or more shots, two large
  cups or two scoops is the about-400 mg row. Labels (총카페인 함량, required
  above 0.15 mg/mL) beat these averages. MFDS's 400 mg daily maximum is a
  safety ceiling, not a sleep threshold.
reasoning: >
  The surveys are objective laboratory measurements by the food regulator
  and the consumer agency, which is why the direction (shop coffee is the
  strongest common serving, shot count drives it, brand spread about
  two-fold) is solid. The individual figures are C because they are 7 to 14
  years old, use different serving bases, and were read through search
  renderings rather than the release tables (all Korean government and news
  hosts were refused by the network policy in this run). The item therefore
  hands the engine bands, not brand numbers, and maps every uncertain case
  upward, consistent with 070's rule that an unknown dose is treated as
  about 200 mg. Large cups, extra shots and pre-workout scoops were not
  surveyed in any source read; those rows are D. Not contested.
---

# sleep-recovery/kr-coffee-serving-caffeine-761 -- 한국에서 마시는 한 잔은 몇 mg인가

**한 줄 그림:** 커피믹스·캔커피·1샷 아메리카노는 "작은 커피"(약 100mg 이하), 커피전문점 일반 아메리카노와
프리워크아웃 한 스쿱은 "약 200mg" 칸으로 본다.

## Serving to cutoff row

| Serving | Surveyed caffeine | 070 row | Spoken cutoff (083) |
|---|---|---|---|
| 커피믹스 1봉 | about 55 mg | up to about 100 mg | 9 h before bed |
| 캔커피 250 mL | about 88 mg | up to about 100 mg | 9 h |
| 1샷 아메리카노 | about 91 mg (2012) | up to about 100 mg | 9 h |
| 에너지음료 1캔 | about 58 mg (up to 162) | up to about 100 mg unless label says more | 9 h |
| 커피전문점 아메리카노 (2샷, 보통 사이즈) | 132-196 mg, up to about 300 | about 200 mg | 13 h |
| 밀크티 | up to 172 mg | about 200 mg | 13 h |
| 프리워크아웃 1스쿱 / 모르는 음료 | label / unknown | about 200 mg | 13 h |
| 3샷 이상, 대용량 두 잔, 2스쿱 | not surveyed | about 400 mg | 14 h |
| 디카페인 | a few mg | below every row | none |

## 한국어 요약 (답변용)

- 같은 "커피 한 잔"이라도 카페인 양이 크게 다르다. 조사에서 커피믹스 1봉은 약 55mg, 250mL 캔커피는 약
  88mg, 에너지음료는 평균 약 58mg(많게는 162mg)이었다.
- 커피전문점 아메리카노는 샷 수가 핵심이다. 2012년 조사에서 1샷 브랜드는 약 91mg, 2샷 브랜드는
  168~196mg이었고, 가장 진한 제품은 300mg 안팎이었다. 2019년 식약처 평균은 400mL당 132mg이었다.
- 그래서 일반 커피전문점 아메리카노는 "작은 커피"가 아니라 프리워크아웃 한 스쿱과 같은 약 200mg 칸으로
  보고, 잠들기 13시간 전을 기준으로 삼는다. 커피믹스나 1샷이면 9시간이다.
- 양이나 사이즈를 모르면 200mg으로 본다. 샷 추가, 대용량 두 잔, 프리워크아웃 두 스쿱은 400mg 칸이다.
- 포장 음료는 라벨의 "총카페인 함량"을 먼저 본다. 1mL당 0.15mg 이상이면 "고카페인 함유"로 표시해야 한다.
- 식약처 하루 최대 권고량(성인 400mg, 임산부 300mg, 청소년 체중 1kg당 2.5mg)은 안전 기준이지 수면 기준이
  아니다. 400mg 아래라도 늦게 마시면 잠이 줄 수 있다.
- 조사 수치는 2012~2019년 자료라 지금 메뉴와 다를 수 있다. 브랜드별 mg을 단정해서 말하지 않는다.
