---
# Warm-up ramp-set sprint 2026-10-07.
# Question: for a trained lifter, how many ramp sets before a heavy compound,
# how many reps per ramp set, how close to the working load the last one
# should get, what a general warm-up adds, and what the ramp costs in time.
# 018 already covers the JUMP SIZE between rungs (D, coaching schemes) and 022
# the general warm-up and stretching modality (B/C); this row covers the
# controlled-trial evidence on the specific (same-lift) ramp itself and turns
# it into ramp_rules for the session table. Companion to the dawn rows
# exercise/early-morning-performance-warmup-068 and
# exercise/early-morning-session-brief-rules-073 (released in v37). Rubric: the exercise rubric @performance-lit.
#
# HONEST SCOPE NOTE. Every trial below is young trained adults, mostly men,
# one lift or two, one session. The heavy-load trials are 1RM tests (Abad,
# Barroso) or 3 x 6 at 80% 1RM (Ribeiro 2020); the null trials are ~10RM
# multi-set work (Enes 2025) or 80% 1RM sets to failure (Ribeiro 2014). No
# trial tested a 3-5 rep working set at 85-90% 1RM after different ramps, and
# no trial measured injury. The ramp shape for heavy work therefore leans on
# the NSCA 1RM protocol (practice) plus the direction of the trials.
#
# ramp_rules is structured data for the set table / ramp builder
# (ax_engine _f6_ramp_sets, ramp_taper_reps). Inputs the
# engine already has: working weight, working rep target, the lift's ramp
# class, slot order in the session, the session start time. Every number in
# constants is labelled with where it comes from; product constants are
# marked as such.
id: exercise/warmup-ramp-sets-heavy-compounds-080
domain: exercise
grade: C (before heavy or maximal work, a specific ramp whose last set sits near the working load beats a light-only ramp, and a long low-intensity general warm-up adds to it); C (before ~10RM multi-set work a specific ramp does not change reps or volume versus none); D (number of rungs, reps per rung and the time budget are protocol and practice, not tested doses)
lane: "@performance-lit"
locale: universal
as_of: 2011-2025
contested: yes
sources:
  - "https://doi.org/10.3390/ijerph17186882"  # Ribeiro B, Pereira A, Neves PP, Sousa AC, Ferraz R, Marques MC, Marinho DA, Neiva HP. 2020, Int J Environ Res Public Health 17(18):6882, PMID 32971729 -- n=40 trained men, 3 x 6 at 80% 1RM after 6 x 40% / 6 x 80% / 6 x 40% + 6 x 80% of the training load; squat MPV higher after the 80% warm-up than the 40% (ES 0.51-0.80); bench time-to-peak-velocity and work better after the two-step ramp than 40% only; "few repetitions and low loads is not enough"; no no-warm-up arm
  - "https://doi.org/10.1016/j.smhs.2025.08.002"  # Enes A, Mohan AE, Pinero A, Hermann T, Sapuppo M, Coleman M, Androulakis Korakakis P, Wolf M, Souza-Junior TP, Swinton PA, Schoenfeld BJ. 2025, Sports Med Health Sci -- read at the SportRxiv preprint 559 (v. 05/2025); randomized crossover, n=29 (22 M, 7 F, 4.5 +/- 3.9 y training); 0 / 1 (3-4 reps at 75% 10RM) / 2 (55% and 75% 10RM) specific sets, 120 s rests, then 4 x 10RM to failure on Smith bench and 45-degree leg press; negligible-to-small differences, strong evidence against more sets > fewer > none; authors: skipping saves ~2-5 min per exercise at ~10RM loads; not tested at 1-3RM, no injury outcome
  - "https://doi.org/10.1519/JSC.0b013e3181e8611b"  # Abad CC, Prado ML, Ugrinowitsch C, Tricoli V, Barroso R. 2011, J Strength Cond Res 25(8):2242-2245, PMID 21544000 -- n=13 trained; specific warm-up 8 reps ~50% + 3 reps ~70% est. 1RM; adding 20 min cycling at 60% HRmax raised leg-press 1RM by 8.4% (p=0.002)
  - "https://doi.org/10.1519/JSC.0b013e3182606cd9"  # Barroso R, Silva-Batista C, Tricoli V, Roschel H, Ugrinowitsch C. 2013, J Strength Cond Res 27(4):1009-1013, PMID 22692116 -- n=16 strength-trained men, general warm-up after the specific one: 15 min at 40% VO2max +3% leg-press 1RM; 5 min at 40% or 70% no different from none; 15 min at 70% -4%
  - "https://doi.org/10.2466/25.29.PMS.119c17z7"  # Ribeiro AS, Romanzini M, Schoenfeld BJ, Souza MF, Avelar A, Cyrino ES. 2014, Percept Mot Skills 119(1):133-145, PMID 25153744 -- n=15 men, 4 sets to failure at 80% 1RM (bench, squat, curl) after control / specific / aerobic / combined warm-up: no difference in total reps or fatigue index
  - "https://doi.org/10.1136/bjsports-2014-094228"  # McCrary JM, Ackermann BJ, Halaki M. 2015, Br J Sports Med 49(14):935-942, PMID 25694615 -- 31 RCTs (21 good PEDro); strong evidence that high-load dynamic warm-ups enhance upper-body strength and power; no study of warm-up and injury found
  - "https://www.hprc-online.org/articles/one-rep-max-for-strength"  # HPRC (US DoD) 2022, restating the NSCA 1RM protocol: 5-10 reps light, 1 min rest; 3-5 reps adding 5-10% (upper) / 10-20% (lower), 2 min rest; 2-3 reps near max, 2-4 min rest; then single attempts. Same steps in Coleman & Szymanski, Strength Training for Baseball (Human Kinetics excerpt)
  - "exercise/warmup-load-rampup-progression-018"  # jump size between rungs (20% default cap, tighter final approach) -- referenced, not restated
  - "exercise/dynamic-warmup-same-day-performance-022"  # the general warm-up direction and the stretching-modality null
  - "exercise/early-morning-performance-warmup-068"  # dawn power gap and the 20 min general warm-up offset (Taylor 2011)
  - "exercise/early-morning-session-brief-rules-073"  # dawn-extend-warmup and dawn-first-sets-feel-heavy rules this row sits behind
  - "exercise/autoregulation-vs-percentage-prescription-030"  # the load is read from the first work set, not from the ramp
  - "exercise/shoulder-prep-specific-vs-general-065"  # within-warehouse (v37): the pressing-day specific-ramp rule (McCrary 2015, Ribeiro 2021 Motricidade review read there); this row is the general heavy-compound ramp, 065 the shoulder-site case (linked v40)
  - "framework:GRADE -- the heavy-load direction rests on three small trained-sample crossovers (Ribeiro 2020, Abad 2011, Barroso 2013) plus a review of upper-body RCTs (McCrary 2015) and is indirect for 3-5 rep work at 85-90% 1RM (C). The moderate-load null rests on two randomized crossovers in machine / Smith and free-weight lifts (Enes 2025, Ribeiro 2014) (C). Rung count, reps per rung, rests and minutes are the NSCA test protocol and coaching practice (D)."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: chronotype
      type: categorical
      role: soft
      unknown_policy: hedge
constants:
  heavy_working_reps_max: 6          # product: a working set of 6 reps or fewer counts as heavy for ramp purposes (Ribeiro 2020 tested 6 at 80% 1RM)
  moderate_working_reps_min: 8       # product: 8+ rep work is the ~10RM band Enes 2025 tested
  last_rung_min_frac: 0.75           # Enes / Ribeiro 2020 tested top rungs at 75-80% of the working load; product floor
  last_rung_heavy_frac: [0.85, 0.92] # NSCA near-max 2-3 rep step, translated to a fraction of the working load; practice
  rung_reps_near_top: [2, 5]         # NSCA 2-3 near max, 3-5 middle; Enes 3-4, Ribeiro 6 -- reps on a rung at or above ~70% of the working weight
  ramp_rung_rir_min: 4               # product, matches ax_engine RAMP_RIR "4+": a rung is never a hard set
  rest_between_rungs_s: [60, 120]    # NSCA 1 min early, 2 min later; Enes 120 s
  rest_last_rung_to_work_s: [120, 180]  # NSCA 2-4 min before the heavy step; product
  general_warmup_heavy_min: [10, 20] # Barroso 15 min / Abad 20 min at low intensity helped; 5 min did nothing; product range
  general_warmup_intensity: low      # Barroso: 15 min at 70% VO2max cost 4% 1RM
  ramp_minutes_per_lift: [3, 6]      # derived from rungs x rest; Enes estimate 2-5 min per exercise at ~10RM
ramp_rules:
  - rule: heavy-compound-full-ramp
    trigger: barbell or machine compound, working reps at or under heavy_working_reps_max, first time that lift or pattern is loaded today
    action: empty bar (or lightest stack setting) plus 2-3 intermediate rungs; jump sizes per 018; last rung at last_rung_heavy_frac of the working weight
    table: true
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: C
  - rule: last-rung-near-working
    trigger: any ramp is built
    action: the top rung is at or above last_rung_min_frac of the working weight; a ramp whose rungs all sit at or under about half the working weight is not a finished ramp for heavy work
    table: true
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: C
  - rule: reps-drop-near-top
    trigger: a rung at or above about 70% of the working weight
    action: reps within rung_reps_near_top and never fewer than ramp_rung_rir_min in reserve; the light rungs may carry more reps; no rung is taken near failure
    table: true
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: D
  - rule: moderate-load-short-ramp
    trigger: working reps at or over moderate_working_reps_min, or the lift's muscles were already loaded earlier in the session
    action: 0-1 rung at about last_rung_min_frac of the working weight, 3-4 reps; dropping it does not cost reps or volume (Enes 2025); keep it if the user wants it, the cost is time only
    table: true
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: C
  - rule: heavy-day-general-warmup
    trigger: a heavy or rep-max / top-set test day
    action: general_warmup_heavy_min of low-intensity general work (bike, rower, brisk walk) before the first ramp; not a hard conditioning bout; at dawn this is the same block 073 dawn-extend-warmup lengthens, not a second one
    table: false
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: C
  - rule: time-cap-cut-order
    trigger: the session is over its time budget before it starts
    action: cut ramps on later moderate-load lifts first (to 0-1 rung), then trim the general warm-up toward its low end; keep the full ramp on the first heavy compound
    table: true
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: D
  - rule: ramp-not-a-readiness-test
    trigger: a ramp rung felt heavy or slow
    action: do not cut the working load from ramp feel alone; read the day from the first work set (RIR), per 030 and 073
    table: false
    basis: exercise/autoregulation-vs-percentage-prescription-030
    basis_grade: D
  - rule: no-injury-claim
    trigger: speech about why the ramp is there
    action: say it prepares the lift and the load; never say it prevents injury -- no trial measured that
    table: false
    basis: exercise/warmup-ramp-sets-heavy-compounds-080
    basis_grade: C
refraction_notes:
  - note: >
      CLOSENESS OF THE LAST RUNG MATTERS MORE THAN THE NUMBER OF RUNGS. In
      Ribeiro 2020 one set of 6 at 80% of the training load beat one set of 6
      at 40% for squat velocity; the two-step 40% -> 80% ramp beat 40% alone on
      bench. In Enes 2025 adding a second, lighter set to a 75% set changed
      nothing. The defensible reading: the top rung near the working load
      carries what benefit there is; extra light rungs are for the bar path,
      the joints and the lifter's confidence, not for output.
    grade: C
  - note: >
      BEFORE ~10RM WORK THE RAMP IS OPTIONAL FOR PERFORMANCE. Two randomized
      crossovers in trained lifters (Enes 2025, Smith bench and leg press at
      10RM; Ribeiro 2014, bench / squat / curl at 80% 1RM to failure) found
      no difference in reps, volume or fatigue between a specific warm-up and
      none. Neither tested injury. So a short-on-time lifter can drop ramps on
      moderate-load lifts without losing reps; do not tell them it is unsafe,
      and do not tell them it is safe either -- that was not measured.
    grade: C
  - note: >
      HEAVY WORK HAS NO DIRECT TRIAL. Nothing compared ramp shapes before 3-5
      rep sets at 85-90% 1RM. The 1RM trials (Abad 2011, Barroso 2013) all
      used a specific ramp in every arm and tested the general warm-up on top
      of it, and the NSCA 1RM protocol (2-3 rungs, near-max step, 1-4 min
      rests) is a testing convention. The full ramp for heavy compounds is the
      practice floor, carried by direction, not by a measured dose.
    grade: D
  - note: >
      THE GENERAL WARM-UP IS LONG AND EASY OR IT IS NOTHING. Barroso 2013:
      15 min at low intensity +3% 1RM, 5 min at either intensity no change,
      15 min at moderate intensity -4%. Abad 2011: 20 min easy cycling +8.4%.
      Both n of 13-16, leg press only. Speak it as "10-20 minutes of easy
      work helps a heavy day", never "5 minutes of cardio primes you", and
      never a hard conditioning piece before heavy lifting.
    grade: C
  - note: >
      POPULATION. All trained young adults; Enes is the only one with women
      (7 of 29); none tested older lifters, where a longer ramp may matter
      more for joint comfort. Hedge outside that band.
    grade: C
claim: >
  For a trained lifter, the part of a warm-up ramp that changes performance is
  the last set: a specific set close to the working load (tested at 75-80% of
  it, few reps) improves the following heavy work more than a light-only ramp,
  and a long, easy general warm-up (15-20 min low intensity) on top of the
  specific ramp raised leg-press 1RM by 3-8% in two small trials, while 5 min
  did nothing and 15 min at moderate intensity cost about 4%. Before moderate
  ~10RM multi-set work, a specific ramp of one or two sets made no difference
  to reps, volume or fatigue versus none, so there it is a time choice, worth
  about 2-5 minutes per exercise. No trial tested ramp shapes before 3-5 rep
  sets at 85-90% 1RM and none measured injury; for heavy compounds the
  defensible floor is the NSCA test shape -- a light set, 2-3 rungs with
  falling reps (3-5, then 2-3 near the top) and 1-3 minute rests, the last
  rung near the working weight -- with jump sizes from 018.
reasoning: >
  Ribeiro et al. 2020 is the only trial that varied the specific warm-up load
  before multi-set heavy work in trained lifters (n=40; 3 x 6 at 80% 1RM): the
  80% set beat the 40% set for squat velocity, and the 40% -> 80% two-step
  ramp beat 40% alone for bench, which the authors summarise as "few
  repetitions and low loads is not enough". It had no no-warm-up arm, so it
  ranks warm-ups but does not show any of them beats none. McCrary et al.
  2015 (31 RCTs) supplies strong review-level support for high-load dynamic
  warm-ups and upper-body strength and power, and found no injury studies.
  Enes et al. 2025 is the best-designed null: randomized crossover, n=29,
  Bayesian models, 0 / 1 / 2 specific sets before 4 x 10RM to failure, and
  strong evidence against a more-sets-is-better ordering; the authors limit
  it to ~10RM loads and name 1-3RM work as untested. Ribeiro et al. 2014 (n=15,
  80% 1RM to failure) agrees. For the general part, Abad et al. 2011 (n=13,
  +8.4% leg-press 1RM with 20 min easy cycling added to the same specific
  ramp) and Barroso et al. 2013 (n=16, +3% only with 15 min at low intensity,
  -4% with 15 min at moderate intensity, no change at 5 min) agree on long and
  easy. The rung count, reps per rung and rests come from the NSCA 1RM
  protocol (restated by HPRC 2022), which is a testing convention, not a
  trial. Contested is set because the common coaching line "always ramp,
  every lift, it prevents injury" outruns the evidence on both counts: the
  ramp did not help ~10RM work and no study tested injury.
---

# exercise/warmup-ramp-sets-heavy-compounds-080 -- 무거운 복합운동 전 램프업 세트

**One line:** before a heavy lift, the ramp set that matters is the last one,
close to the working weight; before a 10-rep set the ramp is optional; a long
easy warm-up helps a heavy day; nobody has shown a ramp prevents injury.

What the trials show, plainly:

- Before 3 sets of 6 at 80% of max, one set of 6 at 80% of the training load
  gave faster squats than one set at 40%, and a two-step ramp (40% then 80%)
  gave faster, higher-work bench sets than 40% alone. Light-only ramps were
  not enough.
- Before 4 sets of 10-rep-max work, one or two short warm-up sets made no
  difference to reps, volume or effort compared with none (29 trained lifters,
  bench and leg press). An older study at 80% of max to failure found the same.
  Skipping saves about 2-5 minutes per exercise.
- On top of the same short ramp, 15-20 minutes of easy cycling raised a
  leg-press max by 3-8% in two small studies. Five minutes did nothing, and
  15 minutes at a moderate pace made the max about 4% worse.
- No study compared ramps before 3-5 rep sets at 85-90% of max, and none
  measured injury.

Practical read: heavy compound first in the session -> empty bar, 2-3 rungs
with the reps falling (about 5, then 3, then 2), the last one close to the
working weight, 1-2 minutes between rungs, jump sizes per 018. Moderate-load
lifts later in the session -> one short rung near the working weight or
none. When time is short, cut the later ramps before the first one.

## Ramp rules (for the set table)

| Rule | Trigger | Action | Basis |
|---|---|---|---|
| heavy-compound-full-ramp | compound, <= 6 working reps, first of its pattern today | bar + 2-3 rungs, last at 85-92% of working | trials + NSCA |
| last-rung-near-working | any ramp | top rung >= 75% of working | Ribeiro 2020, Enes 2025 |
| reps-drop-near-top | rung >= ~70% of working | 2-5 reps, RIR 4+ | NSCA, practice |
| moderate-load-short-ramp | >= 8 working reps, or muscles already warm | 0-1 rung, 3-4 reps | Enes 2025, Ribeiro 2014 |
| heavy-day-general-warmup | heavy or test day | 10-20 min easy general work first | Barroso 2013, Abad 2011 |
| time-cap-cut-order | session over budget | cut later ramps first, keep the first heavy one | practice |
| ramp-not-a-readiness-test | rung felt heavy | no load cut from ramp feel; read the first work set | 030, 073 |
| no-injury-claim | speaking the reason | never "prevents injury" | McCrary 2015, Enes 2025 |

## 한국어 요약 (답변용)

- 무거운 세트 전에 효과를 내는 건 마지막 웜업 세트다. 작업 무게에 가까운 무게(연구에서는 작업
  무게의 75~80%)로 몇 회만 하는 게, 가벼운 무게로만 끝내는 것보다 다음 본세트가 좋았다. 가벼운
  세트를 더 늘린다고 나아지지는 않았다.
- 10회 안팎 반복하는 중간 무게 운동 앞에서는 웜업 세트를 1~2개 하든 안 하든 반복 수·총량·힘든
  정도가 같았다(훈련 경력자 29명). 시간이 없으면 생략해도 횟수는 줄지 않는다. 운동당 2~5분쯤
  아낀다.
- 무거운 날에는 본 운동 전에 10~20분 가볍게(자전거·로잉·빠른 걷기) 몸을 데우면 최대 근력이
  3~8% 올랐다(소규모 연구 2편). 5분은 효과가 없었고, 15분을 중간 강도로 하면 오히려 4% 떨어졌다.
  새벽 운동이면 072의 "일반 워밍업 연장"과 같은 블록이다. 두 번 하지 않는다.
- 무거운 복합운동(본세트 6회 이하)을 그날 처음 할 때: 빈 봉 → 2~3단계, 반복은 내려간다(대략
  5회 → 3회 → 2회), 마지막 단계는 작업 무게 가까이, 단계 사이 1~2분 쉰다. 한 번에 올리는 폭은
  018을 따른다. 어느 웜업 세트도 힘들게 하지 않는다(RIR 4 이상).
- 3~5회 본세트(최대의 85~90%) 앞의 램프 모양을 직접 비교한 연구는 없다. 그 부분은 NSCA 1RM
  측정 절차와 현장 관행이다.
- 웜업이 부상을 막는다고 말하지 않는다. 그걸 잰 연구가 없다. "몸과 무게를 준비한다"고만 말한다.
- 웜업 세트가 무겁게 느껴졌다고 본세트 무게를 미리 줄이지 않는다. 첫 본세트의 RIR로 판단한다.
- 연구 참가자는 대부분 젊은 남성 경력자다. 나이 든 사람이나 초보자는 다를 수 있다.
