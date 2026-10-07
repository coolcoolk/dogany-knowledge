---
# Core / functional accessory sprint 2026-10-07. A trained lifter who already squats, deadlifts,
# presses and rows asks for "core" or a "connected body": what do carries,
# anti-rotation work, the dead bug and crunch variants add, how much, and
# where in the session. The kit has no row for trunk accessories; the
# connection side (037) and the work-capacity side (036) were defined without
# one. Every primary below was read at its abstract on PubMed, except
# Contreras & Schoenfeld 2011 (read at full text, the authors' PDF) and
# Prieske 2016 (read at full text, the University of Potsdam PDF).
#
# core_rules is structured data for the split / accessory code, same posture
# as 056's decision_ladder. number_kind says what a number is: evidence (a
# measured result), expert (one review's recommendation, no trial behind it)
# or product (a plan constant). Never speak an expert or product number as
# measured.
id: exercise/core-functional-accessory-carry-081
domain: exercise
grade: B (trunk training raises trunk strength and endurance; transfer to performance small in trained people; unstable surfaces not a primary mode); C (heavy free-weight lifts load the back extensors more than core drills -- EMG only; carries add a frontal-plane demand -- biomechanics plus one short RCT); D (dose, placement, crunch-volume and morning-flexion limits, anti-rotation and dead-bug specifics)
lane: "@performance-lit"
locale: universal
as_of: 2001-2022
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/35061213/"  # Saeterbakken AH, Stien N, Andersen V, Scott S, Cumming KT, Behm DG, Granacher U, Prieske O 2022, Sports Med 52(7):1599-1622 -- 31 controlled trials, 693 competitive athletes aged 11-37, vs ACTIVE controls: max strength SMD 0.39, local muscular endurance 1.29, lower-limb power 0.30, linear sprint 0.66, CODS/agility 0.70 (large only in children), sport-specific performance 0.64; >18 sessions beat <=18 for power and sprint; median PEDro 5
  - "https://www.uni-potsdam.de/fileadmin/projects/trainingswissenschaft/ATB-Ver%C3%B6ffentlichungen/Prieske_Muehlbauer_et_al_2016_SM.pdf"  # Prieske O, Muehlbauer T, Granacher U 2016, Sports Med 46:401-419 -- healthy trained 16-44 y: trunk strength correlates with performance only -0.05 <= r <= 0.18 (15 studies); core strength training gives large trunk-strength gains (SMD 1.07) but 0 to 0.71 on performance proxies vs no or regular training (16 studies); median PEDro 4. Read at full text
  - "https://pubmed.ncbi.nlm.nih.gov/22784233/"  # Reed CA, Ford KR, Myer GD, Hewett TE 2012, Sports Med 42(8):697-706 -- 24 studies: targeted core stability training gives marginal benefit to athletic performance; core work is rarely isolated from the wider programme
  - "https://pubmed.ncbi.nlm.nih.gov/23542879/"  # Martuscello JM et al. 2013, J Strength Cond Res 27(6):1684-98 -- 17 EMG studies, n=252: lumbar multifidus activity greater in free-weight exercises than ball/device exercises (moderate evidence); TrA similar in core-stability and ball/device; advises multijoint free weights over core-specific drills to train these muscles
  - "https://pubmed.ncbi.nlm.nih.gov/18076231/"  # Hamlyn N, Behm DG, Young WB 2007, J Strength Cond Res 21(4):1108-12 -- n=16: 80% 1RM squat and deadlift erector spinae EMG exceeded superman and side bridge by about 53-69%; NO significant difference in external oblique or lower abdominal activity
  - "https://pubmed.ncbi.nlm.nih.gov/20130673/"  # Behm DG, Drinkwater EJ, Willardson JM, Cowley PM 2010, Appl Physiol Nutr Metab 35(1):109-12 -- CSEP position stand: bracing beats hollowing for spinal stability; unstable bases raise core EMG but cut force, power, velocity and ROM, so not recommended as the primary mode for athletic conditioning; ground-based free weights reach similar or higher core activation; a role in periodisation, rehab and for people avoiding free weights
  - "https://pubmed.ncbi.nlm.nih.gov/19528856/"  # McGill SM, McDermott A, Fenwick CM 2009, J Strength Cond Res 23(4):1148-61 -- EMG-driven spine model of farmer's walk, super yoke, suitcase carry, Atlas stone, keg walk, tire flip, log lift: quadratus lumborum and torso stiffness buttress hip-abduction deficits; super yoke gave the HIGHEST spine load; carrying challenged different abilities from lifting, suggesting loaded carries would enhance lifting-based programmes
  - "https://pubmed.ncbi.nlm.nih.gov/25627449/"  # Winwood PW, Cronin JB, Posthumus LR, Finlayson SJ, Gill ND, Keogh JW 2015, J Strength Cond Res 29(2):429-39 -- RCT n=30 resistance-trained rugby players, 7 weeks 2x/week, strongman vs biomechanically matched traditional training: no significant between-group differences; small edges each way (strongman: muscle mass, acceleration, bent-over row 1RM; traditional: squat and deadlift 1RM, jump, COD, sled push)
  - "https://pubmed.ncbi.nlm.nih.gov/31820223/"  # Hindle BR, Lorimer A, Winwood P, Keogh JWL 2019, Sports Med Open 5:49 -- 11 strongman biomechanics studies; farmer's walk performance tied to stride length/rate and short ground contact; no quantitative data for yoke, unilateral carry, stone; training adaptations and risks unstudied
  - "https://bretcontreras.com/wp-content/uploads/To-Crunch-or-Not-to-Crunch-An-Evidence-Based-Examination-of-Spinal-Flexion-Exercises-Their-Potential-Risks-and-Their-Applicability-to-Program-Design.pdf"  # Contreras B, Schoenfeld B 2011, Strength Cond J 33(4):8-18 -- narrative review, read at full text: the finite-flexion-cycles claim rests on in vitro animal data and is speculative for healthy living spines; contraindication only for existing spinal pathology (disc herniation/prolapse, flexion intolerance); EXPERT recommendations, no trial: <= about 60 lumbar flexion reps per session, 6-15 reps with added load for strength/hypertrophy, >= 48 h (72 h+ by response) between dynamic flexion sessions, no flexion within about 1 h of rising (2 h conservative), a few minutes up and walking after long sitting; holds 10-15 s harder variants or 60 s+ for endurance
  - "https://pubmed.ncbi.nlm.nih.gov/11114441/"  # Callaghan JP, McGill SM 2001, Clin Biomech 16(1):28-37 -- porcine cervical motion segments, up to 86,400 flexion/extension cycles at 1 Hz under compression: herniation with modest compression and highly repetitive flexion. The in vitro origin of the crunch concern
  - "https://pubmed.ncbi.nlm.nih.gov/21804427/"  # Vispute SS, Smith JD, LeCheminant JD, Hurley KS 2011, J Strength Cond Res 25(9):2559-64 -- RCT n=24 sedentary adults, 7 abdominal exercises 2x10, 5 d/week, 6 weeks: no change in body fat, android fat, waist or abdominal skinfold; curl-up endurance improved
  - "https://pubmed.ncbi.nlm.nih.gov/26752509/"  # Steffens D et al. 2016, JAMA Intern Med 176(2):199-208 -- 21 RCTs, 30,850 people: exercise plus education cuts LBP episodes (RR 0.55, 0.41-0.74, moderate quality); exercise alone RR 0.65 (0.50-0.86, low to very low); education alone, back belts, insoles no effect
  - "https://pubmed.ncbi.nlm.nih.gov/26742533/"  # Saragiotto BT et al. 2016, Cochrane CD012004 -- 29 trials n=2431, chronic non-specific LBP: motor control exercise (deep trunk activation) is not clinically more effective than other exercise; choice should follow preference, cost and safety
  - "https://pubmed.ncbi.nlm.nih.gov/27317910/"  # Kim CR, Park DK, Lee ST, Ryu JS 2016, PM R 8(10):979-989 -- n=10 healthy men, curl-up, dead bug, superman, bird dog each graded over 5 levels: trunk EMG rises with level. Dead bug has an EMG progression, not a training trial
  - "exercise/ideal-pilates-controlled-movement-037"  # within-warehouse: the connection side; controlled movement, not holds
  - "exercise/ideal-crossfit-functional-036"  # within-warehouse: functional = work capacity
  - "exercise/emg-not-hypertrophy-proxy-013"  # within-warehouse: why the EMG rows here prove activation, not growth
  - "exercise/caution-severity-ladder-056"  # within-warehouse: back history / pain routes through the ladder
  - "exercise/harm-route-boundary-031"  # within-warehouse: red-flag back pain is routed
  - "exercise/low-back-pain-lifter-loading-059"  # within-warehouse (v37): where a back-pain picture sits on the 056 ladder and the modify-first order; the low-back core_rules here defer to it (linked v40)
  - "framework:GRADE -- trunk-training effects rest on two meta-analyses of many small, low-to-moderate-quality controlled trials (PEDro 4-5) in athletes, not in recreational lifters. The compound-lift coverage claim is EMG (activation, not adaptation; 013). Carry evidence is one biomechanical model and one 7-week RCT of n=30. No trial tests trunk-accessory dose, session placement, crunch volume, the dead bug or anti-rotation presses as training in lifters."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
core_rules:
  - rule: compounds-load-the-back-side
    when: user squats or deadlifts heavy (about 80% 1RM) at least weekly
    action: do not add back-extensor or instability drills as core work for stability reasons; the trunk accessory slot goes to what the lifts do not load, abdominal flexion / anti-extension and lateral (carry) work
    number: none
    number_kind: none
    basis: Hamlyn 2007; Martuscello 2013; Behm 2010
    basis_grade: C
  - rule: accessory-not-lever
    when: user expects core work to raise squat, deadlift, sprint or sport performance
    action: say trunk training reliably builds trunk strength and endurance, but its carry-over to lifts and performance in trained people is small; keep it an accessory, not a priority slot
    number: trunk strength SMD 1.07; performance SMD 0 to 0.71; correlation r at most 0.18
    number_kind: evidence
    basis: Prieske 2016; Saeterbakken 2022; Reed 2012
    basis_grade: B
  - rule: stable-ground-first
    when: an exercise choice offers an unstable surface (ball, BOSU, wobble board) for a trained lifter
    action: prefer ground-based free weights and stable-surface trunk work; unstable variants only as low-load variety or rehab
    number: none
    number_kind: none
    basis: Behm 2010 (CSEP position stand)
    basis_grade: B
  - rule: carries-fill-the-frontal-plane
    when: goal is functional or connected-body and the programme has no carries
    action: add a carry (farmer's walk or one-sided suitcase carry) as an accessory; it trains a lateral trunk demand the lifts do not; expect it to sit alongside, not beat, traditional lifting
    number: none
    number_kind: none
    basis: McGill 2009; Winwood 2015
    basis_grade: C
  - rule: yoke-is-high-spine-load
    when: injury_history names the low back at history-recent or any current rung (056)
    action: exclude heavy yoke carries; keep farmer and suitcase carries at a load that holds a neutral trunk; current back pain routes per 056 before any carry
    number: none
    number_kind: none
    basis: McGill 2009; exercise/caution-severity-ladder-056
    basis_grade: C
  - rule: crunch-allowed-unless-pathology
    when: user asks if crunches or sit-ups harm the spine
    action: healthy spine -> loaded flexion is allowed; known disc herniation or flexion-intolerant back pain -> no dynamic flexion, use anti-extension holds and carries, route pain per 056
    number: none
    number_kind: none
    basis: Contreras 2011 (review of Callaghan 2001 and others)
    basis_grade: D
  - rule: flexion-volume-cap
    when: programme includes dynamic trunk flexion (crunch, cable crunch, sit-up, leg raise)
    action: load it into 6-15 reps; cap about 60 flexion reps per session; at least 48 h between dynamic flexion sessions
    number: 6-15 reps; at most about 60 reps per session; at least 48 h apart
    number_kind: expert
    basis: Contreras 2011
    basis_grade: D
  - rule: no-flexion-right-after-waking
    when: session starts within about 1 h of getting up
    action: move dynamic trunk flexion later or swap it for a hold
    number: about 1 h (2 h conservative)
    number_kind: expert
    basis: Contreras 2011 (disc hydration mechanism)
    basis_grade: D
  - rule: weekly-dose
    when: placing trunk accessories in a week
    action: two to three trunk accessory exposures a week, two to four hard sets each, inside the session; keep it going beyond about 18 sessions before judging it
    number: 2-3 exposures; 2-4 sets; more than 18 sessions
    number_kind: product
    basis: Saeterbakken 2022 (the 18-session split is evidence; the per-week numbers are a plan constant)
    basis_grade: D
  - rule: place-after-main-lifts
    when: the same session has heavy squats, deadlifts or overhead presses
    action: put fatiguing trunk and carry work after the main lifts; light bracing or a dead bug as warm-up is fine
    number: none
    number_kind: product
    basis: no trial located (GAPS.md); trunk fatigue before heavy axial loading is avoided by convention
    basis_grade: D
  - rule: abs-do-not-spot-reduce
    when: user does ab work to lose belly fat
    action: say ab exercise builds the muscle and its endurance but does not cut belly fat; fat loss is the energy balance row
    number: none
    number_kind: none
    basis: Vispute 2011
    basis_grade: C
  - rule: no-special-deep-core
    when: user asks for transversus / deep-core activation work to prevent or fix back pain
    action: exercise in general prevents low-back-pain episodes; deep-core motor control work is not better than other exercise; pick by preference
    number: exercise plus education RR 0.55; exercise alone RR 0.65
    number_kind: evidence
    basis: Steffens 2016; Saragiotto 2016
    basis_grade: B
  - rule: dead-bug-and-anti-rotation-are-craft
    when: choosing between dead bug, bird dog, Pallof press, plank, side plank
    action: treat them as interchangeable trunk drills chosen by goal and tolerance; progress by level (longer lever, added load, slower controlled tempo); never claim one is proven superior
    number: none
    number_kind: none
    basis: Kim 2016 (EMG rises with level); no training trial located
    basis_grade: D
refraction_notes:
  - note: >
      THE BIG LIFTS ALREADY TRAIN THE BACK SIDE OF THE CORE. Heavy squats and
      deadlifts drive the spinal erectors and multifidus harder than planks,
      supermans, side bridges or ball drills, but they do not raise the
      obliques or lower abdominals. For a lifter who squats and pulls, the
      trunk accessory that adds something is abdominal and lateral work, not
      more back-extension or balance-board work. This is EMG -- activation,
      not measured growth (013).
    axis: training_status
    grade: C
  - note: >
      CORE WORK MAKES THE CORE STRONGER, NOT THE SQUAT. In trained people,
      trunk strength barely correlates with performance, and trunk training
      gives large trunk-strength gains but small-to-moderate performance
      gains, in low-quality trials mostly in athletes. Sell it as trunk
      capacity and back resilience, never as a lever on the big lifts.
    grade: B
  - note: >
      "CONNECTED BODY" IS TWO THINGS HERE. If the user means trunk and limbs
      moving as one controlled sequence, that is the Pilates side (037):
      controlled-tempo, full-range movement with breath -- the dead bug done
      slowly with the breath paired to the limb fits that marker. If they
      mean transferring force through the trunk under load, carries are the
      closest tool: a farmer's or one-sided suitcase carry makes the trunk
      hold the pelvis level against a load the hips alone cannot. Ask which,
      once; default to offering both.
    axis: primary_goal
    grade: D
  - note: >
      CRUNCHES ARE NOT A SPINE HAZARD FOR A HEALTHY BACK. The fear comes from
      pig spine segments bent tens of thousands of times in a machine. No
      human study shows a low-volume, loaded flexion routine harms a healthy
      spine. The caveats that do apply: a known disc herniation or back pain
      that flares with bending -> no dynamic flexion; keep flexion sets
      loaded and short rather than hundreds of reps; skip it in the first
      hour after waking. The numbers are one review's advice, not trial
      results.
    grade: D
  - note: >
      CARRIES MATCH, THEY DO NOT REPLACE. Seven weeks of strongman training
      including carries matched biomechanically equal traditional training
      in trained rugby players, with small edges each way. Add carries for
      the lateral trunk demand and grip; do not swap them for squats or
      deadlifts. The heavy yoke is the highest spine load measured among the
      strongman events -- keep it away from a recent or painful back.
    grade: C
  - note: >
      DOSE AND PLACEMENT ARE THE PLAN'S RULE. Two to three trunk exposures a
      week, a few hard sets, after the main lifts, judged over more than
      about 18 sessions: only the 18-session split comes from a
      meta-analysis subgroup (athletes); the rest is a plan constant. Say so.
    grade: D
claim: >
  For a trained lifter, heavy free-weight squats and deadlifts already load
  the spinal erectors and multifidus more than planks, supermans, side
  bridges or unstable-surface drills, though they do not load the
  abdominals more. Dedicated trunk training builds trunk strength and
  endurance (large effects) but transfers only small-to-moderate gains to
  strength, power or sport performance in trained people, from low-quality
  trials mostly in athletes. Unstable surfaces cut force, power and range
  and are not a primary mode. Loaded carries put a lateral, pelvis-holding
  demand on the trunk that lifting does not, and a short strongman trial
  matched traditional training rather than beating it; the heavy yoke loads
  the spine most. Abdominal exercise does not reduce belly fat. Exercise in
  general prevents low-back-pain episodes, and deep-core motor control work
  is not better than other exercise. Loaded flexion (crunch variants) has
  no human evidence of harm in a healthy spine; the concern is in vitro, and
  existing disc pathology or flexion-intolerant pain is the contraindication.
  Dose, session placement, the flexion-volume cap and the dead-bug and
  anti-rotation choices have no training trial in lifters and are held as
  expert or product rules.
reasoning: >
  Two meta-analyses carry the transfer finding: Prieske 2016 (trained 16-44
  year olds, read at full text) and Saeterbakken 2022 (athletes, active
  controls); both rate their trials low-to-moderate, and Reed 2012 reaches
  the same "marginal" verdict narratively, so the trunk-strength gain is
  graded high and the transfer is spoken as small. The coverage claim is
  EMG (Martuscello 2013 systematic review, Hamlyn 2007 at 80% 1RM), which
  shows activation only (013), so it is held one step lower. Behm 2010 is a
  society position stand on instability. Carries rest on McGill 2009's
  spine model (n small, no training outcome) and Winwood 2015's 7-week RCT
  (n=30 trained), plus Hindle 2019 noting that carry adaptations are
  unstudied. The crunch rule leans on Contreras & Schoenfeld 2011, a
  narrative review read at full text whose numeric limits are the authors'
  recommendations, not results; Callaghan & McGill 2001 is the in vitro
  source of the concern. Steffens 2016 and Saragiotto 2016 are high-quality
  pooled clinical rows on back pain. The dead bug has only an EMG
  progression (Kim 2016); no Pallof-press or anti-rotation training trial
  was located. contested is yes because the flexion-safety question is a
  live practitioner dispute (McGill vs Contreras & Schoenfeld) with no in
  vivo human trial on either side. injury_history is hard with
  block_specifics: without knowing whether the user has a disc or
  flexion-intolerant back, the flexion green-light and carry loading are
  withheld and 056 decides.
---

# exercise/core-functional-accessory-carry-081 -- 코어·기능성 보조 운동 (캐리, 안티로테이션, 데드버그, 크런치)

**한 줄 그림:** 스쿼트·데드리프트를 무겁게 하는 사람에게 코어 운동은 큰 운동을 키우는 지렛대가 아니다.
몸통 자체를 튼튼하게 하는 보조 운동이고, 큰 운동이 못 채우는 복근·옆구리(캐리) 쪽을 채운다.

## Core rules (engine-readable summary)

| Rule | Action | Number (kind) |
|---|---|---|
| compounds-load-the-back-side | no extra back-extensor / balance-board "core"; spend the slot on abs and carries | -- |
| accessory-not-lever | trunk strength up a lot, performance up a little | SMD 1.07 vs 0-0.71 (evidence) |
| stable-ground-first | unstable surfaces only as variety or rehab | -- |
| carries-fill-the-frontal-plane | add farmer / suitcase carry for functional or connected-body goals | -- |
| yoke-is-high-spine-load | no heavy yoke with recent or current back caution (056) | -- |
| crunch-allowed-unless-pathology | healthy back: loaded flexion fine; disc / flexion-intolerant pain: no | -- |
| flexion-volume-cap | 6-15 loaded reps, about 60 per session max, 48 h apart | (expert) |
| no-flexion-right-after-waking | no dynamic flexion in the first hour after rising | about 1 h (expert) |
| weekly-dose | 2-3 exposures, 2-4 hard sets, judge after 18+ sessions | (product; 18 sessions from a subgroup) |
| place-after-main-lifts | fatiguing trunk and carry work after the big lifts | (product) |
| abs-do-not-spot-reduce | ab work does not cut belly fat | -- |
| no-special-deep-core | exercise prevents back-pain episodes; deep-core drills not better | RR 0.55 / 0.65 (evidence) |
| dead-bug-and-anti-rotation-are-craft | interchangeable drills, progressed by level | -- |

## 한국어 요약 (답변용)

- 스쿼트·데드리프트를 무겁게 하고 있으면 허리 뒤쪽 근육(척추기립근·다열근)은 이미 플랭크나 슈퍼맨,
  짐볼 운동보다 더 많이 쓰고 있다. 다만 복근·옆구리는 더 쓰지 않는다. 그래서 코어 보조 운동 자리는
  허리 뒤쪽 운동이나 불안정한 바닥 운동보다 복근 운동과 캐리에 쓰는 게 낫다. 이건 근활성도(EMG)
  자료라서 근육이 더 큰다는 뜻까지는 아니다.
- 코어 운동을 하면 몸통 근력·지구력은 확실히 는다. 하지만 훈련된 사람에서 스쿼트·점프·스프린트
  같은 수행으로 넘어가는 효과는 작다. 큰 운동을 올리는 지렛대가 아니라 보조 운동으로 둔다.
- 짐볼·보수볼 같은 불안정한 바닥은 힘·파워·가동범위를 떨어뜨린다. 주된 운동으로 쓰지 않고 가벼운
  변화나 재활용으로만 쓴다.
- 파머스 워크나 한 손 수트케이스 캐리는 들기 운동이 못 주는 옆 방향 버티기를 몸통에 준다. 7주
  연구에서 캐리가 들어간 스트롱맨 훈련은 일반 웨이트 훈련과 비슷했고 더 낫지는 않았다. 스쿼트·
  데드리프트를 대신하지 말고 옆에 더한다. 요크 캐리는 척추 부하가 가장 컸으니 최근 허리를 다쳤거나
  지금 아프면 빼고, 아픈 경우는 주의 단계(056)를 먼저 따른다.
- '연결된 몸'은 두 뜻일 수 있다. 몸통과 팔다리를 하나의 통제된 흐름으로 움직이는 쪽이면 필라테스
  쪽(037)이다. 숨과 맞춰 천천히 하는 데드버그가 여기에 맞는다. 무게를 몸통으로 버티며 전달하는
  쪽이면 캐리가 가장 가깝다. 한 번 물어보고, 모르면 둘 다 제안한다.
- 허리가 건강하면 크런치가 척추를 망친다는 근거는 없다. 그 걱정은 돼지 척추 조각을 기계로 수만 번
  굽힌 실험에서 나왔다. 디스크 탈출증이 있거나 굽히면 아픈 허리라면 굽히는 복근 운동은 빼고 버티기와
  캐리로 바꾼다.
- 굽히는 복근 운동은 무게를 더해 6~15회로 하고, 한 번에 60회 안팎을 넘기지 않고, 48시간 이상
  띄운다. 일어나서 한 시간 안에는 하지 않는다. 이 숫자들은 한 리뷰 저자들의 권고이지 실험 결과가
  아니다.
- 주 2~3번, 한 번에 힘든 세트 2~4개, 큰 운동 뒤에 둔다. 가벼운 브레이싱이나 데드버그는 준비 운동으로
  앞에 해도 된다. 18회 넘게 해 보고 판단한다. 18회 기준만 메타분석(운동선수 하위분석)에서 나왔고
  나머지는 계획의 규칙이다.
- 복근 운동을 해도 뱃살은 빠지지 않는다. 근육과 지구력이 늘 뿐이다.
- 허리 통증 예방에는 운동 자체가 효과가 있다(운동+교육으로 허리 통증 발생 위험 약 45% 감소). 깊은
  코어만 따로 깨우는 운동이 다른 운동보다 낫지는 않다. 데드버그·버드독·팔로프 프레스·플랭크·사이드
  플랭크는 목표와 몸 상태에 맞춰 고르는 비슷한 도구이고, 어느 하나가 더 낫다고 증명된 건 없다.
