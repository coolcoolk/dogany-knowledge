---
# Authored 2026-09-02 (nutrition-lane collection sprint, v11). The consumer asks
# this question daily ("should the log be evened out across meals?"), so the
# absence of a good answer has to be stored as a first-class item rather than
# left for the model to fill in. The positive finding here is exactly the design
# class this lane exists to discount: an n=8 acute crossover.
# Source re-audit 2026-10-07: the "wrong population" limit (note 1) and the
# "nobody has tested" sentence in the body were out of date. Since authoring,
# randomised trials varied the split in dieting adults (Hudson 2017, Lombardo
# 2021, De Leon 2024; owned by nutrition/protein-distribution-while-dieting-
# 090), in young men who had not trained for a year (Yasuda 2020, read at full
# text: total lean tissue P=0.056, appendicular lean tissue identical) and in
# resistance-trained men (Tavares 2025, three vs five protein meals, 18
# completers); Areta 2013 (24 trained men, 12 h) joins the acute positives.
# Claim, note 1, reasoning and body narrowed. Letter and contested flag are
# unchanged: the new trials are small, mostly at about 1 g/kg, or not in lifters.
id: nutrition/protein-distribution-thin-009
domain: nutrition
lane: "@obs-inferential"
grade: C
locale: universal
as_of: 2013-2026
contested: yes
sources:
  - "https://doi.org/10.3945/jn.113.185280"  # Mamerow MM, Mettler JA, English KL, Casperson SL, Arentson-Lantz E, et al. J Nutr 2014;144(6):876-880. PMID 24477298 -- n=8, 7-day crossover, EVEN vs SKEW, the positive acute result
  - "https://doi.org/10.1016/j.clnu.2017.02.020"  # Kim IY, Schutzler S, Schrader AM, Spencer HJ, Azhar G, Wolfe RR, et al. Clin Nutr 2018;37(2):488-493. PMID 28318687 -- 8-week RCT, n=14 older adults, NULL on lean body mass, strength, function
  - "https://doi.org/10.3390/nu14214442"  # Justesen TEH, Jespersen SE, Tagmose Thomsen T, Holm L, van Hall G, et al. Nutrients 2022;14(21):4442. PMID 36364705 -- RCT, n=24 older adults, no difference in muscle protein synthesis
  - "https://doi.org/10.3390/nu12051441"  # Hudson JL, Bergia RE III, Campbell WW. Nutrients 2020;12(5):1441. PMID 32429355 -- review: does the evidence support the concept
  - "https://doi.org/10.1007/s00394-021-02487-2"  # Jespersen SE, Agergaard J. Eur J Nutr 2021. PMID 33550490 -- systematic review: evenness associated with higher muscle mass but NOT strength or turnover
  - "https://doi.org/10.1113/jphysiol.2012.244897"  # Areta JL, Burke LM, Ross ML, et al. J Physiol 2013;591(9):2319-2331. PMID 23459753 -- 24 trained men, 8 per group, 80 g whey over 12 h after lifting; 4 x 20 g every 3 h gave 31-48 percent more myofibrillar synthesis than 8 x 10 g or 2 x 40 g (acute, 12 h, not a growth outcome)
  - "https://doi.org/10.1093/jn/nxaa101"  # Yasuda J, Tomita T, Arimitsu T, Fujita S. J Nutr 2020;150(7):1845-1851. PMID 32321161 -- 26 analysed of 33 men aged 18-26 with no resistance training for a year, 12 weeks with energy intake not restricted; breakfast-enriched vs dinner-heavy split; total lean tissue +2.50 vs +1.77 kg (P=0.056), appendicular lean tissue +1.14 vs +1.14 kg, no group difference in strength. Full text read
  - "https://doi.org/10.23736/S0022-4707.25.16698-X"  # Tavares H, Roschel H, Felício V, et al. J Sports Med Phys Fitness 2025;65(10):1337-1345. PMID 40673785 -- 32 resistance-trained men randomised, 18 completed 8 weeks at energy balance; three vs five protein meals, similar daily protein; lean mass +1.15 vs +0.63 kg, no between-group difference. Abstract only
  - "https://doi.org/10.1016/j.clnu.2023.04.004"  # Agergaard J, Justesen TEH, Jespersen SE, et al. Clin Nutr 2023;42(6):899-908. PMID 37086618 -- 24 older adults at 1.5 g/kg lean mass, even vs skewed; whole-body protein balance more positive in the even group after breakfast and lunch, equal after dinner; muscle synthesis did not differ
  - "source:nutrition/protein-distribution-while-dieting-090 -- the dieting trials (Hudson 2017, Lombardo 2021, De Leon 2024) and the rules that follow"
  - "source:nutrition/protein-intake-002 -- daily total, the claim that does have converged support"
  - "source:exercise/small-n-culture-006 -- the lane rule that forces the discount applied here"
applicability:
  axes:
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE EVIDENCE BASE IS STILL THE WRONG POPULATION for a lifter on a cut.
      The first two outcome-level trials (lean mass, strength, function) were
      in OLDER adults, where the research motivation is sarcopenia. Since then
      the split has been varied in overweight adults while dieting (three
      trials at about 1 g/kg, owned by 090, no difference), in young men who
      had not trained for a year (Yasuda 2020: total lean tissue +2.50 vs +1.77
      kg favouring the breakfast-enriched split at P=0.056, appendicular lean
      tissue identical) and in resistance-trained young men (Tavares 2025:
      three vs five protein meals, 18 completers, no difference). None was
      adequately powered and none put a trained lifter on a cut at a lifter's
      protein target. Applying either the positive or the null result to such a
      user is an extrapolation across populations.
    grade: D
  - note: >
      The systematic-review signal that evenness associates with higher muscle
      mass is OBSERVATIONAL and carries this lane's standard confounding
      objection with unusual force: people who eat protein at breakfast differ
      systematically from people who do not. It did not extend to strength or to
      protein turnover, which is what a causal effect would be expected to move.
    grade: C
claim: >
  Whether daily protein should be spread evenly across meals is not established.
  The often-cited positive results are acute tracer studies of muscle protein
  synthesis: an n=8 seven-day crossover over 24 hours, and a 12-hour study in
  24 trained men in which four 20 g feeds every 3 hours beat two 40 g feeds.
  When the question was taken to controlled trials with real outcomes it mostly
  did not replicate: an 8-week randomised trial (n=14, older adults) found no
  effect of distribution pattern on lean body mass, strength, function or
  synthesis rate, a further trial (n=24, older adults) found no difference in
  synthesis or amino acid utilisation, three trials in dieting adults found no
  difference in lean-mass change or fat loss (see
  nutrition/protein-distribution-while-dieting-090), and in resistance-trained
  men three versus five protein meals gave the same lean-mass gain (18
  completers). The one result in favour of an even split at an outcome level is
  borderline (young men new to lifting, n=26, P=0.056, no difference in arm and
  leg lean tissue). A systematic review found evenness associated with higher
  muscle mass but not with strength or protein turnover, and that association
  is observational. Total daily protein remains the supported lever.
reasoning: >
  This is a case where the field's structure, not any single result, decides the
  grade. The concept is mechanistically attractive and heavily promoted, the
  supporting trials are small acute tracer studies (eight people over 24 hours;
  24 over 12 hours), and the attempts to confirm it at an outcome that matters
  returned null or borderline: two nulls in older adults, three in dieting
  adults, a borderline result in young men whose arm and leg lean tissue did not
  differ, and a null in trained men. Under this lane's rules and
  exercise/small-n-culture-006, an acute crossover of that size is precisely
  what must be discounted, and the outcome-level trials are the more informative
  signal. The letter is not raised although the null side has grown: the new
  trials are small (14-47 completers), most were at about 1 g/kg in untrained or
  overweight people, and the acute work and the borderline result cannot be
  dismissed. It is held at the observational band with a contested flag rather
  than being reported as either established or refuted, because the trials that
  exist are small, mostly outside the lifter-on-a-cut population, and none is
  adequately powered. The honest operational answer for a consumer reading a
  daily log is that skew toward dinner is not a defect to correct, and that
  chasing an even split at the cost of hitting the daily total inverts the
  evidence.
---

# nutrition/protein-distribution-thin-009

Spreading protein evenly across the day is one of the most confidently repeated
pieces of nutrition advice for anyone training, and its evidence base does not
support that confidence. The study everyone cites fed eight people for a week and
measured protein synthesis over twenty-four hours, and a second tracer study in
24 trained men found four 20 g feeds three hours apart beat two 40 g feeds over
twelve hours. When later investigators asked whether the pattern actually changes
anything a person can feel, over eight weeks and with lean mass, strength and
function as endpoints, it did not. A second randomised trial found no difference
in synthesis either, and trials in dieting adults found no difference in the
muscle or fat they lost.

The one supportive signal at scale is a review-level association between an even
intake pattern and higher muscle mass, and it fails the obvious test: it does not
extend to strength or to protein turnover, which is what a real causal effect
should also move. Association without the mechanistic corroborates is exactly the
pattern this lane treats as confounded.

There is a further limitation that is easy to miss. The first two controlled
trials were run in older adults, because the question is funded as a sarcopenia
question. Younger adults have since been tested in small trials: dieting adults
showed nothing, a 26-man trial in people new to lifting found a borderline edge
for a breakfast-enriched split that sat entirely outside the arms and legs, and
three versus five protein meals made no difference in trained men. No trial has
put a trained lifter on a cut and varied the split. So the claim is held at the
observational band with the dispute flagged, and the practical stance is
deliberately permissive: a log that puts most protein at dinner is not a problem
to be fixed, and sacrificing the daily total to even out the split would trade a
supported lever for an unsupported one.
