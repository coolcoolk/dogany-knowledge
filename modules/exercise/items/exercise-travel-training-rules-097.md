---
# Travel-training sprint 2026-10-07.
# The engine-readable synthesis of 096 for the daily / weekly program: what the
# composer does when the calendar holds a trip block (3-14 days away from the
# home gym). It is a routing rule, not a primary finding: each rule names the
# graded row it rests on, and every day count, hour count and threshold is a
# labelled product constant. Same posture as 087 and 091.
#
# It does not replace 087's layoff rows (under 3 weeks -> resume unchanged),
# 060's life-stress-or-travel deload trigger or 091's short_session_rules; it
# calls them. Vocabulary matches 071 (maintenance floor), 072 (per_exercise_min,
# weekly_muscles, set levels), 087 (layoff) and 091 (micro-session). Jet-lag
# light and melatonin advice is the travel lane's (travel 001 / 002); this row
# only picks the training slot and effort.
id: exercise/travel-training-rules-097
domain: exercise
grade: D (synthesis rule over 096, 071, 087, 060 and 091; each rule carries its own basis_grade; every day count, hour count and the session-time mapping are product judgement)
lane: "@gym-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/travel-detraining-minimum-dose-evidence-096"  # detraining over <=2 weeks, minimum dose, light-load / bodyweight / band stand-ins, exercise phase shifts, jet-lag effort
  - "exercise/maintenance-vs-growth-volume-cut-071"  # maintenance dose with the load kept; older adults ~2 sessions and 2-3 sets
  - "exercise/phase-volume-rules-087"  # layoff under 3 weeks -> resume the previous plan unchanged
  - "exercise/deload-planned-vs-reactive-060"  # life-stress-or-travel trigger: offer to move the planned deload into the trip
  - "exercise/short-session-rules-091"  # micro-session and cut_order for a short hotel slot
  - "exercise/early-morning-session-brief-rules-073"  # dawn-session warm-up, read when the trip slot is early local morning
  - "travel item 002 (module not published)"  # light direction by CBTmin; the training slot must not contradict it
  - "travel item 001 (module not published)"  # the jet-lag treatment itself is the travel lane's
  - "travel item 003 (module not published)"  # flight-day VTE risk, the travel lane's
  - "a research sprint 2026-10-07: engine-readable travel_training_rules for the program when a trip block exists"
  - "framework:GRADE -- directions are borrowed from the cited rows at their own grades (no strength loss over <=2 weeks B, low-load near failure B with C for named stand-ins, maintenance dose C, exercise phase shift C, low intensity after arrival D). The trip-length bands, the 3-zone jet-lag threshold, the easy-day count, the body-clock slot mapping, the RIR caps and the rep ceiling are product constants with no direct evidence (D)."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: injury_history
      type: categorical
      role: soft
      unknown_policy: hedge
inputs:
  trip_block: calendar block with start_date, end_date (away days, both travel days counted)
  tz_shift_hours: signed hours, destination minus home (positive = east); 0 when unknown
  gym_access: full | hotel_basic | none | unknown (hotel_basic = dumbbells to a light ceiling, a machine or two, a cable or band)
  minutes_free_per_day: optional; feeds 091 when set
constants:
  trip_days_min: 3                 # product: shorter blocks are a normal schedule gap, not a trip
  trip_days_max: 14                # product: longer blocks route to 087 layoff rows on return as well
  optional_band_max_days: 7        # product: trips up to this length need no session at all (096 B)
  keep_band_sessions_young: 1      # 071 / 096: about 1 session a week holds size in young adults
  keep_band_sessions_older: 2      # 071 / 096: about 2 a week in older adults
  older_age_years: 60              # product: 071's trial compared 20-35 with 60-75 only
  keep_sets_per_exercise_young: 1  # 071 Spiering 2021: 1 hard set per exercise, load kept
  keep_sets_per_exercise_older: [2, 3]  # 071
  light_load_rir_max: 2            # product: light / bodyweight / band sets end at RIR 0-2 to count (096, Schoenfeld 2017 sets to failure)
  light_load_rep_ceiling: 30       # product: past this many reps at RIR 2, pick a harder variation
  jetlag_tz_threshold_hours: 3     # product: below this shift, no jet-lag rule fires
  jetlag_easy_days_east: 3         # product, from consensus "first few days low intensity" (096 D)
  jetlag_easy_days_west: 2         # product: westward adjusts faster (consensus ~half a day per zone)
  jetlag_easy_rir_min: 3           # product: easy days end sets at RIR 3 or more, no max or rep-record attempts
  advance_slots_body_clock: ["06:00-09:00", "13:00-16:00"]  # 096 Youngstedt 2019 (07:00 and 13:00-16:00 advance), widened by product
  delay_slot_body_clock: "19:00-22:00"   # 096 Youngstedt 2019
  body_clock_days: 3               # product: days 1-3 after arrival, body clock is read as home time for slot choice
travel_training_rules:
  - rule: trip-detect
    trigger: a calendar block marked travel (or away from the home gym) spans trip_days_min to trip_days_max days
    action: enter trip mode for the block; outside that span do nothing here (shorter -> normal schedule; longer -> also apply 087 layoff rows on return)
    basis: exercise/travel-detraining-minimum-dose-evidence-096
    basis_grade: D
  - rule: no-loss-to-fix
    trigger: trip mode entered
    action: speak trip sessions as optional upkeep; never frame the trip as losing progress, never add pre-trip or post-trip catch-up volume
    basis: exercise/travel-detraining-minimum-dose-evidence-096
    basis_grade: B
  - rule: short-trip-optional
    trigger: trip length <= optional_band_max_days, age_years under older_age_years (or unknown)
    action: schedule no required session; offer one optional session (full-body, keep-dose) if the user wants to train
    basis: exercise/travel-detraining-minimum-dose-evidence-096
    basis_grade: B
  - rule: keep-dose
    trigger: trip length > optional_band_max_days, or age_years >= older_age_years at any trip length
    action: schedule keep_band_sessions_young (or keep_band_sessions_older) full-body sessions per trip week; each session one exercise per main pattern (squat or lunge, hinge, push, pull) at keep_sets_per_exercise_young (or _older) hard sets; place them on non-travel days
    basis: exercise/maintenance-vs-growth-volume-cut-071
    basis_grade: C
  - rule: offer-deload-in-trip
    trigger: a planned deload falls within the 2 weeks after the trip, or is due
    action: offer to move the deload into the trip (060 life-stress-or-travel); if accepted, the trip counts as that deload and the deload clock restarts on return
    basis: exercise/deload-planned-vs-reactive-060
    basis_grade: D
  - rule: equipment-map
    trigger: gym_access is hotel_basic or none
    action: per pattern, choose the stand-in whose load lets the set end at RIR 0 to light_load_rir_max within light_load_rep_ceiling reps -- push: dumbbell press or push-up (feet raised, then deficit, then single-arm bias as it gets easy); pull: dumbbell or band row, inverted row on a sturdy table edge only if stable; squat: split squat, rear-foot-elevated split squat, goblet squat; hinge: single-leg RDL, hip thrust or bridge (single leg when easy); band where nothing else loads a pattern
    basis: exercise/travel-detraining-minimum-dose-evidence-096
    basis_grade: C
  - rule: effort-condition
    trigger: any light-load, bodyweight or band set
    action: target RIR 0 to light_load_rir_max; if a set reaches light_load_rep_ceiling reps with more than light_load_rir_max in reserve, switch to the next harder variation next set rather than adding reps
    basis: exercise/travel-detraining-minimum-dose-evidence-096
    basis_grade: B
  - rule: gym-full
    trigger: gym_access is full
    action: run keep-dose with the user's usual lifts at the last logged working load; no new maxes; a new machine or unfamiliar setup starts one RIR above usual
    basis: exercise/maintenance-vs-growth-volume-cut-071
    basis_grade: C
  - rule: gym-unknown
    trigger: gym_access unknown and trip mode entered
    action: ask once (casual budget) what equipment there is; if not answered, plan bodyweight stand-ins (equipment-map with none)
    basis: exercise/travel-training-rules-097
    basis_grade: D
  - rule: travel-day-off
    trigger: a day with a flight or a long transfer
    action: no lifting session that day; walking is fine; flight-day movement and VTE advice is the travel lane's (travel 003)
    basis: exercise/travel-detraining-minimum-dose-evidence-096
    basis_grade: D
  - rule: jetlag-easy-days
    trigger: abs(tz_shift_hours) >= jetlag_tz_threshold_hours
    action: for the first jetlag_easy_days_east (positive shift) or jetlag_easy_days_west (negative shift) days after arrival, any session is easy -- sets end at RIR jetlag_easy_rir_min or more, no 1RM, AMRAP or rep-record attempts, and a short night (096 Craven 2022) moves the session rather than adding intensity
    basis: exercise/travel-detraining-minimum-dose-evidence-096
    basis_grade: D
  - rule: jetlag-slot
    trigger: abs(tz_shift_hours) >= jetlag_tz_threshold_hours, days 1 to body_clock_days after arrival, a session is scheduled
    action: convert candidate local slots to home time (the body clock); positive shift (east, need to advance) -> prefer a slot whose home time falls in advance_slots_body_clock and avoid delay_slot_body_clock; negative shift (west, need to delay) -> prefer delay_slot_body_clock and avoid the early advance slot; when the travel lane's light plan (002) is set for the day, the session takes the same window as its light-seeking block; when no slot fits waking hours, ignore the slot preference (the effect is small and untested in travellers)
    basis: exercise/travel-detraining-minimum-dose-evidence-096
    basis_grade: C
  - rule: short-slot
    trigger: minutes_free_per_day under the planned trip session
    action: run 091 cut_order on the trip session; under 091 micro_session_min run the micro-session with stand-ins
    basis: exercise/short-session-rules-091
    basis_grade: C
  - rule: return-resume
    trigger: first home-gym session after a trip of <= trip_days_max days
    action: resume the previous week's plan unchanged (087 layoff under 3 weeks): same sets, last logged loads, usual RIR; no catch-up sets for missed sessions; the first session per main lift may start one RIR above usual if the user reports it felt heavy, not by default
    basis: exercise/phase-volume-rules-087
    basis_grade: C
  - rule: return-jetlag
    trigger: return flight with abs(tz_shift_hours) >= jetlag_tz_threshold_hours
    action: apply jetlag-easy-days to the first home days in the direction of the return flight (a westbound trip returns eastbound); resume-unchanged still applies once those days pass
    basis: exercise/travel-detraining-minimum-dose-evidence-096
    basis_grade: D
never:
  - adding catch-up sets or a volume spike before or after the trip
  - a 1RM, AMRAP or rep-record attempt in the jet-lag easy days
  - a lifting session on a flight day
  - light, bodyweight or band sets ended far from failure (more than light_load_rir_max in reserve) counted as keep-dose sets
  - lowering working loads on return from a trip of 14 days or less
  - speaking the exercise-timing slot as a jet-lag treatment; the jet-lag plan is the travel lane's
refraction_notes:
  - note: >
      THE TRIP IS NOT A HOLE IN THE PROGRAM. Two weeks or less off costs a
      trained young lifter no measurable strength (096), and 087 already
      resumes an under-3-week layoff unchanged. The rule set therefore never
      adds catch-up work and never lowers loads on return; it offers sessions
      on longer trips mainly to hold muscle size and conditioning, which
      move first.
    grade: B
  - note: >
      THE 7-DAY LINE IS OURS. No trial separates a 7-day from a 10-day trip;
      the line where a session becomes scheduled rather than optional is a
      product constant chosen inside the 2-week no-loss window, earlier for
      older users because their losses are larger and their keep-dose is
      higher (071, 096).
    grade: D
  - note: >
      HARD ENOUGH IS THE WHOLE RULE FOR HOTEL WORK. Light loads grow muscle
      only when sets go near failure; push-ups and bands matched weights in
      trials that took them hard. The RIR cap and the 30-rep ceiling are
      product constants that keep a hotel set close to the trials' effort.
    grade: C
  - note: >
      SLOT CHOICE FOLLOWS THE BODY CLOCK, NOT THE LOCAL CLOCK. Exercise
      phase-response windows are body-clock times; in the first days after
      arrival the body runs near home time, so the engine converts. The
      effect is small, lab-measured and never tested on travellers, so the
      slot is a preference that yields to sleep, meetings and the light
      plan, never a requirement.
    grade: C
  - note: >
      EASY DAYS ARE CONSENSUS, THE COUNT IS OURS. Expert consensus keeps
      intensity low for the first few days after a long-haul arrival; field
      evidence for a strength cost is equivocal. Three days east and two
      west follow the consensus per-zone recovery direction, not a trial.
    grade: D
claim: >
  When the calendar holds a 3-14 day trip, the program enters trip mode and
  treats the trip as upkeep, not lost progress: no catch-up volume before or
  after. Up to 7 days (young users) no session is required and one optional
  full-body session is offered; longer trips, and any trip for users 60 or
  older, schedule the keep-dose -- about one full-body session a week with one
  hard set per main pattern (two sessions and 2-3 sets for older users) on
  non-travel days. A planned deload due soon is offered inside the trip. With
  a hotel gym or no gym, each pattern takes a stand-in (dumbbell or push-up
  press, dumbbell or band row, split squat, single-leg hinge) taken to RIR 0-2
  within 30 reps, moving to a harder variation rather than more reps. No
  lifting on flight days. After a shift of 3 or more time zones, the first 3
  days east (2 west) are easy -- RIR 3 or more, no max or rep-record attempts
  -- and the session slot is chosen in home (body-clock) time: about 06:00-09:00
  or 13:00-16:00 to help an eastward advance, 19:00-22:00 for a westward delay,
  agreeing with the travel lane's light plan and yielding to sleep. On return
  the previous plan resumes unchanged at the last logged loads (087), with the
  easy-day rule applied after a long return flight. Directions carry the grades
  of 096, 071, 087 and 060; every number and the slot mapping are product
  constants.
reasoning: >
  096 supplies the no-loss window (B), the keep-dose and older-user split via
  071 (C), the effort condition for light loads (B) with named stand-ins (C),
  the exercise phase-response windows (C) and the consensus easy days (D).
  087 supplies the under-3-week resume rule this row leans on for return;
  060 supplies the deload-into-travel offer; 091 handles any trip day short on
  minutes. The trip-length bands, the older-age line, the RIR and rep caps,
  the jet-lag threshold and easy-day counts, the body-clock window widths and
  the three-day body-clock assumption are product judgement (D). The jet-lag
  treatment itself (light, melatonin) stays with the travel lane; this row
  only avoids a training slot that would push the clock the wrong way.
---

# exercise/travel-training-rules-097 -- 여행 중 운동 규칙 (3~14일)

**한 줄 그림:** 2주 이하 여행은 근력을 잃지 않는다. 7일 이하는 운동이 선택, 그보다 길면 주 1회 전신
1세트씩. 호텔 운동은 가볍게 하되 힘들게. 시차 3시간 이상이면 도착 후 며칠은 쉽게, 몸시계 기준 시간에.
돌아오면 하던 대로.

## Rule map

| Situation | What the program does | Basis |
|---|---|---|
| trip 3-7 days, under 60 | no required session; one optional full-body | 096 |
| trip 8-14 days, or 60+ | 1 (or 2 if 60+) full-body sessions/week, 1 (2-3) hard sets per pattern | 071, 096 |
| deload due soon | offer to put it in the trip | 060 |
| hotel gym / none | stand-ins, RIR 0-2 within 30 reps, harder variation not more reps | 096 |
| flight day | no lifting; walking fine | product |
| tz shift >= 3 h | first 3 days (east) / 2 (west) easy: RIR 3+, no max | consensus, product |
| tz shift >= 3 h, days 1-3 | slot in home time: 06-09 or 13-16 to advance, 19-22 to delay | 096 (lab) |
| short on minutes | 091 cut_order / micro-session | 091 |
| back home | previous plan unchanged, last loads, no catch-up | 087 |

## 한국어 요약 (답변용)

- 3~14일 여행은 운동 계획의 구멍이 아니다. 2주 이하로 쉬어도 근력은 거의 그대로라서, 여행 전에 몰아서
  하거나 다녀와서 보충하지 않는다. 다녀와서 무게를 낮추지도 않는다.
- 7일 이하 여행(60세 미만)은 운동을 꼭 하지 않아도 된다. 하고 싶으면 전신 운동 한 번을 제안한다.
- 7일보다 길거나 60세 이상이면 주 1회(60세 이상은 주 2회) 전신 운동을 넣는다. 스쿼트·힙힌지·밀기·당기기
  패턴마다 힘든 세트 1개(60세 이상은 2~3개)면 된다. 비행 날은 빼고 잡는다.
- 곧 디로드 주가 다가오면, 여행 기간을 디로드로 쓰자고 제안한다(060).
- 호텔 헬스장이 작거나 없으면 대체 운동을 쓴다. 밀기: 덤벨 프레스나 팔굽혀펴기(쉬우면 발 올리기 → 깊게 →
  한 팔 쪽으로), 당기기: 덤벨·밴드 로우, 하체: 스플릿 스쿼트·뒷발 올린 스플릿 스쿼트·고블릿 스쿼트,
  힙힌지: 한 다리 루마니안 데드리프트·힙 쓰러스트·브릿지.
- 가벼운 운동은 힘들게 해야 효과가 같다. 30회 안에 2회 이하 여유가 남도록 하고, 30회를 해도 여유가 많으면
  횟수를 늘리지 말고 더 어려운 동작으로 바꾼다.
- 비행하는 날은 근력 운동을 하지 않는다. 걷기는 괜찮다. 비행 중 혈전 예방은 여행 쪽 항목(travel 003)이
  다룬다.
- 시차가 3시간 이상이면 도착 후 동쪽은 3일, 서쪽은 2일 동안 쉽게 한다. 3회 이상 여유를 남기고, 최고 기록
  도전은 하지 않는다. 잠을 못 잤으면 강도를 올리지 말고 운동 시간을 옮긴다.
- 도착 후 3일은 몸시계가 아직 한국 시간에 가깝다고 보고, 운동 시간을 한국 시간으로 계산한다. 동쪽 여행(시계를
  앞당겨야 할 때)은 한국 시간 아침 6~9시나 오후 1~4시, 서쪽 여행(늦춰야 할 때)은 한국 시간 저녁 7~10시에
  맞춘다. 빛 노출 계획(travel 002)과 같은 방향이어야 하고, 잠·일정이 우선이다. 이건 시차 치료가 아니라
  방해하지 않기 위한 선택이다.
- 돌아오면 여행 전 주 계획을 그대로, 마지막 기록 무게로 이어간다. 장거리 귀국 비행 뒤에는 위의 쉬운 날
  규칙을 한 번 더 적용한다.
- 7일, 60세, 30회, 2회 여유, 3시간, 동 3일·서 2일 같은 숫자는 제품 규칙이다. 연구로 정해진 값처럼 말하지
  않는다.
