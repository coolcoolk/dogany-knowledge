---
# Caffeine / early-training sprint 2026-10-07. Fills the two caffeine questions the v37
# rows left open: TOLERANCE (does a daily user still get the dawn benefit,
# does a daily habit cost night sleep, is the morning "lift" from coffee real
# or withdrawal relief) and the SHORT NIGHT (does caffeine cover for one,
# and for how many). Dose, onset timing and the bedtime cutoff table are NOT
# repeated here: 069 owns the dawn dose, 070 owns the dose x hours-before-bed
# table, 071 / 072 / 073 own the morning rules. Every source below was read
# at PubMed, PMC or the publisher on 2026-10-07; no number is reconstructed
# from memory. Rubric: sleep-recovery @clinical (VC-A).
id: sleep-recovery/caffeine-tolerance-short-night-082
domain: sleep-recovery
grade: B (habitual intake does not remove the acute ergogenic effect; 3-6 mg/kg works, above 6 mg/kg adds nothing); C (daily dosing shrinks but does not erase the effect over about three weeks); C (daily daytime caffeine ending 8 h or more before bed left sleep structure unchanged in habitual users); C (caffeine protected skill after one 3-5 h night); B (twice-daily caffeine stopped protecting alertness after about three nights of 5 h and slowed recovery); C (alertness gains in habitual users are largely withdrawal relief); D (the short-night afternoon top-up as the loop to break)
lane: "@clinical"
locale: universal
as_of: 2005-2025
contested: no
sources:
  - "https://doi.org/10.1007/s40279-022-01685-0"  # Carvalho A, Marticorena FM, Grecco BH, Barreto G, Saunders B. 2022, Sports Med 52(9):2209-2220 -- systematic review and meta-analysis, 60 studies: caffeine vs placebo SMD 0.25 (95% CI 0.20-0.30), no moderation by relative habitual intake (p = 0.59); effective below 3 and at 3-6 mg/kg, not above 6 mg/kg; holds in men, women, trained, untrained, irrespective of withdrawal period
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC6343867/"  # Lara B, Ruiz-Moreno C, Salinero JJ, Del Coso J. 2019, PLoS One 14(1):e0210275, doi 10.1371/journal.pone.0210275, PMID 30673725 -- double-blind crossover, 11 active LOW consumers (< 50 mg/day), 3 mg/kg at 09:00 for 20 days: peak power +4.0% (incremental) and +4.9% (Wingate) on day 1, largest on day 1 and progressively smaller; significant to day 15 (incremental) and day 18 (Wingate); small-to-moderate effect sizes still present on day 20
  - "https://doi.org/10.1038/s41598-021-84088-x"  # Weibel J, Lin YS, Landolt HP, Kistler J, Rehm S, Rentsch KM, Slawik H, Borgwardt S, Cajochen C, Reichert CF. 2021, Sci Rep 11:4668, PMCID PMC7907384 -- double-blind crossover, 20 men, habitual 478 mg/day; 3 x 150 mg at 45, 255 and 475 min after waking for 10 days (last dose 8 h before bed) vs placebo vs withdrawal: total sleep, latency, slow-wave sleep, slow-wave activity and subjective quality not different; sigma activity lower under caffeine AND withdrawal
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC3049131/"  # Cook CJ, Crewther BT, Kilduff LP, Drawer S, Gaviglio CM. 2011, J Int Soc Sports Nutr 8:2, doi 10.1186/1550-2783-8-2, PMID 21324203 -- 10 elite rugby backs (low caffeine users), 3-5 h vs 7-9 h sleep, 1 or 5 mg/kg caffeine at 10:00, passing test 11:30: placebo accuracy fell after the short night, both caffeine doses prevented the fall, no difference between 1 and 5 mg/kg
  - "https://doi.org/10.1093/sleep/zsx171"  # Doty TJ, So CJ, Bergman EM, Trach SK, Ratcliffe RH, Yarnell AM, Capaldi VF, Moon JE, Balkin TJ, Quartana PJ. 2017, Sleep 40(12) -- 48 healthy sleepers in the laboratory, 5 nights of 5 h time in bed, 200 mg gum at 08:00 and 12:00 vs placebo: vigilance kept for the first 3 days, gone by day 4; wakefulness advantage gone after night 2; slower return to baseline during 3 recovery nights
  - "https://pubmed.ncbi.nlm.nih.gov/16001109/"  # James JE, Rogers PJ. 2005, Psychopharmacology 182:1-8, doi 10.1007/s00213-005-0084-6 -- review of consumer vs non-consumer, pre-treatment and long-term withdrawal designs: little evidence of net performance or mood benefit under long-term use vs abstinence; effects largely reversal of overnight withdrawal
  - "https://pubmed.ncbi.nlm.nih.gov/17950009/"  # Roehrs T, Roth T. 2008, Sleep Med Rev 12(2):153-162 -- review: caffeine clearly improves alertness under sleep deprivation, restriction or shift schedules; under habitual sleep it mostly restores performance lowered by sleepiness or by overnight withdrawal; regular dietary intake associates with disturbed sleep in population studies
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC12473705/"  # Kocak A, Georgousopoulou E, Knight-Agarwal CR, Matthews R, Minehan M. 2025, Sports (Basel) 13(9):317, doi 10.3390/sports13090317, PMID 41003623 -- 10 studies, 128 athletes, 3-6 mg/kg taken 16:00-19:45: sleep efficiency -4.87% (95% CI -7.45 to -2.29; not robust in sensitivity analysis), total sleep -32 min (CI crosses zero); GRADE low to very low; athletes reported worse sleep more consistently than the monitors showed
  - "sleep-recovery/caffeine-bedtime-cutoff-070"  # owns the dose x hours-before-bed table this item does not repeat
  - "exercise/early-morning-caffeine-food-069"  # owns the dawn dose (3-6 mg/kg, 200 mg single-dose ceiling)
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # what a short night costs before caffeine enters
  - "sleep-recovery/nap-force-null-shuttle-signal-009"  # the alternative to an afternoon top-up
  - "sleep-recovery/brief-sleep-training-rules-072"  # repeated-short-nights pattern rule this item's Doty row supports
  - "framework:GRADE -- Carvalho 2022 pools 60 placebo-controlled trials for the habitual-intake moderator (B; habitual intake is self-reported and the moderator test is between-study). Lara 2019 is one n=11 crossover in low consumers (C). Weibel 2021 is a well-controlled n=20 crossover with polysomnography, downgraded for an all-male, high-intake sample and one recorded night per arm (C). Cook 2011 is n=10 on one skill task (C). Doty 2017 is a laboratory RCT with n=48 and an objective vigilance endpoint (B; cognitive, not exercise, outcome). James & Rogers 2005 and Roehrs & Roth 2008 are narrative reviews (C). Kocak 2025 is rated low to very low by its own authors (C at best, used as corroboration of 070 only)."
applicability:
  axes:
    - key: caffeine_sensitivity
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [not_pregnant, none]
refraction_notes:
  - note: >
      A DAILY HABIT DOES NOT CANCEL THE PRE-SESSION DOSE. Across 60 trials
      the acute effect of caffeine on exercise (small, SMD 0.25) did not
      depend on how much caffeine people usually took, in men or women,
      trained or not, and whether or not they abstained beforehand. Doses
      below 3 and at 3-6 mg/kg worked; above 6 mg/kg did not add a
      detectable effect. So a heavy coffee drinker does not need a bigger
      pre-session dose, and does not need a "washout" to get the effect.
      Habitual intake was self-reported and compared between studies.
    grade: B
  - note: >
      DAILY DOSING STILL SHRINKS IT A LITTLE. In 11 low consumers who took
      3 mg/kg every morning for 20 days, the power gain was largest on day 1
      and declined; it stayed statistically significant to day 15-18, and a
      small-to-moderate effect remained on day 20. Read with the pooled
      result above: partial tolerance is real, total loss is not shown.
    grade: C
  - note: >
      THE MORNING LIFT IN A HABITUAL USER IS PARTLY RELIEF. For alertness and
      mood (not muscle performance), the reviews conclude that under
      long-term use most of what coffee seems to add in the morning is the
      reversal of overnight withdrawal; under normal sleep caffeine mostly
      restores what sleepiness or withdrawal took. The practical reading for
      a dawn lifter: a habitual user who skips the usual morning coffee
      starts BELOW baseline, and the dull start is not lost fitness.
    grade: C
  - note: >
      DAYTIME HABIT, NIGHT SLEEP. In 20 habitual users (about 480 mg a day),
      150 mg three times a day with the last dose 8 hours before bed did not
      change total sleep, time to fall asleep, deep sleep or how well they
      felt they slept, compared with placebo. One spectral marker (sigma)
      was lower under caffeine and under one day of withdrawal alike. So a
      morning-weighted daily habit is not, on this evidence, the night-sleep
      problem; a late dose is (070). All-male, one night per arm.
    grade: C
  - note: >
      ONE SHORT NIGHT: CAFFEINE COVERS SOME OF IT. After a 3-5 hour night,
      elite rugby players' passing accuracy fell on placebo and did not fall
      with 1 or 5 mg/kg caffeine 1.5 h before -- and the low dose did as well
      as the high one. Reviews agree that caffeine restores alertness lost to
      restricted sleep. This supports the usual dose before a morning session
      after a short night; it does not support a bigger dose.
    grade: C
  - note: >
      SEVERAL SHORT NIGHTS: IT STOPS COVERING. With 5 hours in bed for five
      nights, 200 mg twice a day kept vigilance up for three days and not
      after; the wakefulness advantage was gone after the second night, and
      the caffeine group came back to baseline more slowly over three
      recovery nights. Caffeine masks a short night; it does not repay a run
      of them. Cognitive endpoints, laboratory setting.
    grade: B
  - note: >
      THE LOOP TO BREAK. After a short night the morning dose before training
      is far from bedtime and costs little (070). The extra afternoon coffee
      to get through the day is the dose that can reach tonight's sleep, and
      an early riser's early bedtime moves that cutoff earlier. The loop --
      short night, afternoon top-up, shorter next night -- is a synthesis of
      070's cutoff table and this item's rows, not a tested sequence. A nap
      (009) is the first alternative.
    grade: D
  - note: >
      LATE SESSIONS, ATHLETE DATA. In athletes, 3-6 mg/kg taken before a late
      afternoon or evening session lowered sleep efficiency by about 5
      percent, with a non-significant 32-minute drop in total sleep; the
      review's authors rate this low to very low certainty, and athletes
      reported worse sleep more consistently than devices measured it. It
      agrees in direction with 070 and changes none of its numbers. The same
      review advises longer gaps for oral-contraceptive users; that is its
      authors' advice, not a tested cutoff.
    grade: C
claim: >
  Tolerance and short nights change less about early-morning caffeine than
  people expect. A daily habit does not cancel the acute exercise benefit of
  a pre-session dose (60 trials, no moderation by habitual intake; 3-6 mg/kg
  works, more than 6 mg/kg adds nothing), though daily dosing shrinks it
  somewhat over about three weeks in low consumers. In habitual users, much
  of the morning alertness from coffee is relief of overnight withdrawal, so
  skipping the usual coffee starts the session below baseline. A
  morning-weighted daily habit with the last dose about 8 hours before bed did
  not change measured or felt sleep in habitual users. After one short night
  the usual dose protects some performance (1 mg/kg did as well as 5 in one
  trial), but across a run of 5-hour nights twice-daily caffeine stopped
  protecting alertness after about three days and slowed recovery. The
  practical risk after a short night is the afternoon top-up, which reaches
  tonight's sleep; the morning dose does not.
reasoning: >
  The habitual-intake question has a pooled answer (Carvalho 2022, 60
  trials), which is why "no bigger dose, no washout needed" is B; the
  single within-person tolerance trial (Lara 2019) is small and in low
  consumers and is used only to say tolerance is partial. James & Rogers
  2005 and Roehrs & Roth 2008 are reviews and carry the withdrawal-relief
  reading at C; their scope is alertness and mood, not exercise, and the item
  keeps the two apart -- there is no contradiction between "habit does not
  cancel the exercise effect" and "habit turns the alertness effect into
  withdrawal relief", because they measure different outcomes. Weibel 2021 is
  the cleanest test of a daily habit against sleep and is downgraded for its
  sample. For short nights, Cook 2011 is the only athletic-skill trial found
  and is small; Doty 2017 is larger and laboratory-controlled but measures
  vigilance, so its "about three nights" is transferred to training as a
  direction, not a number. The afternoon-loop note is labelled D because no
  study tested the sequence. Kocak 2025 is added only as athlete-specific
  corroboration of 070's direction. Not contested within these sources.
---

# sleep-recovery/caffeine-tolerance-short-night-082 -- 매일 마시는 카페인과 짧게 잔 날의 카페인

**One line:** a daily coffee habit does not cancel the pre-session dose and a
morning-weighted habit does not cost night sleep; after a short night the
usual dose helps, a bigger one does not, and caffeine stops covering a run of
short nights after about three.

## What the sources show

| Question | Answer | Strength |
|---|---|---|
| Daily user: does the pre-session dose still work? | yes; habitual intake did not change the effect across 60 trials | pooled trials |
| Daily dosing for weeks | effect shrinks, still present at day 20 (one small trial) | small trial |
| Bigger dose for a heavy user? | no; above 6 mg/kg added nothing | pooled trials |
| Morning alertness from coffee in a daily user | largely relief of overnight withdrawal | reviews |
| Daily habit, last dose 8 h before bed | sleep unchanged vs placebo (20 men) | one good trial |
| One 3-5 h night | 1 or 5 mg/kg prevented a skill drop (10 players) | small trial |
| Five 5 h nights | 200 mg twice a day stopped helping alertness after about 3 days | lab trial |
| Short night, afternoon top-up | the dose that reaches tonight's sleep | synthesis |

Dose, onset and the bedtime cutoff are in 069 and 070; this item adds only
what tolerance and short nights change.

## 한국어 요약 (답변용)

- 커피를 매일 마셔도 운동 전 카페인 효과는 사라지지 않는다. 60편을 모은 분석에서 평소 섭취량은 효과
  크기를 바꾸지 않았다. 체중 1kg당 3mg 미만과 3~6mg에서 효과가 있었고 6mg을 넘으면 더 나아지지
  않았다. 많이 마시는 사람이라고 양을 늘릴 필요도, 미리 끊을 필요도 없다.
- 매일 같은 양을 먹으면 효과가 조금씩 줄기는 한다. 평소 거의 안 마시던 11명이 20일 동안 매일
  먹었을 때 첫날 효과가 가장 컸고, 20일째에도 작은 효과는 남아 있었다.
- 매일 마시는 사람이 아침 커피로 느끼는 개운함은 상당 부분 밤사이 생긴 금단 증상이 풀리는 것이다.
  평소 마시던 커피를 거르면 평소보다 낮은 상태에서 시작한다. 몸이 둔한 건 체력이 떨어져서가 아니다.
- 아침·낮에 나눠 마시고 마지막 잔이 잠들기 8시간 전이면, 하루 450mg을 마신 남성 20명의 수면 길이와
  깊은 잠, 체감 수면에 차이가 없었다. 문제는 하루 습관이 아니라 늦게 마신 한 잔이다(070).
- 3~5시간만 잔 다음 날, 평소 양의 카페인은 기술 수행이 떨어지는 걸 막았다(럭비 선수 10명,
  1mg/kg와 5mg/kg 효과가 같았다). 짧게 잤다고 양을 늘릴 이유는 없다.
- 5시간씩 닷새를 자면 하루 두 번 200mg도 사흘쯤 지나 효과가 사라졌고, 회복도 더 느렸다. 카페인은
  하룻밤 부족은 가려 주지만 며칠 쌓인 부족은 메우지 못한다.
- 짧게 잔 날 조심할 것은 아침 운동 전 커피가 아니라 오후에 추가로 마시는 한 잔이다. 그 한 잔이 오늘
  밤잠을 줄이고 다음 날을 또 짧게 만든다. 오후에는 커피보다 낮잠을 먼저 권한다. 이 연결 고리는 연구를
  이어 붙인 판단이고 직접 시험한 연구는 없다.
- 임신 중이면 구체적인 양을 말하지 않는다.
