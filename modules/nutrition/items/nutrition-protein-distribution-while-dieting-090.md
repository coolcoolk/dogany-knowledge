---
# Authored 2026-10-07 (protein distribution re-audit). One narrow question a
# diet card meets on every cut day with a dinner-heavy log: while the user is in
# a calorie deficit, does it matter whether the day's protein is spread across
# the meals or piled at dinner? Owned elsewhere and NOT restated here: the
# general question and the acute tracer work (nutrition/protein-distribution-
# thin-009), the per-meal ceiling dispute (008), timing around a session (024),
# the deficit protein target (062, 023). This item owns only the trials that
# varied the split during energy restriction, the one appetite signal, and the
# rules that follow. Primaries read 2026-10-07: every abstract below on PubMed;
# Yasuda 2020 at full text (Europe PMC); Hudson 2017 methods via the PMC page;
# De Leon 2024 and 2026 as abstract plus the NCT03202069 registry record (full
# text not retrieved).
#
# distribution_rules is structured data for a diet module (nudge, last-call
# line, card copy). Values are plain text; the module copies them, it does not
# compute from them.
id: nutrition/protein-distribution-while-dieting-090
domain: nutrition
lane: "@obs-inferential"
grade: B
locale: universal
as_of: 2013-2026
contested: no
sources:
  - "https://doi.org/10.3945/ajcn.117.158246"  # Hudson JL, Kim JE, Paddon-Jones D, Campbell WW. Am J Clin Nutr 2017;106(5):1190-1196. PMID 28903957, NCT02066948 -- RCT, 41 adults (age 35, BMI 31.5) completed 16 weeks at 750 kcal/day below requirement with resistance training 3 days/week; 90 g protein/day (1.0 g/kg) as 30/30/30 g vs 10/20/60 g at breakfast/lunch/dinner; whole-body lean mass -1.0 kg and fat mass -6.9 kg overall, no difference by pattern; the authors flag statistical power
  - "https://doi.org/10.1016/j.tjnut.2024.02.009"  # De Leon A, Roemmich JN, Casperson SL. J Nutr 2024;154(4):1347-1355. PMID 38365118, NCT03202069 -- RCT, 43 women aged 20-44, BMI 28-45; 8 weeks at 20 percent energy restriction with all food provided, then 8 weeks self-selected; even vs dinner-heavy protein (registry record: 90 g/day, 30 g per meal vs 10/15/65 g); no group or group-by-time effect; fat-free mass -1.0 kg and fat mass -4.6 kg over 16 weeks. Abstract and registry read
  - "https://doi.org/10.23736/S2724-5985.20.02694-X"  # Lombardo M, Bellia C, Aulisa G, et al. Minerva Gastroenterol 2021;67(2):183-189. PMID 32218430 -- RCT, 47 adults (BMI 28.4), 8 weeks at about 788 kcal/day deficit, 90 g protein/day (1.1 g/kg); EVEN vs UNEVEN differed only modestly (breakfast/lunch/dinner/snacks 16.7/32.8/31.3/19.2 vs 15.4/36.6/34.9/12.4 percent); fat mass -2.3 kg, lean mass 0.0 kg, no difference. A weak contrast
  - "https://doi.org/10.1113/JP275246"  # Murphy CH, Shankaran M, Churchward-Venne TA, et al. J Physiol 2018;596(11):2091-2120. PMID 29532476 -- n=10 per group, overweight or obese OLDER men in energy restriction; balanced (25 percent x 4 meals) vs skewed (7:17:72:4) protein pattern; bulk myofibrillar synthesis (deuterated water, 2 weeks) did not differ, with or without resistance training
  - "https://doi.org/10.1016/j.jand.2026.156391"  # De Leon A, Roemmich JN, Casperson SL. J Acad Nutr Diet 2026;126(9):156391. PMID 42242423 -- same trial, 44 analysed: reinforcing value of energy-dense snack foods 0.44 vs 0.55 (P=.0476) and snack food eaten 44.3 vs 62.0 g (P=.0197) in even vs dinner-heavy; snacks earned did not differ (P=.2338). Abstract only
  - "https://doi.org/10.1093/jn/nxaa101"  # Yasuda J, Tomita T, Arimitsu T, Fujita S. J Nutr 2020;150(7):1845-1851. PMID 32321161, UMIN000037583 -- 33 men aged 18-26 with no resistance training for at least a year, 26 analysed, 12 weeks of training 3 days/week with energy intake not restricted (about 2,450-2,600 kcal/day); breakfast-enriched (0.33/0.46/0.48 g/kg) vs dinner-heavy (0.12/0.45/0.83 g/kg); total lean tissue +2.50 vs +1.77 kg (P=0.056, d=0.795) but appendicular lean tissue +1.14 vs +1.14 kg (P=0.991); week-12 total protein 1.30 vs 1.45 g/kg. Full text read
  - "https://doi.org/10.23736/S0022-4707.25.16698-X"  # Tavares H, Roschel H, Felício V, et al. J Sports Med Phys Fitness 2025;65(10):1337-1345. PMID 40673785 -- 32 young resistance-trained men randomised, 18 completed 8 weeks at energy balance; three vs five protein meals above 0.24 g/kg each, similar daily protein; lean mass +1.15 vs +0.63 kg, leg muscle area and knee-extension 1RM up in both, no between-group difference (labelled a randomised non-controlled trial). Abstract only
  - "https://doi.org/10.1113/jphysiol.2012.244897"  # Areta JL, Burke LM, Ross ML, et al. J Physiol 2013;591(9):2319-2331. PMID 23459753 -- 24 trained men, 8 per group, 80 g whey over 12 h after resistance exercise; 4 x 20 g every 3 h gave 31-48 percent more myofibrillar synthesis than 8 x 10 g or 2 x 40 g (acute, 12 h, not a growth outcome)
  - "source:nutrition/protein-distribution-thin-009 -- the general question; its letter is not raised by this item"
  - "source:nutrition/protein-per-meal-ceiling-008 -- a large meal is not wasted protein"
  - "source:nutrition/protein-timing-total-matched-024 -- timing around a session and the Korean day shape"
  - "source:nutrition/protein-deficit-lean-mass-target-062 -- owns the deficit protein target; this item does not restate it"
  - "source:nutrition/protein-deficit-trained-lifter-023 -- the same target read for a trained lifter"
  - "source:nutrition/weight-loss-rate-lean-mass-012 -- the size of the deficit is the larger lean-mass lever"
  - "source:nutrition/meal-protein-nudge-rules-063 -- the nudge table these rules feed"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: sex
      type: categorical
      role: soft
      unknown_policy: hedge
distribution_rules:
  - rule: split-not-a-lever-in-a-cut
    when: program is cut, the day's protein total is at or above the user's floor, and the split is uneven (low breakfast, heavy dinner)
    effect: no distribution nudge and no spread-it-out line; the day is judged on the protein total (063) and the size of the deficit (012)
    basis: Hudson 2017, De Leon 2024 and Lombardo 2021 (no difference in lean-mass change or fat loss while dieting)
    basis_grade: B
  - rule: even-split-hunger-option
    when: program is cut, the user reports evening or between-meal snacking or hunger, and most of the day's protein sits at dinner
    effect: may offer once, as an optional trial, moving a lunch-sized portion of the dinner protein to lunch (the even arm's test lunch held 35 g); say it is a hunger tactic from one trial in women, not a muscle rule; drop it if declined and do not repeat it
    basis: De Leon 2026 (44 women, snack-food task)
    basis_grade: C
  - rule: meal-count-is-free
    when: user asks how many protein meals to eat in a day
    effect: no count is enforced; three and five protein meals gave the same lean-mass gain in resistance-trained men at energy balance; choose by schedule and hunger
    basis: Tavares 2025 (32 randomised, 18 completed); Hudson 2017
    basis_grade: C
  - rule: say-what-was-tested
    when: any distribution line is spoken to a resistance-trained user in a cut
    effect: say the dieting trials were in overweight adults eating about 1 g/kg, not lifters on a 1.6-2.4 g/kg cut; never say the split is proven irrelevant for lifters and never say it is proven to matter
    basis: the populations of Hudson 2017, De Leon 2024 and Lombardo 2021; no trial in trained lifters in a deficit located
    basis_grade: D
refraction_notes:
  - note: >
      THE TRIALS WERE AT ABOUT 1 G/KG, NOT AT A CUT TARGET. Each of the three
      body-composition trials fed 90 g protein a day (1.0-1.1 g/kg) to
      overweight adults (BMI 27-45), and none, as read, selected for
      resistance-training experience. A lifter's cut target is 1.6-2.4 g/kg (062).
      At that total even a dinner-heavy day puts more protein into the lighter
      meals than these trials' skewed arms had, so the trials arguably gave the
      split its best chance to matter. That is an inference, not a finding, and
      no trial in resistance-trained lifters in a deficit was located.
    grade: D
  - note: >
      NO TRIAL REMOVED BREAKFAST PROTEIN. The skewed arms still ate 10-15 g at
      breakfast (Hudson 10 g, De Leon 10 g per registry, Lombardo about 15
      percent of the day). A day with no breakfast, which is a common young
      Korean day (024), puts everything into two meals; that shape was not
      tested for lean mass in a deficit.
    grade: D
  - note: >
      THE ONE YOUNG-ADULT HYPERTROPHY SIGNAL IS BORDERLINE AND NOT IN
      LIFTERS. Yasuda 2020 reports that a breakfast-enriched split is "more
      effective", but total lean tissue differed at P=0.056, appendicular lean
      tissue (the arms and legs) was identical, strength gains did not differ
      significantly by group, the dinner-heavy group ate numerically more
      protein in total (1.45 vs 1.30 g/kg at week 12, group effect not
      significant), 7 of 33 were not analysed, the men had not trained for at
      least a year, and energy was not restricted. It is a lead, not a result,
      and it is not repeated as one.
    grade: C
  - note: >
      THE MECHANISM EXISTS AND HAS NOT TRANSLATED. Areta 2013 found 4 x 20 g
      every 3 h beat 2 x 40 g and 8 x 10 g for 12-hour myofibrillar synthesis in
      24 trained men, which is why the even split is promoted. The two
      outcome-level checks in younger adults that fit the question, Yasuda 2020
      (borderline, above) and Tavares 2025 (three vs five protein meals, no
      difference, 18 completers), did not show the synthesis edge turning into
      measurable growth.
    grade: C
  - note: >
      THE APPETITE SIGNAL IS ONE TRIAL IN WOMEN. De Leon 2026 measured, in a
      lab task, how hard participants would work for energy-dense snack food 2
      hours after a lunch of 35 g (even) or 20 g (skewed) protein, and how much
      they ate. Fewer snacks eaten in the even group (44 vs 62 g) is
      consistent with a satiety effect, but it is a single trial, in women, on a
      laboratory measure, reported at abstract level here. It supports at most
      an optional tactic, never a rule.
    grade: C
claim: >
  While losing weight on a fixed daily protein total, spreading protein across
  the three main meals did not change lean-mass loss or fat loss compared with
  a dinner-heavy split in randomised trials of overweight adults. Hudson 2017
  (n=41, 16 weeks, 750 kcal/day deficit with resistance training, 90 g/day) and
  De Leon 2024 (n=43 women, 8 weeks of 20 percent restriction with all food
  provided plus 8 weeks self-selected) found no difference; Lombardo 2021
  (n=47, 8 weeks) agreed but its two patterns differed little. A tracer study
  in older men in energy restriction (Murphy 2018, n=20) found no difference in
  myofibrillar synthesis. One trial in women (De Leon 2026) found the even split
  lowered the reward value and intake of energy-dense snack foods in a lab
  task. All of this was at about 1 g/kg protein in overweight, mostly untrained
  adults; no trial varied the split in resistance-trained lifters in a deficit
  at a lifter's protein target. For a diet card: the daily total and the size
  of the deficit come first, the split is not worth a nudge, and spreading
  protein to lunch is an optional hunger tactic only.
reasoning: >
  Three randomised trials agree in direction on outcomes that matter (lean mass
  and fat loss) while dieting, in different samples, which puts the narrow claim
  at the RCT-level band. It stops there for four reasons. The trials are small
  (41-47) and one set of authors says so; one of the three barely separated its
  two arms; the protein level (about 1 g/kg) is far below a lifter's cut
  target, so the result transfers to a lifter only by inference; and the
  participants were overweight adults, not people holding muscle on a lean
  cut. The wider distribution question (009) keeps its own lower letter
  because the acute tracer work and one borderline hypertrophy trial point the
  other way, and a null in three small dieting trials does not erase that. Both
  halves are carried rather than averaged. The appetite finding is held lower
  and kept out of the muscle claim on purpose, so that a hunger tactic is
  never spoken as a protein rule.
---

# nutrition/protein-distribution-while-dieting-090

People on a cut are often told to spread their protein evenly across the day.
Three randomised trials put that to the test while participants were losing
weight, and none found the even split protected lean mass or sped fat loss
better than eating most of the protein at dinner. In one, adults at 750
kcal/day below need lifted three days a week for 16 weeks and lost the same
lean mass and fat on 30-30-30 g as on 10-20-60 g. In another, women ate all
their food from the study for eight weeks at a 20 percent deficit and then chose
their own for eight more, with the same result.

Two cautions travel with that. The trials fed about 1 g of protein per kilogram,
which is below a lifter's cut target, and the people were overweight, not lean
lifters trying to keep muscle. So the honest reading is not "the split does not
matter for lifters" but "the one situation where it could most plausibly matter,
a low protein total, did not show it, and nobody has tested a lifter on a cut".
The only young-adult hypertrophy trial that favoured an even split was
borderline, its whole edge sat outside the arms and legs, and it did not
restrict energy.

There is one small, practical positive. In a lab task, women who had eaten their
protein evenly valued energy-dense snack food less, and ate less of it, than
women on a dinner-heavy pattern. If a user is fighting evening snacking, moving
some protein to lunch is a reasonable thing to try, offered as a hunger tactic
and not as a muscle rule.

## Engine rules (diet card)

| Rule | When | Effect | Basis band |
|---|---|---|---|
| split-not-a-lever-in-a-cut | cut, total at or above floor, uneven split | no distribution nudge | RCT-level |
| even-split-hunger-option | cut, evening snacking, dinner-heavy protein | may offer once as a hunger tactic | observational |
| meal-count-is-free | asked how many protein meals | no count enforced | observational |
| say-what-was-tested | any distribution line to a lifter in a cut | name the population, claim neither way | practitioner |

## 한국어 요약 (답변용)

- 감량 중에도 하루 단백질 총량이 같다면, 세 끼에 고르게 나눠 먹은 쪽과 저녁에 몰아 먹은 쪽의
  제지방 손실·지방 감량에 차이가 없었다(과체중 성인 무작위 시험 3건, 41-47명). 감량 중이라고
  끼니별 균등 분배를 지적하지 않는다.
- 이 시험들은 체중 1 kg당 약 1 g(하루 90 g), 과체중 성인 대상이다. 하루 1.6-2.4 g/kg로 감량하는
  근력운동인을 직접 시험한 연구는 찾지 못했다. "근력운동인에게도 증명됐다"고도, "상관없다고
  증명됐다"고도 말하지 않는다.
- 아침 단백질을 아예 뺀 하루(아침 결식)는 어느 시험도 따로 시험하지 않았다. '저녁 몰아먹기' 쪽도
  아침에 10-15 g은 먹었다.
- 여성 44명 시험 하나에서, 단백질을 고르게 먹은 쪽이 고열량 간식을 덜 매력적으로 평가했고 실험에서도
  덜 먹었다. 저녁에 간식이 당기는 사람에게는 점심 단백질을 늘려 보는 방법을 "허기 관리 요령"으로 한 번만 권할 수 있다.
  근육을 위한 규칙이 아니다.
- 단백질 끼니를 3번 먹든 5번 먹든 훈련 경험자 8주 시험(18명 완료)에서 근육 증가가 같았다. 끼니 수를
  정해 주지 않는다.
- "아침에 단백질을 더 먹어야 근육이 붙는다"는 청년 26명 시험은 전체 제지방량 차이가 경계선(P=0.056)이고
  팔다리 제지방은 같았다. 사실처럼 말하지 않는다.
