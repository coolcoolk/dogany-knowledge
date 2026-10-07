# nutrition -- gap list

Split from the warehouse-level GAPS.md at warehouse v42 (module split,
warehouse v43, 2026-10-07). Section text below is unchanged; sections that
were appended at the end of the old file under another heading were refiled
here by their `### nutrition / ...` heading, as those blocks asked.

## nutrition

Dropped for quality: none dropped -- all five converted @obs-inferential rows are
verified 3-vote survivors. (The GRADE-inadequate position was CONTESTED, so it
shipped at C-equivalent with a contested flag rather than being dropped.)

Coverage the rubric names but batch1 does not supply:
- The nutrition lane is currently 4/5 field-METHODOLOGY items (observational
  dominance, eight fallacies, tool instability, GRADE-inadequate debate) + 1
  substantive claim (protein intake). It is heavy on "how to grade nutrition" and
  thin on graded substantive diet/supplement claims.
  -> Fetch substantive supplement/diet claims to grade through the lane: omega-3,
     vitamin D, creatine-for-nutrition-overlap, fiber, added-sugar, dietary-pattern
     (Mediterranean) outcomes. Encode tiny-effect (RR 0.95-1.05 -> C cap) and
     confounding downgrades per this lane's rules.
- MR ERRATA (inherited an internal ticket): Mendelian randomization is retained as a
  method-valid path to the A ceiling in the rubric, but batch1 did NOT empirically
  confirm any MR-backed claim. No MR-backed A item was authored (correctly).
  -> A future sprint must RE-SOURCE an MR-backed A claim before any ships; MR stays
     in the ceiling as a method, not deleted.
- NutriGrade parallel-run: the tool-instability item establishes the rule, but no
  item yet demonstrates an actual GRADE-vs-NutriGrade disagreement forcing a
  CONTESTED flag on a substantive claim. Fetch one worked case.

Filled 2026-09-02 (nutrition-lane collection sprint, v13):
- The lane's headline structural complaint above -- 4/5 field-METHODOLOGY items
  and 1 substantive claim, "heavy on how to grade nutrition and thin on graded
  substantive claims" -- is now PARTIALLY CLOSED. The lane goes 5 -> 15 items.
  The balance is deliberately not all-substantive: a consumer that reads a real
  meal log every day needs the MEASUREMENT items as much as the diet items,
  because the log is the instrument.
  - nutrition/self-report-underreporting-007 (@obs-inferential, A/field-methodology,
    not contested) -- recovery-biomarker validation across 5 pooled US cohorts.
    FFQ understates energy ~28%, single 24-h recall ~15%, protein less. The
    load-bearing part is that under-reporting is DIFFERENTIAL (predicted by BMI,
    age, education), so a flat correction factor would swap a known bias for a
    hidden one. A logged intake is a floor and a trend line, not an estimate.
  - nutrition/protein-per-meal-ceiling-008 (B, contested) -- a live printed
    dispute held against an already-shipped top-band item. Trommelen 2023
    (quadruple tracer, n=36 recreationally active young men, 25 vs 100 g) reports
    no upper limit in magnitude or duration; Witard & Mettler 2024 dispute the
    practical reading and state it does not extend to resistance-trained young
    women; Trommelen replied in print. Deliberately UNRESOLVED. The only
    consumer-facing change is a de-escalation: there is no longer a defensible
    basis for warning a user that protein above ~40 g in one sitting is wasted.
  - nutrition/protein-distribution-thin-009 (C, contested) -- the even-distribution
    concept, traced. Positive result is an n=8 acute crossover; an 8-week RCT
    (n=14) and a further RCT (n=24) both returned null at real outcomes; the
    review-level positive association does not extend to strength or turnover.
  - nutrition/energy-availability-threshold-010 (C, contested) -- the 30 kcal/kg
    FFM cut-off, with the 2023 IOC consensus statement's own walk-back quoted
    verbatim, its n=29 / 5-day / sedentary-female origin named, and the
    male range (~9-25) recorded as lower and less understood.
  - nutrition/body-composition-measurement-floor-011 (B, not contested) --
    instrument-limit item bounding what any body-composition reading can confirm.
  - nutrition/weight-loss-rate-lean-mass-012 (C, contested) -- the 0.5-1 %/wk
    rule traced to one unblinded n=24 trial with a duration confound.
  - nutrition/fibre-doseresponse-013 (C, not contested) -- Lancet 2019 fibre
    series. Partially answers the "fetch substantive diet claims" request above:
    fibre was chosen over the other named candidates (omega-3, vitamin D, added
    sugar, Mediterranean pattern) because it is the one with BOTH a large
    prospective base and a randomised arm, so the lane's observational discount
    lands on something rather than on everything. The item records explicitly why
    the RR 0.95-1.05 cap does NOT apply to it.
  - nutrition/kr-reference-intakes-2025-014 (A/jurisdictional-standard, LOCALE KR).
  - nutrition/metabolizable-energy-atwater-015 (B, not contested) -- measured
    metabolisable energy vs Atwater prediction for tree nuts.
  - nutrition/kr-food-composition-accuracy-016 (C, contested, LOCALE KR).

- KR-LOCALE CHECK RUN, and it changed the answer. This is the first pass to
  check the Korean case for this lane, and two findings came out of it.
  1. STALENESS. Korea revised its national reference standard on 2025-12-31
     (2025 KDRIs, MOHW with the Korean Nutrition Society, statutory 5-year
     cycle). Protein AMDR moved 7-20% -> 10-20%; fibre was re-derived on a new
     12.5 g/1000 kcal basis. Every 2020-edition Korean figure in circulation,
     including ones a model would recite from memory, is a prior edition. Item
     014 carries this as its first refraction note.
  2. DATABASE ACCURACY. Exactly one chemical validation of the Korean food
     composition tables was located (n=66 women, Jeju, 2003): energy 98%,
     protein 101%, lipid +24%, carbohydrate -8%. Its answer is convenient for a
     protein-focused consumer, which is precisely why it ships at the
     observational band with a contested flag rather than as reassurance.

WHAT THE FILL DOES NOT DO: it does not give the consumer a trustworthy number
for what the user actually ate. Three INDEPENDENT error sources now sit on
record between a logged Korean meal and the truth -- self-report bias (007),
composition-table bias (016), and the composition-to-available-energy conversion
(015) -- and they do not cancel in any known ratio. Netting them off against each
other is explicitly forbidden on item 015. The lane can now say how the number is
wrong; it still cannot say what the right number is.

REFUSED THIS SPRINT (recorded rather than dropped, v7/v9 rejected-claim
discipline). Each of these was searched, not assumed:
- RATE-OF-MUSCLE-GAIN TABLES ("a beginner can gain 1-1.5% of body weight per
  month", and the tiered ladders by training age). A targeted search for any
  primary study measuring a maximum or typical rate of lean-mass gain returned
  ZERO results. These numbers are practitioner-authored and have no trial behind
  them anywhere. REFUSED OUTRIGHT -- must never be spoken as research. This is
  the nutrition-side twin of the v9 load-increment finding: the field's most
  confidently quoted number is one nobody has measured.
- CONSUMER FOOD-TRACKING-APP DATABASE ACCURACY. Located studies are n=37
  Filipino adults with obesity and an Australian app-store quality survey.
  Nothing KR-applicable, nothing adequately powered. REFUSED.
- KOREAN MIXED-DISH LOGGING ERROR (jjigae, guk, bibimbap and other composite
  servings). No primary source quantifies portion or nutrient error for Korean
  composite dishes as logged by a consumer. This is the single sub-topic where
  the consumer most needs a number and where there is none. REFUSED, and NOT
  inferred from item 016, which measured correctly identified duplicate portions
  and therefore removes exactly the error this question is about.
- SODIUM AND THE KOREAN DIET. The most obviously Korea-specific nutrition
  question. Outcome evidence is genuinely disputed and needs its own adversarial
  pass. NOT RESEARCHED; its absence is flagged on item 014 so it cannot be read
  as an all-clear.
- MEAL FREQUENCY and INTERMITTENT FASTING. Out of this sprint's brief. Recorded
  as UNTOUCHED, not as absent.

RESIDUAL SUB-GAPS carried out of this sprint, each recorded on the relevant item
and each genuinely unfilled:
1. No Korean-language validation of a consumer meal log against recovery
   biomarkers exists. The direction of self-report bias transfers; the
   percentages do not, and item 007 says so rather than importing them.
2. No adequately powered trial has tested even-vs-skewed protein distribution to
   a HYPERTROPHY endpoint in young resistance-trained adults. Both controlled
   trials are in older adults, because the question is funded as a sarcopenia
   question. Item 009.
3. The per-meal protein ceiling dispute has no trial in resistance-TRAINED
   people, and the published counter-comment asserts the finding does not extend
   to resistance-trained young women. Item 008.
4. No least-significant-change figure exists for consumer bioimpedance under
   uncontrolled home or gym conditions. All precision data are standardised
   laboratory protocols. Item 011 states the direction and DECLINES to publish a
   threshold rather than importing a laboratory one.
5. Rate of weight loss has never been tested with equal-duration arms, so rate
   and training exposure remain confounded in the only trial that exists. No
   data at all outside the two rates tested. Item 012.
6. The Korean composition-table validation has no modern replication and covers
   one regional diet in 66 women from a 2003 publication, against table editions
   since revised. Item 016.
7. No safety-axis review was done for the deficit and energy-availability items.
   A hard gate on pregnancy_status for deficit advice is arguably correct but
   would have been authored from judgment rather than from a source, so it was
   deliberately NOT added. Flagged for a designed decision rather than left as a
   silent omission.

STILL OPEN after this sprint, unchanged: the MR ERRATA below (no
Mendelian-randomization-backed claim was sourced this pass, so the top band still
has no MR-backed item and MR remains a method in the ceiling rather than a
demonstrated path) and the NutriGrade parallel-run worked case below (no item yet
demonstrates an actual GRADE-vs-NutriGrade disagreement forcing a contested flag
on a substantive claim; the five contested items shipped here are contested on
evidence grounds, not on tool-disagreement grounds).

Filled 2026-10-06 (meal-protein sprint, v37):
- nutrition/protein-deficit-lean-mass-target-062 (B, contested on the upper end)
  -- 1.6-2.4 g/kg body weight in a deficit with resistance training; older-adult
  floor 1.0-1.2 (1.2 when active or dieting); hard gate on stated CKD.
- nutrition/meal-protein-nudge-rules-063 (@meal-craft, D synthesis) -- structured
  target_bands / per_meal_dose / nudge_rules for the meal module.
- RE-AUDIT FINDING, applied to nutrition/protein-intake-002: the hypocaloric
  "2.3-3.1 g/kg" band is per kg FAT-FREE MASS in its source (Helms 2014); the
  ISSN 2017 stand dropped the qualifier and 002 spoke it against body weight.
  Corrected; 002's grade and general range untouched (Morton 2018 and Nunes 2022
  still put the energy-balance benefit near 1.6 g/kg).

RESIDUAL SUB-GAPS from the meal-protein sprint, each genuinely unfilled:
8. The deficit-specific trials are small and short (n=39-40, 4-5 weeks) and the
   only deficit dose-response synthesis (Refalo 2025) is self-described as
   exploratory, with a body-weight slope interval that crosses zero. No trial
   compares 1.6 vs 2.4 g/kg head-to-head over a cut longer than ~8 weeks in
   trained people. Item 062 holds the upper end as guidance, not evidence.
9. No trial tests the 1.6-2.4 band in OLDER adults who are dieting. The
   older-adult floor is expert consensus (PROT-AGE, ESPEN) plus a 20-RCT
   weight-loss meta-analysis using a >=1.0 g/kg or >=25% energy split. Item 062
   speaks 1.2 g/kg as the older dieter's floor and labels the band an
   extrapolation.
10. The older-adult per-meal figure (0.4 g/kg) rests on one retrospective pooled
    tracer analysis in men, with the body-mass difference vs young borderline
    (p=.055). No outcome trial has used it. PROT-AGE itself calls timing evidence
    insufficient. Item 063 uses it only to size an add-on.
11. Pre-sleep protein: one RCT (Snijders 2015, n=44 young men) without matched
    daily protein, so it cannot separate timing from the extra 27.5 g. A
    pre-sleep meta-analysis was not read at a primary this pass. Item 063 offers
    it as an option only.
12. No source located for a protein gate on pregnancy_status or on users under
    18; neither gate was added (same discipline as sub-gap 7). Plant-only
    (dietary_pattern) protein quality was not graded this pass; one 2026
    narrative review was seen, no meta-analysis read.
13. Item 063's window (7 days), minimum (4 logged days), margin (0.9 x floor)
    and nudge cap (1/day) are product constants with no evidence; tune them on
    the user's log rather than re-sourcing them.
14. Refalo 2025 (Strength Cond J) is not PubMed-indexed; its abstract was read at
    the AUT open repository. The 2026 Sports Med commentary re-analysing it
    (baseline protein as moderator) is opinion plus exploratory re-analysis.


Rerun-needed: none (batch1 nutrition rows verified 3-0).

Added v37 (2026-10-07, cut-protein sprint):
- nutrition/protein-deficit-trained-lifter-023 (B, contested at the top of the
  band) and nutrition/protein-timing-total-matched-024 (B); item 002 re-audited
  (deficit band unit = per kg fat-free mass).
- OVERLAP (found at the v37 merge): the cut-protein sprint ran in parallel with
  the meal-protein sprint, whose nutrition/protein-deficit-lean-mass-target-062
  already owns the deficit target band (1.6-2.4 g/kg BW, same core trials).
  023 does not restate a different band; it carries the trained-lifter reading
  of the two engine numbers (Morton's 2.2, Schoenfeld & Aragon's 0.4 / 0.55),
  the FFM unit guard and the renal gate as protein_rules for diet-status. A
  later audit may fold 023's rules into 062 (one home for the band).

Searched and not closed:
1. No RCT in RESISTANCE-TRAINED lifters in a deficit compares 1.6 with 2.2-2.4
   g/kg body weight. Pasiakos 2013 (1.6 = 2.4) is in non-lifters; Mettler 2010
   and Longland 2016 compare ~2.3-2.4 only with ~1.0-1.2. The choice inside
   the 1.6-2.4 band is judgement. What would close it: a cut-length (8+ week)
   RCT in trained lifters, 1.6 vs 2.4 g/kg, lean mass by 4C or DXA.
2. All deficit trials located ran 2-4 weeks with 20-40 people. Nothing on a
   12-week contest-style cut except case series. Effect sizes not transported.
3. Longland 2016's registry entry does not record resistance-training
   history; the trained-status of its sample is unverified here.
4. No timing trial (pre/post, bedtime, distribution) was located that ran in
   a calorie deficit in trained lifters. "Timing matters more in a cut" is
   untested theory (024 note 2).
5. Bedtime protein with daily totals matched: one trial, n=13 (Joy 2018).
6. KOREAN PER-MEAL PROTEIN PROFILE OF YOUNG ADULTS. The only KNHANES study of
   protein across meals located is adults 60+ (Park 2018: even but low). No
   per-meal protein profile for Korean 19-39-year-olds, let alone lifters.
7. The 62.1% breakfast-skip figure (age 19-29, KNHANES 2024) is taken from a
   press report (Segye Ilbo 2026-06-09) of the KDCA release; the KDCA table
   itself was not retrieved. Replace with the KDCA fact-sheet URL next pass.
8. Renal gate rests on KDIGO 2024 Practice Point 3.3.2 (ungraded), read via
   the NephJC summary, not the guideline PDF. No evidence was sought on
   high protein in people with normal kidney function beyond noting none was
   found; that is not an all-clear search and is not spoken as one.

ENGINE MISMATCH -- RESOLVED in product 0.33.0 (the diet-status code):
- the 2.2 g/kg day clamp no longer binds in a cut: a cut-day goal is honoured
  up to 2.4 g/kg (023 rule no-evidence-ceiling-at-2.2, cut-band-high); a goal
  under 1.6 g/kg is flagged (`below_cut_floor`, rule cut-floor), not silently
  raised -- the goal stays the one the diet card draws. Outside a cut the 2.2
  cap stays, labelled a product choice.
- 0.4 / 0.55 g/kg per meal are described as split targets (rule
  per-meal-is-a-target); the late-night line no longer says a big meal is not
  used. The one-meal nudge size is kept as a tractability convention.
- FFM figures (2.3-3.1 g/kg FFM, rule ffm-unit-guard) only with a body-fat
  record (kit fat_mass_kg stored, not the code default).
- renal gate: a known kidney condition (kit `renal_condition` other than
  none / healthy) withdraws the cut band (rule renal-gate).
- the diet-status reference: per-meal saturation now graded B,
  disputed (008), matching this warehouse.
STILL OPEN (engine): the kit has no renal_condition capture step; the gate
reads the key only when something wrote it.

Body-composition measurement sprint (v38, 2026-10-07) -- filled and open:
- FILLED (partly): nutrition/bia-day-to-day-noise-028 supplies the PRECISION
  side that 011 left out: InBody 770 between-day least significant change
  under fasted lab conditions, kilogram-scale spans in unchanged adults,
  meal / water / standing effects, and the weekly weight rhythm.
  nutrition/body-measure-reading-rules-029 turns it into engine-readable
  noise_bands / measure_rules / cadence for the retro and brief copy (field
  guide the measure-rules field guide (not public)). Its weekday-not-diet rule and
  the diet-adherence sprint's like-day-comparison (074, below) say the same
  thing on two surfaces and are cross-linked.
- STILL OPEN, narrowed: residual sub-gap 4 above. The only InBody
  least-significant-change figure located (2.8 %BF / 1.9 kg FM / 2.4 kg FFM)
  is a CONFERENCE ABSTRACT (Siedler 2021, Int J Exerc Sci Conf Proc, n=17),
  fasted lab visits within 48 h. A full peer-reviewed between-day LSC for an
  InBody-class device, and ANY LSC for unstandardised gym / home conditions,
  is still missing. 029's speak bands are product constants rounded up from
  that floor.
- OPEN: no published least-significant-change for InBody skeletal muscle mass
  (SMM). 029 uses a 1.5 kg product band from the 3-week span in Looney 2024
  (1.0 +/- 0.4 kg); a sprint should fetch an SMM-specific precision study.
- OPEN: no precision figure for a 7-day MEAN of home body weight (mean-to-mean
  difference). The 0.5 kg weekly-mean band and the 1.0 kg single-pair band in
  029 are product judgement over Looney 2024 (between-morning 0.1-0.7 kg) and
  Turicchi 2020 (0.35 pct weekly swing).
- OPEN: no trial compares body-composition scan cadences (weekly vs monthly)
  for adherence or decisions; 029's 2-4 week cadence is arithmetic over the
  band and the rate convention (012), not evidence.
- OPEN: menstrual-cycle effects on InBody readings were not searched this
  sprint (fluid shifts are plausible); 029 does not gate on cycle phase.
- OPEN: home foot-to-foot / hand-to-foot consumer scales (non-InBody) were
  not covered; 028's numbers are InBody 770 / 720 class only. The Siedler
  abstract's Omron figures (precision error 0.6 %BF, 0.4 kg FM, 0.6 kg FFM)
  were read but not adopted.
- READ AND NOT USED: Koch 2022 (Iowa Orthop J, InBody S10) -- same-day
  inter-rater MDC (4.05 kg FM, 4.83 %BF) in orthopaedic-trauma inpatients;
  population and protocol not transportable.

Filled 2026-10-07 (diet-adherence sprint, v38): nutrition/flexible-vs-rigid-restraint-025
(C), nutrition/diet-breaks-refeeds-026 (B, contested),
nutrition/self-monitoring-frequency-027 (C), nutrition/weekend-drift-073 (C),
and the engine-readable synthesis nutrition/adherence-rules-074 (@meal-craft,
D; field guide the adherence-rules field guide (not public)). Searched and NOT closed:
1. RESTRAINT STYLE HAS NO OUTCOME TRIAL. Every flexible-better finding is a
   questionnaire correlation; the only RCT (Conlin 2021, n=23, 10 weeks)
   manipulated food-list flexibility, not restraint style, and was null on
   loss. What would close it: a trial that randomises restraint framing and
   follows binge episodes and weight for 6+ months.
2. DIET BREAKS: two populations, two answers. MATADOR (obese men, provided
   food, per protocol) vs ICECAP (trained adults, ITT). No trial in
   free-living adults with overweight choosing their own food, none in
   women with overweight, none comparing break lengths or block ratios. The
   3:1 block in 074 is ICECAP's protocol, labelled a constant. MATADOR's
   ongoing follow-up (ACTRN12615000116527) was not located as published.
   No meta-analysis of diet breaks specifically (as opposed to all
   intermittent restriction) was read this pass.
3. REFEEDS: one 27-person trial, fat-free-mass effect disputed in print
   (Peos comment / Campbell reply). Not resolvable from what exists.
4. SELF-MONITORING DOSE: no trial randomises logging or weighing frequency
   with everything else held fixed; "N days a week" thresholds are
   engagement cut-offs. 074 publishes no minimum.
5. EATING-DISORDER SAFETY AXIS: the self-weighing harm signal (Pacanowski
   2015) argues for a gate, and the ledger has no eating-disorder-history
   axis. axes.yaml is framework-owned and append-only, so none was added;
   074's weighing-exit is a conversational trigger until a designed axis
   exists (029's daily weight cadence yields to it). Same open question as
   residual sub-gap 7 above (deficit advice).
6. KOREAN WEEKEND AND HOLIDAY DATA: all weekend-drift figures are US or
   European (and the US recall counts Friday as weekend). No KNHANES
   weekday/weekend intake comparison and no 명절 weight-change study was
   located in this pass. 073 uses the user's own logged gap instead.
7. Orsama 2014 lists a co-author with multiple retracted papers; no notice
   on this paper in Europe PMC (checked 2026-10-07). Its figure is not
   quoted; Turicchi 2020 carries the number.

Alcohol and training (v38, 2026-10-07):
Shipped: nutrition/alcohol-training-recovery-dose-031 (sleep B, muscle
direction B / magnitudes C, energy A/B, alcohol_rules for copy) and
nutrition/kr-alcohol-units-drinking-pattern-032 (KR; KDCA rates A, unit
arithmetic A, Korean guideline thresholds D; field guide
the alcohol-rules field guide (not public)). These partly close leisure OPEN WANTS
1-3 (units, Korean base rates, alcohol and sleep). Still open:
1. MONTHS-LONG LIFTING TRIAL. No trial ran resistance training for weeks to
   months with social drinking as the randomised exposure and measured
   hypertrophy or strength. BEER-HIIT (10 weeks, HIIT circuit, alcohol
   self-selected, ~14 per arm) is the only training-length study. Until one
   exists the muscle rules speak only of acute recovery.
2. MPS AT SOCIAL DOSES. Measured myofibrillar synthesis exists only at
   1.5 g/kg (Parr 2014, n=8 men). Nothing at 0.5-1.0 g/kg, nothing in women,
   nothing in older lifters. Duplanty 2017 (signalling, sex difference) was
   read at abstract only; its doses were not confirmed.
3. NEXT-DAY PERFORMANCE / HANGOVER. Whether strength or session quality the
   day after an evening of drinking (not after eccentric damage) is reduced,
   and by how much, was not searched. The strength-recovery rule leans on the
   Barnes eccentric-damage model only.
4. TESTOSTERONE / CORTISOL. Not researched; deliberately left out of the
   rules because acute hormone changes are a weak proxy for adaptation
   (same reasoning as exercise/emg-not-hypertrophy-proxy-013).
5. OBSERVATIONAL WEIGHT GAIN BY DRINKING PATTERN. Cohort data on drinking
   frequency vs quantity and weight change (and the Korean 안주 / 2차 pattern
   in particular) not read. The fat-loss rule rests on energy arithmetic,
   Kwok 2019 and Siler 1999 only. (Weekend drinking as part of the weekend
   energy gap: 073, cross-linked.)
6. KOREAN DRINKING CULTURE BEYOND RATES. 회식, 2차/3차, 소맥 ratios, 잔 돌리기:
   no primary with numbers was read. The soju glass (~50 mL, ~7 per bottle)
   is labelled a convention. The 2019 Korean guideline original (Lee S et
   al., Korean J Fam Med 2019;40:204-211) was cited via JKMA 2024, not read.
   A KDCA / Ministry of Health and Welfare 절주 guideline from the issuing
   body was still not located.
7. KNHANES VS CHS. 032 carries the 2025 Community Health Survey rates (KDCA
   press release). KNHANES publishes its own 월간음주율 / 고위험음주율 with a
   different design; a search snippet quoted 58.3 percent monthly drinking
   for 2024 KNHANES that was not confirmed at the primary and is not carried.
8. ALDH2 AND MUSCLE / SLEEP. Whether flushers' sleep or recovery responds
   differently per gram is unstudied in what was located; 031 does not lower
   its bands for flushers. The Korean guideline's halving is a health-risk
   rule and is carried only in 032.

Protein distribution re-audit (v44, 2026-10-07) -- filled and open:
- NEW: nutrition/protein-distribution-while-dieting-090 (B) holds the trials
  that varied the split of protein across meals during energy restriction
  (distribution_rules: split-not-a-lever-in-a-cut, even-split-hunger-option,
  meal-count-is-free, say-what-was-tested). nutrition/pre-sleep-protein-
  matched-trials-091 (C, contested) takes the pre-sleep detail out of 024
  (pre_sleep_rules: fill-slot-only, no-bonus-on-a-met-day, not-an-appetite-
  tool, not-a-metabolism-tool, log-its-energy, sleep-claim-withheld,
  population-guard). Both rule blocks use the same fields as 024's
  timing_rules: rule, when, effect, basis, basis_grade. No program code or
  field guide was written; a diet module that reads timing_rules can read these.
- RE-AUDITED IN PLACE: 009 (its "wrong population" limit and "nobody has
  tested" sentence were out of date; letter and contested flag unchanged),
  008 (the placebo arm and 12 per arm were missing from the body; trained-men
  and young-female dose data added), 024 (Casuso 2025, Lak 2024, Wycherley
  2010; the no-timing-trial-in-a-deficit note narrowed to trained lifters), 002
  (the per-meal clause is separated from the daily range that carries the top
  band and pointed to 008), 063 (two rule bases cite 090 / 091; no rule,
  constant or letter changed).
- SUPERSEDES, in part: residual sub-gap 2 above ("both controlled trials are in
  older adults") and items 4 and 5 under the v37 cut-protein block ("no timing
  trial ... in a deficit", "bedtime protein with totals matched: one trial").
  Dieting adults, young men new to lifting and resistance-trained men have now
  been tested, each in small trials, and four matched bedtime comparisons
  exist; the lifter-on-a-cut cell is still empty (open 1).
Searched and not closed:
1. LIFTER ON A CUT. No RCT varies the protein split, the timing around a
   session or protein before sleep in resistance-trained people in a calorie
   deficit at 1.6-2.4 g/kg. Every dieting trial located (Hudson 2017, De Leon
   2024, Lombardo 2021 for the split; Wycherley 2010 for before-vs-after
   training, in type 2 diabetes) is in overweight adults at about 1 g/kg. What
   would close it: an 8-12 week cut in trained lifters, protein fixed at
   1.6-2.4 g/kg, three even meals vs a dinner-heavy split (and a no-breakfast
   arm), lean mass by four-compartment model or DXA, with a stated minimum
   detectable difference.
2. NO BREAKFAST. No trial removed breakfast protein entirely; the skewed arms
   still ate 10-15 g. The usual young Korean day (62.1 percent of 19-29-year-
   olds skip breakfast, press-reported) is untested for lean mass in a
   deficit. A time-restricted-eating trial in resistance-trained people exists
   (Gavanda 2026, n=23, 16:8, a bulk not a cut, lean-mass gain kept at 1.44
   g/kg protein) but it is not a split comparison and was read at abstract
   level only.
3. POWER. The three dieting trials have 41-47 completers and Hudson's authors
   flag power. Yasuda 2020 powered itself for d=1.5 and analysed 26 of 33;
   Tavares 2025 randomised 32 and analysed 18. A pooled analysis of the
   even-vs-skewed trials with body-composition outcomes (none located) is the
   cheap next step.
4. APPETITE SIGNAL. De Leon 2026 (44 women, lab snack task) was read at
   abstract level and is the only trial of the split on appetite or adherence
   outcomes. No trial in men or lifters, no free-living snack intake. 090's
   hunger-tactic rule is the weakest rule in that item.
5. PRE-SLEEP. The matched comparisons are small (13, 26, 24, 42) and Antonio 2017
   has no unsupplemented arm. The Zhou 2024 network meta-analysis (116
   trials; night protein best for strength) was read at abstract level only
   (the publisher page returned 403), so how many trials sit in its night
   node, and whether any matched protein, is unknown here. No pre-sleep trial
   on lean mass during a cut. Next-morning appetite and metabolic rate rest on
   Kinsey 2014 (44 women, one night) and Madzima 2018 (9 women, magnitude-
   based inference); the Snijders 2019 review says no change in either.
6. SLEEP SIDE OF BEDTIME PROTEIN. Aussieker 2026 (9 resistance-trained
   adults, crossover) found whey, but not casein, separated from an isocaloric
   control on sleep latency and efficiency; the abstract reports no
   significant whey-casein difference; not replicated. For the sleep-recovery
   module: its late-evening row (sleep-recovery/late-night-next-morning-
   training-080) does not cover protein drinks.
7. PER-MEAL CEILING IN TRAINED PEOPLE AT HIGH DOSE. Trommelen 2023 is 12 men
   per arm and not resistance-trained; MacNaughton 2016 (trained men) went to
   40 g; Apicella 2025 (young females) to 20 g. The Witard and Mettler comment
   and the Trommelen reply were not re-read (publisher pages returned 403), so
   008's account of the printed dispute is as summarised when it was authored.
8. KOREAN PER-MEAL PROFILE AND BREAKFAST SKIPPING. Still no per-meal protein
   profile for Koreans aged 19-39 (searched again 2026-10-07, nothing found).
   The breakfast-skip rates (35.3 percent overall, 62.1 percent at 19-29,
   46.8 percent in the 30s) are press-reported from the 2024 KNHANES. The
   KDCA release of the 2025 survey (2026-09-30, kdca.go.kr/bbs/kdca/42/
   312791/artclView.do with its two PDFs) carries no breakfast table, and the
   2024 statistics compilation (announced in the KDCA press note of
   2025-12-31) was not retrieved. Replace the press source with that table.
9. LAK 2024. The 2025 correction replaced the ethics-approval body and number
   in the Methods and the Ethics Statement and states no reason; results were
   not changed. The trial was used only as a low-weight supporting comparison
   in 024.
10. READ AT ABSTRACT LEVEL ONLY (numbers outside an abstract were not checked):
   De Leon 2024 and 2026 (protocol from the NCT03202069 registry record),
   Lombardo 2021, Murphy 2018, Tavares 2025, Casuso 2025, Antonio 2017,
   Valenzuela 2023, Chen 2022, Pourabbas 2021, Chapman 2023, Klemp 2025,
   Ormsbee 2022, Kinsey 2014, Madzima 2018, Dela Cruz 2021, Reis 2021, Zhou
   2024, Aussieker 2026, Apicella 2025, MacNaughton 2016. Read at full text:
   Yasuda 2020, Lak 2024, and the Trommelen 2023 methods; Hudson 2017 only
   through a summarising fetch of its PMC page.

## nutrition -- craft lane (@meal-craft)

Added v21 (2026-09-02, nutrition craft-lane opening). This is a SECOND
section for the nutrition domain; the evidence-lane section above (`## nutrition`)
stays authoritative for @obs-inferential and is not superseded. Five items
(017-021) open @meal-craft, VC-E.

WHY THE LANE EXISTS. Before this release, exercise had three lanes, cooking had
two, and every other domain in the warehouse had exactly one -- the evidence
lane. What @gym-craft carries is the reason the exercise domain is usable: how
big a warm-up jump may be, how to cue a muscle that will not fire, what to do
when the plan does not survive contact with the gym floor. None of that is in a
paper. nutrition shipped 15 evidence items in v13 and zero craft items, while the
consumer reads a user's meal log every single day. The evidence lane can now
say precisely how the logged number is wrong; it had nothing at all on what to do
about it.

THE STANDARD APPLIED. VC-E is a different standard, not a lower one. Each item
names its basis and marks the untested part as untested:
- nutrition/log-reask-multiple-pass-017 (@meal-craft, practitioner-protocol band,
  not contested) -- the USDA Automated Multiple-Pass Method's five passes, quoted
  verbatim from the publisher's own description: Quick List, Forgotten Foods, Time
  and Occasion, Detail Cycle, Final Probe. The craft content is the ORDER --
  omission is chased in a dedicated pass before any question of quantity, and
  amount is asked last. Validated against doubly labelled water in 524 adults
  (Moshfegh 2008): still 11 percent short overall, under 3 percent in
  normal-weight subjects, worst in obese subjects. The transfer to a chat-based
  self-log with no interviewer and no food model booklet is UNTESTED and the item
  says so. Also refuses to publish a numeric re-ask trigger, and routes instead
  to structural absence (a missing eating occasion) because the shortfall is
  person-dependent.
- nutrition/portion-estimation-shape-ceiling-018 (observational band, CONTESTED as
  under-evidenced) -- Gibson 2016, n=67, 42 pre-weighed foods. The best unaided
  technique put 80 percent of GEOMETRIC foods within 25 percent of true weight and
  only 13 percent within 10 percent; household cups and spoons managed 29 percent
  within 25 percent. For amorphous foods (cereal, mashed potato, muffin, RICE) not
  one estimate was within 10 percent and exactly one was within 25. For irregular
  protein pieces (fish fillet, chicken breast, beef steak) both methods were off by
  more than half. So portion estimation is a plus-or-minus-25-percent instrument at
  its ceiling, and it fails on exactly the two things a Korean training plate is
  made of.
- nutrition/unlogged-day-not-zero-019 (operating rule, empirically anchored, not
  contested) -- Fraser 2009: 2091 participants re-contacted, 92 percent of missing
  items recovered, and for frequently consumed foods most blanks were NOT zeros,
  with missingness non-random; the authors' stated conclusion is that automatic
  zero imputation will usually be incorrect. Rule: mark unknown, never write zero,
  never let an unknown day into an average or a streak or a trend, reconstruct only
  inside the previous-day window the recall instrument was actually validated for.
  Cross-domain corroboration of the MECHANISM ONLY from
  spending-saving item 003 (module not published): a decaying self-kept diary
  fails by emitting zeros, not smaller numbers. No rate imported.
- nutrition/kr-mixed-dish-logging-unit-020 (professional-tool convention, LOCALE
  KR, not contested) -- the item this lane was opened for. Two published Korean
  units coarser than grams: the clinical exchange system (식품교환표, per-exchange
  content quoted exactly from the Korean Diabetes Association) and the Ministry of
  Food and Drug Safety's measured restaurant-dish dataset (외식 영양성분 자료집,
  108 dishes in volume 2 alone). Rule: log a composite dish by NAME against a
  measured whole-dish entry or in exchange units; never itemise a 찌개 into grams.
- nutrition/kr-protein-exchange-counting-021 (professional-tool convention, LOCALE
  KR, not contested) -- protein against real Korean food. A meat-and-fish exchange
  is 8 g of protein at any fat tier, milk 6 g, grain 2 g, vegetable 2 g, fruit and
  fat none. A 밥 + 국 + 나물 meal of two grain and two vegetable exchanges is about
  8 g of protein in total, so a training target is met almost entirely on the 반찬
  side and essentially not at all by the 주식. Count exchanges, not grams.

WHERE CRAFT AND EVIDENCE DISAGREE. Recorded in the open rather than resolved by
quietly picking a side.
1. THE FLAT CORRECTION FACTOR. Adding a fixed percentage to a client's food log
   ("assume they ate 15-20 percent more than they wrote") is ordinary coaching
   practice. This warehouse's evidence lane forbids it:
   nutrition/self-report-underreporting-007 shows the bias is DIFFERENTIAL, and
   the AMPM validation independently reproduces that by body-mass group (under 3
   percent in normal-weight subjects, worst in obese subjects, from a completely
   separate pool of studies). A flat factor would replace a known bias with a
   hidden one. REFUSED. Evidence wins; the craft practice does not ship.
2. THE PER-MEAL EVEN-DISTRIBUTION PRESCRIPTION. Practitioners near-universally
   teach roughly four meals of 30-40 g. The evidence lane does not support it:
   nutrition/protein-distribution-thin-009 traces the concept to an n=8 acute
   crossover with two later randomised trials null at real outcomes, and
   nutrition/protein-per-meal-ceiling-008 removed the basis for the
   above-40-g-is-wasted warning. NEITHER SIDE IS SUPPRESSED: item 021 keeps a
   per-meal split, re-bases it explicitly on logging tractability and adherence,
   and forbids the physiological justification. Anyone stating the split must say
   which justification they are using.
3. A MAGNITUDE ORDERING THAT READS AS A DISAGREEMENT AND SHOULD BE SAID OUT LOUD.
   nutrition/kr-food-composition-accuracy-016 reports that the Korean tables
   validated cleanly for energy and protein. That is true and it is nearly
   irrelevant to a real Korean log, because item 018 shows the dominant error sits
   UPSTREAM of the table, in the portion, on exactly the amorphous staples the
   plate is built from. The convenient half of 016 invites precisely the wrong
   conclusion, and craft's job here is to say the table is not the problem.
4. A NUMERIC TENSION, not a contradiction. The AMPM's own validation reports an 11
   percent energy shortfall; item 007's pooled figure is about 15 percent for a
   single 24-hour recall and about 28 percent by food frequency questionnaire.
   Same direction, different pools, different instruments. Neither number may be
   quoted as "the" under-reporting figure.

REFUSED THIS SPRINT (recorded rather than dropped, v7/v9/v13/v18 rejected-claim
discipline). Each was searched, not assumed. THE REFUSALS ARE THE POINT OF A
CRAFT LANE: a craft lane is not a licence to ship folklore because no study
exists.
- KOREAN MIXED-DISH LOGGING ERROR, any figure. The evidence lane already refused
  this in v13 and the refusal STANDS. Craft does not fill an evidence hole by
  being confident. Item 020 ships the handling instead of the number, and states
  in its own body that item 016 cannot be extrapolated into one because that
  study's design removed exactly the portion and identification error in question.
- SHARED-DISH APPORTIONMENT. No published method was located for apportioning a
  shared Korean serving (공유 찌개, 공유 반찬). Item 020 ships a bounded-omission
  convention -- count what you can name, mark the shared broth present-but-uncounted
  -- and explicitly labels it the weakest thing in the item. It is chosen because
  its error has a KNOWN SIGN (undercount, same direction as every other error in a
  food record), NOT because it is accurate. An invented apportionment fraction
  would have an unknown sign and would destroy that property.
- KOREAN 눈대중량 / 손대중 PORTION TABLES. Searched directly. Everything located
  was blog posts and community-cafe reposts with no traceable origin. REFUSED
  OUTRIGHT. The only fetched primary on hand-based estimation is Gibson 2016,
  which is Australian, uses investigator-chosen foods, and reports outright
  failure on rice. What would close it: a Korean validation of visual or
  hand-based portion estimation against weighed reference portions of Korean
  foods.
- THE FLAT LOG-CORRECTION FACTOR. See disagreement 1 above. Refused.
- "ADJUST FROM THE OBSERVED WEIGHT TREND, NOT FROM THE LOGGED NUMBER." This is
  the single most useful craft rule a coach would state, and it was hunted for.
  The obvious citable source, Helms ER, Aragon AA, Fitschen PJ, J Int Soc Sports
  Nutr 2014;11:20, was READ DIRECTLY and does NOT contain the recommendation --
  it says only that intake will need adjusting over time as metabolic adaptation
  occurs. REFUSED rather than attributed to a paper that does not say it. Recorded
  here so a later pass does not re-attribute it. What would close it: a peer-
  reviewed practitioner recommendation or position stand that actually states
  outcome-driven adjustment. Note that the rate-of-loss figure often bundled with
  this rule is already owned, and already discounted, by
  nutrition/weight-loss-rate-lean-mass-012.
- RESTAURANT PORTION MULTIPLIERS ("a restaurant serving is N times a standard
  serving"). Not sourced. Item 020 routes 외식 to the ministry's measured
  named-dish values instead, which is a real number rather than a ratio.
- RECONSTRUCTION BEYOND THE PREVIOUS DAY. No instrument with any validation
  reaches further back than the previous day. Item 019 caps reconstruction there
  and deliberately publishes NO accuracy expectation for older reconstruction
  rather than offering a softened one.
- CONSUMER FOOD-TRACKING-APP DATABASE ACCURACY. Already refused in v13 (nothing
  KR-applicable, nothing adequately powered). NOT re-attempted this pass;
  recorded as untouched, not as absent.

RESIDUAL SUB-GAPS carried out of this sprint, each recorded on the relevant item:
1. The probe list inside the AMPM Forgotten Foods pass lives in the instrument,
   not in its published description, and was not retrieved. Item 017 carries the
   EXISTENCE and POSITION of that pass and deliberately does not invent its
   contents. What would close it: the AMPM instrument documentation itself.
2. No study compares itemised against whole-dish logging of a composite dish, in
   any population, for accuracy or for adherence. Item 020's central rule is
   argued from the measurement position, not measured. This is the highest-value
   thing a next pass could close.
3. No study compares exchange-unit counting against gram estimation. Item 021's
   counting convention has the same status.
4. Gibson 2016 is unreplicated, Australian, and its food set contains no Korean
   composite dish. Item 018 ships the shape-dependence and refuses the
   percentages as transferable.
5. The 외식 영양성분 자료집 itself was located but NOT read: retrieval exceeded
   the fetch size limit, so item 020 quotes no figure from the dataset and cites
   only the ministry notice describing it. The notice was additionally read from a
   MUNICIPAL REPOST rather than the ministry's own copy, which is recorded on the
   source line. An edition check (which volumes are current in 2026, and whether
   the 2010 consumption basis has been re-surveyed) is owed, per the v15 lesson
   that a jurisdiction-bound item needs an edition check and not just a source
   check.
6. Structural gap, axes: only items 017 and 021 carry applicability.axes, and the
   axes available are fitness-shaped. The axis a logging item would actually
   refract on -- whether the user has a kitchen scale at all, whether the meal was
   eaten alone or shared, whether the day was 외식 -- does not exist in the ledger.
   Adding axes is an append-only ledger change and was deliberately NOT attempted
   in a content-only release. This is the same finding the v15 cooking sprint
   recorded from a different direction, which makes it a warehouse-level signal
   rather than a per-domain one. Flagged for whoever owns the meal-logging module
   design.

Rerun-needed: none. Every source shipped in this release was retrieved directly
in this pass -- the AMPM five passes from the publisher's own description pages,
the AMPM validation and the two journal articles resolved to full bibliographic
records with DOIs, and the exchange table read from the issuing professional
society's own page. The two sources that could NOT be fully retrieved (the
external dataset PDF and the ministry's own copy of its notice) are named as
such on the item and nothing is quoted from them.

Meal-prep / eating-out sprint (v37, 2026-10-06) --
filled and open. Three items, 070-072, numbered >= 070 for parallel siblings
(renumber at merge if needed). Portion ESTIMATION was already owned by 018 and
020; this pass did not duplicate it and added only the directional
large-meal under-estimate (Almiron-Roig 2013) onto 072.

Filled:
- nutrition/portion-size-effect-intake-070 (@obs-inferential, B, not
  contested) -- Cochrane 2015 (72 RCTs, SMD 0.38, moderate), Zlatevska 2014
  (doubling -> ~35 percent more, curvilinear), Rolls 2007 (+50 percent
  portions -> +423 kcal/day, sustained 11 days). Tableware-only refused as a
  lever (very-low evidence).
- nutrition/meal-prep-preportion-071 (@meal-craft, C, contested =
  under-evidenced) -- planning (Ducrot 2017, n=40,554) and home cooking
  (Mills 2017, n=11,396) are cross-sectional associations; the one RCT
  (Hannum 2004, n=60, 8 wk) is pre-portioned meals vs self-selected. Rules:
  portion at pack time, weigh the batch once, storage routed to cooking
  006/007.
- nutrition/kr-eating-out-fat-loss-072 (@meal-craft, C, KR, contested =
  under-evidenced) -- Lachat 2012, Nago 2014, Koo & Park 2013 (KNHANES
  2007-2009), Urban 2011 and 2013 (bomb calorimetry, US), Almiron-Roig 2013.
  Rules: weekly 외식 count is the lever, decide before eating, leave broth,
  whole-dish logging, stated kcal is an average, day is a floor.

Searched and not closed:
- NO TRIAL OF MEAL PREP / BATCH COOKING ITSELF against a weight endpoint was
  located. Both cohort papers name reverse causation. What would close it: an
  RCT or prospective cohort of planning or batch cooking with weight or
  intake outcomes.
- KOREAN DISH RANKING FOR A CUT ("order 구이 not 튀김", "냉면 vs 비빔밥").
  Needs the ministry's measured 외식 영양성분 자료집 values, still NOT read
  (the v21 fetch-size failure stands; not re-attempted this pass). 072 ships
  no ranking. This is the highest-value next fetch for a meal module.
- WHERE A 찌개 / 국밥's ENERGY SITS (broth vs solids). No Korean measurement
  read. 072's leave-the-broth rule is a counting convention, labelled D.
- KOREAN RESTAURANT PLATE ENERGY BY CALORIMETRY. Only US data (Urban
  2011/2013) were read; no Korean equivalent located. 072 forbids quoting the
  US figure as a Korean plate size.
- RESTAURANT PORTION MULTIPLIER -- still refused (v21), restated as a rule on
  072.
- KNHANES EATING-OUT -> OBESITY with effect sizes. The Koo & Park abstract
  gives intake and guideline adherence, not adiposity; other KNHANES
  analyses surfaced in search (metabolic-syndrome components by eating-out
  frequency, one reporting no BMI association) were not read at the primary
  and are not cited.
- Hannum 2004 and Urban 2011 were read at abstract level via index records
  (PubMed blocked fetch); Rolls 2007 likewise. Figures used are abstract
  figures; a full-text pass is owed.
- Axes: whether the user has a kitchen scale, and whether a meal was 외식 or
  shared, still do not exist on the ledger (v21 sub-gap 6). 071/072 put
  those conditions in meal_rules `when:` text instead of axes. A meal module
  that wants to gate on them needs the append-only ledger change.

## nutrition -- craft lane (@meal-craft), v37 addendum: Korean dish energy

Added 2026-10-06. One item, one re-audit.

Filled:
- v21 RESIDUAL SUB-GAP 5 (the 외식 영양성분 자료집 "located but NOT read") is
  CLOSED. Both volumes were downloaded from foodsafetykorea.go.kr and read
  page by page: vol.1 (2012.2, 130 dishes) and vol.2 (2013.3, 108 dishes).
  nutrition/kr-restaurant-dish-energy-ranking-022 (B, LOCALE KR, not contested)
  carries the class ranking (energy per serving and per 100 g, protein per
  100 kcal, macro energy shares, sodium), the rice-line rule, logging defaults
  and swaps as structured fields. Item 020 got a one-line source re-audit; its
  claim stood.
- EDITION CHECK, half done. K-FIND (various.foodsafetykorea.go.kr/nutrient/),
  the ministry's live DB, was reached and says it updates monthly. Its rows
  were NOT read, because it is a script-driven app and the open API needs a
  key. Whether the 2012-13 restaurant values have been re-measured or
  superseded there is still unknown.

Still open, each searched or checked rather than assumed:
1. BROTH SHARE. Neither volume splits broth from solids, so there is no
   measured figure for how much of a 탕, 국, 찌개 or noodle soup's energy or
   sodium you skip by leaving the broth. Item 022 refuses to give credit for
   it. What would close it: an MFDS or peer-reviewed measurement of broth vs
   solids for Korean soups (sodium first).
2. RICE ACTUALLY EATEN. The rice line's default of one 공기 is a convention.
   No source on how much rice Korean diners eat with a 찌개 or 탕 was read.
   The fact that rice is absent from the entries is inferred from
   carbohydrate arithmetic. The books do not state it.
3. HOME COOKING. Both volumes are restaurant food. No measured dataset of home
   versions of 김치찌개, 된장찌개, 국 or 반찬 was read. Item 022 marks the
   restaurant value as a labelled fallback for home dishes.
4. BETWEEN-RESTAURANT SPREAD. Each value is a mean of 72 samples, published
   without SD or range. No dish-level uncertainty can be shown. Item 022
   leans on cross-class orderings, which are several-fold apart, and not on
   single values. One printed outlier (소불고기 177 kcal per 200 g) is kept
   as printed and flagged.
5. VINTAGE. The dishes were chosen from 2010 KNHANES frequency data. Menu
   composition and portion sizes since then are unverified.
6. AXES. 020's structural gap is unchanged: no eating-out, shared-meal or
   rice-amount axis exists in the ledger, so 022 refracts only on
   primary_goal and dietary_pattern (soft, hedge).

Rerun-needed: none. Every number in 022 was copied from a dish page or
computed from the parsed pages. Spot values were checked against the
rendered page text.

## nutrition -- craft lane (@meal-craft), v38 addendum: Korean protein-swap table

Added 2026-10-07. One item.

- FILLED: nutrition/kr-convenience-protein-options-030 (@meal-craft, C, KR).
  41-row engine-readable table (kr_protein_options + swap_rules) of Korean
  convenience-store protein products and common 외식 dishes, ranked by
  protein per 100 kcal with sodium per 100 kcal and per gram of protein.
  Every value read from MFDS K-FIND on 2026-10-07 (DB update 2026-09-07):
  category medians + IQR over label entries, standard-table rows, and
  single analysed restaurant dishes. It sits beside the v37 dish-energy row
  above (022: class medians from the 2012-13 restaurant volumes) and links
  it, 062 and 063 (the per-meal nudge whose dose a swap fills).
- EDITION CHECK (left half done by the v37 addendum above): K-FIND's rows
  were read this time, through its per-food pages. Its analysed restaurant
  rows (D3xx codes, 분석) date 2012-2022; no 2026 re-analysis of any row was
  found. Residual sub-gap 5 itself was already closed in v37 (022 read both
  volumes).
- OPEN: K-FIND has no restaurant-analysed entry for 설렁탕, 삼계탕, 제육볶음,
  보쌈, 족발 or 갈비탕 (only home-recipe analyses or calculated rows). The
  2012-13 restaurant volumes behind 022 DO carry 설렁탕 (420 kcal, 60 g
  protein per serving) and 삼계탕; 030's home-analysis rows for those two now
  point there (found at the v38 merge; the home 설렁탕 row is 120 kcal / 21 g
  per 500 g). Whether the volumes carry the other four was not checked: 022
  publishes class medians, not dish rows.
- OPEN: K-FIND's calculated 외식 rows (산출, 2022-2024) contradict the
  analysed rows on sodium (calculated 라면 58 mg per 100 mL against analysed
  김치라면 389 mg per 100 g). Excluded from 030. Nobody has checked how far
  the calculated rows can be trusted for anything; flagged so they are not
  picked up as the "newer" data.
- OPEN: label tolerance. Korean labelling rules allow declared values to
  differ from content within legal tolerances; the rule text (식품등의
  표시기준) was NOT read this pass, so 030 states that tolerances exist
  without quoting them.
- OPEN: 편의점 도시락 was searched but not tabled. The K-FIND 도시락 query
  mixes complete lunch boxes with plain 도시락밥 (rice-only) rows, so a
  category median would be meaningless without a per-product filter.
  Likewise there is no per-unit figure for string cheese or sliced cheese
  (multi-unit packs).
- OPEN: allergen tags on 030 rows are curator class defaults, not read from
  each label. A per-product allergen read (K-FIND does not carry the
  allergen field on the pages read) is owed before an allergen gate leans
  on them.
- OPEN, product: shipped suggest names only foods the user has logged.
  Whether a swap path may suggest an unlogged 030 row is a product decision,
  recorded on 030 as swap_rules.logged_foods_only_contract.
- STILL NOT RESEARCHED: sodium outcomes (014's gap). 030's sodium tier is a
  label-budget display rule and does not close it.

## nutrition -- craft lane (@meal-craft), v49 addendum: 회식 on a cut

Added 2026-10-07. One item.

- FILLED: nutrition/kr-hoesik-cut-rules-080 (@meal-craft, KR; D synthesis,
  direction rows B, compensation rows C, Korean 회식 context D).
  eating_out_rules (14 rules) for the diet card and weekly retro: pre-commit,
  bank-modestly, protein-before, company-eats-more, anju-class-default,
  finisher-is-a-meal, drinks-in-jan, log-next-morning-roughly,
  next-day-resume, morning-weight-not-fat, short-night-next-day,
  count-not-event, no-moralizing, banking-exit. Partly closes the
  alcohol-section OPEN item 6 (Korean drinking culture beyond rates) and
  links 072, 031, 032, 022, 074, 025, 073, 070 and sleep-recovery 015.
- OPEN: BANKING FOR ONE EVENT. No trial was found that tested saving
  calories on the day (or days) before a single planned social meal and
  measured intake at that meal or weekly balance. 080 rests on the
  6-month intermittent-vs-continuous equivalence (Headland 2016) and on
  small meal-skipping crossovers (Levitsky 2013). Whether pre-event
  restriction raises intake at the event (the restraint / disinhibition
  prediction) is untested in this setting. No banking kcal figure ships.
- OPEN: NEXT-DAY COMPENSATION BEYOND YOUNG MEN. Deighton 2019 is n=12 men
  aged ~22 after one day at +50 percent. Nothing read in women, older
  adults, people already dieting, or after a day that included alcohol.
- OPEN: COLLEAGUES AS CO-EATERS. Ruddock 2019 splits friends/family
  (effect) from strangers/acquaintances (no effect); work colleagues were
  not analysed as a group. Full text not read (publisher copy 403); the
  moderator details (gender, weight status) are abstract-level only.
- OPEN: KOREAN 회식 DATA. The only numbers carried are one advocacy-
  commissioned 1,000-worker survey (직장갑질119, 2024) read through a news
  report; the survey report itself was not located. The MFDS 주류 소비·섭취
  실태조사 (2017, 2020; per-occasion 잔 by drink, 폭탄주 experience,
  drinking companions) was located only through press summaries; the
  report and its 회식-setting tables were not read. No study of energy
  intake at a Korean 회식 (food plus drink) was found.
- OPEN: KOREAN MEAT-CUT ENERGY. 삼겹살 vs 목살 values (national standard
  food composition table, RDA) were seen only on a retail page (331 vs
  180 kcal per 100 g raw); not read at source, so 080's 고깃집 rule stays
  structural (count pieces, fill with 쌈) with no cut ranking.
- NOT SEARCHED: hangover and next-day food choice; alcohol absorption with
  vs without food (080 keeps a protein meal before on 031's grounds only);
  drink-refusal interventions.

## nutrition -- protein powder choice and shopping (KR), v63 addendum

Added 2026-10-07. Two items.

- FILLED: nutrition/protein-powder-type-label-evidence-092 (@obs-inferential,
  universal; C ledger, source row B, composition A, lactose B, seals D).
  powder_evidence (8 rows): soy or pea = whey for strength and absolute lean
  mass at adequate intake (Messina 2018, Lim 2021, Hevia-Larrain 2021,
  Babault 2015); WPC 80 vs WPI composition (ADPI 2023); lactose per scoop vs
  EFSA 12 g; KCA 2023 label test; amino spiking (Philips 2024); lead (Bandara
  2020, Consumer Reports 2025); seal scope.
- FILLED: nutrition/kr-protein-powder-shopping-rules-093 (@meal-craft, KR;
  D synthesis). protein_powder_rules (14), product_fields (9), rebuy (6)
  for the shopping module: won per 20 g protein, MFDS 80 percent tolerance,
  label-plausibility ceilings, 건강기능식품 mark not a rank, claim classes,
  seal scope, 해외직구 booster gate, plant lead cap, rebuy timing.
- OPEN: 건강기능식품 공전 PROTEIN MONOGRAPH NOT READ AT SOURCE. The
  daily-intake figure, the permitted protein claim wording and the
  manufacturing spec (changed 2023) were not read; the law.go.kr record
  carries the body as an attachment. Only the amino acid score 85 criterion
  ships, as quoted by KCA 2023. Next pass: read the 공전 PDF section for
  단백질 and add a claim-wording row to 093.
- OPEN: KOREAN PRICE DATA IS 2023-02. The only official price-per-protein
  table is KCA's (8 powders, 8 drinks). No current snapshot of Korean
  listings (쿠팡 / 네이버) was taken, so 093 ships the arithmetic and a dated
  band only. A dated live snapshot of 10-20 powders, with protein per
  serving, would let 093 carry a current reference band.
- OPEN: KOREAN LABEL ACCURACY AT SCALE. One failing powder in eight (KCA
  2023) is the whole Korean measured record found. No MFDS 수거검사 of
  protein powder protein content was located (the 2021 MFDS action on 660
  protein bars and shakes was advertising, seen only in a news report).
- OPEN: KOREAN LACTOSE MALABSORPTION PREVALENCE. Storhaug 2017 (global
  meta-analysis) is RETRACTED (2025). The Korean breath-test studies read
  (Park 2016, Oh 2022, Jung 2025/2026) recruited symptomatic adults and give
  no population rate. 092 therefore states the tolerance dose, not a
  Korean prevalence.
- OPEN: LACTOSE IN FINISHED PRODUCTS. ADPI figures are for the ingredient.
  Flavoured Korean WPC powders rarely state lactose; no measured lactose in
  finished powders was found.
- OPEN: PEA, RICE AND BLEND TRIALS. The plant evidence is mostly soy; the one
  large pea trial (Babault 2015) is maker-funded and biceps-only. No trial of
  a pea-rice blend vs whey on training outcomes was read. DIAAS values per
  protein (Mathai 2017) were not read at full text and are not carried.
- OPEN: SEAL PROGRAMMES. NSF's label-claim verification scope was not read
  on a primary page (only third-party summaries say it verifies protein);
  093 says only what Informed Sport and Informed Protein state. No study
  compares sealed with unsealed powders on protein accuracy.
- OPEN: SHELF LIFE AFTER OPENING. No primary study of opened whey powder
  storage (moisture, Maillard browning, lysine loss) at Korean summer
  humidity was read; 093's max_units uses the printed date only.
- NOT SEARCHED: creatine and other additives in protein products; collagen
  as a protein source (low amino acid score) beyond the KCA note; casein
  vs whey for satiety on a cut; children and pregnancy use.
