---
# Goal-calorie sprint 2026-10-08 (
# block 755..759). Owns the STARTING number: how a maintenance (energy-balance)
# estimate is made at goal-setting time and how far it can be trusted for one
# person. 756 owns what a deficit then does to weight over time; 757 is the
# engine rule set. Abstracts re-read via PubMed E-utilities on 2026-10-08
# (Frankenfield 2005, Mifflin 1990, Sanghvi 2015, Park 2020, Park 2023, Kim
# 2015). The Frankenfield per-equation hit rates are in the paywalled full
# text and were NOT read; only the abstract's ranking is carried.
id: nutrition/maintenance-estimate-calibration-755
domain: nutrition
lane: "@obs-inferential"
grade: B (equation error for individuals is directly measured; the calibration rule built on it is product judgement)
locale: universal
as_of: 1990-2023
contested: no
sources:
  - "https://doi.org/10.1016/j.jada.2005.02.005"  # Frankenfield D, Roth-Yousey L, Compher C. Comparison of predictive equations for resting metabolic rate in healthy nonobese and obese adults: a systematic review. J Am Diet Assoc 2005;105(5):775-789. PMID 15883556 -- Mifflin-St Jeor most often within 10% of measured RMR of the four common equations, narrowest error range; "noteworthy errors" in individuals; older adults and ethnic minorities underrepresented
  - "https://doi.org/10.1093/ajcn/51.2.241"  # Mifflin MD, St Jeor ST, Hill LA, Scott BJ, Daugherty SA, Koh YO. A new predictive equation for resting energy expenditure in healthy individuals. Am J Clin Nutr 1990;51(2):241-247. PMID 2305711 -- n=498, aged 19-78, R2 0.71; men 10W + 6.25H - 5A + 5, women the same - 161; Harris-Benedict overestimated by 5%
  - "https://doi.org/10.20463/pan.2020.0002"  # Park HY, Jung WS, Hwang H, Kim SW, Kim J, Lim K. Predicting the resting metabolic rate of young and middle-aged healthy Korean adults: a preliminary study. Phys Act Nutr 2020;24(1):9-13. PMID 32408408 -- n=53 Korean adults; FFM-based equation SEE about 210-220 kcal/day
  - "https://doi.org/10.4162/nrp.2023.17.3.464"  # Park JS, Cho SR, Yim JE. Resting energy expenditure in Korean type 2 diabetes patients: comparison between measured and predicted values. Nutr Res Pract 2023;17(3):464-474. PMID 37266123 -- n=36; Mifflin showed the LARGEST difference from measured REE, FAO/WHO the closest
  - "https://doi.org/10.4162/nrp.2015.9.1.71"  # Kim EK, Yeon SE, Lee SH, Choe JS. Nutr Res Pract 2015;9(1):71-78. PMID 25671071 -- 72 Korean farmers: activity level (PAL) shifted between seasons and the KDRI 2010 EER equation underestimated measured TEE
  - "https://doi.org/10.3945/ajcn.115.111070"  # Sanghvi A, Redman LM, Martin CK, Ravussin E, Hall KD. Validation of an inexpensive and accurate mathematical method to measure long-term changes in free-living energy intake. Am J Clin Nutr 2015;102(2):353-358. PMID 26040640 -- CALERIE, n=140: change in intake from repeated weights alone within 40 kcal/day of DLW/DXA on average; individual RMSD 215 kcal/day
  - "nutrition/self-report-underreporting-007"  # logged intake is a floor; a back-calculation from logs inherits that bias
  - "nutrition/body-measure-reading-rules-029"  # the 7-day mean weight and confirmed-trend rules any calibration must read through
  - "nutrition/deficit-weight-dynamics-756"  # what a deficit does to weight over time; why early weeks mislead
  - "nutrition/goal-calorie-rules-757"  # the engine rules that use this estimate
applicability:
  axes:
    - key: sex
      type: categorical
      role: soft
      unknown_policy: ask
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: ask
    - key: height_cm
      type: numeric
      role: soft
      unknown_policy: ask
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: ask
    - key: activity_level
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: body_fat_pct
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE BEST EQUATION IS STILL A GUESS FOR ONE PERSON. Of the four equations
      in common clinical use, Mifflin-St Jeor most often landed within 10
      percent of measured resting rate and had the narrowest error range. The
      same review warns of noteworthy individual errors and says older adults
      and ethnic minorities were underrepresented in both building and testing
      the equations. Speak the first maintenance number as a starting estimate
      with a band of about plus or minus 10 percent, never as the user's
      metabolism.
    grade: B
  - note: >
      KOREAN ADULTS: NO VALIDATED WINNER. Korean samples are small. In 36
      Korean adults with type 2 diabetes, Mifflin was the furthest of five
      equations from measured REE and FAO/WHO the closest. A 53-person Korean
      study built an FFM-based equation with a standard error of about 210-220
      kcal/day. No study located tests Mifflin against measured REE in
      healthy Korean adults of normal weight. Keep Mifflin as the default
      because it needs no body-composition input, and widen the hedge rather
      than swap equations on this evidence (GAPS.md).
    grade: C
  - note: >
      THE ACTIVITY MULTIPLIER IS THE LARGER ERROR. Resting rate is the part
      that can be predicted. The activity factor that turns it into a daily
      total is self-chosen from a category and can move with season or job:
      in Korean farmers, activity level differed between seasons and the
      national EER equation underestimated measured total expenditure. A user
      who picks a higher category than their week supports inflates the
      target more than any equation choice does.
    grade: C
  - note: >
      THE SCALE CALIBRATES BETTER THAN THE FORMULA. In the CALERIE trial,
      change in intake estimated from repeated body weights alone, through a
      validated model, came within 40 kcal/day of the doubly-labelled-water
      method on average, though about 215 kcal/day apart for a single person.
      The practical form: after the first two to three weeks, the weight trend
      against logged intake corrects the starting estimate. Because logged
      intake runs low (007), a back-calculated maintenance from logs comes out
      low too. Speak it as the user's apparent maintenance at their logging
      habits, not their true expenditure.
    grade: C
claim: >
  A starting maintenance estimate is resting energy from a prediction
  equation multiplied by an activity factor. Of the four common equations,
  Mifflin-St Jeor (men 10 x kg + 6.25 x cm - 5 x age + 5; women the same
  minus 161) most often predicts measured resting rate within 10 percent and
  has the narrowest error range, but individual errors remain noteworthy, and
  older adults and non-white groups were underrepresented in its validation.
  In small Korean samples Mifflin did not perform best, and no equation is
  validated for healthy Korean adults. The activity factor, chosen from a
  category, adds error that can exceed the equation's. Repeated body weights
  calibrate intake better than any formula: a model fed only weights tracked
  intake change within 40 kcal/day on average. So the first calorie target is
  a hypothesis to be corrected by two to three weeks of weight trend, not a
  measurement.
reasoning: >
  The equation evidence is a systematic review of individual-level
  validation data, which supports the direction firmly. The +/-10 percent
  band is what that review uses as its accuracy criterion; it is not a
  guarantee that a given user falls inside it. The Korean rows are small,
  one is in people with diabetes, and they disagree with the Western ranking,
  so they are carried as a hedge note at C rather than used to swap the
  default equation. The calibration note rests on one well-run validation
  in a trial population over two years; for a free-living app user over a few
  weeks the method is noisier (water shifts, 756) and the logged intake is
  biased low (007). Hence the item's grade splits: the error is measured, the
  correction cadence is judgement and lives in 757 as product constants.
---

# nutrition/maintenance-estimate-calibration-755 -- 유지 칼로리 첫 추정과 보정

**한 줄 그림:** 처음 정하는 하루 칼로리는 공식으로 낸 추정치이고, 2-3주 체중 흐름으로 고쳐 가는
가설이다.

A calorie target set on day one starts from an estimate of maintenance: resting
energy from an equation, times an activity factor. The equation most often used,
Mifflin-St Jeor, did best of four common equations in a systematic review, landing
within ten percent of measured resting rate more often than the others. That is
still a band, and the review says individual errors are noteworthy and that older
people and non-white groups were thinly represented.

For Korean users the evidence is thinner. Two small Korean studies did not find
Mifflin the closest equation, one of them in adults with diabetes. No study tested
it in healthy, normal-weight Korean adults, so the default stays and the hedge
widens.

The bigger error usually comes from the activity factor, which the user picks from
a category. The fix is not a better formula but the scale: after two to three weeks,
the weekly weight trend against logged intake says more about this person's
maintenance than any equation. Logs run low, so a maintenance figure worked back
from them is "apparent maintenance at your logging habits", not a lab value.

## 한국어 요약 (답변용)

- 처음 제시하는 유지 칼로리는 **추정치**다. 기초대사량 공식(Mifflin-St Jeor)에 활동 계수를 곱해
  낸다. 이 공식은 흔히 쓰는 넷 중 실제 측정값의 ±10% 안에 드는 경우가 가장 많았지만, 개인에 따라
  그보다 크게 빗나갈 수 있다.
- 한국인 대상 검증은 적다. 소규모 국내 연구에서 Mifflin이 가장 정확하지 않았던 결과도 있다(당뇨
  환자 36명). 건강한 한국 성인에서 검증된 공식은 아직 없다. 그래서 공식은 그대로 쓰고 "대략"이라는
  단서를 더 분명히 붙인다.
- 오차가 더 큰 쪽은 활동 수준을 고르는 단계다. 실제 한 주보다 높은 활동 단계를 고르면 목표
  칼로리가 부풀려진다.
- 2-3주 지나면 공식보다 체중 흐름이 더 정확하다. 기록한 섭취량과 주간 평균 체중 변화를 맞춰 보고
  목표를 고친다. 기록은 실제보다 적게 잡히는 경향이 있어서, 이렇게 거꾸로 계산한 값은 "지금 기록
  습관 기준의 유지 칼로리"로 말한다.
