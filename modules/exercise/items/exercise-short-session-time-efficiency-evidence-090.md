---
# Time-crunched session sprint 2026-10-07.
# The EVIDENCE half: what a lifter with fewer minutes than planned can cut
# without losing the session's training effect -- supersets, shorter rest,
# drop sets / rest-pause, warm-up and stretching, accessories vs sets, and how
# little a session can hold. Companion row: 091 (short_session_rules, the
# engine-readable rule set). Builds on 017 (rest acts through volume-load),
# 070 / 071 / 072 (set floors and the exercise-first trim order) and 080
# (warm-up ramp, its own time-cap cut order); does not restate them.
id: exercise/short-session-time-efficiency-evidence-090
domain: exercise
grade: B (supersets and drop sets keep volume and growth in less time, meta-analyses; rest acts through volume, 017); C (agonist-antagonist vs same-muscle pairing, three chronic superset trials, rest-pause, the minimum dose in trained lifters); D (skip-vs-shorten and every minute count)
lane: "@performance-lit"
locale: universal
as_of: 2010-2025
contested: no
sources:
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC12011898/"  # Zhang X, Weakley J, Li H, Li Z, Garcia-Ramos A 2025, Sports Med 55(4):953-975, PMID 39903375, doi 10.1007/s40279-025-02176-8 -- 19 studies / 313 (mostly trained men): supersets ~37% shorter, efficiency SMD 1.74 (0.46-3.01), volume load SMD 0.05 and reps -0.03 (n.s.); agonist-antagonist reps SMD +0.68; similar-biomechanical (same muscle) volume load SMD -1.08; lactate and RPE (SMD 0.77) higher; chronic (3 studies) 1RM SMD 0.10, hypertrophy -0.05, n.s.; GRADE mostly moderate
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC8449772/"  # Iversen VM, Norum M, Schoenfeld BJ, Fimland MS 2021, Sports Med 51(10):2079-2095, PMID 34125411 -- narrative review: prioritise bilateral multi-joint lifts (one leg press/squat, one pull, one push); >=4 weekly sets per muscle at 6-15RM as the minimum, 10+ when time allows; supersets, drop sets, rest-pause roughly halve time at equal volume; general warm-up and stretching low priority, keep the specific warm-up before heavy loads
  - "https://doi.org/10.1186/s40798-023-00620-5"  # Sodal LK, Kristiansen E, Larsen S, van den Tillaar R 2023, Sports Med Open 9(1):66, PMID 37523092 -- 6 studies / 142 (age 19-27): drop sets vs traditional sets, no significant hypertrophy difference; drop-set sessions took about one half to one third of the time
  - "https://pubmed.ncbi.nlm.nih.gov/28617715/"  # Prestes J et al. 2019, J Strength Cond Res 33 Suppl 1:S113-S121 -- 18 trained, 6 weeks, rest-pause vs 3 x 6 at 80% with 2 min rest: similar strength; thigh thickness 11% vs 1%; sessions ~35 vs ~57 min (per Iversen 2021)
  - "https://vuir.vu.edu.au/6797/"  # Robbins DW, Young WB, Behm DG, Payne WR 2010, J Strength Cond Res -- 15 trained men, 8 weeks, agonist-antagonist complex sets vs traditional sets: similar bench press / bench pull 1RM and power, complex sets more time-efficient (acute companion: same work in ~10 vs ~20 min, JSCR 24(7):1782-1789)
  - "https://pubmed.ncbi.nlm.nih.gov/31797219/"  # Androulakis-Korakakis P, Fisher JP, Steele J 2020, Sports Med 50(4):751-765 -- 6 studies, trained men: one set per exercise (2-9 weekly sets per pattern) of 6-12 reps at 70-85% 1RM, 2-3x/week, to failure, raised squat and bench 1RM over 8-12 weeks, suboptimally
  - "https://pubmed.ncbi.nlm.nih.gov/33629972/"  # Spiering BA, Mujika I, Sharp MA, Foulis SA 2021, J Strength Cond Res 35(5):1449-1458 -- narrative review: strength and size held up to 32 weeks with 1 session / week and 1 set per exercise if the load is kept (young); older adults ~2 sessions and 2-3 sets
  - "exercise/rest-interval-volume-load-017"  # within-warehouse: rest matters through reps kept; short rest only with sets added
  - "exercise/set-floor-by-experience-070"  # within-warehouse: >=2 sets per exercise, >=10 weekly sets trained, ~11 per-session point
  - "exercise/maintenance-vs-growth-volume-cut-071"  # within-warehouse: maintenance dose with the load kept
  - "exercise/set-floor-rule-072"  # within-warehouse: trim exercises before sets
  - "exercise/warmup-ramp-sets-heavy-compounds-080"  # within-warehouse: ramp optional before ~10RM work, keep it before heavy work
  - "exercise/acute-static-stretch-force-deficit-021"  # within-warehouse: long static stretching before lifting costs force
  - "framework:GRADE -- superset time and volume effects: one meta-analysis rated mostly moderate by its authors (B); drop sets: one small meta-analysis (B for no loss of growth, short trials, young adults). Chronic superset outcomes rest on three trials and the type split on acute data (C). Rest-pause one RCT n=18 (C). Minimum dose: one meta-analysis of six small trials in trained men plus a narrative review (C). Whether a short session beats a skipped one, and every minute count, has no trial (D)."
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
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: cardiovascular_condition
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [none]
refraction_notes:
  - note: >
      PAIR OPPOSITE OR DISTANT MUSCLES, NEVER THE SAME ONE. Agonist-antagonist
      supersets (row with press, curl with triceps extension) kept or raised
      reps; supersets of two exercises for the same muscle cut volume load by
      a large margin (SMD -1.08, Zhang 2025). Upper-with-lower pairs sat in
      between and did not differ significantly from traditional sets. Only the
      first two directions are firm; the upper-lower result is acute and
      imprecise.
    grade: C
  - note: >
      SUPERSETS COST EFFORT, NOT GAINS. Lactate, energy cost and RPE are
      higher; perceived recovery and CK were not different. In three chronic
      trials strength and size matched traditional sets. Speak a superset as
      "the same work in about a third less time, it will feel harder", not as
      "a better workout". With a cardiovascular condition, do not prescribe
      superset density without the clinician's line (the higher internal load
      is the reason); give the general direction only.
    grade: B
  - note: >
      HEAVY COMPOUNDS KEEP THEIR REST. Shortening rest saves time only where
      reps hold: isolation and moderate-load work at about 60-90 s. Heavy
      multi-joint strength sets need about 2 min or more for a trained lifter
      to hold the load (017). Do not buy minutes by cutting the primary lift's
      rest; pair it with an unrelated exercise in the rest instead, or keep it
      straight.
    grade: B
  - note: >
      DROP SETS AND REST-PAUSE ARE FOR THE LAST SET OF AN ISOLATION LIFT. Both
      kept growth with about half the time in short trials of young adults;
      rest-pause beat traditional sets for thigh size in one 18-person trial,
      a result to report, not to promise. Both run to failure. They suit
      machines and dumbbells, not a heavy free-weight compound, and they
      should not be used to replace the first, heavy lift of the day.
    grade: C
  - note: >
      A SHORT SESSION STILL WORKS. One hard set per exercise two to three
      times a week still raised trained men's squat and bench (less than
      more sets would). One session a week with the load kept held muscle in
      young adults for 32 weeks. So when the minutes collapse, the compound
      lifts at working load with fewer sets are a real session, not a wasted
      one. No trial compares a shortened session with a skipped one; the
      direction "do the short one" is drawn from these dose data.
    grade: C
  - note: >
      CUT THE STRETCHING AND THE LONG GENERAL WARM-UP FIRST. Iversen 2021
      ranks general warm-up and static stretching as low-yield for strength
      sessions, while the specific ramp before heavy loads stays (080). Long
      static stretching before lifting also costs force (021). Mobility work
      that is the user's own goal or rehab is not "stretching" for this rule.
    grade: B
  - note: >
      POPULATION. The superset and rest-pause trials are mostly trained young
      men; drop-set trials are 19-27 year olds; no time-efficiency trial is in
      adults over 60, for whom the maintenance dose is already higher (071).
    grade: C
claim: >
  When a session has fewer minutes than planned, the training effect survives
  if total working sets, load and effort are kept and the time comes out of
  rest and setup. Supersets cut session time by about a third (Zhang 2025, 19
  studies) with no difference in volume load, reps, strength or growth
  overall, provided the pair does not hit the same muscle: agonist-antagonist
  pairs keep or raise reps, same-muscle pairs cut volume load sharply; RPE and
  lactate are higher. Drop sets keep growth in one half to one third of the
  time (Sodal 2023, 6 studies) and rest-pause matched strength in less time in
  one trial; both are failure methods for isolation work. Shorter rest only
  costs when it costs reps (017), so isolation work can run at 60-90 s while
  heavy compounds keep about 2 min or more. Stretching and long general
  warm-ups are the first time to cut; the specific ramp before heavy loads
  stays (080). The minimum dose is low: one hard set per exercise 2-3 times a
  week still builds strength in trained men, one weekly session at the same
  load holds muscle in young adults, so a short session of the main
  compounds is a real session. Whether a shortened session beats a skipped
  one, and every minute boundary, is untested.
reasoning: >
  Zhang 2025 is the only meta-analysis that pools supersets against
  traditional sets with a type split; its acute volume and time results carry
  the B direction, its three chronic trials (Robbins 2010 among them) only C.
  Iversen 2021 is a narrative review by a group that includes a trial author
  and supplies the cut order (multi-joint first, general warm-up and stretching
  last, advanced techniques to halve time); it is used for direction, not
  numbers, except the weekly set minimum it sources from Schoenfeld 2017 (see
  070). Sodal 2023 gives the drop-set result; Prestes 2019 the rest-pause one.
  017 already holds the rest-interval evidence; this row only applies it to
  time. Androulakis-Korakakis 2020 and Spiering 2021 (with 071's Bickel 2011)
  give the floor below which a short session stops being a training stimulus
  for strength and for holding muscle. The skip-vs-shorten direction and every
  minute number are product inferences (D) and are labelled as such in 091.
---

# exercise/short-session-time-efficiency-evidence-090 -- 시간이 모자란 날, 무엇을 줄여도 되는가

**One line:** keep the sets, the load and the effort; take the minutes out of
rest, setup, stretching and warm-up. Supersets of opposite muscles and drop
sets on isolation lifts do the same work in far less time.

What the trials show, plainly:

- Supersets (two exercises back to back) shortened sessions by about 37% with
  the same total reps and load lifted and, in three longer trials, the same
  strength and muscle gain. The pairing matters: opposite muscles (row +
  press, curl + triceps) kept or raised reps; two exercises for the same
  muscle cut the load lifted a lot. Supersets feel harder.
- Drop sets gave the same muscle growth as normal sets in one half to one
  third of the time (6 studies, young adults). Rest-pause matched strength in
  a 35-minute session against a 57-minute one (one small trial).
- Shorter rest only hurts by costing reps (017). Isolation lifts are fine at
  about 60-90 seconds; heavy compounds need about 2 minutes or more.
- Static stretching and long easy warm-ups are the least useful minutes in a
  lifting session. The warm-up sets before a heavy lift are not (080).
- The minimum is low: one hard set per exercise two to three times a week
  still raised trained men's squat and bench; one session a week at the same
  weights held muscle for months in young adults. A short session of the main
  lifts counts.

Not tested: whether a shortened session beats a skipped one, the best
order to cut things, and anyone over 60.

| Lever | Time saved | What it costs | Strength of evidence |
|---|---|---|---|
| Superset, opposite muscles | ~1/3 of session | harder effort | meta-analysis, mostly acute |
| Superset, same muscle | ~1/3 | load lifted drops | meta-analysis, acute |
| Drop set (isolation, last set) | 1/2-2/3 of that lift | to failure | small meta-analysis |
| Rest-pause (isolation) | ~1/3 of session | to failure | one trial |
| Rest 60-90 s on isolation | some | none if reps hold | 017 |
| Shorter rest on heavy compounds | some | reps and load | 017 |
| Drop stretching / long general warm-up | 5-20 min | little for lifting | review + 021 |
| Fewer exercises, same sets each | per exercise | coverage | 072 order |

## 한국어 요약 (답변용)

- 시간이 모자라면 세트 수·무게·힘쓰는 정도는 그대로 두고, 쉬는 시간·준비·스트레칭·긴 워밍업에서
  시간을 뺀다.
- 슈퍼세트(두 운동을 쉬지 않고 번갈아)는 운동 시간을 3분의 1 정도 줄이면서 총 반복 수와 들어 올린
  총량, 장기적인 근력·근육 증가가 일반 세트와 같았다. 단, 서로 반대 근육(당기기+밀기, 이두+삼두)끼리
  묶어야 한다. 같은 근육 운동 두 개를 묶으면 들어 올리는 총량이 크게 줄었다. 대신 더 힘들게 느껴진다.
- 드롭세트는 일반 세트와 근육 증가가 같고 시간은 절반에서 3분의 1이었다(연구 6편, 20대). 레스트포즈도
  한 연구에서 57분짜리를 35분으로 줄이고 근력이 같았다. 둘 다 실패 지점까지 가는 방법이라, 머신·
  덤벨 고립 운동의 마지막 세트에만 쓴다. 무거운 바벨 복합운동에는 쓰지 않는다.
- 쉬는 시간은 반복 수가 줄어들 때만 손해다. 고립 운동은 60~90초로 줄여도 되지만, 무거운 복합운동은
  2분 이상 쉰다. 그 쉬는 동안 다른 부위 운동을 끼우는 건 괜찮다.
- 스트레칭과 길고 가벼운 전신 워밍업이 가장 먼저 뺄 시간이다. 무거운 운동 전의 워밍업 세트는
  남긴다(080). 재활이나 유연성이 목표라서 하는 운동은 여기 해당하지 않는다.
- 최소량은 생각보다 낮다. 경력자도 종목당 1세트를 주 2~3회 힘껏 하면 스쿼트·벤치 기록이 올랐고,
  젊은 사람은 같은 무게로 주 1회만 해도 몇 달간 근육이 유지됐다. 그래서 짧게라도 큰 운동만 하는 게
  의미 있는 운동이다. 다만 "짧게 하기 vs 건너뛰기"를 직접 비교한 연구는 없다.
- 심혈관 질환이 있으면 슈퍼세트처럼 밀도를 올리는 방법은 담당 의사 기준 없이 권하지 않는다.
- 연구 참가자는 대부분 젊은 남성 경력자다. 60세 이상에서 시험한 연구는 없다.
