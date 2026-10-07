---
# Deload-in-a-cut sprint 2026-10-07.
# 060 (the week: when, what a deload changes) and 061 (the day: RIR
# instrument, readiness signals) already answer the general questions. This
# row adds what they leave open for a TRAINED lifter IN AN ENERGY DEFICIT,
# and gives the weekly retro its reading rules: (1) whether a cut changes
# the deload clock, (2) how to tell a fatigue DROP from the slow strength
# DRIFT a long or fast cut can bring, (3) a one-lift load reset vs a
# whole-week deload, (4) what a lighter week cuts first (sets, not load),
# (5) how the daily wellness check is baselined once a cut starts, and (6)
# how a diet-break week and a deload week relate. Every trigger threshold
# not restated here stays on 060/061 and is linked by name.
#
# Numbering: claimed 079 provisionally (first free at cut time); released
# as 085 in v41 (079-084 were taken by v40).
#
# deload_rules is structured data for the weekly retro and the daily
# program. Each entry carries consumer (retro | daily | both), its own
# basis_grade, and kind (evidence | practice | product constant). The
# YAML-subset reader returns numbers as strings; cast them.
id: exercise/deload-autoregulation-in-a-cut-085
domain: exercise
grade: B (in an energy deficit strength gains hold on average while lean-mass gain is blunted -- meta-analysis of RCTs); C (cut sets before load in a lighter week -- maintenance and taper trials; fatigue and mood worsen in a deficit -- one pilot crossover; strength falls in a long, very lean contest prep -- case studies); D (deload timing in a cut, the drift-vs-drop split, a one-lift reset vs a whole-week deload, the wellness re-baseline and every threshold -- practice and product rules, no trial)
lane: "@gym-craft"
locale: universal
as_of: 2011-2026
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/34623696/"  # Murphy C, Koehler K 2022, Scand J Med Sci Sports 32(1):125-137 -- meta-analysis/meta-regression of RCTs, resistance training in an energy deficit for 3 weeks or more: lean-mass gain impaired vs no deficit (ES -0.57, p=0.02), strength gain comparable (ES -0.31, p=0.28); ~500 kcal/day deficit prevented lean-mass gain. Abstract read (also carried on 071)
  - "https://doi.org/10.1123/ijspp.8.5.582"  # Rossow LM, Fukuda DH, Fahs CA, Loenneke JP, Stout JR 2013, Int J Sports Physiol Perform 8(5):582-592, PMID 23412685 -- case study, one drug-free male bodybuilder, 6 months of prep then 6 months of recovery: body fat 14.8 -> 4.5%, testosterone 9.22 -> 2.27 ng/mL; strength decreased during preparation and did not fully recover within 6 months. Abstract read; the per-lift 1RM figures were seen only in a secondary summary and are NOT carried
  - "https://doi.org/10.1123/ijsnem.2014-0056"  # Helms ER, Zinn C, Rowlands DS, Naidoo R, Cronin JB 2015, Int J Sport Nutr Exerc Metab 25(2):163-170 -- double-blind crossover pilot, 14 resistance-trained men (13 completed), 2 weeks at 60% of habitual calories, high- vs moderate-protein: isometric mid-thigh pull differences trivial; daily DALDA and POMS fatigue / mood disturbance worse on the moderate-protein diet. Abstract read; magnitude-based inference, so direction only
  - "https://doi.org/10.1371/journal.pone.0247292"  # Peos JJ, Helms ER, Fournier PA, Krieger J, Sainsbury A 2021, PLoS One 16(2):e0247292, PMID 33630880 (ICECAP pre-specified secondary analysis, n=26 resistance-trained, 42% women) -- across a 1-week diet break with training continued: strength did not change, leg (not arm) muscle endurance improved, hunger and irritability fell, body weight +0.6 kg, fat-free mass +0.7 kg. Abstract read (trial itself carried on nutrition 026)
  - "https://doi.org/10.1123/ijspp.2018-0489"  # Pritchard HJ, Barnes MJ, Stewart RJ, Keogh JW, McGuigan MR 2019, Int J Sports Physiol Perform 14(4):458-463 -- crossover, 11 strength-trained men, two 4-week blocks each followed by a taper week with ~70% less volume and intensity either +5.9% or -8.5%: the higher-intensity taper gave small improvements in isometric mid-thigh pull and jump measures, the lower-intensity taper only jump height; between-taper difference not significant. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/26670988/"  # Pritchard HJ, Tod DA, Barnes MJ, Keogh JW, McGuigan MR 2016, J Strength Cond Res 30(7):1796-1804 -- interviews, 11 elite raw powerlifters: taper volume cut 58.9 +/- 8.4% with intensity maintained or slightly reduced; accessory work dropped ~2 weeks out. Abstract read
  - "https://shura.shu.ac.uk/33446/"  # Rogerson D et al. 2024, Sports Med Open 10:26 (full text re-read this sprint): deload interval by sport, physique athletes (n=45) 5.8 weeks, powerlifters (n=156) 5.5, all 5.6; NO split by diet phase was asked; 83.7% lower the load on multi-joint lifts and 84.9% lower effort; the introduction notes physique athletes tend to keep training through contest week and manipulate diet instead of tapering
  - "https://pubmed.ncbi.nlm.nih.gov/21131862/"  # Bickel CS, Cross JM, Bamman MM 2011, Med Sci Sports Exerc 43(7):1177-1187 -- young adults kept 16 weeks of gains for 32 weeks at a third or a ninth of the volume when the load was kept (carried on 071)
  - "https://pubmed.ncbi.nlm.nih.gov/33629972/"  # Spiering BA et al. 2021, J Strength Cond Res 35(5):1449-1458 -- narrative review: intensity is the variable that keeps strength and size when volume falls (carried on 071)
  - "exercise/deload-planned-vs-reactive-060"  # within-warehouse: the deload clock, recipe and triggers this row reads, never restates
  - "exercise/rir-accuracy-readiness-signals-061"  # within-warehouse: the anchor-set read, the 2-rep resolution, the wellness and sleep signals
  - "exercise/maintenance-vs-growth-volume-cut-071"  # within-warehouse: the cut aims to keep, sets before load
  - "exercise/deficit-volume-guidance-016"  # within-warehouse: high volume to protect muscle in a deficit was refuted
  - "exercise/rir-set-log-accuracy-077"  # within-warehouse: how far a logged RIR can be trusted set by set
  - "exercise/caution-severity-ladder-056"  # within-warehouse: pain goes to the ladder, not to a deload
  - "exercise/progression-rules-trained-cut-082"  # within-warehouse (linked v41): stall-reset is the same ~10% per-lift reset one-lift-reset-vs-whole-week uses; stall-cut-check (a hold in a cut is expected, check deficit and rate of loss) sits beside slow-drift-is-not-a-trigger -- how a 082 stall and a 060 drop combine in a cut is filed OPEN in GAPS
  - "exercise/stress-training-load-rules-084"  # within-warehouse (linked v41): the stressed-week lighter plan (load kept, sets x0.67, RIR floor 3, 7-day expiry) -- a third lighter-session path beside the 060 deload and the 061 day trim; how it combines with a cut's deload is not specified
  - "source:nutrition/weight-loss-rate-lean-mass-012"  # cross-domain: the rate of loss (Garthe 2011, 0.7 vs 1.4% per week) the drift rule checks first
  - "source:nutrition/diet-breaks-refeeds-026"  # cross-domain: what a diet break is and is not
  - "source:sleep-recovery/short-sleep-appetite-weight-015"  # cross-domain: short sleep during a deficit shifts loss toward lean mass
  - "source:sleep-recovery/regularity-appetite-brief-rules-016"  # cross-domain: the cut-phase-sleep brief rule the retro links to instead of restating
  - "framework:GRADE -- the deficit-vs-strength finding is a meta-analysis of RCTs (mostly not lean, not advanced lifters), held at B. Sets-before-load rests on one maintenance RCT, one maintenance review, one 11-man taper crossover and an elite taper interview study, which agree in direction (C). Fatigue rising in a deficit rests on one 13-man pilot scored with magnitude-based inference (C, direction only). Strength loss late in a very lean prep is case-study evidence (C for 'happens', nothing for how often). No trial tests deload timing, recipe or triggers inside a deficit, and the survey of practice did not split by diet phase; every rule built on those is D with product-constant thresholds."
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
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
deload_rules:
  - rule: cut-keeps-the-clock
    consumer: retro
    condition: primary_goal is fat loss and a planned deload is being scheduled
    engine: keep 060 planned_interval_weeks (default 6, range 4-8); a cut alone does not shorten it; move to 4 only if the user asks or a reactive deload already fired in this cut (product constant)
    kind: practice
    basis: Rogerson 2024 (physique 5.8 vs powerlifting 5.5 weeks, no diet-phase split); no trial
    basis_grade: D
  - rule: drop-is-still-a-drop
    consumer: retro
    condition: a cut is running and the anchor lift meets 060 performance-drop (2 or more reps or RIR off target at the same load, two consecutive exposures)
    engine: fire the 060 deload as in any phase; do not explain the drop away as the diet, because on average strength holds in a deficit
    kind: evidence
    basis: Murphy 2022
    basis_grade: B
  - rule: slow-drift-is-not-a-trigger
    consumer: retro
    condition: a cut is running and the anchor lift loses reps or RIR at a matched load slowly -- at most 1 per exposure, never a 2-rep step -- across 3 or more exposures, with no 060 trigger hit (product constants)
    engine: no deload; switch that lift's weekly target from progress to hold the load (071 sets before load); the retro shows the cut checks in order -- rate of loss above 1% of body weight a week (012), short-sleep nights (sleep-recovery 016 cut-phase-sleep), protein days -- and says a slow drift can happen late in a long or fast cut; if the drift turns into a 060 drop, 060 decides
    kind: product constant
    basis: Rossow 2013 (case); Garthe 2011 via 012; Murphy 2022
    basis_grade: D
  - rule: one-lift-reset-vs-whole-week
    consumer: both
    condition: a 060 performance-drop on ONE anchor lift while the other anchor lifts hold and wellness is not low
    engine: reset that lift only -- one load-reset step down (the logger's per-lift reset, about 10%, is a product constant) and rebuild; a whole-week deload needs the drop on 2 or more anchor lifts in the same week, or 060 performance-drop-plus-wellness (product constants)
    kind: product constant
    basis: none located; linear-progression practice
    basis_grade: D
  - rule: sets-before-load
    consumer: both
    condition: any lighter week or lighter day, especially in a cut
    engine: cut sets first (060 weekly_sets_multiplier 0.5) and keep the working load; trim load only where the 060 RIR floor cannot otherwise be met; never cut load while keeping sets
    kind: evidence
    basis: Bickel 2011; Spiering 2021; Pritchard 2019; Pritchard 2016
    basis_grade: C
  - rule: wellness-rebaseline-in-a-cut
    consumer: daily
    condition: a cut starts (primary_goal changes to fat loss, or a deficit is set)
    engine: score the 061 self-reported-wellness check against the user's own average from the cut's first 14 days, not the pre-cut average, so a deficit-wide dip does not read as "low" every day; 061 actions unchanged (window is a product constant)
    kind: product constant
    basis: Helms 2015 (fatigue and mood worse in a deficit)
    basis_grade: D
  - rule: diet-break-is-not-a-deload
    consumer: retro
    condition: a diet break (maintenance-calorie week, nutrition 026) is scheduled
    engine: train normally through the break and do not count it as a deload; do not stack the deload onto the break by default; if a deload falls due within the break week, offer the user the choice to place it in the week after
    kind: practice
    basis: Peos 2021 (strength held, leg endurance up across a break with training continued)
    basis_grade: D
  - rule: user-asked-deload
    consumer: both
    condition: the user asks for a lighter week ("이번 주 좀 빼자")
    engine: grant it per 060 deload_prescription and restart the clock; this differs from a passive low wellness score, which only trims the day (061)
    kind: practice
    basis: Coleman 2024 via 060 (a lighter week costs little)
    basis_grade: C
  - rule: no-failure-chase-in-a-cut
    consumer: daily
    condition: a cut is running
    engine: keep 061 target RIR bands; do not push sets closer to failure or add sets to "protect muscle" (016 refuted the high-volume version); load is what keeps muscle (071)
    kind: evidence
    basis: 016; 071; Spiering 2021
    basis_grade: C
refraction_notes:
  - note: >
      A CUT IS NOT A REASON TO EXPECT WEAKNESS. Pooled trials of training in
      an energy deficit found strength gains about as large as without one,
      while muscle gain was blunted. So a lifter in a moderate cut who drops
      reps on the same lift two sessions running is showing the same fatigue
      signal as anyone else, and the deload rule applies as usual. The trials
      were mostly not very lean, advanced lifters.
    grade: B
  - note: >
      VERY LEAN AND LONG IS DIFFERENT. In a natural bodybuilder dieting to
      stage leanness, strength fell over the prep and was still not back six
      months later. A slow loss across weeks in a long or fast cut is
      therefore expected and is handled by holding the load and checking the
      rate of loss, sleep and protein, not by repeated deloads. That this
      happens is documented; how often, and at what leanness, is not.
    grade: C
  - note: >
      CUT SETS, KEEP THE WEIGHT. Young adults held their gains for 32 weeks
      at a third of the sets when the load stayed; a taper week with 70% less
      volume tended to do better with the load nudged up than down; elite
      powerlifters taper by cutting about 59% of volume and keeping intensity.
      A lighter week in a cut takes sets away first. Most surveyed lifters do
      also trim the load a little; the engine keeps it unless the effort
      floor demands otherwise.
    grade: C
  - note: >
      DIETING FEELS WORSE, SO MEASURE AGAINST THE DIET. In a two-week 40%
      deficit, resistance-trained men reported more fatigue and mood
      disturbance (less so on higher protein) while strength held. A daily
      check scored against the pre-diet baseline would read "tired" most
      days of a cut and trim every session; the engine re-baselines within
      the cut. The 14-day window is a product rule.
    grade: C
  - note: >
      NO ONE HAS TESTED DELOAD TIMING IN A CUT. Physique athletes, who diet
      every season, reported deloading about as often as powerlifters (every
      5.8 vs 5.5 weeks), and the survey did not ask about diet phase. A
      shorter cut-phase clock is an option the user can choose, not a rule
      the evidence sets.
    grade: D
  - note: >
      A DIET BREAK IS FOOD, NOT REST. In the one trained-adult trial, people
      kept training through a maintenance-calorie week; strength held and leg
      endurance improved. The break is a chance to train well, not a deload,
      and stacking both is a user choice.
    grade: D
claim: >
  For a trained lifter in a cut, the deload rules of 060 and the daily
  rules of 061 stand, with five additions. A deficit does not, on average,
  stop strength from rising (meta-analysis of RCTs), so a repeated drop on
  the same lift is a fatigue signal in a cut as in any phase and is not
  explained away by the diet. Late in a long or fast cut toward stage
  leanness strength can fall slowly (case studies); that slow drift is met
  by holding the load and checking the rate of loss, sleep and protein,
  not by deloading again and again. When a lighter week or day is needed,
  sets go before load, because kept load is what preserves strength and
  size when volume falls (maintenance and taper trials). Dieting raises
  reported fatigue and mood disturbance, so the daily wellness check is
  scored against the cut's own baseline. A diet-break week is maintenance
  eating with normal training, not a deload. Deload timing, recipe and
  triggers have never been tested inside a deficit; the cut does not
  shorten the deload clock by itself, and every threshold here is a
  product constant.
reasoning: >
  Murphy and Koehler 2022 is the anchor: strength held while lean-mass gain
  was blunted, so the 060 performance trigger keeps its meaning in a cut.
  The opposite tail -- strength loss when very lean -- comes from Rossow
  2013, a single case read at abstract level; it justifies a separate,
  slower "drift" path but not a number, so the drift thresholds are product
  constants and the first check is the rate of loss carried on 012 (Garthe
  2011's faster arm). Sets-before-load joins Bickel 2011 and Spiering 2021
  (already on 071) with Pritchard 2019 (taper with load kept tended to do
  better) and Pritchard 2016 (elite practice), all in the same direction.
  Helms 2015 is a small pilot with magnitude-based inference; it supports
  only the direction (fatigue and mood worsen in a deficit), which is all
  the wellness re-baseline needs. Peos 2021 shows a diet-break week with
  training kept is not a performance setback, which is why the break is
  not counted as a deload. Rogerson 2024 was re-read at full text for a
  diet-phase split and has none; its sport-level intervals are the only
  data on how often dieting athletes deload. The one-lift reset is a
  logger practice with no located trial and is marked so. primary_goal
  selects the cut rules; training_status and sleep_baseline_hours only
  shape wording, as on 060 and 061.
---

# exercise/deload-autoregulation-in-a-cut-085 -- 감량 중 디로드와 컨디션 조절

**한 줄 그림:** 감량 중이라고 힘이 빠지는 게 당연한 건 아니다. 같은 운동에서 기록이 두 번 연달아
떨어지면 평소처럼 디로드하고, 긴 감량 끝에 천천히 빠지는 힘은 디로드 대신 무게 유지로 받는다.
가볍게 갈 때는 세트를 먼저 줄이고 무게는 지킨다.

## Deload rules for the weekly retro and the daily program (engine-readable)

| Rule | Reads | Engine | Kind |
|---|---|---|---|
| cut-keeps-the-clock | retro | 060 clock unchanged in a cut; 4 weeks only by user choice or after a reactive deload in this cut | practice |
| drop-is-still-a-drop | retro | 060 performance-drop fires as usual; not blamed on the diet | evidence |
| slow-drift-is-not-a-trigger | retro | at most 1 rep/RIR lost per exposure over 3+ exposures -> hold the load, show rate / sleep / protein checks | product constant |
| one-lift-reset-vs-whole-week | both | drop on one lift -> reset that lift; drop on 2+ lifts or drop plus low wellness -> whole-week deload | product constant |
| sets-before-load | both | cut sets (x 0.5), keep load; trim load only for the RIR floor | evidence |
| wellness-rebaseline-in-a-cut | daily | wellness scored against the cut's first 14 days | product constant |
| diet-break-is-not-a-deload | retro | train normally through a break; deload not stacked by default | practice |
| user-asked-deload | both | grant it, restart the clock | practice |
| no-failure-chase-in-a-cut | daily | keep 061 RIR bands; no extra sets or failure to "protect muscle" | evidence |

Thresholds (1 per exposure, 3 exposures, 2 lifts, 14 days, about 10% reset,
1% a week) are the plan's rules, not measured cut-offs.

## 한국어 요약 (답변용)

- 칼로리를 줄이는 중에도 힘은 평균적으로 계속 늘었다(근육 증가는 둔해짐). 그래서 같은 운동에서 목표
  반복을 두 번 연달아 못 채우면 "다이어트 중이라 그래"로 넘기지 않고 평소처럼 디로드한다(060).
- 대회 수준까지 아주 마르게 오래 감량하면 힘이 서서히 빠질 수 있다(선수 사례 연구). 한 번에 크게가
  아니라 매번 1개 이하로 조금씩, 세 번 이상 빠지는 경우다. 이때는 디로드를 반복하지 않고 그 운동의
  목표를 "무게 유지"로 바꾼 뒤, 체중이 주 1% 넘게 빠지고 있지 않은지, 잠이 짧지 않은지, 단백질을
  챙겼는지를 먼저 본다.
- 한 운동만 떨어지고 나머지는 괜찮으면 그 운동만 무게를 한 단계(약 10%) 내려 다시 쌓는다. 주 전체
  디로드는 두 운동 이상이 같은 주에 떨어지거나, 기록 하락과 피로감이 겹칠 때다. 이 기준은 제품 규칙이다.
- 가볍게 갈 때는 세트를 먼저 줄이고 무게는 지킨다. 젊은 성인은 세트를 3분의 1로 줄여도 무게를
  지키면 근육이 유지됐고, 볼륨을 70% 줄인 주에도 무게를 살짝 올린 쪽이 내린 쪽보다 결과가 좋은
  경향이었다.
- 감량 중에는 피로감과 기분 저하가 늘어난다(단백질을 많이 먹은 쪽이 덜했다). 그래서 매일 컨디션
  점수는 감량 전이 아니라 감량 시작 후 2주 평균과 비교한다. 안 그러면 감량 내내 매일 "피곤함"으로
  읽혀 운동이 계속 깎인다.
- 감량 중이라고 디로드를 더 자주 해야 한다는 연구는 없다. 매 시즌 다이어트하는 보디빌더도 파워리프터와
  비슷하게 5~6주마다 디로드했다. 더 짧게(4주) 가는 건 사용자가 고를 수 있는 선택이다.
- 다이어트 브레이크(유지 칼로리로 먹는 한 주)는 디로드가 아니다. 그 주에도 평소처럼 운동했을 때
  힘은 유지되고 하체 근지구력은 오히려 좋아졌다. 디로드를 같은 주에 겹칠지는 사용자에게 묻는다.
- 사용자가 "이번 주 좀 빼자"고 하면 그대로 디로드한다. 손해가 거의 없기 때문이다. 다만 컨디션 점수가
  낮다는 것만으로는 그날 운동만 조금 줄인다(061).
- 근육을 지키겠다고 감량 중에 세트를 늘리거나 실패까지 더 밀어붙이지 않는다. 근육을 지키는 건
  무게다.
