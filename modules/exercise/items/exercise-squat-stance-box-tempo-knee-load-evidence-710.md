---
# Squat-knee sprint 2026-10-07.
# Evidence half for a lifter who squats with one cautious knee (front-of-knee
# picture under 057). 058 already carries knee angle (depth), leg extension,
# lunge step length, knees-behind-toes and the depth-vs-quad-growth trial;
# this row adds what 058 left out: depth x LOAD together, stance width and
# foot angle, the box squat, tempo / pausing, front vs back squat, the leg
# press and Bulgarian split squat as switch targets, and what a bilateral
# squat does with a one-sided knee. The engine half is 711 (squat_knee_rules).
#
# Every source here was read as a web-search index rendering of its abstract
# or record: the egress proxy refused pubmed, pmc, biomedcentral, the
# university repositories and crossref on 2026-10-07. Numbers are carried
# only where the rendering stated them; the module GAPS logs the re-read.
id: exercise/squat-stance-box-tempo-knee-load-evidence-710
domain: exercise
grade: C (kneecap load rises with load and is highest below parallel under load; stance width changes knee compression in opposite directions in the squat and the leg press; foot angle changes no knee force; the leg press loads the kneecap less than the squat; the box squat keeps a vertical shin and the lowest spine and ankle moments; the Bulgarian split squat is hip-dominant; tempo 0.5-8 s grows muscle alike) -- all model or small-sample lab data in healthy lifters; D (front vs back squat for the kneecap -- conflicting; whether tempo changes kneecap load -- not studied; how a painful knee shares load in a bilateral squat under a bar -- not studied)
lane: "@clinical-physio"
locale: universal
as_of: 2001-2021
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/11528346/"  # Escamilla RF, Fleisig GS, Zheng N, Lander JE, Barrentine SW, Andrews JR, Bergemann BW, Moorman CT 2001, Med Sci Sports Exerc 33(9):1552-1566 -- n=10 experienced male lifters, squat vs high- and low-foot leg press, wide vs narrow stance, feet straight vs turned out 30 deg: tibiofemoral and patellofemoral compression generally GREATER in the squat than either leg press; no knee-force difference between high and low foot placement; foot angle changed no muscle activity or knee force; in the SQUAT the wide stance gave greater tibiofemoral and patellofemoral compression than the narrow, in the LEG PRESS the narrow stance gave greater compression; wide stance more PCL tension in all. Abstract as rendered by the search index
  - "https://lida.sport-iat.de/ta/Record/4064480"  # Patellofemoral joint kinetics in females when using different depths and loads during the barbell back squat, Eur J Sport Sci 2021 (authors not read) -- experienced female lifters, above parallel / parallel / below parallel at 0, 50 and 85% of depth-specific 1RM: peak PF joint reaction force rose with load and was higher below parallel; peak PF stress showed a depth-by-load interaction, rising with load within a depth and greatest below parallel within a load; authors: monitor depth AND load together. Record / abstract as rendered by the search index; the companion thesis (scholarworks.montana.edu handle 1/16371) also tested stance width, results not read
  - "https://pubmed.ncbi.nlm.nih.gov/11390050/"  # Salem GJ, Powers CM 2001, Clin Biomech 16(5):424-430 -- collegiate women, body-weight squats to about 70, 90 and 110 deg knee flexion: peak knee extensor moment, PF reaction force and PF stress did NOT differ between the three depths. Abstract as rendered by the search index
  - "https://research.bond.edu.au/en/publications/a-biomechanical-comparison-of-the-traditional-squat-powerlifting-/"  # Swinton PA, Lloyd R, Keogh JWL, Agouris I, Stewart AD 2012, J Strength Cond Res 26(7):1805-1816 -- n=12 male powerlifters at 30, 50, 70% 1RM lifted fast: traditional squat narrow stance (48 cm), powerlifting and box squat wide (90-92 cm); in the traditional squat the knee travelled past the toes and the centre of mass moved forward, in the powerlifting and box squat the shin stayed more vertical and the centre of mass moved back; peak spine and ankle moments largest in the traditional squat, then powerlifting squat, then box squat; hip moments largest in the powerlifting squat. Peak knee moments by variant not read. Abstract as rendered by the search index
  - "https://doi.org/10.1186/s13102-018-0103-7"  # Lorenzetti S, Ostermann M, Zeidler F, Zimmer P, Jentsch L, List R, Taylor WR, Schellenberg F 2018, BMC Sports Sci Med Rehabil 10:14 -- 21 novice and 21 experienced squatters, 3 stance widths x 3 foot angles (0, 21, 42 deg), 0 and 50% body weight: stance width and foot angle both changed hip and knee moments (frontal and sagittal); wider foot angle more side-to-side knee travel, wider stance less; novices more knee travel; added load less. Authors: choose stance and foot angle by the joint moments you want. Abstract as rendered by the search index
  - "https://shura.shu.ac.uk/32297"  # Sinclair J, Atkins S, Kudiersky N, Taylor PJ, Vincent H 2015, J Biomed Eng Inform 2(1):76-81 -- n=35 experienced men at 70% 1RM: patellofemoral load higher in the back squat than the front squat. Record as rendered by the search index
  - "https://www.mdpi.com/2076-3417/15/16/8784"  # Applied Sciences 2025, 15(16):8784 (authors not read) -- unloaded front vs back squat: PF stress similar; more trunk flexion went with lower knee stress; deeper raised PF stress in both. As rendered by the search index; conflicts with Sinclair 2015 under load
  - "https://digitalcommons.wku.edu/ijes/vol14/iss1/10"  # Mackey ER, Riemann BL 2021, Int J Exerc Sci 14(1) -- n=20 resistance-trained men, back squat at 70% 1RM vs Bulgarian split squat at 35% 1RM: both hip-dominant; in the BSS knee net joint moment impulse and peak moment were LESS than the ankle's, in the back squat knee impulse greater than ankle; knee peak displacement smaller in the BSS (d = 0.82). Authors: BSS suits phases where hip extension is wanted with low knee demand, e.g. early knee rehabilitation. Abstract as rendered by the search index
  - "https://doi.org/10.1186/s13102-017-0085-x"  # Severin AC, Burkett BJ, McKean MR, Wiegand AN, Sayers MGL 2017, BMC Sports Sci Med Rehabil 9:23 -- cross-sectional, 20 adults with long-standing UNILATERAL anterior knee pain vs 20 matched controls, body-weight squats: the double-leg squat was symmetrical on land; the single-leg squat showed less hip flexion and altered shank motion on the affected side. Abstract as rendered by the search index
  - "https://pubmed.ncbi.nlm.nih.gov/25601394/"  # Schoenfeld BJ, Ogborn DI, Krieger JW 2015, Sports Med 45(4):577-585 -- meta-analysis, 8 studies, training to failure >= 6 weeks: hypertrophy similar with repetition durations 0.5-8 s; very slow (about 10 s) inferior. Abstract as rendered by the search index
  - "exercise/knee-friendly-squat-depth-variants-058"  # within-warehouse: knee angle, leg extension range, lunge step, knees-behind-toes, Kubo 2019 half vs full squat; NOT repeated here
  - "exercise/knee-pain-symptom-guided-loading-057"  # within-warehouse: the 2/10 knee ceiling and the knee rung this row serves
  - "exercise/caution-severity-ladder-056"  # within-warehouse: rungs
  - "exercise/machine-free-weight-equivalence-075"  # within-warehouse: leg press and squat grow the thigh alike (C); squat transfers better to jumping (C)
  - "exercise/knee-prep-hip-adductor-abductor-078"  # within-warehouse: hip work alongside any swap
  - "framework:GRADE -- every knee-load finding is a model estimate or a moment calculation in 10-42 healthy lifters per study (indirect for a painful knee, imprecise); front vs back squat conflicts between two lab studies; no study measures kneecap load by tempo or pause, none compares knee PAIN outcomes between stance widths, box vs free squats, or squat vs leg press vs split squat in lifters with knee pain. All abstracts read only through a search-index rendering."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
knee_load_levers:
  - lever: load at a given depth
    direction: kneecap force rises with bar load; under load it is highest below parallel
    knee_use: at a cautious knee, load and depth are stepped back together, not depth alone
    basis: Eur J Sport Sci 2021 (females, depth x load); Salem 2001 (no depth effect without load)
    basis_grade: C
  - lever: stance width
    direction: squat -- wide stance more knee compression than narrow; leg press -- narrow stance more than wide
    knee_use: no width is knee-friendly by default; try the other width at a light load and keep the one that stays inside the knee ceiling
    basis: Escamilla 2001
    basis_grade: C
  - lever: foot angle (0-30 deg out)
    direction: no knee-force difference; wider angle more side-to-side knee travel
    knee_use: pick the angle that lets the knee track over the foot; not a knee-load lever
    basis: Escamilla 2001; Lorenzetti 2018
    basis_grade: C
  - lever: box squat (wide stance, sit back to a box)
    direction: more vertical shin, centre of mass back, lowest spine and ankle moments of three squat styles; hip moments high
    knee_use: the box fixes the depth reached on every rep; useful as a depth stop for a knee, but the load moves toward the hip
    basis: Swinton 2012
    basis_grade: C
  - lever: front vs back squat
    direction: conflicting -- back squat more kneecap load at 70% 1RM in one study; similar unloaded in another
    knee_use: no rule picks one for the knee; choose by the user's response
    basis: Sinclair 2015; Applied Sciences 2025
    basis_grade: D
  - lever: tempo and pauses
    direction: kneecap load by tempo not studied; muscle growth similar across 0.5-8 s reps
    knee_use: a controlled descent and a pause are free to use for growth; any knee benefit comes through the lighter load a slow or paused rep forces, not a measured effect
    basis: Schoenfeld 2015
    basis_grade: D
  - lever: switch to leg press
    direction: less kneecap compression than the squat at matched effort; thigh growth alike
    knee_use: first switch target when the squat keeps breaching the ceiling and the squat is not a named goal lift
    basis: Escamilla 2001; Escamilla 1998 (058); 075
    basis_grade: C
  - lever: switch to Bulgarian / split squat
    direction: hip-dominant, knee demand lower relative to the hip and ankle than the back squat
    knee_use: switch target for a ONE-sided knee: each leg gets its own range and load
    basis: Mackey 2021; Severin 2017
    basis_grade: C
refraction_notes:
  - note: >
      DEPTH AND LOAD TOGETHER. Without a bar, kneecap load barely changed
      between squatting to 70, 90 and 110 degrees. With a bar, it rose with
      the load and was highest below parallel. So for a cautious knee the
      first step back is lighter AND a little higher, not just higher with
      the same weight.
    grade: C
  - note: >
      NO STANCE IS THE KNEE STANCE. In the squat a wide stance pressed the
      knee harder than a narrow one; on the leg press it was the other way
      round. Turning the feet out up to 30 degrees changed no knee force. The
      stance that suits a painful knee is found by trying, at a light load.
    grade: C
  - note: >
      A BOX IS A DEPTH STOP THAT MOVES SOME LOAD TO THE HIP. The box squat
      kept the shin more upright and had the lowest back and ankle load of
      three squat styles in powerlifters. Its practical use for a knee is
      that every rep stops at the same height, so the depth can be set and
      lowered one notch at a time.
    grade: C
  - note: >
      THE LEG PRESS IS GENTLER ON THE KNEECAP THAN THE SQUAT. In experienced
      lifters, kneecap and knee compression were generally higher in the
      squat than in the leg press, and the leg press grows the thigh about as
      well. When the squat keeps hurting, the leg press with a stop is the
      first swap; the squat stays only if it is a goal in itself.
    grade: C
  - note: >
      ONE BAD KNEE: SPLIT THE LEGS. People with one painful kneecap squatted
      symmetrically on two legs (body weight), so a bilateral squat does not
      show or spare the bad side; on one leg the bad side moved differently.
      A split squat or Bulgarian split squat lets each leg have its own depth
      and load, and its knee demand is lower relative to the hip than a back
      squat's.
    grade: C
  - note: >
      TEMPO IS NOT A PROVEN KNEE TOOL. Muscle grows alike with reps of half a
      second to eight seconds, so a slow descent or a pause costs nothing.
      Whether it lowers kneecap load has not been measured; it mainly works
      by making the same set need a lighter bar.
    grade: D
  - note: >
      FRONT OR BACK SQUAT: NO SETTLED ANSWER FOR THE KNEE. One study found
      more kneecap load in the back squat at a working weight; another found
      none unloaded and less knee stress with more forward lean. Neither
      choice is a knee rule.
    grade: D
claim: >
  For a lifter squatting with a cautious front-of-knee, kneecap load depends on
  bar load and depth together: without a bar it hardly changed between 70 and
  110 degrees, with a bar it rose with load and peaked below parallel. Stance
  width moves knee compression in opposite directions in the squat (wide
  higher) and the leg press (narrow higher), and turning the feet out changes
  no knee force, so stance is chosen by response. The box squat keeps the shin
  vertical and spine and ankle load lowest, and its use for a knee is as a
  fixed depth stop. The leg press loads the kneecap less than the squat and
  grows the thigh as well, so it is the first switch when the squat keeps
  hurting; the Bulgarian split squat is hip-dominant with lower relative knee
  demand and lets a one-sided knee set its own range and load. Tempo between
  half a second and eight seconds per rep grows muscle alike; its effect on
  the knee is not measured. Front versus back squat has conflicting knee data.
reasoning: >
  This row extends 058 rather than repeating it: 058 owns knee angle, leg
  extension, lunge step and the knees-behind-toes cue. Escamilla 2001 is the
  one study testing stance and foot angle in both the squat and leg press with
  modelled knee forces, in 10 experienced men, which is why stance is a
  try-and-keep lever rather than a prescription. The female depth-by-load
  study and Salem 2001 together explain why depth alone is the wrong single
  dial. Swinton 2012 describes the box squat's mechanics in powerlifters
  lifting fast at submaximal loads; it measured no knee pain. Mackey 2021
  compared different relative loads (70 vs 35% 1RM), so its knee-vs-hip
  balance is a pattern, not a matched dose. Severin 2017 is body-weight and
  cross-sectional; it says a bilateral squat hides a one-sided knee, not that
  a split squat treats it. Schoenfeld 2015 sets tempo free for growth; no
  kneecap-by-tempo study was found, so the tempo note is D. Front vs back
  squat is marked contested. All abstracts were read only as search-index
  renderings (egress refused the primary hosts), so numbers are carried
  sparingly and the re-read is logged in GAPS.
---

# exercise/squat-stance-box-tempo-knee-load-evidence-710 -- 무릎이 신경 쓰일 때 스쿼트 스탠스·박스·템포, 언제 레그프레스·스플릿 스쿼트로 바꾸나

**한 줄 그림:** 무릎 부담은 깊이 하나가 아니라 무게와 깊이가 같이 정한다. 스탠스는 정답이 없어 가볍게
시험해 보고 고른다. 박스는 깊이를 고정하는 도구다. 스쿼트가 계속 아프면 레그프레스로, 한쪽 무릎만
문제면 스플릿 스쿼트로 바꾼다.

## Knee-load levers (engine-readable)

| Lever | What changes at the knee | How the plan uses it | Evidence |
|---|---|---|---|
| bar load at a depth | kneecap force up with load; highest below parallel under load | step back load and depth together | lab, small |
| stance width | squat: wide > narrow; leg press: narrow > wide | try the other width light, keep what stays in the ceiling | lab, n=10 |
| foot angle 0-30 deg | no knee-force change | pick for knee tracking, not load | lab |
| box squat | vertical shin, lowest spine / ankle load, hip load up | fixed depth stop, lowered one notch at a time | lab, n=12 |
| front vs back squat | conflicting | no knee rule | conflicting |
| tempo / pause | not measured for the knee; growth alike 0.5-8 s | free to use; helps by forcing a lighter bar | meta-analysis (growth only) |
| leg press | less kneecap compression than the squat | first switch when the squat keeps hurting | lab |
| Bulgarian / split squat | hip-dominant, lower relative knee demand | switch for a one-sided knee | lab, n=20 |

## 한국어 요약 (답변용)

- 맨몸 스쿼트에서는 70도, 90도, 110도로 깊이를 바꿔도 슬개골 부담이 거의 같았다. 바벨을 들면 무게가
  늘수록 부담이 커지고, 패럴렐보다 깊을 때 가장 컸다. 그래서 무릎이 신경 쓰이면 깊이만 줄이지 말고
  무게도 같이 줄인다.
- 스탠스는 무릎에 좋은 정답이 없다. 스쿼트에서는 넓은 스탠스가 좁은 스탠스보다 무릎을 더 눌렀고,
  레그프레스에서는 반대였다. 발끝을 30도까지 벌리는 건 무릎 부담에 차이가 없었다. 가벼운 무게로 두
  스탠스를 해 보고 덜 아픈 쪽을 쓴다.
- 박스 스쿼트는 정강이가 더 세워지고 허리·발목 부담이 가장 작았지만 엉덩이 부담은 컸다. 무릎에는
  매번 같은 깊이에서 멈추게 해 주는 도구로 쓰고, 박스 높이를 한 칸씩 낮춰 간다.
- 레그프레스는 스쿼트보다 슬개골 압박이 대체로 작고, 허벅지 근육은 비슷하게 큰다. 스쿼트가 계속
  아프면 먼저 레그프레스(멈춤 장치로 범위 제한)로 바꾼다. 스쿼트 자체가 목표인 사람만 스쿼트를 남긴다.
- 한쪽 무릎만 아픈 사람도 양발 스쿼트에서는 좌우가 비슷하게 움직였다. 양발 스쿼트로는 아픈 쪽을 따로
  조절할 수 없다는 뜻이다. 스플릿 스쿼트나 불가리안 스플릿 스쿼트는 다리마다 깊이와 무게를 따로 정할 수
  있고, 백스쿼트보다 엉덩이 비중이 크다.
- 템포는 0.5초부터 8초까지 근육 성장에 차이가 없었다. 천천히 내리거나 멈추는 건 손해가 없지만, 무릎
  부담을 줄인다는 연구는 없다. 같은 세트를 더 가벼운 무게로 하게 만드는 효과가 있을 뿐이다.
- 프론트 스쿼트와 백스쿼트 중 무릎에 더 나은 쪽은 연구 결과가 엇갈린다. 정해진 답이 없다.
- 이 행의 연구는 모두 건강한 사람을 대상으로 한 실험실 계산이다. 아픈 무릎에서 스탠스, 박스, 레그프레스,
  스플릿 스쿼트를 비교한 연구는 없다.
