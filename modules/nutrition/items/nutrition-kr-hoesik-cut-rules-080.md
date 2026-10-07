---
# Eating-out sprint 2026-10-07.
# KR-LOCALE companion to 072 (외식 in a fat-loss phase) for one specific
# event: the 회식 / 술자리 -- a planned evening with colleagues, shared
# 안주, drinks and often a 2차. 072 owns the general 외식 rules (frequency,
# decide-before-eating, broth, whole-dish logging, day-is-floor); 031/032
# own the alcohol dose, energy and unit rows; 074 owns the weekly adherence
# rules; 022 owns the measured dish-class energy. This row adds only what
# those do not: (1) eating with familiar people raises intake, (2) "banking"
# calories before the event -- what redistribution within a week is and is
# not supported, (3) the day after: no automatic appetite compensation,
# so no "it evens out" and no punishment day either, (4) 회식-specific copy
# (pre-commit, 안주 class, 2차, drink pressure, no moralising).
#
# eating_out_rules is structured data for the meal module / diet card /
# weekly retro (no module reads it yet). Same field shape as 074's
# adherence_rules: rule, surface, trigger, action, never, constants, basis,
# basis_grade, kind. The YAML-subset reader returns scalars as strings.
# Every constant is a product constant unless its basis says otherwise.
# No program code was changed.
id: nutrition/kr-hoesik-cut-rules-080
domain: nutrition
lane: "@meal-craft"
grade: "D (synthesis: the eating_out_rules as a set; each rule carries its own basis_grade); B (direction: eating with friends or family raises intake, meta-analysis of 42 studies; weight loss is the same whether a matched restriction is spread evenly or intermittently, meta-analysis of trials of 6 months or more); C (one day of 50 percent overfeeding produced no next-day appetite or intake compensation, n=12; a skipped meal was not fully compensated later the same day, small crossovers; implementation-intention effects on eating, small to medium); D (Korean 회식 frequency and drink pressure, one commissioned worker survey read through a news report)"
locale: KR
as_of: 2011-2024
contested: no
sources:
  - "https://doi.org/10.1093/ajcn/nqz155"  # Ruddock HK, Brunstrom JM, Vartanian LR, Higgs S. A systematic review and meta-analysis of the social facilitation of eating. Am J Clin Nutr 2019;110(4):842-861. 42 studies, experimental and non-experimental: people select and eat more with friends than alone (SMD 0.76, 95% CI 0.48-1.03); no evidence with strangers or acquaintances (SMD 0.21, -0.10 to 0.51); diary studies put meals with friends 29-48 percent larger; partly mediated by longer meals and perceived appropriateness; some moderation by gender, weight status and food type. Abstract read at the Bristol repository record 2026-10-07; full text not read (publisher copy 403)
  - "https://doi.org/10.1017/S0007114519000205"  # Deighton K, King AJ, Matu J, Shannon OM, Whiteman O, Long A, Huby MD, Sekula M, Holliday A. A single day of mixed-macronutrient overfeeding does not elicit compensatory appetite or energy intake responses but exaggerates postprandial lipaemia during the next day in healthy young men. Br J Nutr 2019;121(8):945-954. Counterbalanced crossover, 12 men aged 22, BMI 26: energy balance 10,755 kJ vs overfed +50 percent 16,132 kJ; next day appetite, ghrelin, GLP-1, PYY not different; ad libitum intake 6,081 vs 6,182 kJ (P=0.78); fasting NEFA lower and postprandial TAG higher after overfeeding. First page and abstract read from the publisher PDF 2026-10-07
  - "https://doi.org/10.1016/j.physbeh.2013.05.006"  # Levitsky DA, Pacanowski CR. Effect of skipping breakfast on subsequent energy intake. Physiol Behav 2013;119:9-16. Two randomised crossovers in habitual breakfast eaters and skippers: (1) no breakfast vs 335-360 kcal breakfast, lunch intake unchanged; (2) ad libitum breakfast averaging 624 kcal vs none, skipping raised lunch by 144 kcal, net deficit 408 kcal by end of day. Citation checked at Crossref; abstract read via index records 2026-10-07
  - "https://doi.org/10.3390/nu8060354"  # Headland M, Clifton PM, Carter S, Keogh JB. Weight-loss outcomes: a systematic review and meta-analysis of intermittent energy restriction trials lasting a minimum of 6 months. Nutrients 2016;8(6):354. PMC4924195. 9 trials, 981 randomised; 6 compared intermittent with continuous restriction; neither superior for weight loss. Abstract read at PMC 2026-10-07
  - "https://doi.org/10.1016/j.appet.2010.10.012"  # Adriaanse MA, Vinkers CDW, De Ridder DTD, Hox JJ, De Wit JBF. Do implementation intentions help to eat a healthy diet? A systematic review and meta-analysis of the empirical evidence. Appetite 2011;56(1):183-193. 23 studies; if-then plans raised healthy eating d=0.51 and cut unhealthy eating d=0.29. Abstract read at Europe PMC 2026-10-07; the effect for healthy eating may be inflated by weak control conditions (authors' own caveat)
  - "https://www.kyeonggi.com/article/20241028580037"  # 경기일보 2024-10-28, report of a 직장갑질119 survey (fieldwork 글로벌리서치, 2024-09-02 to 09-10, 1,000 employed adults 19+, +/-3.1 pp): 회식 frequency none 24.4 percent, 1-10 times a year 43.7, 1-3 a month 19.4, 1-2 a week 10.8, 3+ a week 1.7; of 756 who attend 회식, 23.4 percent had been pressed to drink. Advocacy-commissioned survey read through a news report; the survey report itself was not located
  - "source:nutrition/kr-eating-out-fat-loss-072 -- the general 외식 rules this row specialises; frequency, decide-before-eating, whole-dish logging, day-is-floor are not restated"
  - "source:nutrition/alcohol-training-recovery-dose-031 -- dose bands, energy-counts, food-follows-drink, protein-window, sleep and no-moralizing alcohol rules"
  - "source:nutrition/kr-alcohol-units-drinking-pattern-032 -- 잔 / 병 / 캔 conversion and the KDCA binge definitions; never a label for one night"
  - "source:nutrition/kr-restaurant-dish-energy-ranking-022 -- measured dish-class energy (튀김, 구이, 전, 찜, 탕, 찌개, 밥류, 면류) behind the 안주 and 후식 rules"
  - "source:nutrition/adherence-rules-074 -- no-all-or-nothing, bounded carry-over and weigh-as-trend, which the next-day rules defer to"
  - "source:nutrition/flexible-vs-rigid-restraint-025 -- why banking is offered as flexible redistribution, never as fasting or a punishment day"
  - "source:nutrition/weekend-drift-073 -- the next-morning weight bump is noise; compare like days"
  - "source:nutrition/portion-size-effect-intake-070 -- shared, refilled plates raise intake; the decide-before-eating lever"
  - "source:sleep-recovery/short-sleep-appetite-weight-015 -- a late 회식 shortens the night; short sleep raises next-day intake"
  - "framework:VC-E craft -- social facilitation and the redistribution equivalence are meta-analyses; the no-compensation finding is one small crossover in young men; 회식 culture is one advocacy survey; every rule is a convention routed from those rows and labelled with its basis_grade"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [not_pregnant, none]
    - key: medication_list
      type: categorical
      role: hard
      unknown_policy: block_specifics
eating_out_rules:
  - rule: hoesik-pre-commit
    surface: diet_card
    trigger: a 회식, 술자리 or dinner out is known in advance (user mention or calendar)
    action: one line the day before or that morning offering two or three if-then choices the user picks, e.g. 공기밥 or not, how many 잔, whether to go to 2차; store the choice and do not re-ask at the table
    never: [a rule list, a ban, "참아야 해요"]
    constants: at most 3 choices; one prompt per event
    basis: Adriaanse 2011 (if-then plans, d 0.29 on unhealthy eating); nutrition/portion-size-effect-intake-070
    basis_grade: C
    kind: convention
  - rule: bank-modestly
    surface: diet_card
    trigger: user asks to save calories for a 회식, or the module offers to
    action: allowed as redistribution inside the declared week -- trim the other meals that day or the day before toward a lighter plate while keeping the protein target and staying above the calorie floor; show the week total, not the day
    never: [굶고 가기, 공복으로 술자리, skipping the protein meal, crossing the calorie floor, banking across a week boundary]
    constants: same calorie floor and same-week boundary as the diet-status carry-over (074 note 2); no fixed banking kcal
    basis: Headland 2016 (spreading matched restriction unevenly loses the same weight); Levitsky 2013 (a skipped meal is not fully made up later the same day); nutrition/flexible-vs-rigid-restraint-025 (rigid restriction travels with disinhibition)
    basis_grade: C
    kind: convention
  - rule: protein-before
    surface: diet_card
    trigger: banking on a 회식 day, or any drinking evening on a cut
    action: keep a protein meal before the event; at the table protein-heavy 안주 count as the meal, not extra
    never: [drink on an empty stomach to save calories]
    constants: none
    basis: nutrition/alcohol-training-recovery-dose-031 (protein-window-blunted, food-follows-drink)
    basis_grade: C
    kind: convention
  - rule: company-eats-more
    surface: diet_card
    trigger: copy about why a 회식 ran over plan
    action: say that eating with people you know runs longer and larger for most people; it is the setting, not a lack of will; the lever is plating once and deciding the 밥 and 후식 before the meal
    never: [의지 부족, you should have said no]
    constants: none
    basis: Ruddock 2019 (friends SMD 0.76, diary meals 29-48 percent larger; colleagues sit between friends and acquaintances and were not tested as a group)
    basis_grade: B
    kind: evidence
  - rule: anju-class-default
    surface: diet_card
    trigger: user asks what to order or pick at a 술자리 / 고깃집
    action: by default favour 탕, 찌개, 찜 and 회 type 안주 over 튀김 and 전; at a 구이 table fill the plate with 쌈 vegetables and take meat from the grill onto your plate in counted pieces; the cut or fish decides, not the word 구이
    never: [a dish ban, "삼겹살은 안 돼요"]
    constants: none
    basis: nutrition/kr-restaurant-dish-energy-ranking-022 (kcal per 100 g medians: 튀김 310, 구이 267, 전 188, 찜 181, 탕 70, 찌개 61; 구이 fat share 58 percent of energy)
    basis_grade: B
    kind: convention
  - rule: finisher-is-a-meal
    surface: diet_card
    trigger: 후식 볶음밥, 냉면, 라면사리 or a 2차 with food
    action: name it as another serving -- a one-bowl rice dish median about 700 kcal, a noodle dish about 640 kcal in the measured dataset; share it or skip it by the pre-commit choice
    never: [the US 1,300 kcal restaurant figure as a Korean plate size]
    constants: none
    basis: nutrition/kr-restaurant-dish-energy-ranking-022; nutrition/alcohol-training-recovery-dose-031 (food-follows-drink, Kwok 2019)
    basis_grade: B
    kind: convention
  - rule: drinks-in-jan
    surface: diet_card
    trigger: drinks at a 회식
    action: count in 잔, 병 or 캔 and convert per 032; offer pacing levers (water or a non-alcoholic drink between rounds, keep your own glass partly full so it is not refilled); a decline is a normal choice and may be phrased however the user likes
    never: [a prescribed drink limit as a diet rule, a health benefit of drinking, 고위험음주자 or any label from one night]
    constants: none
    basis: nutrition/kr-alcohol-units-drinking-pattern-032; nutrition/alcohol-training-recovery-dose-031; 직장갑질119 survey 2024 (23.4 percent of attendees pressed to drink)
    basis_grade: D
    kind: convention
  - rule: log-next-morning-roughly
    surface: diet_card
    trigger: a 회식 day with no or partial entries
    action: one prompt next morning for dish names and 잔 count only; log whole dishes by name (072) and mark the day as a floor
    never: [a gram-by-gram reconstruction, shaving entries down, reading an unlogged 회식 as a light day]
    constants: one prompt, next morning only
    basis: nutrition/kr-eating-out-fat-loss-072 (log-as-whole-dish, day-is-floor); nutrition/unlogged-day-not-zero-019
    basis_grade: C
    kind: convention
  - rule: next-day-resume
    surface: diet_card
    trigger: the day after a 회식
    action: resume the normal plan at the next meal; if the surplus is spread, it goes over the rest of the declared week under the floor (existing carry-over), never as a fast or extra cardio; do not promise that appetite will even it out
    never: [보상 단식, 벌충, punishment cardio, "내일 덜 먹으면 돼요" as a promise, "몸이 알아서 맞춰요"]
    constants: carry-over bounds as in 074
    basis: Deighton 2019 (no next-day appetite or intake compensation after +50 percent); nutrition/adherence-rules-074 (no-all-or-nothing); nutrition/flexible-vs-rigid-restraint-025
    basis_grade: C
    kind: convention
  - rule: morning-weight-not-fat
    surface: both
    trigger: a weight reading the morning or two after a 회식
    action: do not comment on it alone; a salty, late, larger meal and drinks move the scale through water and gut content; read the weekly mean or same weekday
    never: [오늘 n kg 쪘어요, a fat-gain estimate from the scale]
    constants: none
    basis: nutrition/weekend-drift-073; nutrition/adherence-rules-074 (weigh-as-trend)
    basis_grade: C
    kind: convention
  - rule: short-night-next-day
    surface: diet_card
    trigger: 회식 ending late on a work night
    action: the next day may be hungrier after a short night; plan a protein breakfast and a set lunch rather than relying on willpower; no nightcap to sleep
    never: [sleep is optional, drink to sleep]
    constants: none
    basis: sleep-recovery/short-sleep-appetite-weight-015 (restricted sleep raises intake about 385 kcal a day); nutrition/alcohol-training-recovery-dose-031 (sleep-not-a-sleep-aid)
    basis_grade: B
    kind: evidence
  - rule: count-not-event
    surface: weekly_retro
    trigger: two or more 회식 or 술자리 logged in the week
    action: name the weekly count and their share of the week's surplus in the user's own numbers, once; no comment on any single event
    never: [회식 줄이세요 as an order, a per-event verdict]
    constants: threshold 2 per week (product constant)
    basis: nutrition/kr-eating-out-fat-loss-072 (frequency-is-the-lever)
    basis_grade: C
    kind: convention
  - rule: no-moralizing
    surface: both
    trigger: every 회식 mention
    action: same tone as any meal: what was eaten, roughly what it adds to the week, one lever for next time; 회식 is part of working life, not a lapse
    never: [치팅, 실패, 망쳤다, 반성, 죄책감, 참았어야, 의지]
    constants: none
    basis: nutrition/adherence-rules-074 (no-all-or-nothing); nutrition/alcohol-training-recovery-dose-031 (no-moralizing)
    basis_grade: D
    kind: convention
  - rule: banking-exit
    surface: diet_card
    trigger: user mentions a disordered-eating history, compensatory fasting or purging, or distress about eating out
    action: do not offer banking or next-day trimming at all; keep the normal plan and the general eating-out lines
    never: [save calories for tonight]
    constants: none
    basis: nutrition/adherence-rules-074 (weighing-exit; no ED axis on the ledger)
    basis_grade: D
    kind: convention
refraction_notes:
  - axis: primary_goal
    note: >
      For a user who is not cutting, none of the banking, logging or count
      rules fire unprompted. A 회식 for a maintenance user is a meal.
    grade: D
  - note: >
      BANKING IS REDISTRIBUTION, NOT A HACK. Trials of six months or more
      found the same weight loss when a matched restriction was spread
      unevenly as when it was spread evenly, so eating lighter earlier in
      the week to leave room for a 회식 is arithmetically fine. Nothing here
      tested banking for a single evening, and skipping a meal beforehand
      was only partly compensated in small crossovers, so the rule permits
      a lighter plate, keeps protein and the floor, and does not endorse
      arriving starving.
    grade: C
  - note: >
      THE BODY DOES NOT EVEN IT OUT FOR YOU. After a day 50 percent over
      requirement, twelve young men were no less hungry and ate the same the
      next day. One small trial in lean-to-overweight young men; it supports
      saying "do not count on it evening out" and nothing about women, older
      adults or dieters.
    grade: C
  - note: >
      COMPANY RAISES INTAKE. Across 42 studies people ate more with friends
      and family than alone; with strangers the effect was not shown.
      Colleagues at a 회식 are neither group cleanly. Speak it as "eating
      together usually runs larger", not as a percentage for this user.
    grade: B
  - note: >
      KOREAN 회식 NUMBERS ARE THIN. One commissioned survey of 1,000 workers
      (read through a news report) found about one in ten attending 회식
      weekly or more and about a quarter of attendees pressed to drink. It
      sets context only; never quote it as the user's situation.
    grade: D
  - note: >
      PREGNANCY OR MEDICATION UNKNOWN -> no drink counts or amounts
      (block_specifics, as in 031); the food rules still apply.
    grade: D
claim: >
  A 회식 on a cut is handled by planning, not by restriction or penance.
  Eating with familiar people raises intake (a meta-analysis of 42 studies:
  more with friends than alone, meals 29-48 percent larger in diary
  studies), so the lever is a few decisions made beforehand -- 밥, 잔 count,
  2차 -- which if-then planning modestly supports. Saving calories ahead is
  arithmetically sound as redistribution within the week, because trials of
  six months or more found intermittent and even restriction equally
  effective, but it should mean a lighter plate with protein kept, not an
  empty stomach. After the event the body does not compensate on its own:
  one day 50 percent over requirement left next-day appetite and intake
  unchanged in a small crossover. So the next day resumes the normal plan
  at the next meal, any spreading stays within the week above the floor,
  the morning weight is not read alone, and nothing is phrased as failure.
  안주 choices lean on the measured Korean dish classes (fried and grilled
  dishes are the most energy-dense; soups and stews the least; a 볶음밥 or
  냉면 finisher is a full serving), and drinks are counted in 잔 with
  pacing levers and no labels.
reasoning: >
  The domain already had the parts: general 외식 rules (072), alcohol dose
  and energy (031, 032), dish energy (022) and adherence copy (074). What
  was missing was the 회식 as one planned event with a before, a table and
  an after, and the question users actually ask -- "can I save calories for
  tonight?" and "will I eat less tomorrow?". The two directional answers
  rest on meta-analyses (social facilitation; intermittent vs continuous
  restriction), so those are carried at the randomised/pooled band for
  direction only. The two answers about compensation (a skipped meal before,
  an overfed day after) rest on small crossovers and stay observational
  in weight. The cultural context is one advocacy-commissioned survey seen
  through a news report and sits in the practitioner band; it explains why
  drink pressure needs a neutral rule and is never used as a number about
  the user. All rules route to existing graded rows, so the item as a whole
  is a synthesis. Deliberately not here: a banking kcal figure (none is
  tested), Korean pork-cut energy values (the national composition table
  was not read at source; see GAPS), hangover-food claims (not searched to
  primary), and any rule that would reward fasting.
---

# nutrition/kr-hoesik-cut-rules-080 -- 감량 중 회식

**One line:** 회식은 미리 몇 가지만 정해 두고, 다음 날은 다음 끼니부터 평소대로. 굶어서 미리 갚거나
나중에 벌충하지 않는다.

What this row adds to 072 (외식 일반), 031/032 (술) and 074 (지속 규칙):

- **Company.** People eat more with friends and family than alone, across 42
  studies; with strangers the effect did not show. A 회식 runs longer and
  larger for most people. That is the setting, not a failure of will.
- **Banking.** Spreading a fixed weekly restriction unevenly loses the same
  weight as spreading it evenly, in trials of six months or more. So a lighter
  plate earlier to leave room is fine. Skipping a meal was only partly made up
  later in small crossovers, but arriving starving at a 술자리 is the pattern
  rigid-restraint research warns about; keep protein and the calorie floor.
- **After.** One day at 50 percent over requirement did not make twelve young
  men less hungry or eat less the next day. Do not count on it evening out;
  do not punish it either. Resume at the next meal.

| Rule | Surface | Trigger | Action |
|---|---|---|---|
| hoesik-pre-commit | diet card | 회식 known ahead | 2-3 if-then choices once (밥, 잔, 2차) |
| bank-modestly | diet card | user asks to save calories | lighter plate within the week, protein and floor kept |
| protein-before | diet card | banking / drinking evening | a protein meal before; no empty-stomach drinking |
| company-eats-more | diet card | "why did I go over" | setting raises intake; plate once |
| anju-class-default | diet card | what to order | 탕/찌개/찜/회 over 튀김/전; count grill pieces, fill with 쌈 |
| finisher-is-a-meal | diet card | 볶음밥, 냉면, 2차 food | another serving (~700 / ~640 kcal medians) |
| drinks-in-jan | diet card | drinks | count in 잔; pacing levers; declining is normal |
| log-next-morning-roughly | diet card | unlogged 회식 | names and 잔 only; day is a floor |
| next-day-resume | diet card | day after | next meal normal; week carry-over only |
| morning-weight-not-fat | both | weight after 회식 | not read alone |
| short-night-next-day | diet card | late night | plan protein breakfast and lunch |
| count-not-event | weekly retro | 2+ 회식 in a week | name the count once, own numbers |
| no-moralizing | both | every mention | no 치팅 / 실패 / 반성 |
| banking-exit | diet card | ED history, compensatory fasting | no banking or trimming offered |

## 한국어 요약 (답변용)

- 아는 사람들과 먹으면 대부분 더 먹는다. 42개 연구를 모은 분석에서 친구·가족과 먹을 때가 혼자
  먹을 때보다 많았고, 일기 연구에서는 한 끼가 29~48% 컸다. 낯선 사람과는 차이가 없었다. 회식에서
  더 먹은 건 의지 문제가 아니라 자리의 영향이다.
- 회식이 잡혀 있으면 전날이나 당일 아침에 두세 가지만 정해 둔다. 공기밥을 먹을지, 몇 잔까지
  마실지, 2차를 갈지. 자리에서 다시 묻지 않는다.
- "미리 칼로리를 아껴 둬도 되나요?"에는 된다고 답한다. 같은 양을 줄인다면 주중에 고르게
  나누든 몰아서 하든 6개월 이상 연구에서 감량 결과가 같았다. 다만 그날이나 전날 끼니를 가볍게
  하는 정도로, 단백질은 지키고 하한선 아래로 내려가지 않는다. 굶고 가거나 빈속에 술을 마시는
  방식은 권하지 않는다. 섭식 문제 이력이 있거나 보상 단식을 언급한 사용자에게는 이 제안 자체를
  하지 않는다.
- 안주는 기본적으로 탕·찌개·찜·회 쪽이 튀김·전보다 가볍다. 식약처 실측 외식 자료에서 100 g당
  튀김류 310, 구이류 267, 전류 188, 탕류 70, 찌개류 61 kcal(중앙값)였다. 고깃집에서는 쌈 채소를
  먼저 채우고 고기는 내 접시에 몇 점인지 세며 덜어 먹는다. '구이'라는 이름보다 부위와 생선 종류가
  더 중요하다.
- 후식 볶음밥·냉면·라면사리나 2차 안주는 '한 끼가 더'다. 실측 자료에서 한 그릇 밥 요리는 약
  700 kcal, 면 요리는 약 640 kcal(중앙값)였다. 미리 정한 대로 나눠 먹거나 넘긴다.
- 술은 잔·병·캔으로 세고(032 환산), 사이사이 물이나 무알코올 음료, 잔을 조금 채워 두어 계속
  따르지 않게 하는 방법을 제안할 수 있다. 거절은 평범한 선택이다. 한 번의 술자리로
  고위험음주자 같은 꼬리표를 붙이지 않는다. 임신 여부나 복용 약을 모르면 잔 수 같은 숫자는
  말하지 않는다.
- 다음 날은 다음 끼니부터 평소 계획대로 먹는다. 하루 필요량보다 50% 더 먹은 다음 날에도 배고픔과
  먹는 양이 줄지 않았다는 실험이 있다(젊은 남성 12명). "몸이 알아서 맞춘다"고 말하지 않고,
  굶거나 운동으로 벌충하라고도 하지 않는다. 남은 차이는 이번 주 안에서, 하한선 위로만 나눈다.
- 회식 다음 날 아침 체중은 짠 음식, 늦은 식사, 술 때문에 오른 물과 장 내용물이 섞여 있다. 그
  숫자 하나로 말하지 않고 주 평균이나 같은 요일끼리 비교한다.
- 늦게 끝나 잠이 짧았다면 다음 날 더 배고플 수 있다(잠을 줄이면 하루 약 385 kcal 더 먹었다는
  분석). 아침 단백질과 점심 메뉴를 미리 정해 둔다. 잠들려고 마시는 술은 수면에 도움이 되지 않는다.
- 기록은 다음 날 아침 한 번, 음식 이름과 잔 수만 묻는다. 그날 합계는 하한선으로 둔다.
- 한 주에 회식이 두 번 이상이면 주간 회고에서 횟수와 그 몫을 사용자 숫자로 한 번만 짚는다. 회식
  하나하나를 평가하지 않는다.
- 말투: 치팅, 실패, 망쳤다, 반성, 참았어야 같은 말은 쓰지 않는다. 회식은 직장 생활의 일부다.
- 한국 회식 실태 수치는 얇다. 직장인 1,000명 조사(뉴스 보도로만 확인)에서 주 1회 이상 회식이
  12.5%, 회식 참석자 중 23.4%가 음주 강요를 경험했다. 배경일 뿐 사용자에게 적용하지 않는다.
