# exercise -- gap list

Split from the warehouse-level GAPS.md at warehouse v42 (module split,
warehouse v43, 2026-10-07). Section text below is unchanged; sections that
were appended at the end of the old file under another heading were refiled
here by their `### exercise / ...` heading, as those blocks asked.

## exercise

Dropped for quality / not sourced:
- @gym-craft lane (exercise/dc-inversion-craft-007 in the rubric) is EMPTY of
  shippable items. The rubric's single @gym-craft row is a STRUCTURAL inversion
  RULE (D may outrank a confounded observational C for training-craft), explicitly
  marked "[unconfirmed -- no single primary claim row]" in the rubric. It has no
  sourced 3-vote survivor behind it, so it was NOT converted into an item. The
  gym-craft lane therefore ships with zero items in warehouse #1.
  -> A collection sprint should fetch real, sourced training-craft claims
     (split/tempo/volume/frequency programming consensus from coaching literature
     + hypertrophy meta-analyses) so the D/C-inversion lane has substantive items,
     not just a grading rule.
  PARTIALLY FILLED 2026-08-17 / 2026-08-21 (bookkeeping correction 2026-08-22 --
  the paragraph above still read "zero items" long after it stopped being true):
  @gym-craft now holds exercise/volume-landmarks-heuristic-015,
  exercise/deficit-volume-guidance-016, exercise/warmup-load-rampup-progression-018,
  exercise/serratus-anterior-integration-019 and
  exercise/female-training-considerations-020. STILL OPEN: all five are
  theory-only or single-source practitioner digests. The lane still has no item
  that demonstrates the D-over-confounded-C INVERSION doing actual work, which
  was the original point of the gap.

Coverage the rubric implies but batch1 does not supply:
- No substantive @clinical-physio items beyond creatine + protein-window + BCAA +
  the COI rule. Missing high-value ergogenics the AIS framework grades Group A:
  caffeine, beta-alanine, sodium bicarbonate, nitrate/beetroot. These are named
  by the anchored AIS framework but were not in the batch1 findings.
- No @performance-lit substantive training claims -- only the two field-methodology
  rules (replication crisis, small-n culture). The lane needs actual performance
  findings (e.g. training-volume/-frequency dose-response) graded THROUGH those
  rules to show the lane doing work, not just describing its own hazards.
- REP-RANGE vs TECHNICAL-STABILITY/INJURY-RISK for heavy multi-joint free-weight
  compounds (squat/deadlift/RDL-class hinge, barbell row/press) was an UNLOGGED
  coverage hole -- flagged 2026-08-07 (a user asked whether "heavy
  compound multi-joint lifts -> low reps because synergist/stabilizer fatigue +
  neural-control loss raises injury risk" is graded knowledge). No item or raw
  covers this; closest adjacent item is exercise/rest-interval-volume-load-017
  (rest, not rep-count), which itself flags compound extrapolation as unverified.
  The interim answer was a conventional coaching heuristic, explicitly
  NOT presented as warehouse-graded. -> A collection sprint should fetch sourced
  claims on rep-range selection, technical breakdown risk, and injury incidence
  by rep-range for trained lifters on heavy compound multi-joint lifts.

Rerun-needed: none in exercise (batch1 verified cleanly, 3-0 across the rows used).

Filled 2026-08-23 (load-increment size / microloading collection sprint, v9):
- LOAD-INCREMENT SIZE / MICROLOADING (2.5 vs 5 kg jumps, minimum effective load
  increment, absolute-vs-relative load jump) had NO item at any grade. Queued
  here 2026-08-23 by the weekly gap-review cron after sitting locally for
  23 days; the condition that it wait for an explicit go was satisfied
  by an explicit trigger (the cron notice alone was correctly not treated
  as one). Filled by a sprint of 2 research passes + 3 adversarial verification
  passes into four items. The headline is an ABSENCE: nobody has studied how big
  an increment should be.
  - exercise/load-increment-size-evidence-gap-027 (@performance-lit, B/D,
    contested) -- the documented absence and its provenance trace. ACSM 2009's
    2-10% rule carries exactly one citation and that citation is a narrative
    prescription review, not an experiment; ACSM 2026 is silent (recorded as an
    argument from silence, NOT a repudiation); Hostler 2001 (n=19, untrained,
    upper-body) is the only trial ever to manipulate increment magnitude, and
    it is an unrejected null, not demonstrated equivalence.
  - exercise/progression-modality-load-vs-reps-028 (@performance-lit, B/C,
    not contested) -- load-vs-rep progression equivalence (Plotkin 2022, Chaves
    2024) with its three bounds: the tested envelope is ~2x the rep target over
    8 weeks, the equivalence is HYPERTROPHY-only (strength favours high load),
    and the load dose-response is threshold-then-plateau, not linear.
  - exercise/increment-verification-floor-029 (@clinical-physio, B/C,
    contested) -- MDC95 ~8-12% of 1RM for a single test-retest pair, derived
    three ways and shown; plus the category distinction (undetectable is not
    inert) with the linear-extrapolation rescue stripped.
  - exercise/autoregulation-vs-percentage-prescription-030 (@performance-lit,
    B/C, contested) -- the standard escape from the increment question, which
    fails twice: no measured advantage over percentage-based prescription, and
    an instrument error (RIR ~0.65-1.0 reps, ~3-4% of 1RM near 85%) larger than
    the increments under dispute.
  ROUTING NOTE: all four to EXERCISE. Three to @performance-lit, whose two
  methodology rules (replication-power-crisis-005, small-n-culture-006) are
  exactly what position-stand prescription and small-pool meta-analysis need to
  be graded through. Item 029 is the non-obvious one: it went to
  @clinical-physio (VC-A) despite sports-science sources, because its subject is
  clinimetric (test-retest reliability, SEM, minimal detectable change) and
  measurement-instrument limits belong to the clinical verification culture --
  the same placement sleep-recovery/tracker-accuracy-003 already has in its own
  domain.
  WHAT THE FILL DOES NOT DO: the LIVE CONSEQUENCE recorded on the queued entry
  (the B7 plate policy picking micro-anchor lifts from an unsourced
  relative-load-jump heuristic) is NOT resolved by a graded number, because no
  evidence supports one. What the sprint supplies instead is the arithmetic
  justification for relative framing without the rejected physiological story,
  an explicit statement that no increment size is evidence-backed, removal of
  the injury-risk rail, and a measurement floor bounding what any retest can
  confirm. The policy remains a heuristic; it is now a heuristic that knows it
  is one.
  RESIDUAL SUB-GAPS carried out of this sprint -- all seven genuinely unfilled,
  and each recorded on the relevant item:
  1. No trial has manipulated increment magnitude in TRAINED lifters. Hostler
     2001 is untrained, upper-body only, n=19.
  2. Absolute (kg) versus relative (%) increment framing has NEVER been tested
     head-to-head. Both framings carry error (percentage framing is itself
     ~2.5 reps wide at 80% 1RM, Nuzzo 2024); neither is the demonstrated
     correct one.
  3. Increment SIZE and increment FREQUENCY have never been separated. Every
     protocol confounds them.
  4. MDC/SEM for WORKING-SET loads is thin to absent -- all reliability data is
     laboratory 1RM testing under standardized protocol. The transfer to the
     loads a lifter actually manipulates week to week is an extrapolation of
     unknown direction.
  5. Machine and cable FIXED-STACK progression has ZERO research literature --
     vendor and forum sources only. Treat as ABSENT, not weak. This is the case
     where the trainee cannot choose the increment at all, so it is the case
     where guidance would matter most.
  6. Failed-increment and reset protocols are untested. The nearest RCT
     (Coleman 2024, PMC10809978) tested complete CESSATION, not a load
     reduction and not a reset, and found it impaired lower-body strength.
  7. No study interacts increment size with training age, sex, or bodyweight.

Filled 2026-10-07 (early-morning training sprint, v37 -- a research sprint; the target trainee trains 05:00-06:00 and the morning
brief goes out at 04:30):
- exercise/early-morning-performance-warmup-068 (@performance-lit) -- Knaier
  2022 (63 studies, morning power/jump/grip below the afternoon), Grgic 2019
  (morning and evening training give similar strength and size gains), Taylor
  2011 (20 min extra general warm-up closed the 08:00 power gap, n=8),
  Facer-Childs 2018 (chronotype / time since waking sets the size).
- exercise/early-morning-caffeine-food-069 (@clinical-physio) -- caffeine
  scoped to the dawn session: ISSN 2021 dose band, Mora-Rodriguez 2012
  (morning caffeine restores bar velocity, n=12), Gardiner 2023 sleep cutoffs,
  EFSA 2015 safety ceiling; Aird 2018 and Naharudin 2019 on fasted vs fed.
- exercise/early-morning-session-brief-rules-073 (D synthesis) -- ten
  engine-readable session_rules + constants for the brief / prep code.
OVERLAP (found at the v37 merge): the sleep-training sprint in the same
release authored sleep-recovery/early-morning-session-071 (the sleep side of a
05:00-06:00 session: bedtime anchor, wake buffer), sleep-recovery/caffeine-
bedtime-cutoff-070 (the caffeine-vs-sleep cutoff, Gardiner 2023 + 2025 RCT)
and sleep-recovery/brief-sleep-training-rules-072 (brief rules). The exercise
rows own the training side (performance gap, warm-up, pre-session caffeine
dose, fed vs fasted); the cutoff numbers are the sleep lane's -- 069 / 073 quote
the same Gardiner 2023 estimates and must move with 070 if it is re-graded.
Two brief rule sets (073 and sleep 072) now exist; the brief code should read
both and a later audit may merge them.
PARTIALLY closes the batch1 "caffeine missing" line above: the ergogenic
direction and dose band are now carried, but only inside a dawn-session item.
A general caffeine item (habituation, genotype, sex, endurance vs strength
magnitudes) is still not authored.
RESIDUAL SUB-GAPS (each searched, none filled):
  - NOTHING TESTS 05:00. Every time-of-day, warm-up, caffeine and breakfast
    trial used 06:00-10:00 "morning" arms (Taylor and Facer-Childs 08:00,
    Mora-Rodriguez 10:00). The dawn edge is extrapolated in direction only.
  - Warm-up dose-response at dawn: one tested dose (20 min bike, n=8 men,
    jump/power outcomes). No trial on multi-set heavy lifting after an
    extended vs standard morning warm-up. The 5-10 extra minutes in 073 is a
    product constant.
  - Short sleep AND a dawn session together: Craven 2022's AM subgroup is not
    split by how soon after waking the test ran, and the pooled AM effect was
    still negative (-5.4%) despite the "largely unaffected" wording. No trial
    tested rep-max testing after short sleep at dawn; 073's no-test rule is
    product judgement.
  - Pre-session snack timing for a session starting within an hour of
    waking: no trial. The only resistance feeding trial fed 2 h before
    (impossible at 05:00 without a 03:00 alarm) and was unblinded. Whether a
    30-60 min small carbohydrate snack beats fasting for a ~1 h lifting
    session is untested.
  - Caffeine onset at dawn (gum vs coffee vs capsule when taken 30 min before)
    is untested; the 04:30 brief time cannot be graded as a good or bad dose
    time.
  - Chronic effect of a fixed early wake time (cumulative late restriction
    across weeks) on training outcomes: no performance-endpoint study found;
    same hole as the sleep-recovery SLEEP DEBT gap.
  - Every source is young and mostly male except Facer-Childs 2018
    (33 F / 21 M); age and sex effects on the morning gap are unresolved.

Filled 2026-08-22 (stretching / DOMS / recovery collection sprint, v7):
- STRETCHING + RECOVERY was a total blind spot -- the warehouse held ZERO items,
  at any grade, on acute static stretching, dynamic warm-up / mobility effects,
  DOMS, active recovery, blood-flow recovery modalities, recovery timelines, or
  session spacing. Discovered when a live user question (prep work on a
  still-fatigued muscle) returned nothing; the miss was never logged at the time
  (see the local gap log, second unlogged-hole incident after rest-interval).
  Now covered by six items from a 19-source deep-research pass:
  - exercise/acute-static-stretch-force-deficit-021 (@performance-lit, B/C,
    contested) -- duration-dependent force deficit, ~60 s per muscle group
    threshold; deficit is specific to ISOLATED MAXIMAL STRENGTH and does not
    extend to jump/sprint/RFD; disappears inside a full warm-up.
  - exercise/dynamic-warmup-same-day-performance-022 (@performance-lit, B/C,
    contested) -- the warm-up carries the benefit; the stretching MODALITY
    inside it is a small and possibly null increment.
  - exercise/doms-timeline-mechanism-023 (@clinical-physio, B/C, contested) --
    onset/peak/resolution timeline + repeated-bout effect; soreness correlates
    POORLY with every objective damage marker, so it is not a training gauge;
    mechanism genuinely contested (classical damage-inflammation vs the
    bradykinin/NGF nociceptor-sensitization pathway).
  - exercise/recovery-modality-soreness-vs-performance-024 (@performance-lit,
    C/B, contested) -- the PERCEIVED-SORENESS vs MEASURED-PERFORMANCE split;
    massage tops the soreness meta and is null on every performance endpoint.
  - exercise/recovery-kinetics-session-spacing-025 (@performance-lit, C/D,
    contested) -- proximity to failure / volume / movement complexity, not a
    per-muscle-group clock.
  - exercise/prep-on-fatigued-muscle-two-effects-026 (@clinical-physio, C/C/D,
    contested) -- the originating question, answered as two separately graded
    effects.
  ROUTING NOTE: all six went to the EXERCISE domain, NOT sleep-recovery, even
  though "recovery" is in that domain's name. sleep-recovery's single lane
  (@clinical, VC-A) is anchored to the AASM/sleep-medicine authority hierarchy,
  the wrong verification culture for exercise-induced muscle physiology; the
  exercise domain's 3-lane structure maps the evidence cleanly (@clinical-physio
  for the nociception/physiotherapy RCT material, @performance-lit for the
  sports-science meta-analytic material). The sleep-recovery substantive-claim
  gap below is therefore STILL OPEN and was not touched by this sprint.
  RESIDUAL SUB-GAPS carried out of this sprint (each on the relevant item's
  refraction_notes, and each genuinely unfilled):
  - No trial exists on the DIRECT question -- prep performed on a muscle already
    carrying fatigue from a previous session. Item 026 is assembled inference
    from adjacent designs and says so.
  - No trial tests whether pre-session stretching changes reps-at-load across a
    multi-set heavy compound SESSION. All stretching outcomes are single efforts
    (one contraction, one jump, one sprint).
  - No systematic comparison of recovery kinetics ACROSS muscle groups under
    matched volume/intensity/proximity-to-failure exists anywhere. The
    per-muscle-group recovery tables in circulation are practitioner
    constructions. This is a real hole in the field, not just in this warehouse.
  - Cold-water immersion's alleged blunting of long-term hypertrophy/strength
    adaptation was NOT researched in this pass; flagged on item 024 so its
    absence is not read as an all-clear.
  - The stretching/warm-up evidence base is overwhelmingly young adult males;
    the 2024 meta states its results are not interpretable for women or children.
    Interacts with exercise/female-training-considerations-020's claim (6), which
    recommends stability work over static stretching for women -- that specific
    sex-conditioned claim remains D-tier practitioner material and was NOT
    upgraded by this sprint.
  - Whether performance-based readiness proxies (first-set rep performance, bar
    speed, jump height) are practical day-to-day autoregulation signals for a
    general trainee is untested; item 025 names them only as what the trials
    measured.

Filled 2026-07-31:
- Inter-set REST INTERVAL was an UNLOGGED coverage hole -- the warehouse held
  volume/dose-response and regional-hypertrophy items but nothing on rest, and
  this gap was never even recorded here. Now covered by
  exercise/rest-interval-volume-load-017 (@performance-lit, grade B/C) from a
  2026-07-31 deep-research run (11 sources, 25 claims verified 3-0). Residual
  sub-gaps carried on that item's refraction_notes: no direct compound-vs-
  isolation head-to-head rest trial; the volume-equated evidence is isolation/
  untrained/short-duration, so heavy-compound + trained-strength application is
  an extrapolation; RIR-by-rest quantitative thresholds are undetermined.

CLOSED 2026-08-23: the "Queued 2026-08-23" LOAD-INCREMENT SIZE / MICROLOADING
entry that stood here was filled by the v9 sprint and has been rewritten as the
"Filled 2026-08-23" block above, in newest-first order with the other fills. Its
original terms are preserved there (local logging 2026-07-31, the
23-day delay, the cron promotion, the explicit-go block, and
the B7 plate-policy live consequence), together with what the fill did NOT do
and the seven sub-gaps that remain open. The first cron-promoted gap on record
is therefore also the first cron-promoted gap closed.

Safety boundary -- drugs row (added 2026-09-25, pack_health 0.17.1):
- exercise/harm-route-boundary-031 lists "drugs" (PEDs / injections /
  non-prescribed drugs for body composition) as a caught route but NO graded
  item carries its reasons. The row tells the agent to invent nothing and point
  to a physician. A collection sprint should fetch sourced @clinical-physio
  items on anabolic-androgenic steroid harms and on non-prescribed diuretic /
  stimulant use for weight loss, then re-point the row at them.

Body-ideal archetype sprint (v33, 2026-09-30) -- filled and open:
- FILLED: exercise/body-ideal-archetype-map-032 and one row per archetype,
  033-045 (classic X, men's V, open bodybuilding, CrossFit/functional,
  Pilates, calisthenics/gymnast, yoga/mobility, powerlifting,
  weightlifting/athletic power, endurance, swimmer, combat, healthy-lean).
  Machine index: body_ideal_archetypes.
- OPEN, not sourced: no peer-reviewed quantification of the classic-physique
  proportions (shoulder-to-waist, thigh-to-waist). Federation judging is
  qualitative ("harmonious", "good proportion"); the only numbers are the
  height-indexed weight caps. Do not invent a target ratio.
- OPEN: segmental InBody (arms/legs/trunk lean) validity in resistance-trained
  adults. nutrition/body-composition-measurement-floor-011 covers whole-body
  bias; segment-level agreement with DXA was seen to vary by population
  (hundreds of grams per limb, kilograms in the trunk) in clinical samples
  only. A sprint should fetch a trained-population segmental validation before
  any item grades a segmental lean-mass CHANGE as real.
- OPEN: Pilates tempo is qualitative in every source found ("slow",
  "controlled", "flow"); no source gives seconds per repetition. The
  controlled_tempo marker proposed for the kit therefore needs a craft
  definition (e.g. a stated eccentric/concentric tempo, or a Pilates-type
  movement tag), not an evidence-derived threshold.
- OPEN: yoga fitness evidence located only in older adults (Shin 2021) and
  clinical groups; no pooled trial set in healthy young/middle-aged adults.
- OPEN: injury data for straight-arm calisthenics skills (planche, levers,
  muscle-ups) outside CrossFit samples; the gymnast review is competitive
  gymnastics only.
- OPEN: swimmer look -- selection (limb length) vs training contribution is
  unquantified; the item is contested on that point.
- OPEN: Hyrox / fitness-racing not itemised separately (one acute-response
  study found, Brandt 2025); currently read as CrossFit/functional + endurance.
- STILL OPEN from v32: the drugs row of exercise/harm-route-boundary-031 has
  no graded harm item. v33 added the prevalence side only (Sagoe 2014, cited in
  035), not harms.
- MEASUREMENT GAPS (not warehouse gaps, recorded here so they stay visible):
  no kit token for girths, range of motion, pace/distance, jump/sprint/bar
  speed, skill level, controlled-tempo share, benchmark times, or weekly
  cardio minutes; segmental lean mass is readable but not a strand token. The
  proposed names are in body_ideal_archetypes `missing_token_defs`.

Body-ideal archetype sprint pass 2 (v34, 2026-09-30) -- filled and open:
- FILLED: 046 climber, 047 grappler / 씨름 / wrestler (split from the
  striking-leaning combat row 044), 048 sprinter/athletic, 049 rower, 050
  cyclist, 051 dancer, 052 ski/snowboard, 053 racket sports; map 032 and
  body_ideal_archetypes v2 updated.
- OPEN: 씨름 has almost no English-language sport science -- two small
  Korean studies (isokinetic asymmetry n=25; short-term weight loss n=6).
  The grappler row leans on wrestling/judo reviews. A sprint should fetch
  KCI (Korean) literature on 씨름 physiology and injury before any item
  claims something 씨름-specific beyond the rule and the classes.
- OPEN: 씨름 and lightweight-rowing class limits were read from press /
  broadcaster explainers; the 대한씨름협회 and World Rowing rulebooks were not
  fetched. The 'above-the-knee touches the ground' loss rule is widely
  repeated but was NOT found in the UNESCO or Korea.net text fetched, so no
  item relies on it.
- OPEN: no study links neck strength to neck-injury risk in wrestling (Lee
  2017 critically appraised topic); neck training in 047 is craft.
- OPEN: climbing injury risk factors are "inconclusive and contradictory"
  (Zielinski 2025); the leanness-pressure evidence is one recreational survey.
- OPEN: squash has no dedicated source; the racket row is tennis- and
  badminton-led. Table tennis only appears as a trigger word.
- OPEN: dancer evidence on supplementary strength training is two studies
  (Angioi 2009) plus one feasibility trial; energy-deficiency figures are
  small professional cohorts whose prevalence depends on method.
- OPEN: ski/snowboard physiology (eccentric demand, low-position endurance)
  is craft here; the sources found are injury-side only. Track-sprint
  cycling is named as a separate picture inside 050, not itemised.
- MEASUREMENT GAPS added: grip, finger hang, climbing grade, neck girth,
  loaded carries, rowing and riding distance, cycling power, single-leg
  balance, agility. Proposed names in body_ideal_archetypes
  `missing_token_defs`.

Injury-caution sprint (v36, 2026-10-06) -- filled and open:
- FILLED: 054 injury history and re-injury risk (by recency and tissue), 055
  tendon / plantar-fascia load management (pain-monitoring ceiling, spacing),
  056 the engine-readable caution ladder (decision_ladder + tissue_modifiers).
- OPEN: NO prospective re-injury cohort in recreational or competitive
  LIFTERS was located. Every history magnitude in 054 is team sport
  (football, Australian football) or post-ACL-reconstruction; only the
  direction is carried. A sprint should look for powerlifting / weightlifting
  / gym-goer cohorts that model prior injury as a predictor.
- OPEN: no study sets a time after which a past injury stops mattering. The
  12-month recent/old boundary in product code is a convention; nothing
  compares windows.
- OPEN: the "over half of hamstring recurrences occur in the first month
  after return" figure is widely repeated (59% is the usual number) but was
  not confirmed at a primary in this sprint. de Visser 2012 gives only
  13.9-63.3% recurrence in the same season to 2 years. Not carried until a
  primary is read.
  PARTIALLY CLOSED 2026-10-07 (v40, 079 / 054 re-audit): Wangensteen 2016
  (Am J Sports Med, abstract) found more than 50% of 19 MRI-confirmed
  reinjuries within ~4 weeks of return. The 59% figure itself is still not
  traced to a primary.
- OPEN: SPREAD vs CONCENTRATE. No trial compares spreading a symptomatic
  site's weekly load across more, lighter days against fewer, heavier days in
  resistance trainees -- not for the patellar tendon / patellofemoral joint,
  not for the shoulder (rotator-cuff / impingement-type pain under pressing),
  not for the plantar fascia. 055's spacing note is collagen-turnover timing
  (Magnusson 2010) plus the every-second-day / 3x-week design of the trials
  that worked, held at the practitioner floor.
- OPEN: the pain-monitoring model (5/10 ceiling, next-morning settle,
  no week-to-week rise) was tested on the Achilles only (Silbernagel 2007,
  n=38). Its use for patellar, rotator-cuff and plantar-fascia pain is by
  analogy. Isometric analgesia for tendon pain was not researched here.
- PARTLY FILLED v37 (knee, low back): 057 / 058 now cover patellofemoral
  pain and knee OA; 059 covers the low back (ladder mapping by picture,
  modify-first order, red flags). See the v37 blocks below. Still open: hip,
  shoulder (glenohumeral cartilage) and other joints. Original entry:
  joint / cartilage (knee osteoarthritis, chondral stiffness) and
  low-back pain have no loading row in this warehouse; 056 treats joint
  stiffness without pain as mild and present joint pain as current-other
  (triage). The low back is among the commonest lifting injury sites
  (Keogh & Winwood 2017) and deserves its own row.

Low-back row (v37, 2026-10-06) -- open:
- OPEN: NO trial in competitive or recreational LIFTERS with back pain
  compares training through (modified hinge) against pausing the hinge, or
  ranks which modification to make first. 059's modify_order is
  practitioner synthesis plus survey data (Stromback 2018: 81% modify,
  16% stop). The only lifting trial is Aasa 2015 / Michaelson 2016 (n=70,
  general mechanical LBP patients, physio-supervised deadlift).
- OPEN: Berglund 2015 predictor cut-offs (pain < 60/100 VAS, Biering-Sorensen
  > 60 s) circulate in secondary summaries but were not in the abstract
  read; full text not read. Not carried as engine thresholds until read.
- OPEN: the 055 pain-monitoring ceiling has never been tested for the low
  back; 059 uses it by analogy (D). A symptom-contingent loading rule tested
  in LBP would replace it.
- OPEN: lifting belts. Steffens 2016's belt trials are occupational back
  supports; no study located on whether a lifting belt changes back-pain
  onset or recurrence in lifters.
- OPEN: imaging findings (disc bulge, spondylolysis) in young lifters and
  whether they should change loading -- not researched in this pass; 059
  routes structural suspicion to triage only.
- OPEN: Tung 2024 (updated weightlifting / powerlifting SR) read at
  abstract only; site percentages for the lower back not extracted.
- OPEN: Malliaras 2015 (patellar tendinopathy load management, JOSPT) and
  Koc 2023 (heel-pain CPG) were cited from their records, not read at full
  text; no specific recommendation strength from either is quoted in 055.

Shoulder prehab dose (v37, 2026-10-07) --
filled and open:
- FILLED: 074 shoulder ER / lower-trap / scapular dose keyed to the 056 rungs
  (structured shoulder_prehab + shoulder_prehab_placement), evidence vs
  folklore table. Siblings in the same release: 064 (pressing selection +
  cuff work for a painful shoulder) and 065 (specific vs general shoulder
  prep); 074 owns only the DOSE and placement of the prehab work.
- NARROWED (055's pain-model gap): Holmgren 2012 used the same
  pain-monitoring model (5/10 ceiling, settle before the next session) to
  set load in a shoulder RCT. It was the load method, not the tested
  variable, so the Achilles-only gap stands for the model itself.
- OPEN: NO shoulder-prevention or shoulder-prehab RCT in LIFTERS. Both
  prevention trials are handball (Andersson 2017 n=660; Asker 2022 n=627);
  lifter data are cross-sectional (Kolber 2017 n=55) and retrospective
  epidemiology (Keogh & Winwood 2017). Every 074 number is a transported
  protocol.
- OPEN: no trial compares sets, frequency or reps for shoulder PREVENTION;
  Malliaras 2020 (dose in cuff tendinopathy) found three small conflicting
  trials. The 2-3 x 8-16, 3x/week dose is "what worked", not "what is
  needed".
- OPEN: no trial of within-session PLACEMENT (prep before vs accessory
  after pressing) for any shoulder outcome. The "fatiguing cuff work after
  pressing" rule rests on one lab mechanism study (Chopp 2010).
- OPEN: the Asker 2022 Shoulder Control programme content (exercises,
  sets, reps) was not read; only the PEDro abstract. Bury 2016, Naunton
  2020, Malliaras 2020 and Fredriksen 2020 read at abstract / evidence
  summary only.
- OPEN: no outcome trial for a pull:push set ratio, for face pulls as
  prevention, or for any single "best" lower-trapezius exercise; EMG
  rankings exist (not fetched) but do not answer outcome questions (013).
  (066 pull-push-plane-balance carries the same "no ratio trial" finding.)
- OPEN (catalog, not knowledge): the product drill catalog has ER drills and
  band pull-aparts but no lower-trapezius drill (prone Y / cable Y-raise);
  see the shoulder-prehab field guide (not public).

Knee joint / patellofemoral follow-up (v37, 2026-10-06)
-- filled and open:
- FILLED: 057 knee pain symptom-guided loading (ladder placement, 2/10 knee
  ceiling, 2-3 knee days), 058 squat depth and knee-friendly variants.
- OPEN: NO knee pain-monitoring trial in ADULTS or LIFTERS. The only knee
  ceiling read at a primary (Rathleff 2019) is 2/10 in 10-14-year-olds,
  uncontrolled. Whether adults with patellofemoral pain do as well under the
  055 Achilles-style 5/10 ceiling is untested; 057 uses 2 as the cautious
  default. A sprint should look for adult PFP / knee OA trials that set and
  report a pain-during-exercise limit (GLA:D's acceptable-pain guidance was
  NOT verified at a primary and is not carried).
- OPEN: weekly knee frequency. Juhl 2014's >=3x/week signal is a
  between-trial meta-regression in knee OA (supervised sessions), not a
  within-trial dose comparison, and nothing exists for PFP or for lifters.
- OPEN: MACHINE vs CABLE vs DUMBBELL vs BARBELL. No study compares knee pain
  or patellofemoral load for the same movement across equipment types. 058's
  equipment remarks are practitioner judgement (D).
- OPEN: squat depth and knee PAIN outcomes. PF stress by knee angle is from
  modelling in 7-18 healthy people (Powers 2014, Escamilla 1998 / 2008 / 2022);
  no trial in painful knees compares training outcomes by squat depth. Kubo
  2019 (n=17) is the only depth-hypertrophy trial read.
- OPEN: lifting and long-run knee OA. Only Kujala 1995 (29 former elite
  weight lifters, BMI-confounded, retrospective) was located; nothing in
  recreational lifters. Hartmann 2013's claim that heavy partial squats favour
  degeneration is argument, not data, and is not carried as a rule.
- OPEN: Willy 2019 PFP CPG and the START trial's per-session %1RM were not
  read at full text (403 / captcha); no CPG recommendation letter is quoted.

Shoulder sprint (v37, 2026-10-06) -- filled and open:
- FILLED: 064 pressing selection + cuff / scapular work for subacromial /
  rotator-cuff related shoulder pain (selection_rules keyed to 056 rungs);
  065 shoulder prep, specific ramp vs general warm-up vs activation drills
  (prep_policy).
- OPEN: NO trial of any isolated shoulder activation drill (band or cable
  external rotation, halo, face pull, machine "activation") before pressing,
  for injury or for performance, in lifters. Searched PubMed-indexed
  literature and warm-up reviews; only EMG studies and practitioner content
  exist. 065's drill choice and primer dose are product constants.
- OPEN: NO injury outcome for upper-body warm-up of any kind (McCrary 2015
  found zero such studies). The shoulder-prep injury evidence is two handball
  cluster RCTs (overhead throwers, multi-component packages); transfer to
  pressing lifters is assumed, not tested.
- OPEN: NO prospective shoulder-injury cohort in recreational lifters. The
  lifter variant signals (lateral raise / upright row above 90 degrees; ER
  training protective) are one cross-sectional sample of 46 trainers
  (Kolber 2014), read at abstract only.
- OPEN: bench grip <=1.5x bi-acromial width and scapular retraction rest on
  a 10-athlete OpenSim model at 16 kg (Noteboom 2024) plus opinion reviews
  (Green & Comfort 2007, Fees 1998 -- cited from records). No injury outcome.
- OPEN: whether machine pressing lowers shoulder injury or symptom flares
  versus free weights is untested; Haugen 2023 only shows the swap costs no
  hypertrophy or general strength.
- OPEN: specific (cuff + scapular) vs general exercise for shoulder pain is
  contested (Holmgren 2012 vs Shire 2017 / Bury 2016); 064 carries it as
  contested. Reinold 2004 (EMG of ER exercises) cited from its record.

Fatigue-management sprint (v37, 2026-10-06) -- filled and open:
- FILLED: 060 deloads (planned vs reactive, recipe, triggers; structured
  deload_prescription + deload_triggers), 061 RIR accuracy and daily
  readiness signals (structured rir_rules + readiness_signals).
- OPEN: NO trial tests deload vs no deload over a long horizon (6+ months)
  in trained lifters; Coleman 2024 is 9 weeks, lower body only, and used a
  full week OFF, not a reduced-volume deload. Pancar 2026 (reduced volume)
  is untrained, single-joint, read at abstract only.
- OPEN: planned vs reactive (autoregulated) deload timing has never been
  compared. The 6-week default and the reactive trigger thresholds (2 RIR
  below target, two consecutive exposures, low wellness on 3 of 5 days) are
  product constants with no validation.
- OPEN: deload RECIPE size. No study compares sets x 0.5 vs other cuts, RIR
  floors, or load-kept vs load-cut deloads. Direction only (Delphi +
  survey).
- OPEN: no validated threshold for a "performance drop" that separates
  day-to-day noise from functional or non-functional overreaching in
  lifters; the RT overreaching literature lacks follow-up testing (Grandou
  2020).
- OPEN: daily-adjustment size (one load step per 2 reps off target) is
  derived from the reps-per-%1RM relationship (030), not tested as an
  adjustment rule. No RCT compares an anchor-set-driven daily program with a
  fixed one beyond the two small flexible-order trials (Colquhoun 2017
  trained n=25 null; McNamara 2010 beginners n=16, leg press only).
- OPEN: no resistance-training validation of HRV-guided training or any
  consumer readiness score against next-session lifting performance (also
  open on sleep-recovery 011).
- OPEN: Halperin 2022, Robinson 2024, Grandou 2020, Pancar 2026 and Travis
  2020 were read at abstract only; Meeusen 2013 cited from the record.
  Rogerson 2024, Bell 2023 and Coleman 2024 were read at full text.
- OPEN: female lifters and lifters over 40 are almost absent from the deload
  and RIR-accuracy samples (Coleman 2024: 10 women, mean age 21.8).

Cardio-in-a-cut sprint (2026-10-06) -- filled and open:
- FILLED: 062 concurrent-training interference with its modifiers (session
  separation, order, training status, mode, dose) and the deficit ceiling;
  063 the engine-readable placement rule (placement_rules, mode_preference,
  dose_bands, deficit_budget, step_up).
- OPEN: NO concurrent-training trial run INSIDE an energy deficit in
  resistance-trained lifters was located. Every interference estimate is at
  energy balance; the diet-plus-modality trials (Villareal 2017, Willis 2012)
  are obese middle-aged or older, mostly untrained adults. Whether the
  interference modifiers grow in a deficit is unknown.
- OPEN: stepmill / stair climbing has no interference data at all; 063
  ranks it by analogy to cycling (low impact, concentric-dominant) at the
  practitioner floor. Incline treadmill walking has ONE trial (Gergley 2009,
  folded in at v38) and it found more leg-press interference than cycling,
  so 063 ranks it below cycling. A sprint should look for any trial or
  acute-signalling study using these modes alongside lifting.
- OPEN: the mode question is split across pools (Wilson 2012 and Lundberg
  2022 type I fibres: running worse; Sabag 2018 HIIT: cycling trend worse;
  Schumann 2022: no difference). No head-to-head trial in trained lifters.
- OPEN: no dose-response for weekly cardio minutes against lean mass or
  strength in a cut. Wilson 2012's frequency / duration correlations are the
  only quantitative signal; the 063 minute bands (0-90 / 90-150 / 150-250),
  the 30-minute step and the 2-week wait are product constants.
- OPEN: the gap between sessions. Schumann 2022 separated at >=3 h, Robineau
  2016 compared 0 / 6 / 24 h in one rugby cohort (n=58). The 6 h default is a
  convention; nothing tests 3 vs 6 vs 24 h in lifters.
- OPEN: the ~500 kcal/day ceiling is a meta-regression estimate (Murphy &
  Koehler 2022) on lean-mass GAIN, from mixed populations; it was not
  derived for lean-mass RETENTION in lean, trained dieters, and it does not
  say how to estimate cardio energy cost (wearable kcal error not
  researched here).
- MEASUREMENT GAP (already listed above): no kit token for weekly cardio
  minutes or cardio mode; 063's dose bands cannot be read from data yet.
- MERGED v38 (2026-10-07): a
  parallel sprint wrote this same row from the same sources (provisional
  exercise 070, never released). Folded into 062/063 rather than shipped;
  its residual gaps, de-duplicated against the list above:
  - INCLINE WALKING beyond Gergley 2009 (n=30 untrained, 2x/week, 9 weeks,
    MORE leg-press interference than cycling): nothing in trained lifters,
    nothing at the 10-15 percent grades gyms use for "12-3-30".
  - NO trial tests cardio the DAY BEFORE a heavy lower-body session;
    Robineau 2016 always ran strength first. 063's guard-leg-day is
    mechanism.
  - Wilson 2012's practical cut-offs (often quoted as ~20-30 min, ~2-3 days
    a week) were not read at full text and are not carried.
  - Before any item moves the mode ordering above the observational band, a
    sprint should read the full texts' modality subgroups (study counts,
    intensity matching) in Wilson 2012, Lundberg 2022, Schumann 2022 and
    Sabag 2018. All of that sprint's sources were read at PubMed abstract
    only.

Pull-plane balance pass (v37, 2026-10-06) -- filled and open:
- FILLED: 066 pull/push and horizontal/vertical plane balance, with
  plane_coverage (five compose rules) and the shoulder-caution rules.
- OPEN: NO trial randomises lifters to different pull:push set ratios with a
  shoulder pain or injury outcome. The 2:1 / 3:1 program ratios were searched
  for a primary and none was found; they stay refused until one is read.
- OPEN: NO training study compares vertical against horizontal pulling for
  latissimus / upper-back growth (ultrasound or MRI). A within-subject
  pulldown-vs-row trial is registered (ClinicalTrials.gov NCT07360236,
  lat pulldown vs lat row by arm, lat hypertrophy; status not yet recruiting
  on 2026-10-06) -- fetch results when posted.
  Until then 066's both-planes floor is D.
- OPEN: every lifter shoulder study located is Kolber's group and
  cross-sectional (2009, 2013, 2017). No prospective lifter cohort models
  external-rotation strength, strength ratios or exercise selection as an
  injury predictor; the prospective and RCT evidence is handball (Clarsen
  2014, Andersson 2017).
- OPEN: whether ordinary front overhead pressing raises shoulder risk in
  lifters is unstudied; compose grades shoulder + vertical_push "high" as a
  product rule. Kolber 2013 implicates the behind-the-neck ("high-five")
  position only.
- OPEN: the push:pull strength ratios found are descriptive and athletic
  (Baker 2004, rugby league n=42; Appleby 2011, conference abstract n=13).
  No recreational-lifter or female norms; no ratio tied to an outcome.
- OPEN: Kolber 2009/2017 full texts (which ratios, which values) were not
  read; 066 quotes abstract-level findings only.

Adjacent-recovery sprint (v37, 2026-10-07) -- filled and open:
- FILLED: 067 back-to-back overlap cost (performance / adaptation / injury)
  by overlap type, with an adjacent_overlap block for the composer. 025
  source re-audit (Morán-Navarro / Pareja-Blanco attribution).
- OPEN: NO next-day cross-exercise trial was read. No study located measures
  hinge or deadlift performance the day after a squat session, or the
  reverse. A University of South Florida thesis (digitalcommons.usf.edu,
  etd article 5790, "Comparisons of acute neuromuscular fatigue and
  recovery...") appears to report squat velocity down 24 h after deadlift
  training. It returned 403 and is NOT carried. Fetch it first.
- OPEN: AXIAL / SPINAL LOAD. No trunk-extensor or spinal recovery time course
  across 24-72 h after squats or deadlifts was found. The squat-hinge
  adjacency in 067 is built from shared hip-extensor work, at the
  practitioner floor.
- OPEN: GRIP. Grip fatigue is shown only within the session (Jukic 2021,
  straps). No next-day grip carry-over data exist, so heavy pulling on
  consecutive days is unpriced.
- OPEN: INJURY. No lifter study links back-to-back overlap, frequency or
  session spacing to injury. Keogh & Winwood 2017 analysed age, sex,
  standard and class only. The general claim that "inadequate recovery
  raises injury risk" traces to muscle-damage reviews (Cheung 2003 et al.,
  via Sousa 2024), not to lifting cohorts.
- OPEN: UPPER vs LOWER. Sousa 2024 states the lower body needs 48-72 h and
  the upper body 24 h or less, citing Bartolomei 2017, Belcher 2019, Lewis
  2022 and Raeder 2016. None of the abstracts read here makes that matched
  comparison: Belcher found no between-lift difference, and Bartolomei and
  Raeder are lower-body or whole-microcycle. Lewis 2022 was not read.
  Contested in 067 until a matched upper-vs-lower trial is read.
- OPEN: Abaidia 2017 (via Sousa 2024: an upper session the day after a
  lower session sped strength recovery vs passive rest) was NOT located at a
  primary. Europe PMC returned only Abaidia's cryotherapy and curcumin
  papers. Not carried.
- OPEN: frequency trials are 6 weeks in young trained men. Grgic 2018
  (volume-equated frequency meta) was read at abstract level only. Whether
  adjacency is free over a longer block, in novices, in older lifters or in
  women is untested.
- OPEN: Goulart 2021 is the only design that repeats the session itself, and
  only to failure. The same repeated-session design short of failure (the
  case a composer mostly schedules) has not been run.

Set-floor sprint (v37, 2026-10-07) -- filled and open:
- FILLED: 070 weekly and per-exercise set floors by experience plus the
  per-session point, 071 maintenance vs growth volume in a cut, 072 the
  engine-readable set_floor / goal_floor / trim_order rule.
- OPEN: NO trial randomises novices and trained lifters to the same weekly
  volume ladder. Pelland 2025 entered training status as a covariate and did
  not report it as a moderator of the volume slope. The novice floor (6) and
  returner floor (8) in 072 are product constants inferred from which
  populations the volume studies used.
- OPEN: RETURNERS. Regaining muscle after a long layoff ("muscle memory")
  was not researched in this sprint; nothing says how much lower a
  returner's floor may sit or for how long.
- OPEN: TRIM EXERCISES vs TRIM SETS under a fixed time budget. No trial
  compares fewer exercises at more sets against more exercises at fewer sets
  with weekly sets and minutes held equal. 072's order rests on the per-
  exercise multi-set evidence, the absence of benefit for redundant
  exercises (Kassiano 2022, 8 studies, young men) and the composer's own
  transition cost.
- OPEN: MAINTENANCE DOSE OUTSIDE THE THIGH. Bickel 2011 used knee extension,
  leg press and squat only, about ten people per age-by-dose arm. Upper-body
  and small-muscle maintenance fractions are extrapolated.
- OPEN: MAINTENANCE IN A DEFICIT. Every maintenance trial found was at
  energy balance; no trial tests a maintenance dose inside a calorie deficit,
  so 071's cut split is a product rule. The 016 gap (which volume best spares
  muscle in a cut) is unchanged.
- OPEN: the ~11 fractional sets per muscle per session point is one
  SportRxiv preprint (Remmert et al., March 2025, not peer reviewed at the
  time read). Re-check for a peer-reviewed version before raising its grade.
- OPEN: AGE BOUNDARY. The maintenance trial compared 20-35 with 60-75 years;
  the age-60 switch in 072 is a constant. Nothing located covers 36-59.
- OPEN: ACSM 2026 full text was read through its abstract, infographic and
  pronouncement slides only; the per-population tables were not read.
- EXCLUDED, recorded so it is not re-added: Barbalho et al. 2020 IJSPP
  ("Evidence of a ceiling effect for training volume ... less is more?",
  PMID 31188644) is retracted (notice PMID 32804467); several other
  Barbalho papers were retracted for data irregularities (Retraction Watch
  2020-2021). Do not cite any of them for volume floors.

RIR-accuracy sprint (v38, 2026-10-07) -- filled and open:
- FILLED: exercise/rir-set-log-accuracy-077 (how far a LOGGED RIR can be
  trusted by set position, rep count, distance from failure and exercise
  type; rir_rules for the set logger / rx code). Links 030 and
  exercise/rir-accuracy-readiness-signals-061 (the DAY read, v37); the
  practice line on both 030 and 061 is now scoped to Remmert 2023 (re-audit,
  one line each).
- OPEN: POST-SET RIR IS UNVALIDATED. Every accuracy study has the lifter
  call RIR during a set and then continue to failure. The set logger stores
  a retrospective RIR for a set the user ended voluntarily, with no failure
  test behind it. No study measures that. 077 carries the intraset findings
  across as the best available transfer (D).
- OPEN: no RIR-accuracy data on the DEADLIFT / RDL / row family by
  subjective call in trained lifters (Chen 2026 tested velocity on the
  hex-bar deadlift and it failed; Helms 2017 has deadlift RPE-load
  selection in 12 powerlifters only). Bench and squat dominate the
  free-weight evidence; machine evidence is curls, pushdowns, seated rows.
- OPEN: PRACTICE EFFECT is split 2-1 across three small studies (Hermann
  2025 and Wiedenmann 2026 improved; Remmert 2023, n=9, did not). Nobody
  tested whether feedback from failure on a machine lift transfers to
  free-weight compounds, which is the only calibration route the RIR-floor
  policy leaves open.
- OPEN: no study tests a logger-side progression trigger (e.g. RIR above
  target on N consecutive exposures) against any alternative. The
  2-exposure rule in 077 is a product constant (as is 060's two-exposure
  deload trigger, listed under the fatigue-management sprint above).
- OPEN: women are a minority or absent in most samples (Refalo 2024 12/24
  and Remmert 2023 single-joint 31/58 are the exceptions, both reporting
  no sex effect); older adults appear only in Gomez-Redondo 2025 and
  Wiedenmann 2026 (larger under-estimation at RIR 2-4 in the former).
- OPEN: Hermann 2025 accuracy magnitudes (bench vs squat, change over 8
  weeks) were not in the abstract; full text not read.
- EXCLUDED: Hughes, Peiffer & Scott 2020 (J Strength Cond Res, doi
  10.1519/JSC.0000000000003865) is retracted. Its "RIR accurate at 85% 1RM,
  not at 65-75%" is widely quoted; do not cite it.

Equipment sprint (v38, 2026-10-07, machine vs free weight) -- filled and open:
- FILLED: 075 machine vs free-weight equivalence (growth, test-specific
  strength, jump transfer), 076 engine-readable machine-first selection rules
  (equipment_rules). At a caution site 076 defers to the v37 site rows: the
  057 knee ceiling and 058 variant swaps at the knee, 064 selection_rules at
  the shoulder.
- NOT CLOSED by 075: the knee follow-up's "MACHINE vs CABLE vs DUMBBELL vs
  BARBELL" gap above. 075 compares growth and strength by equipment class,
  not knee pain or patellofemoral load.
- OPEN: NO trial longer than 12 weeks and none in advanced lifters compares
  modalities; Haugen 2023's hypertrophy pool is 6 small trials, half measured
  by skinfold, circumference or whole-body plethysmography. A sprint should
  look for MRI / ultrasound muscle-level comparisons in trained lifters.
- OPEN: NO exposure-adjusted injury rate by modality was found. Kerr 2010
  (NEISS) counts ED visits without hours of use, so "machines are safer" is
  not established; 076's caution-site rule is mechanism + judgement (D).
- OPEN: no trial of machine-first loading after injury or at a symptomatic
  site (vs free-weight variants at matched load); 076 caution-site rule
  untested.
- OPEN: fatigue, recovery and lean-mass retention by modality in a caloric
  deficit -- not studied; the cut rule inherits 016's theory-only floor.
- OPEN: unilateral vs bilateral and cable vs plate-loaded vs selectorised
  machines were not separated; "machine" is one class in every trial found.
- NOT READ AT FULL TEXT: Schwanbeck 2020, Wirth 2016, Amanuma 2025 (abstracts
  via Europe PMC), Rossi 2018 (repository abstract). Haugen 2023 full text and
  Kerr 2010 abstract (article PDF) were read.

Knee-prep row (v38, 2026-10-07) -- filled and open:
- FILLED: 078 hip adductor / abductor / glute work for front-of-knee
  (patellofemoral-type) discomfort, with a structured knee_prep block
  aligned to the 056 rungs (field guide Rules 9-12 in
  the caution-ladder field guide (not public)). Written on the v36 base; aligned at
  the merge to the v37 knee rows (057 ceiling at current-load-pain, 058
  variant swaps).
- OPEN: NO trial tests the placement of hip work immediately before squats
  against the same work after the main lifts or on another day, and no
  patellofemoral trial is in barbell lifters. 078's prep dose (1-2 drills,
  1-2 sets of 10-15, about 5 min) and placement rule are product constants
  built from adjacent evidence (022, Straszek 2019, Comyns 2015).
- OPEN: whether pre-fatiguing the hip abductors changes squat knee
  mechanics was not researched; the abductor-fatigue landing studies were
  not read. 078 keeps the prep short on general grounds, not on that data.
- OPEN: optimal dose for patellofemoral exercise is unknown by the CPG's own
  statement; 078's strengthening figures are copied from trial protocols
  (3 x 10 at 60% of 10RM; high-volume 3 x 30+ in one moderate trial).
- PAIN CEILING: same gap as the knee follow-up above (no adult-validated
  patellofemoral ceiling; 057 carries Rathleff 2019's 2/10 from an
  adolescent cohort as the cautious default). 078 uses 057's ceiling and
  transports no number of its own.
- RESOLVED BEFORE THIS ROW MERGED: the sprint's proposal that a
  triage-confirmed, familiar patellofemoral ache take current-load-pain
  behaviour instead of current-other was made in v37 (056 joint-cartilage
  modifier -> 057). 078 now follows it.
- PRODUCT NOTE (not applied, no program code in this task):
  compose_rank_rules caution_policy.site_prep.knee lists
  hip_adduction_machine + ankle_mobility and no posterolateral hip drill.
  078 ranks posterolateral hip first and the adductor third; swapping or
  adding a drill is a product-approved change. Ankle mobility was not
  reviewed for knee pain here.
- SOURCE NOTES: Hott 2019 was read via a report of the paper and its PEDro
  record, not full text; Rathleff 2014 and Dolak 2011 at abstract level;
  Straszek 2019 reports experimental pain thresholds, not clinical knee pain.

Hamstring strain row (v40, 2026-10-07) -- filled and open:
- FILLED: 079 hamstring tightness vs strain triage by the user's words,
  skip vs train-around, staged return (isometric -> eccentric / lengthened
  hip -> Nordic and RDL -> running -> sprinting), red flags for referral,
  with a structured hamstring_rules block (field guide Rules 13-15 in
  the caution-ladder field guide (not public)). 056 muscle modifier now points to
  it; 054 re-audited for the first-month reinjury figure.
- OPEN: NO LIFTER DATA. Every rehabilitation and prevention trial found is
  in football players, sprinters / jumpers or (Hickey) 43 men with running-
  sport strains. A strain sustained in a heavy RDL or stiff-leg deadlift,
  and its return course, was not studied on its own.
- OPEN: THE WORD MAP IS UNTESTED. The tightness vs strain triage rests on
  the Munich classification table (level-V expert opinion). No study was
  found that tests a lay questionnaire (sudden vs gradual, one spot vs
  spread, walking pain, bruise) against MRI or clinical diagnosis. Look for
  validation of self-reported onset descriptors.
- OPEN: NEXT-DAY RULE. Hickey 2020 / 2022 set the ceiling for pain during
  exercise only (0 vs <= 4/10). The "next day no worse" rule in 079 is a
  product constant; no hamstring trial tests a next-day criterion.
- OPEN: Askling L-protocol dose (sets, reps, frequency of extender / diver /
  glider) and Hickey's running progression (supplementary table) were not
  read; 079 names the exercises, not the dose. Petersen 2011 per-week Nordic
  scheme also not read.
- OPEN: RDL vs NORDIC. No head-to-head trial of RDL / hip-extension loading
  vs Nordics for return time or reinjury was located; 079 places both in
  stage 3 on mechanism and protocol design (Maeo 2024 via 048 is growth, not
  injury).
- OPEN: one-week walking-pain referral cut is a product constant built from
  Warren 2010 (>1 day -> longer course) and Jacobsen 2016 (day-7 exam);
  no study sets a referral day for a self-managing adult.
- OPEN: avulsion urgency rests on observational surgical series (Harris
  2011, Hillier-Smith 2022) and a Delphi (Plastow 2023); no trial compares
  early vs delayed referral. The 4-week acute / chronic split is a reporting
  convention in those series.
- NOT READ AT FULL TEXT: everything except the Munich table (Europe PMC XML)
  and Hickey 2022 (accepted manuscript); the rest at abstract level. Reurink
  2014 NEJM is a letter record only.

Core / functional accessory sprint (v40, 2026-10-07) -- filled and open:
- FILLED: 081 trunk accessories for trained lifters (compound-lift coverage,
  small performance transfer, stable ground first, carries, crunch safety,
  spot reduction, back-pain prevention) with engine-readable core_rules.
- OPEN: NO training trial of trunk accessories in recreational or
  intermediate LIFTERS was located. Prieske 2016 (trained 16-44 y) and
  Saeterbakken 2022 (competitive athletes) pool small trials with median
  PEDro 4-5. Whether adding core work to a squat/deadlift programme changes
  anything beyond trunk strength in gym-goers is untested.
- OPEN: dose-response. No study varies weekly sets or exposures of trunk
  accessories. The only programming moderators are Saeterbakken's subgroups
  (>18 sessions; session length), athlete-only and univariate. The 2-3
  exposures / 2-4 sets in 081 are a plan constant.
- OPEN: session placement. No trial located that tests trunk fatigue BEFORE
  heavy squats / deadlifts against trunk work after them (performance or
  injury). 081's place-after-main-lifts rule is convention.
- OPEN: crunch safety in vivo. Contreras & Schoenfeld 2011 note no human
  in vivo study of flexion exercise on disc health; the porcine data
  (Callaghan & McGill 2001) is the whole case against. Their 60-reps,
  48-h and 1-h-after-waking limits are authors' recommendations.
- OPEN: anti-rotation (Pallof press), dead bug, bird dog, plank variants:
  EMG only (Kim 2016 graded levels); no PubMed hit for a Pallof-press EMG
  or training study in this sprint. A sprint should fetch any controlled
  trial comparing anti-rotation / anti-extension drills with dynamic
  flexion work on an outcome.
- OPEN: loaded-carry training. One 7-week RCT (Winwood 2015, n=30 rugby
  players, strongman package -- carries not isolated) and biomechanics
  (McGill 2009, Hindle 2019). No trial of farmer's or suitcase carries
  added to a lifting programme; grip-strength and carry-load norms absent
  (the v34 "loaded carries" measurement gap stands).
- OPEN: rectus abdominis HYPERTROPHY from crunch variants vs compound lifts
  in trained people was not located at a primary (only EMG / acute
  ultrasound, which 013 does not accept as a growth proxy).
- OPEN: the McGill vs Contreras/Schoenfeld flexion dispute is carried as
  contested; McGill's own reviews of "Big 3" (curl-up, side bridge, bird
  dog) were not read at a primary here.


Progression-models sprint (v40, 2026-10-07) -- filled and open:
- FILLED: the provisional deficit row (Murphy & Koehler 2022) was MERGED into
  exercise/maintenance-vs-growth-volume-cut-071 at the v40 merge, no new id;
  exercise/progression-rules-trained-cut-082, engine-readable progression rules for trained lifters in a cut
  (model_selection + progression_rules).
- OPEN: NO trial compares double progression with RIR-based load selection
  head to head, in any population. The model comparison in 082 rests on
  self-adjusting vs preset load (Mann 2010, n=23, volume unmatched; Graham &
  Cleather 2021, n=31, unsupervised) and on matched comparisons that found no
  difference (Helms 2018, n=21; 030).
- OPEN: NO progression-model trial run in an energy deficit. 071 is the only
  deficit row and it compares deficit vs no deficit, not progression schemes.
  The included-study populations of Murphy & Koehler (trained vs untrained,
  lean vs overweight) were not read at full text; transfer to trained lean
  lifters is direction-only.
- OPEN: the in-session RIR adjustment (082 next-set-rir: 1-rep dead zone,
  one increment per set) is built on the RIR error figure from 030; no study
  tests a set-to-set load-adjustment rule against a fixed-load session.
- OPEN: stall definition (2 sessions) and reset size (about 10%) remain
  untested constants (also 027 sub-gap 6). A one-week complete break cost
  lower-body strength (Coleman 2024), but a load reduction, a volume-only
  deload and a hold were never compared.
- OPEN: the rep-range "top + 2" microload extension and the 5%-of-load
  trigger have no source at all; machine / fixed-stack progression is still
  absent (027 sub-gap 5).


Warm-up ramp-set sprint (v40, 2026-10-07) -- filled and open:
- FILLED: exercise/warmup-ramp-sets-heavy-compounds-080 (specific ramp before
  heavy compounds, ramp optional at ~10RM, long easy general warm-up;
  constants + ramp_rules for the set table).
- OPEN: NO trial compares ramp shapes (number of rungs, top-rung load, reps)
  before 3-5 rep working sets at 85-90% 1RM -- the commonest heavy-compound
  case. 080's full ramp for heavy work is the NSCA 1RM test protocol plus the
  direction of Ribeiro 2020 (6 reps at 80% 1RM work). A sprint should look for
  velocity-based or reps-to-failure studies at >= 85% 1RM with varied ramps.
- OPEN: no study measures warm-up / ramp and injury in lifters (McCrary 2015
  found none for the upper body; Enes 2025 names it untested). 080 forbids an
  injury claim until one exists.
- OPEN: reps per rung near the top. Trials used 3-6 reps at 75-80% of the
  working load; nothing tests 7+ reps there. The engine's
  RAMP_REP_RATIO_BY_BAND top band (0.7 x working reps, fitted to one user's logs)
  gives 7-8 reps under 10-12 rep work -- outside the tested range, not shown
  harmful. A product decision.
- OPEN: a carry-over warm-up (second lift for the same muscles / pattern
  needs fewer rungs) is coaching practice only; no source located.
- OPEN: older lifters, women (7 of 29 in Enes 2025 is the only female data),
  and free-weight squat / deadlift under the null result (Enes used Smith
  bench and leg press).
- NOT READ: Neves, Marques, Neiva & Alves, scoping review on resistance-
  training warm-up and re-warm-up (J Sci Sport Exerc, 2025/26, doi
  10.1007/s42978-025-00361-9) and the 2021 Motricidade systematic review on
  warm-up and strength (11 studies) -- both pages blocked (403); the
  Motricidade conclusion ("specific warm-up at loads close to the maximum")
  was seen only in a search snippet and is not cited. Enes 2025 was read at
  the SportRxiv preprint, not the journal version. (v40 merge: the Motricidade
  review -- Ribeiro, Pereira, Neves, Marinho, Marques, Neiva 2021, Motricidade
  17(1) -- was read for v37's exercise/shoulder-prep-specific-vs-general-065;
  080 links 065 and still does not cite it.)


Stress / training-load sprint (v40, 2026-10-07) -- filled and open:
- FILLED: 083 life stress and strength gains / recovery / injury / adherence
  (C; acute mental fatigue B), 084 the engine-readable stress_rules +
  ask_policy for the session brief, rx, retro and e1RM / miss-streak
  predicates (D). Companion mental-health row 071 (how to ask).
- OPEN, THE CENTRAL ONE: NO TRIAL tests whether lightening the session in a
  stressful week preserves strength gains or reduces injury versus training
  as planned. Searched (PubMed, web) for wellness- or stress-guided
  resistance-training load adjustment versus a fixed program; found
  autoregulation-by-RIR/RPE trials (030) and endurance HRV-guided trials
  (sleep-recovery 011), nothing stress-guided. 084's lever choice is
  inferred from neighbouring rows (Spiering 2021 maintenance, 025 recovery
  drivers).
- OPEN: the strength-gain and recovery evidence is ONE research group,
  undergraduate weight-training classes, and the 2012 and 2014 recovery
  papers are the same 31 people. Bartholomew 2008 effect sizes were not read
  at full text (abstract gives significance only). No study in trained
  recreational lifters or in Korean / East Asian samples was located; no
  dose (stress threshold, size of the gain deficit) is carried.
- OPEN: 084's numbers -- sets x0.67, RIR floor 3, 7-day expiry, once-a-week
  ask, 3-week renegotiation -- are product constants with no direct
  evidence. Spiering 2021 is a NARRATIVE review; its 1 set / 1 session per
  week maintenance figure is for maintenance over months, not for one
  lighter week, and is not transported as a number.
- OPEN: mental-fatigue resistance-exercise trials are small crossovers with
  a lab cognitive task (Stroop etc.), certainty LOW by the newest pooling's
  own GRADE (Solon-Junior 2026). A workday is not a Stroop task; the
  same-session expectation in 084 is by analogy.
- OPEN: Mann 2016 (exam weeks, injury restriction OR 1.78) is one American
  football team; Ivarsson 2017 is athletes only. The injury direction is not
  used to set any number in 084.
- OPEN (v40 merge): 084 lightens one session in a hard week; v37\'s 060 has a
  life-stress-or-travel trigger that moves a planned deload into that week.
  How the two combine when both fire is not specified in either row; no
  source speaks to it, so it is a product decision for the composer.

Deload-in-a-cut sprint (v41, 2026-10-07;
pack-repo branch, provisional 079 released as 085) -- filled and open:
- FILLED: 085 deload and autoregulation for a trained lifter in a cut
  (structured deload_rules for the weekly retro and daily program). 060 and
  061 already covered the general deload / RIR / readiness questions and
  were linked, not restated.
- OPEN: NO trial of deload timing, recipe or triggers inside an energy
  deficit. Rogerson 2024 (re-read at full text) did not ask about diet
  phase; its physique-athlete subgroup (n=45) deloads every 5.8 weeks vs
  powerlifters 5.5, which is the only data on dieting athletes' practice.
  The "cut -> shorter deload clock (e.g. 4 weeks)" line in the program-edit
  lane has no source and stays a user option on 085.
- OPEN: the leanness / duration at which strength starts to fall in a cut.
  Murphy and Koehler 2022 (strength holds, B) pools mostly non-lean,
  non-advanced samples; the stage-lean decline is case-study evidence
  (Rossow 2013, abstract read; Pardue 2017 not read). The drift thresholds
  (1 per exposure, 3 exposures) are product constants with no validation.
- OPEN: no study separates a fatigue drop from a deficit-driven drift in
  logged sets; the 085 split is a product rule.
- OPEN: one-lift load reset size (the logger's ~10% after two misses) and
  the "2 or more anchor lifts -> whole-week deload" rule have no located
  source; linear-progression practice only.
- OPEN: subjective fatigue / mood in a deficit rests on one 13-man pilot
  with magnitude-based inference (Helms 2015, abstract read); the 14-day
  wellness re-baseline window is a product constant.
- OPEN: stacking a deload onto a diet-break week vs training through it is
  untested; Peos 2021 (ICECAP secondary, n=26) only shows strength held and
  leg endurance improved with training continued across a break.
- OPEN: Pritchard 2019 (taper, n=11 crossover; higher-intensity vs
  lower-intensity at equal ~70% volume cut, difference not significant) is
  the only trial comparing load-kept vs load-cut in a reduced-volume week,
  and it is a pre-test taper, not a mid-block deload. Read at abstract only,
  as was Pritchard 2016.
- OPEN (v41 merge): v40's 082 was cut after this branch and was not seen
  by it. 082 stall-define / stall-reset (2 sessions below the rep-range
  bottom -> ~10% reset) and stall-cut-check ("a hold in a cut is expected;
  check deficit and rate of loss") sit beside 085 drop-is-still-a-drop
  (2+ reps or RIR off target twice -> 060 deload, not blamed on the diet),
  one-lift-reset-vs-whole-week and slow-drift-is-not-a-trigger. The reset
  size is the same constant; which rule fires first when a lift in a cut
  meets both definitions is not specified in either row. Linked, not
  merged; a product decision for the composer.
- OPEN (v41 merge): 084's stressed-week lighter plan (sets x0.67, RIR floor
  3) is a third lighter-session path beside the 060 deload and the 061 day
  trim; how it combines with a cut's deload is not specified.
- KNOWN CONFLICT (v41, for the composer maintainer; NOT resolved here, neither
  side changed): 085 sets-before-load reads 060 deload_prescription --
  weekly_sets_multiplier 0.5 (halved sets) and rir_floor 3 (RIR >= 3), both
  product constants. The live program's deload is 60% volume and RIR
  +2 (relative to the user's usual target). The two disagree on the volume
  cut (50% vs 40% removed) and on the effort rule (an absolute floor of 3
  vs a +2 offset). The knowledge rows grade their numbers D and only the
  direction (fewer sets, further from failure) is sourced, so neither
  number is evidence-backed over the other; the live program's rule governs
  the live program. Whether 060 / 085 should adopt the live program's numbers
  is the composer maintainer's call.

Goal-phase sprint (v41, 2026-10-07; provisional
086 / 087 released as 086 / 087) -- filled and open:
- FILLED: exercise/phase-energy-volume-ramp-evidence-086 (surplus size,
  previous-volume anchoring, detraining time course, the absence of any
  lifting ramp trial) and exercise/phase-volume-rules-087 (engine-readable
  phase_volume_rules, ramp_rules, weekly_goal_fit_check,
  goal_reconsult_triggers for the goal re-consult and the weekly check).
- OPEN: RAMP RATE. No resistance-training trial tests how fast to raise
  weekly volume after a cut, a maintenance block or a layoff. The only
  fixed weekly ramp trial located (Buist 2008, 10% rule) is in novice
  runners and null. 087's step (larger of 2 sets or 20% a week), the
  2-week start window and the 3-week layoff boundary are product constants.
- PARTLY ADDRESSED (the set-floor sprint's RETURNERS gap): Psilander 2019
  (size back to baseline after 20 weeks off, strength ~60% retained,
  retraining response not faster in the previously trained leg -- but no
  myonuclear gain in the first phase, so muscle memory was not truly
  tested) and Ogasawara 2013 (3-week breaks cost nothing overall). Still
  open: how fast a returner regains size, and whether a returner tolerates
  a steeper ramp. Seaborne 2018 (epigenetic memory) was not read.
- OPEN: SURPLUS SIZE. One randomised trial in trained lifters (Helms 2023,
  17 completers, 8 weeks, mixed experience) plus Garthe 2013 in elite
  athletes. No trial of surplus size beyond 8-12 weeks or in advanced
  lifters; the 0.25-0.5% weekly gain band is a review number (Iraki 2019).
- OPEN: PREVIOUS-VOLUME ANCHORING was tested only at energy balance, in
  trained young men, over 8 weeks (Barsuhn 2025, n=29; Scarpelli 2022,
  n=16, one leg each); Brigatto 2022 (32 > 16 weekly sets) points the other
  way. No trial runs it inside a surplus or a deficit, in women, or in
  novices.
- OPEN: RECOMPOSITION. Whether novices and returners can gain muscle in a
  deficit (Barakat et al. 2020, Strength Cond J review) was found only
  through secondary summaries; the paper was not read, so 087 has no
  recomp phase. A future row should read it before adding one.
- OPEN: WEEKLY CHECK WINDOWS. The 2-week strength window, 3-week weight
  window, 4-week flat-gain window, 16-week open-cut trigger and the
  one-proposal-a-week cap have no source; they are product constants
  sized to the nutrition 029 noise bands.
- OPEN: REVERSE DIETING (stepping calories up after a cut) was not
  researched; 087 says only that cut -> maintain changes the eating and
  keeps the volume.
- SOURCE NOTES: all primary trials in 086 were read at abstract level
  (Europe PMC records); Slater 2019 and Iraki 2019 at abstract level.
- OPEN (v41 merge): 087 weekly_goal_fit_check cut_falling ("falling on two
  or more main lifts -> smaller deficit, a deload (060) or a maintenance
  stretch") and 085 one-lift-reset-vs-whole-week / slow-drift-is-not-a-
  trigger read the same logged sets in a cut with different windows; the
  two branches were cut in parallel and did not see each other. Linked
  (087 -> 085, 082); which proposal the retro speaks first is a product
  decision for the composer.
- NAMING NOTE (v41 merge): 086's "ramp" is weekly volume after a phase
  switch or layoff; v40's 080 "ramp sets" are warm-up sets before a heavy
  lift. Unrelated rows, no overlap.

Plantar heel pain / foot rules (v41, 2026-10-07; provisional 088 released as 088) -- filled and open:
- FILLED: 088 plantar heel-raise dose keyed to the 056 rungs (structured
  foot_rules: dose, placement, week_load, footwear, intrinsic), evidence vs
  folklore table. 055 re-audited: Riel 2023 (n=180) found heel raises add
  nothing over advice + heel cup; 055's plantar wording narrowed, letter kept.
- OPEN: NO plantar-heel-pain trial in LIFTERS. All three treatment RCTs
  (Rathleff 2015 n=48, Riel 2019 n=70, Riel 2023 n=180) are one Danish
  group, middle-aged adults, mostly not lifting. Whether squats, deadlifts,
  leg press or walking lunges aggravate plantar fasciopathy is untested;
  088's "keep them under the 055 ceiling" is product judgement.
- OPEN: LIFTING FOOTWEAR. No study of flat vs heeled (weightlifting) shoes,
  barefoot or minimalist lifting in plantar heel pain. 088 leaves the
  user's lifting shoe alone (D).
- OPEN: heel-raise PREVENTION. No trial gives heel raises (or any foot
  work) to lifters to prevent plantar heel pain; Taddei 2020 foot-core
  training cut ALL running injuries in runners (n=118) and is not
  plantar-specific. 088 adds nothing at baseline.
- OPEN: INTRINSIC-FOOT DOSE. Huffer 2017 could not identify a treatment
  benefit; 088's 1-2 drills x 2-3 x 10-15 is product judgement. A
  plantar-fasciopathy RCT of intrinsic training (e.g. NCT05455645) was
  registered but no result was read.
- OPEN: the 2023 heel-pain CPG (Koc 2023, JOSPT) still not read at full text
  (publisher 403, host DNS failure). Resistance training B carried from two
  agreeing secondary summaries; the orthosis letter disagrees between them
  and is not carried. Re-read at full text and replace.
- OPEN: the pain ceiling for the heel raise. Riel 2019/2023 allowed ANY
  tolerable pain during the exercise; 088 applies 055's 5/10 ceiling
  (Achilles-derived). Neither ceiling was tested in plantar fasciopathy.
- OPEN: heel-raise "replaces the program calf raise" and "after the main
  lifts" placement have no trial; calf-hypertrophy volume and the fascia
  heel-raise dose were never studied together.
- SOURCE NOTES: Riel 2018 (isometric crossover), Huffer 2017, Taddei 2020,
  van Leeuwen 2016 at abstract; Riddle 2003 at record; Rathleff 2015,
  Riel 2019, Riel 2023 at full text.

Elbow tendinopathy / pulling lifters (v46 provisional, 2026-10-07; provisional 089) -- filled and open:
- FILLED: 089 lateral / medial elbow rules keyed to the 056 rungs
  (structured elbow_rules: site, dose, swaps, placement, info_only),
  evidence vs folklore table.
- OPEN: NO elbow tendinopathy trial in LIFTERS. Every treatment trial is
  lateral elbow tendinopathy in middle-aged, mostly non-lifting adults
  (Bisset 2006 n=198, Coombes 2013 n=165, Peterson 2011 n=81 / 2014 n=120,
  Tyler 2010 n=21, Vuvan 2020 n=40). The grip-swap order, straps, machine
  swaps, "replace the program's wrist curls" and "after the main pulls" have
  no trial (D).
- OPEN: MEDIAL elbow (golfer's elbow). See 2026 review: 5 small studies,
  143 patients, low certainty, no meta-analysis; Tyler 2014 is an
  uncontrolled case series. 089 mirrors the lateral dose to the wrist
  flexors (transport D). A medial RCT should replace it when one exists.
- OPEN: the elbow pain rule. 089 uses about 3/10 during the forearm
  exercise and settled by morning (Coombes 2015, expert commentary); 055's
  5/10 ceiling (Achilles, Silbernagel 2007) is the outer limit for the gym
  lifts. Neither was tested in elbow tendinopathy. The rule is likely to
  need a decision when 055 / 056 next change.
- OPEN: 056's tendon modifier and 055's tissue list (patellar, Achilles,
  rotator cuff) do not name the elbow; 089 applies them by analogy. A
  smallest-edit pointer from 056 (line "other joints have no graded loading
  row yet") to 089 was NOT made on this branch (left to the merge, to avoid
  colliding with sibling edits to 056).
- OPEN: distal biceps tendinopathy (front-of-elbow ache without a tear) was
  not researched; 089 routes front-of-elbow pain to triage.
- OPEN: no elbow source checked for the circulating "10,000 elbow
  extensions a week" lifter claim seen in secondary web copy; no primary
  found, not carried.
- OPEN: Lowdon 2024 (J Hand Surg Am) network meta-analysis found at record
  only (abstract not released); not read, not cited.
- SOURCE NOTES: Bisset 2006, Tyler 2010, Coombes 2015 and the Stasinopoulos
  2022 editorial at full text; Coombes 2013, Karanasios 2021, Peterson
  2011 / 2014, Coombes 2016, Vuvan 2020, Struijs 2001 at abstract; See 2026
  and Tyler 2014 at record.
