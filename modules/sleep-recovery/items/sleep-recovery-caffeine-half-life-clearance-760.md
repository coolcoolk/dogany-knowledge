---
# Caffeine timing for training vs sleep sprint 2026-10-07 (block 760..764, numbers are this branch's
# claim). Fills the "why" under 070's cutoff table: how fast caffeine peaks
# and clears, how wide the person-to-person spread is, and which named
# factors (smoking, oral contraceptives, pregnancy) move the half-life. The
# cutoff hours themselves stay in 070; this item only explains them and
# names who should be read against the conservative column.
#
# SOURCE ACCESS (2026-10-07): PubMed, PMC, NCBI Bookshelf, Europe PMC,
# Crossref and the publisher hosts were refused by the network policy (403
# at the proxy). Every primary below was read only as its search-index
# abstract / record text; no full text was opened. Numbers quoted are the
# ones the abstract records state; anything only a secondary summary gave
# is labelled. Re-read list in GAPS.md.
#
# clearance_modifiers is structured data for the brief / cutoff code: each
# row names a stated fact and what it does to 070's cutoff. NO row shortens
# a 070 cutoff (070's own rule: sensitivity lengthens, never shortens). The
# engine never computes a decay curve from these numbers (REFRACTION.md: the
# model never computes a number); the residual table in the body is worked
# illustration, not engine data. Rubric: sleep-recovery @clinical (VC-A).
id: sleep-recovery/caffeine-half-life-clearance-760
domain: sleep-recovery
grade: B (oral caffeine peaks in blood about 30 min after intake; half-life in healthy non-smoking adults is several hours and varies widely between people); B (smoking shortens and oral contraceptives lengthen the half-life, roughly 3.5 vs 6.0 h and 10.7 vs 6.2 h in the original comparisons); C (late pregnancy lengthens it severalfold; reported up to about 18 h); D (no modifier is allowed to shorten a 070 cutoff; slow-clearance groups speak the conservative column)
lane: "@clinical"
locale: universal
as_of: 1978-2022
contested: no
sources:
  - "https://doi.org/10.1007/BF00613933"  # Blanchard J, Sawers SJ. 1983, Eur J Clin Pharmacol 24:93-98, PMID 6832208 -- absolute bioavailability, 10 healthy men: oral absorption very rapid, peak plasma concentration at 29.8 +/- 8.1 min (mean +/- SEM); bioavailability essentially complete. Search-index record only
  - "https://doi.org/10.1002/cpt197824140"  # Parsons WD, Neims AH. 1978, Clin Pharmacol Ther 24(1):40-45 -- salivary caffeine elimination in 13 healthy smokers vs 13 non-smokers: mean half-life 3.5 h vs 6.0 h, attributed to hepatic enzyme induction by smoking. Search-index abstract only
  - "https://pk-db.com/data/PKDB00057/"  # Patwardhan RV, Desmond PV, Johnson RF, Schenker S. 1980, J Lab Clin Med -- oral contraceptive steroids and caffeine elimination; half-life about 10.7 h in OC users vs 6.2 h in non-users, as quoted by the search-index summary (PK-DB curation record Patwardhan1980). Paper not opened; volume / pages / PMID not verified (GAPS)
  - "https://doi.org/10.1007/BF00544361"  # Eur J Clin Pharmacol record 'Impairment of caffeine clearance by chronic use of low-dose oestrogen-containing oral contraceptives' (authors and year not read; GAPS) -- direction only: low-dose OCs reduce caffeine clearance. Title read in the search index only
  - "https://doi.org/10.3389/fphar.2021.752826"  # Grzegorzewski J, Bartsch F, Koller A, Konig M. 2022, Front Pharmacol 12:752826, PMCID PMC8914174 -- systematic analysis of reported caffeine pharmacokinetic data (PK-DB), stratified meta-analysis of clearance and half-life by smoking and oral-contraceptive use and by dose; confirms smoking raises clearance and OCs lower it. Abstract / record only; its stratified numbers were not read
  - "https://pubmed.ncbi.nlm.nih.gov/29514871/"  # Nehlig A. 2018, Pharmacol Rev 70(2):384-411, doi 10.1124/pr.117.014407 -- review: caffeine metabolism and clearance are affected by age, sex and hormones, liver disease, obesity, smoking and diet; CYP1A2 handles most of it; ADORA2A variants shape sleep and anxiety responses. Abstract only
  - "literature:Aldridge A, Bailey J, Neims AH. 1981, Semin Perinatol -- caffeine disposition in pregnancy; secondary reviews quote a rise in half-life to about 18 h at the end of pregnancy. Not opened; no URL, volume or PMID verified in this run (GAPS)"
  - "https://doi.org/10.2903/j.efsa.2015.4102"  # EFSA NDA Panel 2015, EFSA Journal 13(5):4102 -- single doses up to 200 mg (about 3 mg/kg for 70 kg) and 400 mg a day raise no safety concern for healthy non-pregnant adults; 200 mg single dose also safe under 2 h before intense exercise. Search-index abstract only
  - "sleep-recovery/caffeine-bedtime-cutoff-070"  # the cutoff table this item explains; product_hours / conservative_hours live there
  - "sleep-recovery/caffeine-morning-brief-rules-083"  # safety-gate (pregnancy, cardiovascular, medication, hormonal contraception) this item supplies the mechanism for
  - "sleep-recovery/caffeine-tolerance-short-night-082"  # Kocak 2025's 8-10 h suggestion for OC users, which 082 already labels as authors' advice
  - "exercise/early-morning-caffeine-food-069"  # dawn dose and the 200 mg single-dose ceiling
  - "framework:GRADE -- peak time and the smoking / OC direction rest on controlled pharmacokinetic studies with objective plasma or saliva measures, consistent across decades and confirmed by the 2022 systematic data analysis (B, downgraded from A for small samples, all read at abstract level only, and the OC figures being secondary-quoted). The pregnancy figure is a 1981 review quoted second-hand (C). The rule that no modifier shortens a cutoff is product policy (D)."
applicability:
  axes:
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
    - key: caffeine_sensitivity
      type: categorical
      role: soft
      unknown_policy: hedge
clearance_modifiers:
  - factor: none stated (healthy non-smoking adult)
    stated_by: default
    half_life_h: "about 5-6 (6.0 in Parsons 1978 non-smokers; 6.2 in Patwardhan 1980 non-users); wide individual spread"
    effect_on_070: use product_hours as spoken by 083 cutoff-speak-one-number
    basis_grade: B
  - factor: daily smoker
    stated_by: user says they smoke
    half_life_h: "about 3.5 (Parsons 1978)"
    effect_on_070: none -- do NOT shorten the cutoff; quitting smoking lengthens clearance again, so a recent quitter is read as the slow row
    basis_grade: B
  - factor: recently quit smoking
    stated_by: user says they quit in the last weeks
    half_life_h: "returns toward the non-smoker value (direction only; no time course read)"
    effect_on_070: speak the conservative column; the same coffee lasts longer than it used to
    basis_grade: C
  - factor: oral contraceptive (oestrogen-containing)
    stated_by: user mentions the pill or hormonal contraception
    half_life_h: "about 10.7 vs 6.2 (Patwardhan 1980, secondary-quoted)"
    effect_on_070: speak the conservative column and no mg number (083 safety-gate)
    basis_grade: B
  - factor: pregnancy
    stated_by: pregnancy_status
    half_life_h: "rises through pregnancy; up to about 18 at term (Aldridge 1981, secondary-quoted)"
    effect_on_070: hard gate -- direction only, no hours or mg; refer to the clinician's caffeine limit
    basis_grade: C
  - factor: liver disease or a medication that slows caffeine clearance
    stated_by: medication_list or a stated liver condition
    half_life_h: "lengthened (direction only; Nehlig 2018 names liver disease; specific drugs not read)"
    effect_on_070: hard gate -- direction only, no hours or mg
    basis_grade: C
caffeine_rules:
  - rule: half-life-explains-cutoff
    when: the user asks why the cutoff is so long, or says "it wears off in a few hours"
    level: none
    say: the feeling fades sooner than the caffeine; it peaks in about half an hour and a typical adult clears only half of it every five to six hours, so a big afternoon dose is still partly there at bedtime
    never_say: a computed mg left at bedtime for this user; that the user is a fast or slow metaboliser
    product_constant: false
    basis_grade: B
  - rule: smoker-no-shorter-cutoff
    when: the user says they smoke and asks whether that lets them drink coffee later
    level: none
    say: smoking does clear caffeine faster, but the cutoff stays the same; if you cut down or quit, the same coffee will last longer
    never_say: a shorter cutoff for smokers; anything that frames smoking as a benefit
    product_constant: true
    basis_grade: D
  - rule: slow-clearance-conservative
    when: the user mentions hormonal contraception, a recent smoking quit, liver disease, or a medication on medication_list
    level: hedge
    say: this is one of the things that makes caffeine last longer; use the cautious cutoff and keep caffeine to the morning
    never_say: a number of hours specific to the user; a dose in mg
    product_constant: true
    basis_grade: C
  - rule: genotype-not-asked
    when: the user asks about a caffeine gene test or says they are a "fast metaboliser"
    level: none
    say: people do differ, partly by genes, but the sleep cutoffs are set so they work for most people without a test; a "fast" label does not shorten them
    never_say: that a test result should change the cutoff; a recommendation to buy a test
    product_constant: true
    basis_grade: D
refraction_notes:
  - note: >
      Caffeine is absorbed fast and cleared slowly. Taken by mouth it is
      essentially fully absorbed and peaks in the blood about half an hour
      later (Blanchard and Sawers 1983, 10 men). Clearance is slower: in the
      two classic comparisons the average non-smoking adult's half-life was
      about 6 hours. That is the mechanism behind 070's long cutoffs -- a
      200 mg pre-workout serve still leaves something on the order of a
      quarter to a third of the dose in the blood twelve hours later.
    grade: B
  - note: >
      Smoking and oral contraceptives pull in opposite directions. Smokers
      cleared caffeine in about 3.5 hours against 6.0 in non-smokers;
      women on low-dose oestrogen pills took about 10.7 hours against 6.2.
      The smoking effect is not a licence for later coffee: it reverses on
      quitting, and the cutoffs are set for sleep, not for the blood level.
    grade: B
  - note: >
      Pregnancy, liver disease and some medications lengthen the half-life
      further, in pregnancy to many hours by term. These sit behind the hard
      gates in 083; this item only adds why.
    grade: C
  - note: >
      Individual spread is wide and partly genetic (CYP1A2 for clearance,
      ADORA2A for sleep and anxiety response). The warehouse does not
      personalise on genotype: no trial located tests a genotype-specific
      sleep cutoff.
    grade: C
claim: >
  Oral caffeine peaks in the blood about 30 minutes after intake and is
  cleared slowly: the average healthy non-smoking adult's half-life was
  about 6 hours in the classic comparisons, with a wide spread between
  people. Smoking shortens it (about 3.5 h vs 6.0 h), oestrogen-containing
  oral contraceptives lengthen it (about 10.7 h vs 6.2 h), and late
  pregnancy lengthens it much further. This is why 070's cutoffs are long and
  why "it wears off in a few hours" is a feeling, not the blood level. The
  operative rules: no factor ever shortens a 070 cutoff (smokers included,
  since the effect reverses on quitting); hormonal contraception, a recent
  quit, liver disease or a clearance-slowing medication move the user to the
  conservative column with no mg number; pregnancy is a hard gate; and a
  gene test or "fast metaboliser" label does not change the cutoff.
reasoning: >
  The peak-time and smoking numbers come from small, old but controlled
  pharmacokinetic studies whose direction is uncontested and confirmed by a
  2022 systematic analysis of all reported caffeine PK data, so the direction
  is B. Every source was read as a search-index abstract or record only (the
  network policy refused PubMed and the publishers), and the oral
  contraceptive and pregnancy figures came through secondary quotation, so
  no number here is stronger than C on its own and the item says which
  figures were secondary. The item deliberately adds no cutoff: 070 owns the
  sleep cutoffs, which come from sleep outcomes, not from blood levels, and
  converting half-life into a personal cutoff would invent precision the
  sleep trials do not support. The modifier rows only ever push toward 070's
  conservative column. Not contested.
---

# sleep-recovery/caffeine-half-life-clearance-760 -- 카페인은 빨리 오르고 천천히 빠진다

**한 줄 그림:** 카페인은 마시고 30분이면 혈중 최고치에 닿지만, 절반이 빠지는 데 보통 5~6시간이 걸린다.
그래서 "몇 시간이면 깬다"는 느낌과 달리 오후 카페인이 밤까지 남는다.

## How long a dose stays (worked illustration, not engine data)

| Hours after intake | Fraction left at a 6 h half-life | 200 mg serve leaves about |
|---:|---:|---:|
| 0.5 | peak | 200 mg |
| 6 | 1/2 | 100 mg |
| 12 | 1/4 | 50 mg |
| 18 | 1/8 | 25 mg |

The cutoff hours in 070 come from sleep trials, not from this arithmetic;
the table only shows why they are long.

## Who clears it slower or faster

| Stated fact | Half-life (source) | What the brief does |
|---|---|---|
| none | about 6 h (non-smokers, 1978 / 1980) | 070 as spoken by 083 |
| smoker | about 3.5 h (1978) | no change; never a later cutoff |
| oral contraceptive | about 10.7 h vs 6.2 h (1980) | conservative column, no mg |
| pregnancy | up to about 18 h at term (1981, quoted) | hard gate, direction only |
| liver disease, some medicines | longer (direction) | hard gate, direction only |

## 한국어 요약 (답변용)

- 카페인은 마시고 약 30분 뒤 혈중 농도가 가장 높고, 건강한 비흡연 성인 기준으로 절반이 빠지는 데 약
  6시간이 걸린다. 사람마다 차이가 크다.
- 그래서 오후 5시에 마신 프리워크아웃 한 스쿱(약 200mg)은 밤 11시에도 절반 가까이 남아 있다. 각성 느낌이
  사라져도 몸에는 남아 있다.
- 흡연자는 카페인이 더 빨리 빠지지만(약 3.5시간), 그렇다고 늦게 마셔도 되는 건 아니다. 담배를 줄이거나
  끊으면 같은 커피가 더 오래 남는다.
- 경구피임약을 먹으면 반감기가 길어진다(한 연구에서 약 10.7시간 대 6.2시간). 이 경우 더 보수적인 기준을
  쓰고 mg 숫자는 말하지 않는다.
- 임신 중에는 반감기가 크게 길어진다. 시간과 양은 말하지 않고 담당 의료진의 기준을 따르도록 안내한다.
  간 질환이나 일부 약도 카페인을 늦게 빠지게 한다.
- 유전자 검사나 "나는 카페인 빨리 분해해요"라는 말로 취침 전 기준을 줄이지 않는다.
