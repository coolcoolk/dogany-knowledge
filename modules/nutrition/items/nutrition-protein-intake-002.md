---
# Knowledge warehouse #1. Frozen F2 contract + v3 map + an internal ticket.
# Converted from an internal research batch file finding [9] (protein dose
# worked example, vote 3-0). Rubric: the nutrition rubric @obs-inferential row
# nutrition/protein-intake-002. This item OWNS the dose/absorption claim (v3 5
# single-ownership: protein-dose-absorption = nutrition evidence base). Its
# hypertrophy-timing sibling (the anabolic window) owns exercise/ -- see
# source:exercise/protein-anabolic-window-002 (two distinct claims, not a dual ID).
# Source re-audit 2026-10-06: the hypocaloric 2.3-3.1 band was quoted per kg
# body weight via the ISSN 2017 stand; its source (Helms 2014, PMID 24092765)
# states it per kg FAT-FREE MASS. Note + prose now point to 062. Range, per-meal
# figure and grade unchanged (Morton 2018 / Nunes 2022 still support ~1.6).
# Source re-audit 2026-10-07 (a research sprint, folded at the v37
# merge): the same FFM unit confirmed at the Helms 2014 abstract; the
# trained-lifter reading of Morton's 2.2 and the per-meal figures lives in
# nutrition/protein-deficit-trained-lifter-023.
# Source re-audit 2026-10-07 (protein distribution re-audit): the per-meal
# clause (~0.25 g/kg or 20-40 g "maximized at") is separated from the daily
# range in the claim and handed to nutrition/protein-per-meal-ceiling-008,
# where a 2023 tracer trial and its printed dispute hold it as contested. The
# daily range, its sources and the letter are unchanged; 063 still sizes a
# one-meal add-on with the figure, as a planning dose and never as a cap.
id: nutrition/protein-intake-002
domain: nutrition
grade: A
lane: "@obs-inferential"      # optional on a single-lane domain; kept for clarity.
locale: universal
as_of: 2017
contested: no
sources:
  - "https://www.tandfonline.com/doi/full/10.1186/s12970-017-0177-8"  # ISSN 2017 protein stand (batch1 3-0)
  - "ACSM/AND/DC joint position stand (~1.2-2.0 g/kg/day)"            # independent corroboration
  - "IOM Acceptable Macronutrient Distribution Range (protein)"       # independent corroboration
  - "MacNaughton 2016 -- per-meal MPS refinement inside the range"
  - "source:nutrition/protein-deficit-lean-mass-target-062 -- owns the deficit target; corrects the FFM unit"
  - "source:nutrition/protein-per-meal-ceiling-008 -- the per-meal figure is contested there; this claim no longer rests on it"
  - "framework:GRADE spine -- converged multi-body corroboration, no credible dispute"
applicability:
  axes:
    - key: body_weight_kg     # kit_life-measured axis, used as a scaling input.
      type: numeric
      role: scale
      unknown_policy: ask
      rescale:                # per-unit range refract multiplies by the
        per_unit_low: 1.4     # user's measured weight (RESCALE op). The model
        per_unit_high: 2.0    # never computes this -- data drives the number.
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      Total daily protein scales with body weight (1.4-2.0 g/kg/day). RESCALE
      from the user's measured weight rather than quoting fixed grams. In a
      caloric deficit the target is owned by
      nutrition/protein-deficit-lean-mass-target-062 (1.6-2.4 g/kg body
      weight); the 2.3-3.1 band is per kg of FAT-FREE MASS and must never be
      multiplied by body weight.
    grade: A
claim: >
  Total daily protein intake of ~1.4-2.0 g/kg/day is sufficient for most
  exercising adults. A per-meal figure of ~0.25 g/kg body weight, or an
  absolute 20-40 g, is the long-used planning dose for one meal; that it is
  the most a meal can use for muscle-building is contested and is not part of
  this claim (nutrition/protein-per-meal-ceiling-008).
reasoning: >
  The ISSN 2017 protein stand aligns with the joint ACSM/AND/DC position
  (~1.2-2.0 g/kg/day) and the IOM Acceptable Macronutrient Distribution Range;
  no credible body disputes the intake range, and MacNaughton 2016 refines the
  per-meal figure inside it. That per-meal figure is a planning dose, not a
  ceiling: a 2023 tracer trial and the dispute it started are carried in
  nutrition/protein-per-meal-ceiling-008, so the top band applies to the daily
  range only. Convergence across independent institutional bodies with no
  dispute on the range reaches the top confidence band on the GRADE spine. This is the
  dose/absorption claim (nutrition-owned); the timing/anabolic-window claim is a
  separate exercise-owned item.
---

# nutrition/protein-intake-002

The daily-intake range is the load-bearing number. It is corroborated across
independent institutional bodies with no credible dispute, so the claim sits at
the top of the confidence ladder. The per-meal dose (about 0.25 g/kg, 20-40 g)
is kept as a planning figure only; whether a meal can use more is under live
dispute in nutrition/protein-per-meal-ceiling-008.

The daily figure scales with the user's body weight; the answer path RESCALES
from a measured weight rather than reciting the fixed grams. Lean-mass retention
during a caloric deficit is a separate target owned by
nutrition/protein-deficit-lean-mass-target-062; the 2.3-3.1 figure often quoted
for it is per kilogram of fat-free mass, not body weight. Protein timing (the anabolic window) is a
separate, exercise-owned claim and is deliberately not decided here.
