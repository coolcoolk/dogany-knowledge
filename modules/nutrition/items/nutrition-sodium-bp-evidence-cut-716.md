---
# Eating-out / convenience sprint 2026-10-07.
# Partial fill of the long-standing sodium gap (014's "WHAT THIS ITEM DOES NOT
# COVER: sodium"; GAPS "SODIUM AND THE KOREAN DIET"). Scope is deliberately
# narrow: what a diet card on a cut may say about sodium -- direction of the
# blood-pressure effect, the one large hard-outcome trial, the low-end dispute,
# the Korean reference number, and whether a salty meal shows on the scale.
# It does NOT adjudicate the sodium-mortality curve and does not set any
# personal target.
#
# READ PATH, stated plainly: every external source below was seen ONLY through
# search-index records (abstract summaries) on 2026-10-07. Publisher pages,
# PubMed, PMC, Cochrane and every Korean government host were blocked by the
# network egress proxy for this run. No full text was read; numbers were
# cross-checked between at least two index records where possible. Grades are
# held one notch below what the evidence type would support where only one
# record was seen. A source re-audit at source is owed (GAPS).
#
# sodium_rules is structured data for the diet card / meal log, same field
# shape as 080's eating_out_rules. No program code changed.
id: nutrition/sodium-bp-evidence-cut-716
domain: nutrition
lane: "@meal-craft"
grade: "B (direction: modest salt reduction lowers blood pressure, Cochrane / BMJ meta-analysis of randomised trials of 4 weeks or more); B (a potassium salt substitute lowered stroke, cardiovascular events and death in one large randomised trial in older high-risk rural Chinese adults); C (low sodium below about 3 g a day associated with more events in one large cohort, spot-urine estimate, disputed); C (a controlled metabolic-ward study found high salt raised plasma volume but not body mass or total body water at steady state, 32 men); D (Korean 2,300 mg chronic-disease reference, 2020 edition, seen via secondary records; 2025 edition value not read); D (the sodium_rules as a set)"
locale: universal
as_of: 2000-2021
contested: yes
sources:
  - "https://doi.org/10.1136/bmj.f1325"  # He FJ, Li J, MacGregor GA. Effect of longer term modest salt reduction on blood pressure: Cochrane systematic review and meta-analysis of randomised trials. BMJ 2013;346:f1325 (also Cochrane CD004937.pub2). Trials of 4 weeks or more; a 4.4 g/day reduction in salt (about 1.7 g sodium) went with a mean change of -4.18 mmHg systolic and -2.06 mmHg diastolic overall, larger in hypertensive than normotensive participants. Seen via search-index records (McMaster Optimal Aging, EPA HERO, Cochrane abstract record) 2026-10-07; full text not read
  - "https://doi.org/10.1056/NEJMoa2105675"  # Neal B, Wu Y, Feng X, et al. Effect of salt substitution on cardiovascular events and death. N Engl J Med 2021;385:1067-1077 (SSaSS). 20,995 participants in 600 Chinese villages with prior stroke or age 60+ with uncontrolled hypertension, mean age 65, 50 percent women, 4.74 years; potassium-enriched salt substitute vs regular salt: stroke rate ratio 0.86 (95% CI 0.77-0.96), major cardiovascular events 0.87, death 0.88; no excess serious hyperkalaemia events reported. Seen via search-index records (ACC trial summary, Action on Salt news) 2026-10-07; exclusion criteria not read at source; DOI not confirmed at source
  - "https://doi.org/10.1056/NEJMoa1311889"  # O'Donnell M, Mente A, Rangarajan S, et al. Urinary sodium and potassium excretion, mortality, and cardiovascular events. N Engl J Med 2014;371(7):612-623 (PURE). 101,945 people, 17 countries, single fasting morning urine converted to estimated 24-h excretion; mean 4.93 g sodium a day; 3.7 years; against 4.00-5.99 g, 7 g or more OR 1.15 (1.02-1.30) and under 3 g OR 1.27 (1.12-1.44) for death or major cardiovascular events. Observational; the spot-urine estimate and reverse causation are the standing criticisms. Seen via search-index records (University of Galway and repository records) 2026-10-07; DOI not confirmed at source
  - "https://pubmed.ncbi.nlm.nih.gov/10751219/"  # Heer M, Baisch F, Kropp J, Gerzer R, Drummer C. High dietary sodium chloride consumption may not induce body fluid retention in humans. Am J Physiol Renal Physiol 2000;278(4):F585-F595. Metabolic ward, 32 healthy men, NaCl 50, 200, 400 or 550 mmol a day: plasma volume rose dose-dependently (+315 ml at 550) but total body water and body mass did not increase. Seen via the PubMed record (PMID 10751219) summary in search results 2026-10-07
  - "2020 한국인 영양소 섭취기준 (보건복지부·한국영양학회) -- sodium 충분섭취량 1,500 mg and 만성질환위험감소섭취량 (CDRR) 2,300 mg a day for adults, seen via secondary records (news and university repository summaries) 2026-10-07. The 2025 edition (nutrition/kr-reference-intakes-2025-014) was NOT read for sodium; whether the value changed is unknown"
  - "source:nutrition/kr-reference-intakes-2025-014 -- the Korean reference standard; its sodium note is answered in part here, not closed"
  - "source:nutrition/kr-convenience-protein-options-030 -- the 2000 mg label reference used for display parity"
  - "source:nutrition/kr-restaurant-dish-energy-ranking-022 -- Korean soup, stew and noodle servings at a median 1786-2193 mg sodium"
  - "source:nutrition/kr-convenience-restaurant-menu-choice-715 -- the menu rules that display sodium using this row"
  - "source:nutrition/weekend-drift-073 -- day-to-day weight noise; compare like days"
  - "source:nutrition/kr-hoesik-cut-rules-080 -- its morning-weight-not-fat rule names salty food as one cause of a scale bump; see the scale note below"
  - "framework:VC-E craft -- the direction rests on randomised meta-analysis and one large outcome trial; the low end is disputed observational evidence; the display rules are conventions"
applicability:
  axes:
    - key: cardiovascular_condition
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: renal_condition
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: medication_list
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
sodium_rules:
  - rule: sodium-is-not-a-fat-loss-lever
    surface: both
    trigger: user asks whether cutting salt helps fat loss, or a low-sodium plan is proposed for weight
    action: say sodium does not change fat loss; it matters for blood pressure; on a cut the lever is energy and protein
    never: [저염식으로 살 빼기, "소금 줄이면 붓기 빠져서 살 빠져요"]
    constants: none
    basis: no fat-mass effect in any source read; Heer 2000 (no body-mass change with high salt at steady state)
    basis_grade: C
    kind: evidence
  - rule: bp-direction
    surface: diet_card
    trigger: user asks why sodium is flagged
    action: lowering salt modestly for a month or more lowers blood pressure on average (about 4 mmHg systolic for about 4.4 g less salt a day), more in people with high blood pressure; say it as an average, not a prediction for the user
    never: [a mmHg prediction for this user, a diagnosis]
    constants: none
    basis: He 2013 (meta-analysis of randomised trials)
    basis_grade: B
    kind: evidence
  - rule: korean-daily-reference
    surface: diet_card
    trigger: a daily sodium total is displayed
    action: show the day against 2,300 mg (Korean chronic-disease risk reduction intake) and label packs against 2000 mg (label reference); call it a reference, not a limit to fear
    never: [a target below 1,500 mg, a per-meal health threshold]
    constants: 2300 mg daily reference; 2000 mg label reference
    basis: 2020 KDRI via secondary records (2025 edition not read for sodium); nutrition/kr-convenience-protein-options-030
    basis_grade: D
    kind: convention
  - rule: no-extreme-restriction
    surface: both
    trigger: user aims for very low sodium (for example under 1,500 mg) without a clinician's instruction
    action: say the reference is about getting down toward 2,300 mg; going far lower is not what the guidance asks and the low end of the evidence is disputed; a clinician sets lower targets
    never: ["낮을수록 좋아요", "너무 적게 먹으면 위험해요" as a scare]
    constants: none
    basis: O'Donnell 2014 (association at under 3 g estimated sodium, disputed); 2020 KDRI 1,500 mg adequate intake
    basis_grade: C
    kind: evidence
  - rule: salt-substitute-not-suggested
    surface: both
    trigger: user asks about 저염 소금, 칼륨 소금 or salt substitutes
    action: say a large trial in older high-risk adults found fewer strokes with a potassium salt substitute; the app does not suggest one, because potassium substitutes are unsafe with some kidney conditions and medicines; ask a clinician or pharmacist
    never: [a recommendation to switch, a brand]
    constants: none
    basis: Neal 2021 (SSaSS); medication_list hard gate
    basis_grade: B
    kind: evidence
  - rule: scale-bump-hedged
    surface: both
    trigger: weight up the morning after a salty meal
    action: say a one-day change is mostly noise from food and fluid in transit; do not blame salt specifically or promise it will drop in a set number of days; read the weekly mean
    never: ["소금 때문에 2 kg 늘었어요", a water-weight estimate]
    constants: none
    basis: Heer 2000 (high salt at steady state did not raise body mass; acute shifts not measured here); nutrition/weekend-drift-073
    basis_grade: C
    kind: evidence
  - rule: condition-defers
    surface: both
    trigger: cardiovascular_condition or renal_condition present, or blood-pressure or kidney medication in medication_list
    action: show the same reference display, give no personal sodium or potassium number, and point to the treating clinician
    never: [a personal mg target, stopping or changing medicine]
    constants: none
    basis: convention; medication_list block_specifics
    basis_grade: D
    kind: convention
refraction_notes:
  - axis: medication_list
    note: >
      MEDICATION UNKNOWN -> no potassium, salt-substitute or personal sodium
      numbers (block_specifics); the reference display still shows.
    grade: D
  - note: >
      THE DIRECTION IS SETTLED, THE LOW END IS NOT. Randomised trials agree that
      eating less salt lowers blood pressure, and one large randomised trial in
      older high-risk adults found fewer strokes and deaths with a potassium
      salt substitute. Whether intakes below about 3 g sodium a day carry their
      own risk rests on cohort data with spot-urine estimates and is disputed.
      The app speaks the direction and stays at the national reference.
    grade: B
  - note: >
      THE SCALE STORY IS WEAKER THAN FOLK WISDOM. In a metabolic-ward study,
      weeks of very high salt raised plasma volume but not body weight or total
      body water. Short-term shifts after one salty meal were not what it
      measured, so the app neither blames salt for a scale bump nor promises a
      drop; it reads the trend.
    grade: C
  - note: >
      READ PATH. Every external source here was seen only through search-index
      abstract records; no full text and no Korean ministry document was read
      this pass. The direction and trial headline numbers agree across records;
      the details (exclusions, subgroup effects, the 2025 KDRI sodium value) are
      owed a read at source.
    grade: D
claim: >
  Sodium is a blood-pressure question, not a fat-loss lever. Randomised trials
  of a month or more show that eating about 4.4 g less salt a day lowers blood
  pressure on average by about 4/2 mmHg, more in people with hypertension, and
  one large randomised trial in older high-risk Chinese adults found a
  potassium salt substitute cut strokes by about 14 percent and deaths by
  about 12 percent. Whether very low intakes carry their own risk is disputed
  (one large cohort with spot-urine estimates). The Korean reference sets
  1,500 mg as adequate and 2,300 mg as the chronic-disease line (2020 edition;
  the 2025 value was not read). A diet card on a cut therefore shows sodium
  against those references, flags very salty meals without alarm, sets no
  personal target, never suggests a salt substitute, and does not blame salt
  for a morning scale bump, because a controlled study found high salt raised
  plasma volume but not body weight at steady state.
reasoning: >
  Korean eating-out meals routinely carry 1,100-2,200 mg sodium per serving
  (022, 715), so the diet card needs a sentence about it, and the warehouse
  had none graded. A full adjudication of the sodium-outcome curve was out of
  this run's scope and its sources could not be read at source, so the item
  takes only what is robust across records: the randomised blood-pressure
  direction and one landmark outcome trial at B, the cohort dispute at C as a
  reason not to push extremes, and the Korean reference at D until the 2025
  edition is read. The scale rule replaces a commonly repeated but
  unsupported "salt = water weight" line with the trend-reading rule the
  warehouse already uses. Deliberately not here: a sodium-mortality curve,
  potassium targets, salt-sensitivity testing, and any rule for people with
  hypertension, heart failure or kidney disease beyond deferring to their
  clinician.
---

# nutrition/sodium-bp-evidence-cut-716 -- 나트륨: 감량과 혈압

**One line:** 나트륨은 체지방이 아니라 혈압 문제다. 하루 기준선 2,300 mg을 보여 주되 겁주지 않고,
개인 목표나 대체염은 권하지 않는다.

- **Direction (B).** About 4.4 g less salt a day for 4+ weeks → about −4/−2 mmHg on average
  (He 2013 meta-analysis of RCTs); larger in hypertension.
- **Outcomes (B, one trial).** Potassium salt substitute, 20,995 older high-risk rural Chinese adults,
  4.7 years: stroke RR 0.86, death 0.88 (SSaSS 2021).
- **Disputed low end (C).** PURE cohort: estimated sodium under 3 g/day associated with more events
  (OR 1.27) as well as 7 g or more (OR 1.15); spot-urine estimates, contested.
- **Scale (C).** High salt raised plasma volume, not body mass or total body water, at steady state
  (Heer 2000, 32 men).
- **Korea (D).** 2020 KDRI: adequate 1,500 mg; chronic-disease reference 2,300 mg. 2025 value not read.

| Rule | Surface | Trigger | Action |
|---|---|---|---|
| sodium-is-not-a-fat-loss-lever | both | "salt and weight loss" | not a fat-loss lever |
| bp-direction | diet card | why sodium is flagged | average BP effect, not a prediction |
| korean-daily-reference | diet card | daily total | vs 2,300 mg; packs vs 2,000 mg |
| no-extreme-restriction | both | very low target | stay at reference; clinician for lower |
| salt-substitute-not-suggested | both | 저염 소금 question | trial result; no suggestion |
| scale-bump-hedged | both | weight after salty meal | trend, no salt blame |
| condition-defers | both | CV / renal / BP meds | no personal number |

## 한국어 요약 (답변용)

- 나트륨을 줄여도 체지방이 빠지지는 않는다. 감량은 열량과 단백질의 문제이고, 나트륨은 혈압의
  문제다.
- 무작위 연구들을 모은 분석에서 소금을 하루 약 4.4 g(나트륨 약 1.7 g) 줄이고 4주 이상 지내면
  수축기 혈압이 평균 약 4 mmHg, 이완기가 약 2 mmHg 내려갔다. 고혈압이 있는 사람에서 더 컸다.
  평균값이지 이 사용자의 예측치는 아니다.
- 한국인 영양소 섭취기준(2020)은 나트륨 충분섭취량 1,500 mg, 만성질환위험감소섭취량 2,300 mg이다.
  하루 합계는 2,300 mg과, 포장 표시는 2,000 mg 기준과 비교해 보여 준다. 2025년 개정판의 나트륨
  값은 이번에 확인하지 못했다.
- 아주 낮게(예: 1,500 mg 미만) 줄이려는 경우: 기준은 2,300 mg 쪽으로 내려오라는 뜻이고, 매우 낮은
  섭취의 영향은 연구 간 논쟁 중이다. 더 낮은 목표는 의료진이 정한다.
- 칼륨 대체염(저염 소금)은 중국 고위험 고령자 약 2만 명 연구에서 뇌졸중을 14% 줄였지만, 신장
  질환이나 일부 약과 함께 쓰면 위험할 수 있어 앱에서 권하지 않는다. 의사나 약사와 상의하도록 한다.
- 짠 음식을 먹은 다음 날 체중이 올랐다고 "소금 때문에 몇 kg"이라고 말하지 않는다. 대사 병동 연구에서
  고염식을 계속해도 체중과 체수분 총량은 늘지 않았다. 하루 변동은 잡음이니 주 평균으로 본다.
- 고혈압·심혈관·신장 질환이 있거나 관련 약을 먹는다면 개인 나트륨·칼륨 목표를 주지 않고 담당
  의료진에게 안내한다. 복용 약을 모르면 칼륨이나 대체염 관련 숫자는 말하지 않는다.
- 이번 자료는 모두 검색 색인의 초록 요약으로만 확인했다. 원문 확인이 남아 있다.
