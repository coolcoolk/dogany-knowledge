---
# Main-lift cue sprint 2026-10-08. The
# engine-readable half: for each main lift, the setup, two or three active
# execution cues (English and Korean, each tagged external or internal focus),
# and the one common fault the coach looks for, with its fix. Plus cue_rules
# that pick which cue to say on which set (by load, goal and caution site)
# from 745's focus findings. A coaching table, not a primary finding: every
# cue is practitioner consensus (NSCA-style technique teaching, the Myer 2014
# back-squat assessment) unless a basis names a study; each row carries its
# own basis_grade.
#
# lift_cues plug into existing vocabulary: 056 rungs, 711 squat_knee_rules,
# 093 press-angle rules, 064 bench-grip-max-1.5-biacromial, 059 low-back
# modify_order, 076 machine setup cues. Caution-site rules in those items
# OVERRIDE a cue here (they decide range, variant and load; this row only
# words the set).
#
# Read depth: Myer 2014 and Noteboom 2024 read in full text (PMC / Frontiers,
# 2026-10-08); Green & Comfort 2007, Fenwick 2009, Sperandei 2009, Andersen
# 2014, Saeterbakken & Fimland 2013, Saeterbakken 2011, Blazek 2019 and
# Swinton 2012 only as search-index renderings of their abstracts or records.
id: exercise/main-lift-cues-746
domain: exercise
grade: D (cue wording, the cue set per lift and every fault choice are practitioner consensus; the focus-type rule rests on 745's C rows; the bench grip and scapula cue on C-level model data at a light load in 10 lifters; the row, pulldown and press variant notes on C-level EMG or spine-load lab data; no trial tests any listed cue set against another for strength, growth or injury)
lane: "@gym-craft"
locale: universal
as_of: 2007-2024
contested: no
sources:
  - "exercise/attentional-focus-cue-evidence-745"  # within-warehouse: external on heavy sets, internal allowed on light growth sets, one cue, same cue on test days, external-superiority not settled (C / B)
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC4262933/"  # Myer GD, Kushner AM, Brent JL, Schoenfeld BJ, Hugentobler J, Lloyd RS, Vermeil A, Chu DA, Harbin J, McGill SM 2014, Strength Cond J 36(6):4-27 -- full text read: Back Squat Assessment, 10 criteria (head neutral, gaze forward; chest up, scapulae retracted; trunk parallel to tibia with slight lumbar lordosis; hips level; knee does not cross medial malleolus (no valgus); tibia parallel to trunk, whole foot on floor; controlled hip-hinge descent; thighs at least parallel; shoulders and hips rise at the same speed); stance heels about shoulder width, toes forward or out up to 10 deg; inhale about 80% and hold before the descent to raise intra-abdominal pressure. Expert commentary, no outcome data
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC11224528/"  # Noteboom L, Belli I, Hoozemans MJM, Seth A, Veeger HEJ, Van Der Helm FCT 2024, Front Physiol 15:1393235 -- full text read: 10 experienced lifters, 21 bench techniques at a 16 kg bar, OpenSim model: widening grip from 1.5 to 2 bi-acromial widths raised acromioclavicular compression; 1 BAW and 45 deg shoulder abduction raised glenohumeral superior shear; scapular retraction (squeeze the blades, slight arch) lowered total glenohumeral force and posterior shear; mediolateral bar force varied a lot between lifters and changed shoulder loads
  - "https://lida.sport-iat.de/ta/Record/4013441"  # Green CM, Comfort P 2007, Strength Cond J 29(5):10-14 -- narrative review: grip wider than 1.5 bi-acromial width linked to shoulder injury; narrowing costs about 5% 1RM. Record as rendered by the search index (also in 064)
  - "https://pubmed.ncbi.nlm.nih.gov/19197209/"  # Fenwick CMJ, Brown SHM, McGill SM 2009, J Strength Cond Res 23(5):1408-1417 -- inverted row, standing bent-over row, standing one-arm cable row: bent-over row gave the largest lumbar spine load (and highest spine stiffness); inverted row the highest lat and upper-back activation with lower spine load; one-arm cable row challenged trunk rotation. Abstract as rendered by the search index
  - "https://pubmed.ncbi.nlm.nih.gov/19855327/"  # Sperandei S, Barros MAP, Silveira-Junior PCS, Oliveira CG 2009, J Strength Cond Res 23(7):2033-2038 -- 24 trained men, 80% 1RM, behind-neck vs front-of-neck vs V-bar pulldown: front pulldown recommended; no advantage to behind-neck. Abstract as rendered by the search index
  - "https://sci-sport.com/en/does-grip-width-influence-muscle-activity-during-lat-pull-down-106/"  # Andersen V, Fimland MS, Wiik E, Skoglund A, Saeterbakken AH 2014, J Strength Cond Res 28(4):1135-1142 -- 15 men, pronated grips 1, 1.5, 2 x bi-acromial: similar concentric lat EMG across grips; medium grip a reasonable default. Secondary summary as rendered by the search index
  - "https://pubmed.ncbi.nlm.nih.gov/19826307/"  # Snyder BJ, Leech JR 2009, J Strength Cond Res 23(8):2204-2209 -- instruction to emphasise the lats raised lat EMG on the pulldown (also in 745)
  - "https://www.bisp-surf.de/Record/PU201311007613"  # Saeterbakken AH, Fimland MS 2013, J Strength Cond Res 27(7):1824-1831 -- 15 trained men, seated vs standing, barbell vs dumbbell overhead press: standing raised deltoid (posterior about 25%) activity over seated; dumbbells raised anterior deltoid over barbell. Record as rendered by the search index
  - "https://app.cristin.no/results/show.jsf?id=741530"  # Saeterbakken AH, van den Tillaar R, Fimland MS 2011, J Sports Sci 29(5):533-538 -- 12 resistance-trained men, Smith, barbell and dumbbell chest press: dumbbell 1RM 17% below barbell and 14% below Smith; pectoralis major and anterior deltoid EMG did not differ between the three. Record / abstract as rendered by the search index
  - "https://www.termedia.pl/Systematic-review-of-intra-abdominal-and-intrathoracic-r-npressures-initiated-by-the-Valsalva-manoeuvre-during-r-nhigh-intensity-resistance-exercises,78,38043,0,1.html"  # Blazek D, Stastny P, Maszczyk A, Krawczyk M, Matykiewicz P, Petr M 2019, Biol Sport 36(4):373-386 -- systematic review, 16 studies: intra-abdominal pressure highest in squats (over 200 mmHg), then deadlift, row, leg press (161-176), lowest in bench press (79); intrathoracic highest in leg press and deadlift; bench press and row suggested for beginners and people with hypertension. Abstract as rendered by the search index
  - "https://research.bond.edu.au/en/publications/a-biomechanical-comparison-of-the-traditional-squat-powerlifting-/"  # Swinton PA et al. 2012, J Strength Cond Res 26(7):1805-1816 -- box squat mechanics (via 710)
  - "exercise/squat-knee-rules-711"  # within-warehouse: box height, step-back, tempo at a knee caution site; knees-forward-allowed
  - "exercise/squat-stance-box-tempo-knee-load-evidence-710"  # within-warehouse: stance width by response, foot angle 0-30 deg not a knee lever
  - "exercise/knee-friendly-squat-depth-variants-058"  # within-warehouse: knees-behind-toes is not a default cue
  - "exercise/low-back-pain-lifter-loading-059"  # within-warehouse: lumbar flexion while lifting not a back-pain risk factor (Saraceni 2020, C); technique cues are performance and load-control cues
  - "exercise/shoulder-pressing-selection-cuff-work-064"  # within-warehouse: bench-grip-max-1.5-biacromial and scapular retraction
  - "exercise/press-angle-rules-093"  # within-warehouse: incline angle cap and shoulder rules
  - "exercise/incline-press-angle-upper-chest-shoulder-evidence-092"  # within-warehouse: incline angle evidence
  - "exercise/machine-first-selection-rules-076"  # within-warehouse: machine setup and path cues are still given
  - "exercise/caution-severity-ladder-056"  # within-warehouse: rungs
  - "exercise/harm-route-boundary-031"  # within-warehouse: pain and red flags are routed, not coached
  - "a research sprint 2026-10-08: setup + execution cues for main lifts, 2-3 active cues and one common fault each, internal vs external focus evidence, engine-readable lift_cues"
  - "framework:GRADE -- cue sets and faults are practitioner consensus (expert commentary, technique manuals), D; the focus rule borrows 745's C; joint-load and EMG notes are small healthy-lifter lab or model data, C, used only to pick between cue variants, never as injury-prevention claims."
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
      unknown_policy: hedge
    - key: cardiovascular_condition
      type: categorical
      role: hard
      unknown_policy: hedge
constants:
  cues_per_set_max: 1             # product: one execution cue said per set (745 -- an instructed focus beats none; more than one splits attention)
  new_cues_per_session_max: 2     # product: at most two new cues per lift per session; a cue is kept until the fault is gone for a session
  heavy_set_pct_1rm: 80           # from 745 (Calatayud 2016): above about 80% 1RM a muscle cue no longer raised that muscle's activity; also used for RIR 0-2 top sets
  light_set_pct_1rm: 60           # from 745 (Calatayud 2016): muscle cue raised target EMG at 20-60% 1RM
  cue_switch_sessions: 2          # product: sessions a cue is tried before switching to the other focus wording
  bench_grip_max_biacromial: 1.5  # from 064 / Noteboom 2024: grip no wider than 1.5 bi-acromial widths
  bench_elbow_deg: [45, 75]       # product inside Noteboom 2024's tested 45-90 deg: below 45 with a narrow grip raised superior shear, 90 with a wide grip is the flared fault
  squat_toe_out_deg: [0, 30]      # from 710 (Escamilla 2001, Lorenzetti 2018): foot angle is a tracking choice, not a knee-load lever; Myer 2014 teaches 0-10 to beginners
  rdl_knee_bend_deg: [15, 25]     # product: soft knee, fixed through the rep
lift_cues:
  - lift: bench_press
    setup: eyes under the bar; feet flat and planted; shoulder blades pulled back and down into the bench with a small arch; grip no wider than bench_grip_max_biacromial, forearms vertical at the bottom
    setup_ko: 눈이 바 바로 아래; 발바닥 전체를 바닥에 고정; 견갑을 뒤·아래로 모아 벤치에 박고 허리는 살짝 아치; 그립은 어깨너비의 1.5배 이내, 바닥 지점에서 전완이 수직
    cue_1: bend the bar (pull it apart) to lock the shoulder blades
    cue_1_ko: 바를 양쪽으로 찢듯이 쥐어 견갑 고정
    cue_1_focus: external
    cue_2: touch the lower chest with the elbows about 45-75 degrees from the body
    cue_2_ko: 팔꿈치는 몸통에서 45-75도, 가슴 아래쪽에 터치
    cue_2_focus: internal
    cue_3: drive the bar back up over the shoulders, push yourself away from the bar
    cue_3_ko: 바를 어깨 위쪽으로 밀어내며 몸을 바에서 밀어낸다
    cue_3_focus: external
    heavy_cue: cue_3
    fault: wide grip with elbows flared to 90 degrees, bar lowered toward the neck
    fault_ko: 넓은 그립에 팔꿈치를 90도로 벌리고 바를 목 쪽으로 내림
    fault_fix: grip in to bench_grip_max_biacromial, tuck to bench_elbow_deg, touch lower on the chest; re-set the shoulder blades before the set
    basis: Noteboom 2024; Green & Comfort 2007; 064
    basis_grade: C
  - lift: incline_barbell_press
    setup: bench at the 093 low incline (chest slot, never above its cap); hips and upper back on the pad; shoulder blades back and down; same grip rule as the bench
    setup_ko: 벤치 각도는 093의 낮은 인클라인(가슴 슬롯 상한 이하); 엉덩이와 등 상부를 패드에 붙임; 견갑 뒤·아래; 그립 규칙은 벤치와 같음
    cue_1: lower the bar to just under the collarbone
    cue_1_ko: 바를 쇄골 바로 아래로 내린다
    cue_1_focus: external
    cue_2: keep the hips on the seat, drive through the feet
    cue_2_ko: 엉덩이는 시트에 붙인 채 발로 바닥을 민다
    cue_2_focus: internal
    cue_3: press up and slightly back so the bar finishes over the shoulders
    cue_3_ko: 위로, 살짝 뒤로 밀어 어깨 위에서 마무리
    cue_3_focus: external
    heavy_cue: cue_3
    fault: hips lift off the seat (or the bench is set steep), turning it into a shoulder press
    fault_ko: 엉덩이가 들리거나 벤치가 너무 세워져 숄더프레스가 됨
    fault_fix: lower the angle to the 093 low incline, reduce load until the hips stay down
    basis: 093; 092
    basis_grade: D
  - lift: incline_dumbbell_press
    setup: sit with the dumbbells on the thighs, kick them up one knee at a time as you lie back; shoulder blades back and down; palms forward or turned slightly in
    setup_ko: 덤벨을 허벅지에 올리고 눕는 동시에 무릎으로 하나씩 차올림; 견갑 뒤·아래; 손바닥은 정면 또는 약간 안쪽
    cue_1: elbows stay under the wrists all the way down
    cue_1_ko: 내려가는 내내 팔꿈치가 손목 바로 아래
    cue_1_focus: internal
    cue_2: lower until the dumbbells are about level with the chest, not as deep as you can go
    cue_2_ko: 덤벨이 가슴 높이쯤 올 때까지만 내린다(끝까지 떨어뜨리지 않음)
    cue_2_focus: external
    cue_3: press the dumbbells up and slightly together
    cue_3_ko: 덤벨을 위로, 살짝 서로 모으듯 밀어 올린다
    cue_3_focus: external
    heavy_cue: cue_3
    fault: dumbbells drift wide and sink far below the chest, one side lagging
    fault_ko: 덤벨이 바깥으로 벌어지며 가슴 아래로 깊게 처지고 한쪽이 늦음
    fault_fix: lighter pair (dumbbell 1RM runs about 17% below the barbell's), stop at chest level, the weaker side sets the reps
    basis: Saeterbakken 2011; 093 unilateral-caution-decouple
    basis_grade: D
  - lift: back_squat
    setup: bar on the upper back with the upper back squeezed tight; feet about shoulder width, toes out squat_toe_out_deg as the knees track; big breath held and brace before each rep
    setup_ko: 바를 등 상부에 올리고 등 위쪽을 조임; 발은 어깨너비쯤, 발끝은 무릎이 따라갈 만큼 0-30도 바깥; 매 반복 전 크게 숨을 들이마시고 배에 힘을 줘 고정
    cue_1: spread the floor, push the floor away
    cue_1_ko: 바닥을 양옆으로 벌리듯, 바닥을 밀어낸다
    cue_1_focus: external
    cue_2: knees travel in line with the toes
    cue_2_ko: 무릎은 발끝 방향으로
    cue_2_focus: internal
    cue_3: chest and hips rise together out of the bottom
    cue_3_ko: 바닥에서 가슴과 엉덩이가 같이 올라온다
    cue_3_focus: internal
    heavy_cue: cue_1
    fault: hips shoot up first out of the bottom and the squat turns into a good morning
    fault_ko: 바닥에서 엉덩이만 먼저 솟아 굿모닝처럼 됨
    fault_fix: reduce load, cue_3 on warm-ups, brace before the descent; if it persists at light loads, a pause at the bottom
    basis: Myer 2014
    basis_grade: D
  - lift: box_squat
    setup: box height from 711 (start_range_box) or the user's goal depth; stance a little wider than the free squat; brace as in the back squat
    setup_ko: 박스 높이는 711 기준 또는 목표 깊이; 스탠스는 일반 스쿼트보다 조금 넓게; 백스쿼트처럼 숨 참고 복압
    cue_1: sit back to the box, shins near vertical
    cue_1_ko: 정강이를 세운 채 엉덩이를 뒤로 보내 박스에 앉는다
    cue_1_focus: external
    cue_2: touch the box and stay tight, no relaxing onto it
    cue_2_ko: 박스에 닿아도 힘을 풀지 않는다
    cue_2_focus: internal
    cue_3: drive up off the box by pushing the floor away
    cue_3_ko: 바닥을 밀어내며 박스에서 일어난다
    cue_3_focus: external
    heavy_cue: cue_3
    fault: dropping onto the box and rocking back to start the rep
    fault_ko: 박스에 털썩 앉아 몸을 뒤로 젖혔다가 반동으로 일어남
    fault_fix: lighter load, 2-3 s descent, touch-and-go or a 1-2 s tight pause (711 constants)
    basis: 711; Swinton 2012 via 710
    basis_grade: D
  - lift: romanian_deadlift
    setup: start standing with the bar (from a rack or a deadlift); soft knees at rdl_knee_bend_deg held fixed; bar against the thighs; brace
    setup_ko: 랙에서 들거나 데드리프트로 바를 들고 선 자세에서 시작; 무릎은 15-25도 살짝 굽혀 고정; 바는 허벅지에 붙임; 복압
    cue_1: push the hips back toward the wall behind you
    cue_1_ko: 엉덩이를 뒤쪽 벽에 닿게 하듯 뒤로 보낸다
    cue_1_focus: external
    cue_2: keep the bar sliding down the thighs, close to the legs
    cue_2_ko: 바가 허벅지를 타고 미끄러지듯 다리에 붙여 내린다
    cue_2_focus: external
    cue_3: stop where the hips stop moving back, then stand up by driving the hips forward
    cue_3_ko: 엉덩이가 더 뒤로 안 갈 때 멈추고, 엉덩이를 앞으로 밀며 일어선다
    cue_3_focus: internal
    heavy_cue: cue_1
    fault: chasing the floor -- the knees bend more and the back rounds to get the bar lower once the hips have stopped moving back
    fault_ko: 엉덩이가 멈춘 뒤에도 바를 더 내리려 무릎을 더 굽히거나 등을 말아 바닥을 쫓음
    fault_fix: end the range at the hips (cue_3), lighter load; a performance and range fault, not an injury verdict (059)
    basis: 059; practitioner consensus
    basis_grade: D
  - lift: overhead_press
    setup: standing, grip just outside the shoulders, bar resting on the front of the shoulders with forearms vertical; glutes and abs tight, ribs down
    setup_ko: 선 자세, 그립은 어깨보다 살짝 넓게, 바를 어깨 앞에 얹고 전완 수직; 엉덩이와 복부 조임, 갈비뼈를 내림
    cue_1: press the bar straight up, move the head back then through once the bar passes the forehead
    cue_1_ko: 바를 수직으로 밀고, 이마를 지나면 머리를 바 밑으로 넣는다
    cue_1_focus: external
    cue_2: squeeze the glutes and keep the ribs down
    cue_2_ko: 엉덩이를 조이고 갈비뼈를 내린다
    cue_2_focus: internal
    cue_3: finish with the bar over the middle of the foot, arms by the ears
    cue_3_ko: 바가 발 중앙 위, 팔이 귀 옆에서 끝난다
    cue_3_focus: external
    heavy_cue: cue_1
    fault: leaning far back from the lower back to get the bar up, turning it into an incline press
    fault_ko: 허리를 크게 젖혀 인클라인 프레스처럼 밀어 올림
    fault_fix: reduce load, cue_2; seated with back support if the lean persists (standing raises deltoid activity, seated removes the trunk demand)
    basis: Saeterbakken & Fimland 2013; 064
    basis_grade: D
  - lift: barbell_row
    setup: hinge as in the RDL to a torso angle you can hold still (about 45 degrees or lower); soft knees; bar hanging under the shoulders; brace
    setup_ko: RDL처럼 힌지해 버틸 수 있는 각도(약 45도 이하)로 상체 고정; 무릎 살짝; 바는 어깨 아래; 복압
    cue_1: pull the bar to the belly button
    cue_1_ko: 바를 배꼽 쪽으로 당긴다
    cue_1_focus: external
    cue_2: drive the elbows back toward the hips
    cue_2_ko: 팔꿈치를 엉덩이 쪽 뒤로 보낸다
    cue_2_focus: internal
    cue_3: torso stays still -- the back does the rowing, not the hips
    cue_3_ko: 상체는 고정, 엉덩이 반동 없이 등으로 당긴다
    cue_3_focus: internal
    heavy_cue: cue_1
    fault: the torso rises and jerks on every rep to swing the bar up
    fault_ko: 매 반복 상체가 올라오며 반동으로 바를 끌어올림
    fault_fix: reduce load until the torso holds still; with a low-back caution switch to a chest-supported or cable row (bent-over row carries the largest spine load of the rows tested)
    basis: Fenwick 2009; 059
    basis_grade: C
  - lift: seated_cable_row
    setup: feet on the plate, knees slightly bent; sit tall with the chest up; arms long at the start
    setup_ko: 발판에 발, 무릎 살짝 굽힘; 가슴을 세우고 바르게 앉음; 시작은 팔을 길게
    cue_1: pull the handle to the stomach
    cue_1_ko: 손잡이를 배 쪽으로 당긴다
    cue_1_focus: external
    cue_2: shoulder blades travel -- let them reach forward, then pull them back first
    cue_2_ko: 견갑이 앞으로 나갔다가 먼저 뒤로 모이며 당긴다
    cue_2_focus: internal
    cue_3: torso stays tall and still
    cue_3_ko: 상체는 세운 채 움직이지 않는다
    cue_3_focus: internal
    heavy_cue: cue_1
    fault: rocking the torso back and forth to move the stack
    fault_ko: 상체를 앞뒤로 흔들어 무게를 당김
    fault_fix: reduce the stack until the torso holds still; muscle cue (cue_2) on lighter growth sets
    basis: practitioner consensus; 745
    basis_grade: D
  - lift: lat_pulldown
    setup: thigh pad snug; grip about 1.5 times shoulder width (any of 1-2 times works); slight lean back; bar comes down in front of the face
    setup_ko: 허벅지 패드를 밀착; 그립은 어깨너비의 약 1.5배(1-2배 모두 가능); 상체를 살짝 뒤로; 바는 얼굴 앞으로 내린다
    cue_1: pull the bar to the top of the chest
    cue_1_ko: 바를 가슴 위쪽까지 당긴다
    cue_1_focus: external
    cue_2: drive the elbows down to the back pockets
    cue_2_ko: 팔꿈치를 뒷주머니 쪽으로 내린다
    cue_2_focus: internal
    cue_3: control the bar back up until the arms are long
    cue_3_ko: 팔이 다 펴질 때까지 천천히 올린다
    cue_3_focus: external
    heavy_cue: cue_1
    fault: leaning far back and swinging the torso to yank the bar down
    fault_ko: 상체를 크게 젖히며 반동으로 바를 끌어내림
    fault_fix: reduce the stack, keep the lean slight and fixed; cue_2 on lighter sets raises lat activity; never move to behind-the-neck
    basis: Snyder 2009; Sperandei 2009; Andersen 2014
    basis_grade: C
  - lift: leg_press
    setup: feet mid-platform about hip width; lower back and hips flat on the pad; set the machine stop (711 / 058 range at a knee caution site)
    setup_ko: 발은 발판 중앙에 골반너비쯤; 허리와 엉덩이를 패드에 붙임; 안전 멈춤 장치 설정(무릎 주의 시 711/058 범위)
    cue_1: push the platform away through the whole foot
    cue_1_ko: 발바닥 전체로 발판을 밀어낸다
    cue_1_focus: external
    cue_2: knees track in line with the toes
    cue_2_ko: 무릎은 발끝 방향으로
    cue_2_focus: internal
    cue_3: lower only until just before the hips start to curl off the pad
    cue_3_ko: 엉덩이가 패드에서 말려 뜨기 직전까지만 내린다
    cue_3_focus: external
    heavy_cue: cue_1
    fault: going so deep the hips curl off the pad at the bottom
    fault_ko: 너무 깊게 내려 바닥 지점에서 엉덩이가 패드에서 들림
    fault_fix: set the range at cue_3 (machine stop if available) and reduce load; a range-control fault, not an injury verdict (059)
    basis: 076; 059; practitioner consensus
    basis_grade: D
cue_rules:
  - rule: route-not-coach
    trigger: any site at 056 rung current-other or red-flag, or the user reports sharp or worsening pain on the lift
    action: no cue rule applies; triage first (031, 056); a cue is never offered as the fix for pain
    basis: exercise/harm-route-boundary-031
    basis_grade: D
  - rule: caution-rules-first
    trigger: a caution site at the knee, shoulder or low back (any lower rung)
    action: 711 (knee), 093 / 064 (shoulder) and 059 (back) set range, variant and load first; this row then words the set; a cue never reopens a range or variant those rules closed
    basis: exercise/caution-severity-ladder-056
    basis_grade: D
  - rule: setup-first-novice
    trigger: training_status novice, or the first session on a lift
    action: teach the setup line, then one execution cue per set; add a second cue only after the first fault is gone for a session (new_cues_per_session_max)
    basis: exercise/attentional-focus-cue-evidence-745
    basis_grade: D
  - rule: one-cue-per-set
    trigger: any working set
    action: say at most cues_per_set_max execution cue; pick the cue that targets the fault last seen, else the lift's heavy_cue
    basis: exercise/attentional-focus-cue-evidence-745
    basis_grade: C
  - rule: heavy-set-external
    trigger: a set at heavy_set_pct_1rm or above, a top set, or RIR 0-2 on a compound lift
    action: use the lift's heavy_cue (external wording); no muscle-squeeze cue on that set
    basis: exercise/attentional-focus-cue-evidence-745
    basis_grade: C
  - rule: growth-set-internal-allowed
    trigger: primary_goal muscle size or physique, and an accessory, machine or cable set at or below light_set_pct_1rm (or 10+ reps far from failure)
    action: an internal cue (the lift's internal cue or "squeeze the target muscle") may be used; present it as an option, not as proven better for growth on compound lifts
    basis: exercise/attentional-focus-cue-evidence-745
    basis_grade: C
  - rule: switch-wording
    trigger: the user says a cue does not help or confuses them, or the same fault is still there after cue_switch_sessions sessions
    action: switch to the other focus wording for that fault (external to internal or back); if both fail, lower the load before adding cues
    basis: exercise/attentional-focus-cue-evidence-745
    basis_grade: B
  - rule: same-cue-on-test-day
    trigger: a 1RM, rep-max or AMRAP test
    action: give the same single cue as the last test (or none) and log it with the result
    basis: exercise/attentional-focus-cue-evidence-745
    basis_grade: C
  - rule: fault-is-not-injury-verdict
    trigger: any fault is named to the user
    action: frame it as a performance, range or load-control fix; never say a rounded back, knees past the toes or a flared elbow caused or will cause an injury
    basis: exercise/low-back-pain-lifter-loading-059
    basis_grade: C
  - rule: brace-heavy-compounds
    trigger: squat, box squat, RDL, row, overhead press or leg press at a working load, and no cardiovascular_condition reported
    action: setup includes a big breath held and braced before the rep, released at or after the hardest part; the hold lasts one rep, not the set
    basis: Myer 2014; Blazek 2019
    basis_grade: D
  - rule: no-breath-hold-cardiac
    trigger: cardiovascular_condition reported (high blood pressure, heart disease)
    action: replace the breath-hold with breathe out through the effort; prefer bench, machine and row variants (lowest pressures in Blazek 2019); no heavy single-rep work without medical clearance (route per 031)
    basis: Blazek 2019
    basis_grade: C
  - rule: knees-forward-allowed
    trigger: any squat or leg press cue
    action: never use a knees-behind-the-toes cue as a default (058); knees track over the toes, wherever the toes are
    basis: exercise/knee-friendly-squat-depth-variants-058
    basis_grade: C
answer_rules:
  - question: what should I think about during a heavy squat (or bench)?
    answer: one outside cue per set -- push the floor away on the squat, push yourself away from the bar on the bench; outside cues gave slightly more force than muscle cues in small studies, but the difference is small, so if a cue does not help, try another
    basis: exercise/attentional-focus-cue-evidence-745
    basis_grade: C
  - question: does the mind-muscle connection work?
    answer: on lighter accessory sets, focusing on the muscle raises its activity and in one trial grew the biceps more; on heavy sets above about 80% of your max it stopped working, and there is no evidence it helps squats or presses grow more
    basis: exercise/attentional-focus-cue-evidence-745
    basis_grade: C
  - question: how wide should I grip the bench and where do my elbows go?
    answer: no wider than about one and a half times your shoulder width, forearms vertical at the bottom, elbows about 45-75 degrees from your body, shoulder blades pulled back; very wide with flared elbows loaded the shoulder joint more in a model study
    basis: exercise/shoulder-pressing-selection-cuff-work-064
    basis_grade: C
  - question: is behind-the-neck lat pulldown better?
    answer: no; pulling to the front of the chest worked the lats as well in trained men and is the easier position for the shoulder; grip width from one to two shoulder widths makes little difference
    basis: Sperandei 2009; Andersen 2014
    basis_grade: C
  - question: my back rounds on RDLs, will I get hurt?
    answer: a rounding back at the bottom usually means you went past the point your hips stopped moving back; stop there and use a load you control -- it is a range and load fix, and research does not show that some back rounding while lifting causes back pain
    basis: exercise/low-back-pain-lifter-loading-059
    basis_grade: C
never_say:
  - external cues are proven better than internal cues
  - mind-muscle connection doesn't work (or always works)
  - never let your knees pass your toes
  - rounding your back will injure you
  - behind-the-neck pulldowns or presses work the back (or shoulders) better
  - hold your breath through the whole set
  - this cue will prevent injury
refraction_notes:
  - note: >
      THE CUE LISTS ARE COACHING CONSENSUS. No trial compared one set of
      bench, squat or row cues against another for strength, growth or injury.
      The wording follows common technique teaching (the 2014 back-squat
      assessment, standard press and row coaching); the evidence decides only
      the focus type by load and the grip, row and pulldown variant notes.
    grade: D
  - note: >
      EXTERNAL ON HEAVY, INTERNAL ALLOWED ON LIGHT. Each lift lists a
      heavy_cue that is externally worded; muscle cues are kept for lighter
      sets where they still raise the target muscle's activity. This follows
      745's small-study evidence and is a default, not a proven method.
    grade: C
  - note: >
      FAULTS ARE PERFORMANCE FIXES. The one fault per lift is the most common
      thing that costs load control or range on that lift in coaching
      practice; it is not an injury predictor. Pain goes to the caution rules,
      not to a cue.
    grade: D
claim: >
  Every main lift gets a setup line, three short execution cues (English and
  Korean, each tagged external or internal) and one common fault with its
  fix: bench (bend the bar; elbows 45-75 deg, grip no wider than 1.5x
  shoulder width; push away from the bar -- fault wide flared elbows), incline
  barbell (bar under the collarbone, hips down -- fault hips up or bench too
  steep), incline dumbbell (elbows under wrists, stop at chest level -- fault
  dumbbells drifting wide and deep), back squat (spread the floor, knees over
  toes, chest and hips rise together -- fault hips shoot up), box squat (sit
  back, stay tight on the box -- fault dropping and rocking), RDL (hips back to
  the wall, bar on the thighs, stop where the hips stop -- fault chasing the
  floor), overhead press (straight up, head through, ribs down -- fault big
  lean back), barbell row (bar to the belly button, elbows to hips -- fault
  torso jerking), cable row (handle to stomach, blades travel -- fault
  rocking), lat pulldown (bar to the upper chest, elbows to the back pockets
  -- fault swinging), leg press (push through the whole foot, stop before the
  hips curl -- fault going too deep). One cue is said per set; heavy sets get
  the externally worded cue, light accessory growth sets may use a muscle
  cue; test days keep the same cue; a cue that does not help is switched;
  caution-site rules override any cue, and no fault is presented as an
  injury verdict. Brace with a held breath on heavy compounds unless a
  cardiovascular condition is reported.
reasoning: >
  The cue sets are practitioner craft, the @gym-craft lane's job; their only
  study-backed parts are the variant notes (Noteboom 2024 and Green & Comfort
  2007 for bench grip and scapula; Fenwick 2009 for the bent-over row's spine
  load; Sperandei 2009 and Andersen 2014 for pulldown position and grip;
  Saeterbakken 2011 and 2013 for dumbbell and standing-vs-seated presses;
  Blazek 2019 for which lifts raise body pressure most) and the focus-type
  rule from 745. Noteboom's data are a model at a 16 kg bar in 10 lifters, so
  the elbow band is a product range inside the tested angles, not a measured
  optimum. Myer 2014 is expert commentary; its squat criteria are used as cue
  wording, not as an injury screen. injury_history is hard because a caution
  site hands range and variant to 711 / 093 / 064 / 059 before any cue;
  cardiovascular_condition is hard because it removes the breath-hold cue
  (hedge when unknown, since the brace is standard for a healthy lifter);
  training_status decides how many cues are introduced at once; primary_goal
  decides whether an internal cue is offered on growth sets.
---

# exercise/main-lift-cues-746 -- 주요 운동별 세팅·실행 큐 2-3개와 흔한 실수 하나 (벤치·인클라인·스쿼트·RDL·OHP·로우·랫풀다운·레그프레스)

**한 줄 그림:** 세팅을 먼저 잡고, 세트마다 큐는 하나만 준다. 무거운 세트에서는 "바닥을 밀어내" 같은
바깥 큐를 쓰고, 가벼운 보조 운동에서는 근육 큐도 괜찮다. 실수는 기록과 범위를 위한 교정이지 부상
판정이 아니다.

## Lift cues (engine-readable)

| Lift | Cues (focus) | Heavy-set cue | Common fault -> fix | Grade |
|---|---|---|---|---|
| bench press | bend the bar (E); elbows 45-75 deg, lower chest (I); push away from the bar (E) | push away | wide grip + 90 deg flare -> grip <= 1.5x, tuck, touch lower | C |
| incline barbell | bar under collarbone (E); hips on seat (I); up and slightly back (E) | up and back | hips lift / bench too steep -> 093 angle, less load | D |
| incline dumbbell | elbows under wrists (I); stop at chest level (E); up and together (E) | up and together | DBs drift wide and deep -> lighter, stop at chest | D |
| back squat | spread / push the floor (E); knees over toes (I); chest and hips rise together (I) | push the floor | hips shoot up -> less load, pause | D |
| box squat | sit back, shins vertical (E); stay tight on box (I); drive off the box (E) | drive off | drop and rock -> 2-3 s down, tight pause | D |
| RDL | hips back to the wall (E); bar slides down thighs (E); stop where hips stop (I) | hips back | chasing the floor -> end range at the hips | D |
| overhead press | straight up, head through (E); glutes tight, ribs down (I); finish over mid-foot (E) | straight up | big lean back -> less load, seated if it persists | D |
| barbell row | bar to belly button (E); elbows to hips (I); torso still (I) | bar to belly button | torso jerks -> less load; back caution: supported row | C |
| seated cable row | handle to stomach (E); blades travel (I); torso still (I) | handle to stomach | rocking -> less stack | D |
| lat pulldown | bar to upper chest (E); elbows to back pockets (I); control up (E) | bar to chest | swinging -> less stack, slight fixed lean; never behind the neck | C |
| leg press | push through whole foot (E); knees over toes (I); stop before hips curl (E) | push away | hips curl off pad -> set range / stop, less load | D |

E = external focus, I = internal focus. Caution-site rules (711 knee, 093 / 064 shoulder, 059 back) set
range, variant and load before any cue.

## 한국어 요약 (답변용)

- 처음 배우는 운동은 세팅부터 잡고, 세트마다 큐는 하나만 준다. 첫 실수가 한 세션 동안 안 나오면 다음
  큐를 추가한다.
- 1RM의 80% 이상이나 마지막 무거운 세트에서는 바깥 큐를 쓴다. 스쿼트는 "바닥을 밀어내", 벤치는 "바에서
  몸을 밀어내", RDL은 "엉덩이를 뒤쪽 벽으로", 로우는 "바를 배꼽으로". 근육에 집중하는 큐는 그 무게에서
  효과가 없었다.
- 근육을 키우는 게 목표라면 가벼운 보조·머신·케이블 세트에서 "등을 쥐어짜", "팔꿈치를 뒷주머니로" 같은
  근육 큐를 써도 된다. 다만 스쿼트나 프레스에서 근육 큐가 더 키운다는 근거는 없다.
- 큐가 도움이 안 되거나 헷갈린다고 하면 두 세션 뒤 반대쪽 표현(바깥↔근육)으로 바꾼다. 둘 다 안 되면 큐를
  늘리지 말고 무게를 줄인다.
- 벤치프레스는 그립을 어깨너비의 1.5배 이내로, 팔꿈치는 몸통에서 45-75도, 견갑은 뒤·아래로 모은다. 아주
  넓은 그립에 팔꿈치를 90도로 벌리면 모델 연구에서 어깨 관절 부담이 커졌다.
- 랫풀다운은 바를 가슴 앞으로 당긴다. 목 뒤로 당겨도 등 근육이 더 쓰이지 않았다. 그립은 어깨너비의 1-2배
  어느 쪽이든 큰 차이가 없다.
- 바벨 로우는 비교한 로우 중 허리 부담이 가장 컸다. 허리가 신경 쓰이면 가슴을 대는 로우나 케이블 로우로
  바꾼다.
- 실수를 짚을 때는 "기록과 범위를 위한 교정"으로 말한다. "등이 굽으면 다친다", "무릎이 발끝을 넘으면
  안 된다"고 말하지 않는다. 통증이 있으면 큐가 아니라 주의 규칙(무릎 711, 어깨 093·064, 허리 059)으로 간다.
- 무거운 스쿼트·RDL·로우·OHP·레그프레스는 매 반복 전 숨을 크게 들이마시고 배에 힘을 줘 고정한다. 세트
  내내 참지 않고 한 반복 단위로 한다. 고혈압이나 심장 질환이 있으면 숨을 참지 말고 힘쓸 때
  내쉰다.
- 1RM이나 최대 반복 테스트 날에는 지난 테스트와 같은 큐를 주거나 아예 주지 않는다.
