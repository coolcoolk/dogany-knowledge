---
# Progression-models sprint 2026-10-07.
# The engine-readable synthesis for the next-set (set-add -> set-table) and
# next-session (rx-calc apply_progression / e1rm_rx) prescription paths: which
# progression model, when to add reps vs load, microloading, RIR adjustment,
# stall handling, in a cut. It is a ROUTING rule over graded rows, not a primary
# finding -- same posture as 056. Each rule names the row it rests on and its
# basis_grade; every number marked "product constant" is the plan's convention
# and has no direct evidence behind it.
#
# model_selection and progression_rules are structured data. Values are
# directions, triggers and step counts in INCREMENTS (the slot's own increment
# or lattice step); no rule here fixes a kilogram size (027: none is
# evidence-backed). Field guide: the progression-rules field guide (not public).
id: exercise/progression-rules-trained-cut-082
domain: exercise
grade: D (synthesis rule; RIR-tracking or rep-range progression beats a fixed preset load is C-backed, load-vs-reps and autoregulation-vs-percentage equivalence are B-backed rows, every trigger count and percentage is product judgement)
lane: "@gym-craft"
locale: universal
as_of: 2010-2024
contested: no
sources:
  - "exercise/progression-modality-load-vs-reps-028"  # adding reps vs adding load: similar hypertrophy over ~8 wk inside ~2x the rep target; strength favours heavy loads
  - "exercise/autoregulation-vs-percentage-prescription-030"  # autoregulated vs percentage: no detected strength advantage; RIR error ~0.65-1.0 reps
  - "exercise/load-increment-size-evidence-gap-027"  # no increment size is evidence-backed; failed-increment / reset protocols untested
  - "exercise/increment-verification-floor-029"  # one test-retest pair cannot confirm changes under ~8-12% of 1RM
  - "exercise/maintenance-vs-growth-volume-cut-071"  # in a deficit, lean-mass gain blunted, strength gain not detectably
  - "exercise/deficit-volume-guidance-016"  # volume in a deficit (theory-only)
  - "exercise/recovery-kinetics-session-spacing-025"  # proximity to failure drives recovery cost
  - "https://pubmed.ncbi.nlm.nih.gov/20543732/"  # Mann JB, Thyfault JP, Ivey PA, Sayers SP 2010, J Strength Cond Res 24(7):1718-1723, doi 10.1519/JSC.0b013e3181def4a6 -- n=23 Division I football players, 6 wk: APRE beat a preset linear-periodized load increase on bench 1RM (93.4 vs -0.40 N) and estimated squat 1RM (192.7 vs 37.2 N); volume not matched between groups
  - "https://research.stmarys.ac.uk/3067/"  # Graham T, Cleather DJ 2021 (online 2019), J Strength Cond Res 35(9):2451-2456, PMID 31009432, doi 10.1519/JSC.0000000000003164 (accepted manuscript read) -- n=31 trained men (2+ yr), 12 wk, 2x/wk squat, unsupervised: RIR-prescribed load beat fixed %-of-pre-test load, front squat +11.7 vs +8.3% (p=0.004), back squat +10.8 vs +7.1% (p=0.006); the RIR group ended up training heavier (83.2-83.6 vs 80.4% average intensity)
  - "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5877330/"  # Helms ER et al. 2018, Front Physiol 9:247, doi 10.3389/fphys.2018.00247 -- n=21 trained men, 8 wk, sets and reps matched: RPE-selected vs %1RM load, both effective, between-group differences non-significant; magnitude-based inference suggested a small likely squat advantage for RPE
  - "https://pubmed.ncbi.nlm.nih.gov/35044672/"  # Moesgaard L et al. 2022, Sports Med 52(7):1647-1666, doi 10.1007/s40279-021-01636-1 -- 35 volume-equated studies: periodized > non-periodized for 1RM (ES 0.31, 95% CI 0.04-0.57), not for hypertrophy (ES 0.13, CI -0.10 to 0.36); undulating > linear periodization for 1RM (ES 0.31)
  - "https://pubmed.ncbi.nlm.nih.gov/38970765/"  # Robinson ZP et al. 2024, Sports Med 54(9):2209-2231, doi 10.1007/s40279-024-02069-2 -- meta-regressions on estimated RIR: hypertrophy rises as sets end closer to failure; strength gain similar across a wide RIR range; RIR estimated from study descriptions
  - "https://pubmed.ncbi.nlm.nih.gov/38393985/"  # Refalo MC et al. 2024, J Sports Sci 42(1):85-101, doi 10.1080/02640414.2024.2321021 -- n=18 trained, within-subject legs, 8 wk: failure vs 1-2 RIR, similar quadriceps thickness; failure produced more velocity and rep loss
  - "https://pubmed.ncbi.nlm.nih.gov/32058362/"  # Aube D et al. 2022, J Strength Cond Res 36(3):600-607, doi 10.1519/JSC.0000000000003524 -- n=35 trained (squat 2.09x BM), 8 wk: 12 / 18 / 24 weekly lower-body sets; no difference in muscle thickness; squat 1RM trend favouring 18 over 24 (p=0.052)
  - "https://pubmed.ncbi.nlm.nih.gov/38274324/"  # Coleman M et al. 2024, PeerJ 12:e16777, doi 10.7717/peerj.16777 -- n=39 trained, 9 wk: a 1-week complete break at mid-program gave smaller lower-body strength gains and no hypertrophy difference vs continuous training
  - "framework:GRADE -- no trial compares double progression with RIR-based load selection head to head, in any population, and none is run in a deficit. The comparative evidence is (a) self-adjusting schemes beat a preset schedule that does not track the lifter (Mann 2010, Graham & Cleather) in small, partly unsupervised or volume-unmatched trials, (b) autoregulated and percentage prescription are not detectably different in pooled trained samples (030), (c) adding reps and adding load are similar for hypertrophy (028). The rules are product synthesis on top of that; triggers and percentages are constants."
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
model_selection:
  - model: double
    words: rep range per slot; hold the load and add reps until the top of the range is reached at the target RIR, then add one increment and restart at the range bottom
    use_when: default for every loaded slot of a trained lifter, cut or not; required where the increment is coarse (machines, dumbbells)
    avoid_when: none
    basis: exercise/progression-modality-load-vs-reps-028
    basis_grade: C
  - model: rir-load
    words: today's load picked so the set lands in the target RIR band (from an e1RM estimate or the previous set)
    use_when: main compounds with an e1RM estimate; equal choice to double, not a superior one
    avoid_when: no RIR is logged, or the lifter cannot rate RIR
    basis: exercise/autoregulation-vs-percentage-prescription-030
    basis_grade: B
  - model: linear
    words: a fixed load added every session or week regardless of what the last session showed
    use_when: novices only, and only while every session still hits its reps
    avoid_when: trained lifters; any cut
    basis: Mann 2010; Graham and Cleather 2021 (preset load that does not track the lifter lost to self-adjusting load)
    basis_grade: C
  - model: hold
    words: load and reps kept; no progression
    use_when: rehab / maintenance slots; a lift that has stalled twice in the same cut (see stall-repeat)
    avoid_when: as a blanket response to starting a cut
    basis: exercise/maintenance-vs-growth-volume-cut-071
    basis_grade: B
progression_rules:
  - rule: load-up
    scope: next-session
    when: top working set reaches rep_range top with logged RIR not below the slot's target band
    action: add one increment next session; reset the rep target to rep_range bottom
    params: one increment, never two from a single session
    basis: exercise/progression-modality-load-vs-reps-028
    basis_grade: C
  - rule: no-double-jump
    scope: next-session
    when: rep_range top reached with RIR well above the band (band_high + 2 or more)
    action: still one increment; a bigger correction only through the e1RM re-solve path, which needs several sessions
    params: single RIR reading error is about 1 rep
    basis: exercise/autoregulation-vs-percentage-prescription-030
    basis_grade: C
  - rule: reps-up
    scope: next-session
    when: top working set inside the rep range (bottom <= reps < top)
    action: keep the load; target one more rep on the top set
    params: none
    basis: exercise/progression-modality-load-vs-reps-028
    basis_grade: C
  - rule: strength-goal-load-first
    scope: plan
    when: primary_goal is strength (a 1RM lift)
    action: keep the slot's rep_range low and progress load; do not widen the range upward to keep adding reps
    params: rep target never drifts past about twice the slot's original top
    basis: exercise/progression-modality-load-vs-reps-028
    basis_grade: B
  - rule: microload
    scope: next-session
    when: one increment is more than 5% of the working load (product constant), or rounding the next load would put the rep target below rep_range bottom
    action: use a smaller step if the lattice has one; otherwise add reps up to rep_range top + 2 before the jump, then jump and restart at rep_range bottom
    params: the 5% and the +2 are product constants; no increment size is evidence-backed
    basis: exercise/load-increment-size-evidence-gap-027
    basis_grade: D
  - rule: next-set-rir
    scope: next-set
    when: a working set is logged with RIR (set-add)
    action: RIR within 1 rep of the target band -> keep the load; RIR 2+ above band_high -> next set one increment up; RIR 2+ below band_low, or a missed rep target -> next set one increment down or keep the load and accept fewer reps
    params: one increment per set at most; the 1-rep dead zone is the instrument error
    basis: exercise/autoregulation-vs-percentage-prescription-030
    basis_grade: C
  - rule: rir-band
    scope: plan
    when: setting a slot's target RIR band
    action: compounds 1-3 RIR; isolation 0-2 RIR; failure is optional, not required, in a cut
    params: band values are product constants
    basis: Robinson 2024 (hypertrophy rises toward failure, strength flat across RIR); Refalo 2024 (1-2 RIR matched failure for hypertrophy in trained lifters)
    basis_grade: C
  - rule: stall-define
    scope: next-session
    when: top set below rep_range bottom at the same load in 2 consecutive trusted sessions (bad-condition and early-stop sessions do not count)
    action: mark the lift stalled; one miss alone is a hold, not a stall
    params: 2 sessions is a product constant
    basis: exercise/increment-verification-floor-029
    basis_grade: C
  - rule: stall-reset
    scope: next-session
    when: stall-define fires
    action: drop the load about 10% (rounded down to the lattice) and climb back by double progression; do not answer a stall with extra sets; do not prescribe a full week off by default
    params: 10% is a product constant; reset protocols are untested
    basis: exercise/load-increment-size-evidence-gap-027; Coleman 2024 (one-week break cost lower-body strength); Aube 2022 (24 weekly sets no better than 18 in trained lifters)
    basis_grade: D
  - rule: stall-cut-check
    scope: plan
    when: a stall happens during a cut
    action: say a hold in a cut is expected; check the deficit size and rate of loss before changing the program
    params: about 500 kcal per day is the rough line (exercise/maintenance-vs-growth-volume-cut-071)
    basis: exercise/maintenance-vs-growth-volume-cut-071
    basis_grade: C
  - rule: stall-repeat
    scope: plan
    when: the same lift resets twice in the same cut
    action: switch the slot to hold (keep load, keep reps) for the rest of the cut, or swap to a close variant; keep the other slots progressing
    params: two resets is a product constant
    basis: exercise/maintenance-vs-growth-volume-cut-071
    basis_grade: D
  - rule: set-add-volume
    scope: plan
    when: considering adding a weekly set to a muscle in a cut
    action: add at most one set per muscle per week, and only while that muscle's lifts are progressing; never as a stall response
    params: one set per week is a product constant
    basis: exercise/deficit-volume-guidance-016; Aube 2022
    basis_grade: D
refraction_notes:
  - note: >
      WHAT MATTERS IS THAT THE LOAD TRACKS THE LIFTER. The two trials that
      found a difference between models both pitted a self-adjusting scheme
      against a load set in advance: APRE beat a preset weekly increase in
      college football players (Mann 2010), and RIR-selected load beat a fixed
      percentage of the pre-test max over twelve weeks in trained men, where
      the RIR group ended up training heavier as they got stronger (Graham and
      Cleather). When the comparison is two self-adjusting or matched schemes
      (Helms 2018; the pooled reviews on 030), no difference is detected. So
      double progression and RIR-based load are equal choices; a preset
      schedule that ignores the last session is the weak one.
    grade: C
  - note: >
      "LINEAR PERIODIZATION" IS NOT "LINEAR PROGRESSION". The periodization
      meta-analysis (Moesgaard 2022) compares planned phase structures with
      volume equated: periodized beat non-periodized for 1RM by a small margin
      and not for hypertrophy, and undulating beat linear periodization for
      1RM. That is about how load and volume are arranged across weeks, not
      about adding a fixed amount every session. Do not cite it for or against
      session-to-session linear progression.
    grade: C
  - note: >
      REPS OR LOAD: FOR GROWTH, EITHER; FOR A MAX, LOAD. Adding reps at a fixed
      load and adding load in a rep range gave similar hypertrophy over about
      eight weeks, inside roughly twice the rep target (028). For a lifter
      chasing a one-rep max, heavier loads win, so the range is kept low and
      load is the lever. This is why double progression, which does both in
      turn, is the default.
    grade: B
  - note: >
      THE RIR DEAD ZONE IS THE INSTRUMENT ERROR. Trained lifters misjudge RIR
      by about two-thirds of a rep to a full rep (030). A one-rep deviation
      from the target band is inside that error and should not move the next
      set's load; a two-rep deviation is a signal. The one-increment cap per
      set keeps a single misread from compounding.
    grade: C
  - note: >
      CLOSE TO FAILURE HELPS SIZE, NOT STRENGTH. Across studies, muscle growth
      rose as sets ended closer to failure while strength gain was flat across
      a wide RIR range (Robinson 2024, RIR estimated from study descriptions);
      in trained lifters, stopping 1-2 reps short matched training to failure
      for quadriceps growth with less fatigue (Refalo 2024, n=18). In a cut,
      where recovery is the scarce resource (016, 025), compounds sit at 1-3
      RIR and failure is an option for isolation work, not a requirement.
    grade: C
  - note: >
      A STALL IS TWO SESSIONS, AND THE RESET IS A CONVENTION. One flat session
      sits inside test-retest noise (029). The 10% reset is the engine's
      existing constant; no trial has compared reset sizes or reset against
      hold (027, sub-gap 6). The one relevant trial tested a full week off, not
      a load reduction, and found smaller lower-body strength gains (Coleman
      2024), which is why a week off is not the default stall answer. Extra
      sets are not the answer either: in trained lifters 24 weekly sets did not
      beat 18 (Aube 2022), and in a deficit the volume guidance points down,
      not up (016).
    grade: D
  - note: >
      IN A CUT, PROGRESS CONTINUES, MORE SLOWLY. Strength gains were not
      detectably blunted by a deficit while lean-mass gains were (exercise/maintenance-vs-growth-volume-cut-071). So the
      engine keeps every loaded slot progressing when a cut starts; holds are
      expected more often and are spoken as normal; only a lift that has
      reset twice in the same cut drops to hold for the rest of it. That
      second rule is product judgement.
    grade: C
claim: >
  For a trained lifter, in a cut or not, the progression model matters less
  than whether the load tracks what the lifter just did. Self-adjusting
  schemes beat a load fixed in advance in two small trials (APRE versus a
  preset weekly increase; RIR-selected load versus a fixed percentage of the
  pre-test max, where the RIR group ended up training heavier), while matched
  self-adjusting schemes do not detectably differ from each other. So double
  progression (hold the load and add reps up to the top of a rep range, then
  add one increment and restart at the bottom) is the default for every loaded
  slot, RIR-based load selection is an equal alternative for main compounds,
  and fixed session-to-session linear loading is for novices only. Adding reps
  and adding load are interchangeable for growth inside about twice the rep
  target; for a one-rep-max goal, load is the lever. When one increment is too
  coarse, add reps further or take a smaller step, without claiming any step
  size is evidence-based. Within a session, a logged RIR within one rep of the
  target band leaves the next set's load alone (that is the instrument's
  error); two reps off moves it one increment. A stall is two consecutive
  trusted sessions below the rep floor at the same load; the response is a
  load reset of about 10% and a climb back, not extra sets and not a week off.
  In a cut, strength progress continues more slowly, holds are expected, and
  only a lift that resets twice drops to hold for the rest of the cut. Every
  count and percentage here is a product constant.
reasoning: >
  The rows already in the warehouse answer most of the pieces separately: 028
  says reps and load are interchangeable for growth and not for maximal
  strength; 030 says autoregulated and percentage prescription are not
  detectably different and puts a number on RIR error; 027 says no increment
  size and no reset protocol is evidence-backed; 029 says one retest cannot
  confirm a small change; exercise/maintenance-vs-growth-volume-cut-071 says a deficit blunts lean-mass gain but not
  detectably strength gain. What was missing was the direct comparison of
  progression models and a set of rules the prescription code can read. The
  model comparison was read at the primaries: Mann 2010 (APRE beat a preset
  linear increase, n=23, volume unmatched) and Graham and Cleather (RIR-based
  beat fixed percentage over 12 weeks in 31 trained men, unsupervised, with the
  RIR group training heavier) both show a self-adjusting load beating a preset
  one; Helms 2018 (sets and reps matched, n=21 trained) shows no significant
  difference between RPE-selected and percentage loads. The consistent reading
  is about tracking, not about which tracking method. Moesgaard 2022 is kept
  in only to stop its "linear periodization" from being misread as linear
  progression. The RIR-band and set-volume rules use Robinson 2024, Refalo 2024
  and Aube 2022, each small or meta-regressive. The stall rules keep the
  engine's existing two-miss trigger and 10% reset as labelled constants and
  add the two things the evidence does say: a full week off cost lower-body
  strength (Coleman 2024), and more sets did not beat moderate volume in
  trained lifters. No trial compares double progression with RIR-based load in
  any population, and no progression trial runs in a deficit (GAPS.md).
---

# exercise/progression-rules-trained-cut-082 -- 숙련자 감량기 진행 규칙: 반복 수를 늘릴까, 무게를 올릴까

**한 줄 그림:** 어떤 진행 방식이냐보다 "무게가 지난 세션 결과를 따라가느냐"가 중요하다. 기본은
반복 수 범위 안에서 반복을 늘리고, 범위 꼭대기에 닿으면 한 단계 올리는 이중 진행이다.

## Model choice

| Model | Use | Avoid |
|---|---|---|
| double (rep range, then load) | default, every loaded slot; coarse-increment machines and dumbbells | -- |
| rir-load (load picked to land in the RIR band) | main compounds with an e1RM estimate; equal to double, not better | no RIR logged |
| linear (fixed add every session) | novices while every session hits its reps | trained lifters; any cut |
| hold | rehab / maintenance; a lift that reset twice in this cut | a blanket response to starting a cut |

## Rules the prescription code can read

| Rule | Scope | When | Action |
|---|---|---|---|
| load-up | next session | top set hits range top, RIR not below band | +1 increment, reps back to range bottom |
| no-double-jump | next session | range top with RIR band_high + 2 or more | still +1; bigger moves only via the e1RM re-solve |
| reps-up | next session | top set inside the range | same load, +1 rep on the top set |
| strength-goal-load-first | plan | goal is a 1RM lift | keep the range low, progress load |
| microload | next session | one increment > 5% of the load, or rounding drops reps below range bottom | smaller step if the lattice has one; else reps to range top + 2, then jump |
| next-set-rir | next set | a set is logged with RIR | within 1 rep of band: keep; 2+ above: +1 increment; 2+ below or rep miss: -1 increment or keep and accept fewer reps |
| rir-band | plan | setting a slot's band | compounds 1-3, isolation 0-2, failure optional |
| stall-define | next session | below range bottom at the same load, 2 trusted sessions running | stalled; one miss is a hold |
| stall-reset | next session | stalled | about -10%, climb back; no extra sets, no default week off |
| stall-cut-check | plan | stall in a cut | say it is expected; check deficit size and rate first |
| stall-repeat | plan | same lift resets twice in one cut | hold or swap that lift for the rest of the cut |
| set-add-volume | plan | adding weekly sets in a cut | at most one per muscle per week, only while progressing |

Increments are the slot's own increment or lattice step. The 5%, +2 reps, 2
sessions, 10%, two resets and one set per week are product constants.

## 한국어 요약 (답변용)

- 숙련자에게 중요한 건 방식 이름이 아니라 무게가 지난 세션 결과를 따라 움직이느냐다. 미리 정한
  무게표대로만 올린 쪽은, 그날 수행에 맞춰 무게를 고른 쪽(RIR 기반, APRE)보다 작은 연구 두 개에서
  덜 늘었다. 결과를 따라가는 방식끼리는 차이가 보이지 않았다.
- 기본은 이중 진행이다. 같은 무게로 반복을 하나씩 늘리다가 범위 꼭대기에 목표 RIR로 닿으면 다음
  세션에 한 단계 올리고, 반복은 범위 바닥부터 다시 시작한다. 한 세션 결과로 두 단계를 올리지는 않는다.
- 근육을 키우는 게 목적이면 반복을 늘리든 무게를 올리든 비슷했다(원래 목표 반복의 두 배 정도까지).
  1RM이 목적이면 무게가 중요하니 반복 범위를 낮게 두고 무게를 올린다.
- 한 단계가 너무 크면(작업 무게의 5% 초과, 제품 기준) 더 작은 원판·핀이 있으면 그걸 쓰고, 없으면
  범위 꼭대기보다 2회 더 채운 뒤 올린다. 몇 kg씩 올려야 한다는 근거는 없다고 말한다.
- 세트 사이: 기록한 RIR이 목표 범위에서 1회 이내로 벗어나면 다음 세트 무게를 그대로 둔다(RIR 추정
  오차가 원래 1회 안팎이다). 2회 이상 여유가 남으면 한 단계 올리고, 2회 이상 모자라거나 목표 반복을
  못 채우면 한 단계 내리거나 무게를 두고 반복을 덜 한다.
- 정체는 같은 무게에서 두 세션 연속 범위 바닥을 못 넘긴 경우다(컨디션 불량·조기 종료 세션 제외).
  한 번 못 한 건 정체가 아니다. 정체면 약 10% 내리고 다시 올라간다. 세트를 더하거나 일주일을 통째로
  쉬는 건 기본 처방이 아니다. 숫자는 모두 제품 기준이다.
- 감량기에도 힘은 계속 늘 수 있다. 다만 느려지니 같은 무게에 머무는 건 정상으로 본다. 정체가 오면
  먼저 결핍이 너무 크거나(하루 약 500kcal 이상) 감량 속도가 빠르지 않은지 본다. 같은 종목이 한 감량기
  안에서 두 번 리셋되면 그 종목만 감량이 끝날 때까지 유지로 돌린다.
