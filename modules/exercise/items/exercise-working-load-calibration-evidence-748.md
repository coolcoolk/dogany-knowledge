---
# Warm-up ladder sprint 2026-10-08.
# Question: what does the ladder builder need to know before it can turn a
# working weight into ramp rungs, and what can it do when there is no
# working weight yet (first session, no log)? 018 holds the jump size, 080
# the ramp evidence (last rung near the working load, ramp optional at
# ~10RM). This row holds the inputs: how far a load-by-reps estimate can be
# trusted, how big a calibration step is (upper vs lower body), how a
# barbell number converts to dumbbells, and which way novices miss when they
# pick their own load. 741 turns it into ladder_rules.
#
# Sources read 2026-10-08: Reynolds 2006 at the author's PDF (full text);
# Nuzzo 2024 at PMC full text; Saeterbakken 2011 / 2013 and Glass & Stanton
# 2004 at the Europe PMC abstract; NSCA protocol at the HPRC page (already
# cited by 080).
id: exercise/working-load-calibration-evidence-748
domain: exercise
grade: C (reps at a given %1RM vary widely between people and are higher on the leg press than the bench; 1RM estimates from a rep max are tight at 5RM and loosen past 10 reps); C (dumbbell press loads sit 7-17% under the barbell in small trained-male samples); C (novices self-select loads well under 60% 1RM); D (the calibration step sizes are the NSCA test protocol, not a tested dose)
lane: "@performance-lit"
locale: universal
as_of: 2004-2024
contested: no
sources:
  - "https://doi.org/10.1007/s40279-023-01937-7"  # Nuzzo JL, Pinto MD, Nosaka K, Steele J. 2024, Sports Med 54(2):303-321, PMID 37792272 -- meta-regression, 952 reps-to-failure tests, 7289 people, 269 studies; main model ~5 reps at 90% and ~15 at 70% 1RM; bench ~4 / ~9 / ~14 at 90 / 80 / 70%; leg press ~9 / ~13 / ~19; between-person SD 2.51 reps at 80% and 4.36 at 60%; sex, age and training status did not clearly moderate; data mostly healthy adults 20-40 y
  - "https://doi.org/10.1519/R-15304.1"  # Reynolds JM, Gordon TJ, Robergs RA. 2006, J Strength Cond Res 20(3):584-592, PMID 16937972 -- n=70 (34 M, 36 F, 18-69 y, mixed experience); 1/5/10/20RM on barbell bench and plate-loaded leg press; 5RM = 87.5% / 85.9%, 10RM = 75.7% / 70.1%, 20RM = 61.6% / 51.6% of 1RM (bench / leg press); 5RM gave the best prediction (R2 0.993 bench, 0.974 leg press); "no more than 10 repetitions should be used in linear equations"; leg-press SEE 16 kg vs bench 3 kg; adding sex, age, anthropometry did not help
  - "https://doi.org/10.1080/02640414.2010.543916"  # Saeterbakken AH, van den Tillaar R, Fimland MS. 2011, J Sports Sci 29(5):533-538, PMID 21225489 -- n=12 trained men; dumbbell chest-press 1RM 17% below barbell and 14% below Smith; barbell ~3% above Smith; pectoralis and anterior deltoid EMG did not differ
  - "https://doi.org/10.1519/JSC.0b013e318276b873"  # Saeterbakken AH, Fimland MS. 2013, J Strength Cond Res 27(7):1824-1831, PMID 23096062 -- n=15 men; standing dumbbell shoulder-press 1RM ~7% below standing barbell and ~10% below seated dumbbell
  - "https://doi.org/10.1519/R-12482.1"  # Glass SC, Stanton DR. 2004, J Strength Cond Res 18(2):324-327, PMID 15142014 -- 13 M / 17 F novices; self-selected loads on five lifts all below 60% 1RM (range 42-57%); same for men and women
  - "https://www.hprc-online.org/articles/one-rep-max-for-strength"  # HPRC (US DoD) restating the NSCA RM protocol: 5-10 reps light, 1 min; 3-5 reps adding 5-10% upper / 10-20% lower, 2 min; 2-3 reps near max, 2-4 min; on a miss remove 2.5-5% upper / 5-10% lower; same protocol for a 10RM; multi-rep tests on power lifts unreliable above 5RM
  - "exercise/warmup-load-rampup-progression-018"  # jump size between rungs; referenced, not restated
  - "exercise/warmup-ramp-sets-heavy-compounds-080"  # ramp evidence and constants the ladder rules build on
  - "exercise/rir-set-log-accuracy-077"  # RIR under-called by ~1 rep, worst in the first set and in long sets; e1RM only from sets of 12 or fewer at RIR 0-3
  - "exercise/autoregulation-vs-percentage-prescription-030"  # the day's load is read from the first work set
  - "exercise/machine-free-weight-equivalence-075"  # machine and free-weight strength are test-specific; no conversion ratio
  - "exercise/increment-verification-floor-029"  # 1RM retest noise 8-12%; a converted load is inside that noise
  - "framework:GRADE -- the reps-to-%1RM spread and the leg press vs bench gap rest on a 269-study meta-regression (non-systematic search, healthy adults) and one 70-person prediction study (C). The dumbbell ratios are two small crossovers in trained men, two lifts (C, narrow). Novice under-selection is one 30-person study (C). The calibration step sizes come from a testing protocol, not from a trial of calibration methods (D)."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
constants:
  reps_at_pct_main:  # Nuzzo 2024 main model, approximate means
    pct_90: 5
    pct_70: 15
  reps_at_pct_bench:  # Nuzzo 2024 bench model
    pct_90: 4
    pct_80: 9
    pct_70: 14
  reps_at_pct_leg_press:  # Nuzzo 2024 leg-press model
    pct_90: 9
    pct_80: 13
    pct_70: 19
  reps_sd_between_people:  # Nuzzo 2024
    pct_80: 2.5
    pct_60: 4.4
  rm_frac_bench:  # Reynolds 2006
    rm5: 0.875
    rm10: 0.757
    rm20: 0.616
  rm_frac_leg_press:  # Reynolds 2006
    rm5: 0.859
    rm10: 0.701
    rm20: 0.516
  estimate_reps_max: 10                     # Reynolds 2006: no more than 10 reps in a linear estimate
  calib_step_up_upper: [0.05, 0.10]         # NSCA protocol
  calib_step_up_lower: [0.10, 0.20]         # NSCA protocol
  calib_step_down_upper: [0.025, 0.05]      # NSCA protocol
  calib_step_down_lower: [0.05, 0.10]       # NSCA protocol
  db_to_bb_flat_press: 0.83                 # Saeterbakken 2011: dumbbell pair total vs barbell, chest press
  db_to_bb_standing_ohp: 0.93               # Saeterbakken 2013: standing dumbbell vs standing barbell shoulder press
  novice_self_select_pct_1rm: [0.42, 0.57]  # Glass & Stanton 2004
refraction_notes:
  - note: >
      A PERCENT IS A GUESS ABOUT REPS. At 80% 1RM the average lifter gets
      about 9 bench reps, but one standard deviation either side is about 2.5
      reps, and at 60% it is over 4. On the leg press the same percentage
      gives about 4-5 more reps than on the bench. So a working weight worked
      out from a percentage is a first guess the first work set corrects;
      lower-body machine lifts drift highest.
    grade: C
  - note: >
      ESTIMATE FROM SHORT SETS. Reynolds 2006: a 5RM predicted 1RM almost
      exactly on the bench and well on the leg press; 10RM was worse and
      20RM worse again; the authors cap linear estimates at 10 reps. Taken
      with 077 (RIR under-called by about one rep, worse in long sets), a
      reported "X kg for N reps" is usable for a working-weight estimate when
      N is 10 or fewer and the set was close to failure.
    grade: C
  - note: >
      DUMBBELLS ARE LIGHTER THAN THE BAR, BY LIFT. In trained men the
      dumbbell chest-press pair total was 17% under the barbell and the
      standing dumbbell shoulder press 7% under the standing barbell. Two
      lifts, 12 and 15 men; nothing for rows, lunges, women or novices. A
      converted dumbbell load is a starting guess, not a match.
    grade: C
  - note: >
      NOVICES START TOO LIGHT. Thirty novices picked 42-57% of their 1RM on
      five lifts, men and women alike. A first-session ladder for a new
      lifter should expect the working weight to go up during calibration,
      not down.
    grade: C
  - note: >
      CALIBRATION STEPS ARE TEST PROTOCOL. The NSCA rep-max protocol raises
      the load 5-10% between sets for upper-body lifts and 10-20% for lower,
      and on a miss takes off 2.5-5% / 5-10%. That is how a test is run, not a
      trial showing these steps find a working weight best.
    grade: D
claim: >
  A working weight is an estimate before it is lifted. Reps at a given
  percentage of 1RM vary a lot between people (about 2.5 reps either side at
  80%, over 4 at 60%) and run higher on the leg press than the bench (about
  13 vs 9 at 80%), with no clear sex, age or training-status effect. A rep max
  of 5 predicts 1RM closely (5RM about 86-88% of 1RM), a 10RM less well, and
  linear estimates should not use sets over 10 reps. Dumbbell press loads sit
  below the barbell: the dumbbell chest-press pair 17% lower, the standing
  dumbbell shoulder press 7% lower, in small trained-male samples. Novices
  left to choose pick 42-57% of their 1RM. The only published way to step
  toward an unknown load is the NSCA rep-max protocol: raise 5-10% per set on
  upper-body lifts and 10-20% on lower-body lifts, take off 2.5-5% / 5-10%
  after a miss, rest 2-4 minutes near the top. No trial compares methods of
  finding a first working weight.
reasoning: >
  Nuzzo 2024 is the largest pooled reps-to-failure data set (269 studies) and
  replaces the textbook table with means plus between-person spread; its
  search was non-systematic and its data mostly healthy 20-40 year olds, so it
  is strong for "the spread is wide" and for the leg press vs bench gap,
  moderate for any exact number. Reynolds 2006 measured 1/5/10/20RM directly
  in 70 mixed men and women (18-69 y) and cross-validated in 20 more; it is
  the source for the 10-rep cap on estimates and for the RM-to-1RM fractions
  on one upper and one lower lift. The two Saeterbakken crossovers are the
  only primary 1RM comparisons of dumbbell and barbell versions located; both
  are small, trained men, pressing only. Glass & Stanton 2004 is one study of
  novices on five lifts. The NSCA protocol, read through the HPRC restatement,
  gives the upper / lower step sizes; it is the same protocol 080 cites for
  rung shape, used here for the other job it describes (finding a rep max).
  Not contested: no source located argues the opposite on any of these
  points; the numbers are narrow in sample, not disputed.
---

# exercise/working-load-calibration-evidence-748 -- 작업 무게를 모를 때: 첫 세션 보정, 상체·하체, 바벨·덤벨

**One line:** a working weight is a guess until the first work set is
lifted; estimate it from a short set (10 reps or fewer), step toward it in
bigger jumps on the legs than on the upper body, start dumbbells lighter than
the bar number, and expect a new lifter's first pick to be too light.

What the studies show:

| Question | Finding | Source |
|---|---|---|
| reps at 80% 1RM | bench ~9, leg press ~13; SD ~2.5 reps between people | Nuzzo 2024 |
| reps at 60% 1RM | SD ~4.4 reps between people | Nuzzo 2024 |
| 5RM as % of 1RM | bench 87.5%, leg press 85.9% | Reynolds 2006 |
| 10RM as % of 1RM | bench 75.7%, leg press 70.1% | Reynolds 2006 |
| longest set to estimate from | 10 reps | Reynolds 2006 |
| dumbbell vs barbell, chest press | dumbbell pair 17% lower | Saeterbakken 2011 |
| dumbbell vs barbell, standing shoulder press | dumbbells 7% lower | Saeterbakken 2013 |
| novice self-chosen load | 42-57% of 1RM | Glass & Stanton 2004 |
| step up between test sets | upper 5-10%, lower 10-20% | NSCA (HPRC) |
| step down after a miss | upper 2.5-5%, lower 5-10% | NSCA (HPRC) |

What is not known: no trial compares ways of finding a first working weight;
no dumbbell-to-barbell ratio exists for rows, lunges, split squats or
Romanian deadlifts; no machine-to-free-weight ratio exists at all (075:
strength is test-specific, and stacks differ by maker).

## 한국어 요약 (답변용)

- 작업 무게는 들어 보기 전까지 추정치다. 같은 1RM의 80%라도 사람마다 반복 수가 위아래로 2~3회씩
  다르고, 60%에서는 4회 넘게 차이 난다. 레그프레스는 같은 퍼센트에서 벤치프레스보다 4~5회 더 나온다.
  퍼센트로 정한 무게는 첫 본세트에서 고친다.
- "몇 kg로 몇 회 했다"는 기록으로 무게를 잡을 때는 10회 이하로, 실패 가까이 한 세트만 쓴다. 5회
  최대 무게는 1RM의 86~88%로 거의 정확했고, 반복이 길수록 추정이 흔들렸다.
- 처음 무게를 찾을 때 한 번에 올리는 폭은 상체 5~10%, 하체 10~20%다. 실패하면 상체 2.5~5%, 하체
  5~10% 내린다. 근력 측정 절차에서 쓰는 숫자이고, 이 폭이 가장 좋다는 연구는 없다.
- 덤벨은 바벨보다 가볍게 시작한다. 벤치프레스는 덤벨 두 개 합이 바벨보다 17%, 서서 하는 숄더프레스는
  7% 낮았다. 훈련한 남성 12~15명의 결과이고 로우·런지 같은 다른 운동은 자료가 없다.
- 머신과 프리웨이트 사이에는 환산 비율이 없다. 머신마다 무게 스택이 달라서 머신은 그 자리에서 새로
  찾는다.
- 처음 운동하는 사람이 스스로 고른 무게는 1RM의 42~57%였다. 첫 세션에서는 무게가 내려가기보다 올라갈
  것으로 보고 단계를 짠다.
