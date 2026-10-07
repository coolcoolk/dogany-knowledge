---
# Main-lift cue sprint 2026-10-08. Evidence
# half: what the research says about HOW a lifting cue should be worded --
# an external focus (on the bar, the floor, the movement's effect) or an
# internal focus (on a muscle or a body part) -- for strength on a heavy set,
# for long-term strength and muscle gains, and for EMG. The engine half is 746
# (lift_cues), which tags every cue with its focus type and reads the
# focus_findings below to choose the wording by goal and load.
#
# Read depth: Chua 2021, McKay 2024, Grgic 2021 (strength) were read in full
# text (PDFs from the publishers' / authors' repositories, 2026-10-08).
# Schoenfeld 2018, Calatayud 2016, Kristiansen 2018 and Snyder & Leech 2009
# were read only as search-index renderings of their abstracts (pubmed
# refused a cookie-less fetch); numbers are carried only where the rendering
# stated them. The module GAPS logs the re-read.
id: exercise/attentional-focus-cue-evidence-745
domain: exercise
grade: C (an external cue lifts acute strength on the set a little -- SMD 0.34 over 7 small studies, not corrected for publication bias; over 6-12 weeks no overall strength difference, lower-body subgroup favours external from 3 trials); C (an internal "squeeze the muscle" focus grew the biceps more than an external one in one 8-week trial in untrained men, with no difference at the quadriceps; internal focus raises the target muscle's EMG at 20-60% 1RM but not at 80%); B (the broad motor-learning claim that an external focus is always better is NOT settled -- the 2021 meta-analysis found g 0.26-0.58, the 2024 bias-corrected reanalysis of the same data found g 0.01-0.15 with the data favouring the null)
lane: "@performance-lit"
locale: universal
as_of: 2009-2024
contested: yes
sources:
  - "https://doi.org/10.1037/bul0000335"  # Chua LK, Jimenez-Diaz J, Lewthwaite R, Kim T, Wulf G 2021, Psychol Bull 147(6):618-645 -- full text read: 73 studies / 1,824 participants (performance) after removing 18 outlier effects, external > internal focus Hedges g 0.264 (95% CI 0.217-0.310); retention g 0.583 (0.425-0.741, 40 studies); transfer g 0.584 (0.325-0.842); EMG (12 studies, 216 participants) g 0.833 (0.453-1.213) toward lower EMG with external focus; distal > proximal external g 0.224 (0.019-0.429); no moderation by age, health or skill level. Egger's test showed small-study effects for performance, t(47) = 2.900, p = .006, and t(98) = 4.113, p < .001 before outlier removal; the authors judged the results robust by the Mathur-VanderWeele selection model
  - "https://doi.org/10.1037/bul0000451"  # McKay B, Corson AE, Seedu J, De Faveri CS, Hasan H, Arnold K, Adams FC, Carter MJ 2024, Psychol Bull 150(11):1347-1362 -- full text read (authors' repository PDF): preregistered robust Bayesian reanalysis of the Chua 2021 data sets; moderate to strong evidence of publication bias in every analysis; bias-corrected mean effects g 0.01 (performance), 0.15 (retention), 0.09 (transfer), 0.06 (EMG), -0.01 (distal vs proximal); Bayes factors favour the null, BF01 1.3 (retention) to 5.75 (performance); clear heterogeneity in every analysis (tau about 0.40-0.65), i.e. focus effects vary for reasons not yet known; authors: a more cautious approach is needed when recommending external foci
  - "https://doi.org/10.3390/sports9110153"  # Grgic J, Mikulic I, Mikulic P 2021, Sports 9(11):153 -- full text read (Victoria University repository PDF): 10 studies; ACUTE (7 studies, n 11-30 each; isometric mid-thigh pull, handgrip, isometric elbow flexion, squat, deadlift) external > internal SMD 0.34 (95% CI 0.22-0.46), I2 40%; LONG-TERM (3 trials, 6-12 weeks; squat, deadlift, knee extension, elbow flexion) SMD 0.32 (-0.08 to 0.73), ns; lower-body subgroup SMD 0.47 (0.07-0.87). PEDro fair to good; only two studies blinded participants, none blinded assessors. Authors: standardise or avoid focus cues in strength testing; external focus may help in strength sports. No publication-bias correction (too few studies)
  - "https://lida.sport-iat.de/ta/Record/4060516"  # Schoenfeld BJ, Vigotsky A, Contreras B, Golden S, Alto A, Larson R, Winkelman N, Paoli A 2018, Eur J Sport Sci 18(5):705-712 -- RCT, 30 untrained college-aged men, 8 weeks, 3 sessions a week, 4 x 8-12 to failure, curl and leg extension: INTERNAL ("squeeze the muscle") vs EXTERNAL ("get the weight up"); elbow flexor thickness +12.4% internal vs +6.9% external (significant); quadriceps thickness similar; isometric elbow flexion strength favoured internal, knee extension external, neither significant. Abstract as rendered by the search index
  - "https://www.sponet.de/Record/4068196"  # Calatayud J, Vinstrup J, Jakobsen MD, Sundstrup E, Brandt M, Jay K, Colado JC, Andersen LL 2016, Eur J Appl Physiol 116(3):527-533 -- 18 resistance-trained men, bench press at 20, 40, 50, 60, 80% 1RM, no focus vs focus on pectoralis vs focus on triceps: focusing on a muscle raised that muscle's EMG at 20-60% 1RM but not at 80%; the other muscle's EMG did not fall (triceps focus also raised pectoralis EMG at 50-60%). Abstract as rendered by the search index
  - "https://vbn.aau.dk/da/publications/external-and-internal-focus-of-attention-increases-muscular-activ"  # Kristiansen M, Samani A, Vuillerme N, Madeleine P, Hansen EA 2018, J Strength Cond Res 32(9):2442-2451 -- 21 resistance-trained men, bench press at 60% 3RM: BOTH an instructed external and an instructed internal focus raised mean EMG of 6 upper-body muscles over a no-instruction baseline. Record as rendered by the search index
  - "https://pubmed.ncbi.nlm.nih.gov/19826307/"  # Snyder BJ, Leech JR 2009, J Strength Cond Res 23(8):2204-2209 -- 8 women with little training, wide-grip front lat pull-down at 30% max: after verbal instruction to emphasise the lats and de-emphasise the arms, latissimus EMG rose (p = .005); biceps and teres major unchanged -- more lat, not isolation. Abstract as rendered by the search index
  - "exercise/emg-not-hypertrophy-proxy-013"  # within-warehouse: EMG rises are not growth evidence; the Calatayud / Kristiansen / Snyder rows pick wording, never predict outcome
  - "exercise/increment-verification-floor-029"  # within-warehouse: why an untested-in-practice 1RM shift of a few percent is below the test-retest floor
  - "framework:GRADE -- strength rows: small within-subject studies (n 11-30), mostly unblinded, one meta-analysis of 10 studies without a bias correction; the parent motor-learning literature it sits in shows publication bias that erases the average effect when corrected (McKay 2024), so the acute-strength SMD is held at C and marked contested. Hypertrophy row: one RCT in untrained men, two muscles, opposite-direction trends -- C at most, not generalised to compound lifts. EMG rows are mechanism only (013)."
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
focus_findings:
  - finding: acute strength on a heavy set
    direction: external (bar, floor, movement effect) slightly above internal
    size: SMD 0.34 (95% CI 0.22-0.46), 7 small studies, not bias-corrected
    lift_use: on heavy sets (about 80% 1RM and up, or a top set) the cue is worded externally
    basis: Grgic 2021
    basis_grade: C
  - finding: long-term strength gain
    direction: no overall difference; lower-body subgroup favours external
    size: SMD 0.32 (-0.08 to 0.73) overall; 0.47 (0.07-0.87) lower body, 3 trials
    lift_use: external wording is the default for squat, hinge and leg press strength work; no claim of a bigger gain
    basis: Grgic 2021
    basis_grade: C
  - finding: muscle growth, single-joint
    direction: internal ("squeeze the muscle") grew the biceps more; quadriceps alike
    size: elbow flexor thickness +12.4% vs +6.9%, n=30 untrained, 8 weeks
    lift_use: an internal cue is allowed on isolation and machine accessory sets for growth; not extended to compound main lifts
    basis: Schoenfeld 2018
    basis_grade: C
  - finding: target-muscle EMG by load
    direction: internal focus raises the named muscle's EMG at 20-60% 1RM, not at 80%; other prime movers not reduced
    size: EMG only, n=18 trained (bench)
    lift_use: a muscle cue is useful on light-to-moderate sets (warm-ups, 10+ rep sets, pulldowns and rows); dropped on heavy sets
    basis: Calatayud 2016; Kristiansen 2018; Snyder 2009
    basis_grade: C
  - finding: any instructed focus vs none
    direction: both instructed focuses raised bench EMG over no instruction
    size: EMG only, n=21 trained, 60% 3RM
    lift_use: one short cue per set beats a silent set or a list; the cue count stays at one or two per set
    basis: Kristiansen 2018
    basis_grade: C
  - finding: general motor learning, external superiority
    direction: contested -- g 0.26-0.58 before bias correction, g 0.01-0.15 after; heterogeneous
    size: 73 / 40 / 22 studies; corrected BF01 1.3-5.75 for the null
    lift_use: never tell a user external cues are proven better; offer the other wording if a cue does not help
    basis: Chua 2021; McKay 2024
    basis_grade: B
  - finding: strength testing
    direction: focus wording shifts measured strength
    size: same as acute strength
    lift_use: use the same cue (or none) on every test day so a 1RM or rep test stays comparable
    basis: Grgic 2021
    basis_grade: C
refraction_notes:
  - note: >
      HEAVY SET, OUTSIDE CUE. On a near-maximal set, telling the lifter to
      push the floor away or drive the bar up gave a little more force than
      telling them to tighten a muscle, in small lab studies. The edge is
      small and the strength studies were never corrected for publication
      bias, so this is a wording default, not a strength method.
    grade: C
  - note: >
      GROWTH SET, INSIDE CUE IS ALLOWED. In one 8-week trial in untrained men,
      thinking "squeeze the biceps" on curls grew the biceps more than
      thinking "get the weight up"; on leg extensions it made no difference.
      Focusing on a muscle raised its activity at 20-60% of max on the bench
      press but not at 80%. So a muscle cue fits lighter accessory and machine
      sets; it is not evidence for compound lifts.
    grade: C
  - note: >
      THE "EXTERNAL ALWAYS WINS" RULE IS NOT SETTLED. The 2021 meta-analysis
      of 73 motor-skill studies favoured an external focus, but a
      preregistered 2024 reanalysis of the same data, correcting for
      publication bias, put the average effect near zero and found it varies
      a lot between tasks for unknown reasons. The useful practice is to give
      one cue, see whether it helps this person, and switch wording if not.
    grade: B
  - note: >
      SAME CUE ON TEST DAY. Because focus wording changes how much a person
      lifts on the day, a 1RM or rep test is only comparable if the cue is the
      same (or none) each time.
    grade: C
claim: >
  An external cue (on the bar, the floor, or where the weight should go)
  raised strength on the set a little over an internal cue (on a muscle) in
  seven small studies, SMD 0.34; over 6-12 weeks of training the overall
  strength difference was not significant, with a lower-body subgroup
  favouring external in three trials. An internal "squeeze the muscle" focus
  grew the biceps more than an external focus in one 8-week trial in
  untrained men but made no difference at the quadriceps, and a muscle focus
  raised that muscle's EMG on the bench press at 20-60% of 1RM but not at
  80%. The wider claim that an external focus is always superior for motor
  skills rests on a literature with strong publication bias: corrected, the
  average effect is near zero and highly variable. So cue wording is a small
  lever: external by default on heavy compound sets, internal allowed on
  lighter growth and accessory sets, one cue at a time, and kept the same on
  test days.
reasoning: >
  Grgic 2021 is the only meta-analysis of focus on muscular strength; its
  acute pool (7 studies) is small, mostly within-subject and unblinded, and
  could not test for publication bias. McKay 2024 reanalysed Chua 2021's
  motor-learning data sets (not Grgic's strength set) and found the effect
  shrinks to near nil once bias is modelled; the strength studies sit inside
  that literature and share its small-sample design, so the acute-strength
  effect is graded C and the item is contested. The B grade on the
  not-settled note is for the finding that the broad superiority claim does
  not survive a bias correction (two meta-analyses of the same data, full
  texts read), not for any direction of effect. Schoenfeld 2018 is one trial
  in untrained men on two single-joint exercises; it licenses an internal
  cue on accessory work, not a rule for squats or presses. The EMG studies
  (Calatayud, Kristiansen, Snyder) only show that attention changes muscle
  activity and that this fades at heavy loads; per 013, EMG does not predict
  growth, so they choose wording and load band, nothing more.
---

# exercise/attentional-focus-cue-evidence-745 -- 운동 큐는 근육에 집중(내적)할까, 바벨·바닥에 집중(외적)할까

**한 줄 그림:** 무거운 세트에서는 "바닥을 밀어내", "바를 천장으로" 같은 바깥 큐가 힘을 조금 더 낸다.
가벼운 보조 운동에서 근육을 키우려면 "근육을 쥐어짜" 같은 안쪽 큐도 괜찮다. 어느 쪽이 무조건 낫다는
주장은 출판 편향을 보정하면 거의 사라진다. 큐는 한 번에 하나, 안 맞으면 바꾼다.

## Focus findings (engine-readable)

| Finding | Direction | How the cue engine uses it | Grade |
|---|---|---|---|
| acute strength, heavy set | external a little higher (SMD 0.34) | heavy / top sets get an external cue | C |
| long-term strength | no overall difference; lower body favours external | external default on squat, hinge, leg press | C |
| growth, single-joint | internal grew biceps more; quads alike | internal cue allowed on accessory / machine growth sets | C |
| muscle EMG by load | internal raises it at 20-60% 1RM, not 80% | muscle cue on light-moderate sets only | C |
| instructed vs none | both focuses raise EMG over no cue | one short cue per set | C |
| "external always better" | contested: g 0.26-0.58 raw, 0.01-0.15 bias-corrected | never claim it is proven; switch wording if a cue does not help | B |
| strength testing | wording shifts the result | same cue (or none) on every test day | C |

## 한국어 요약 (답변용)

- 무거운 세트에서는 "바닥을 밀어내", "바를 위로 밀어 올려"처럼 바벨·바닥·움직임 결과에 집중하는 큐가
  "가슴 근육에 힘 줘" 같은 근육 큐보다 힘이 조금 더 났다. 작은 연구 7개를 모은 결과이고 차이는 작다.
- 6-12주 동안 꾸준히 훈련했을 때 근력이 늘어난 정도는 전체적으로 차이가 없었다. 하체 운동만 따로 보면
  바깥 큐 쪽이 조금 나았다(연구 3개).
- 근육 크기는 달랐다. 운동 경험이 없는 남성 30명이 8주 동안 덤벨 컬을 할 때 "이두를 쥐어짜"에 집중한
  쪽이 "무게를 들어 올려"에 집중한 쪽보다 이두가 더 컸다(12.4% 대 6.9%). 레그 익스텐션의 허벅지는
  차이가 없었다. 그래서 근육 큐는 컬·머신 같은 보조 운동에서 쓸 만하고, 스쿼트·벤치 같은 주 운동의
  근거는 아니다.
- 벤치프레스에서 특정 근육에 집중하면 1RM의 20-60% 무게에서는 그 근육이 더 많이 쓰였지만 80%에서는
  차이가 없었다. 무거워지면 근육 큐는 효과가 없다.
- "바깥 큐가 항상 낫다"는 말은 확정이 아니다. 운동 기술 연구 73개를 모은 2021년 분석은 바깥 큐가 낫다고
  했지만, 같은 자료를 출판 편향까지 보정해 다시 분석한 2024년 연구에서는 평균 효과가 거의 0이었고 과제에
  따라 결과가 크게 달랐다.
- 그래서 큐는 한 세트에 하나만 준다. 효과가 없으면 다른 표현으로 바꿔 본다.
- 1RM이나 반복 횟수를 테스트하는 날에는 매번 같은 큐를 주거나 아예 주지 않아야 기록을 비교할 수 있다.
