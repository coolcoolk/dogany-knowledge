---
# Injury-caution follow-up 2026-10-07.
# The elbow analogue of 088 (plantar heel) and 074 (shoulder): what the
# engine does for a lifter whose outside (lateral) or inside (medial) elbow
# aches from gripping, curls, rows and chin-ups. 055 owns the "load, don't
# rest" default and the outer pain ceiling; 056 owns the rungs and the
# tendon modifier that moves a familiar tendon ache to current-load-pain.
# This row owns the elbow-specific part: which pulling variants to swap
# first, the wrist-extensor / wrist-flexor loading dose, the isometric and
# eccentric questions, how the clock runs, and what goes to triage.
#
# Every treatment trial is in lateral elbow tendinopathy (tennis elbow) in
# middle-aged adults (mean age about 47-51), mostly not lifters. Medial
# elbow tendinopathy (golfer's elbow) has no adequately powered trial; its
# rows are the lateral protocol mirrored to the flexor-pronator group and
# are labelled transport D. No trial in resistance-trained lifters was
# found; every grip and variant swap is product judgement.
#
# elbow_rules is structured data for the composer. Dose rows key to 056
# rungs; numbers are copied from the source named in `basis`, never
# derived. Rows marked basis_grade D are product judgement.
#
# Numbering: claimed 089 provisionally (088 is the module max on main at
# branch time; parallel branches may collide -- renumber at merge).
id: exercise/elbow-tendinopathy-pulling-lifter-rules-089
domain: exercise
grade: B (lateral elbow tendinopathy improves in about 9 of 10 people within a year whatever is done; exercise-based physiotherapy speeds the first 6 weeks but does not change the 1-year result; a corticosteroid injection helps at 6 weeks and worsens the 1-year result and recurrence); C (exercise beats passive care by a small margin at low certainty; eccentric emphasis speeds pain relief but not the 12-month result; isometrics do not relieve pain on the spot and are doubtful as a sole treatment; braces unproven; medial elbow evidence low certainty); D (grip and variant swaps, placement in a lifter's week, the medial dose, red-flag routing)
lane: "@clinical-physio"
locale: universal
as_of: 2001-2026
contested: no
sources:
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC1633771"  # Bisset L, Beller E, Jull G, Brooks P, Darnell R, Vicenzino B 2006, BMJ 333(7575):939 -- single-blind RCT n=198, lateral elbow pain >= 6 weeks, age 18-65 (mean 47.6): 8 x 30 min physiotherapy over 6 weeks (elbow manipulation + exercise, home band exercise and booklet) vs one corticosteroid injection vs wait-and-see (advice to modify daily activities to avoid aggravating pain while staying as active as possible; analgesics, heat, cold or a brace as needed). Success at 6 weeks: wait-and-see 27%, injection 78%, physio 65%; at 52 weeks: 90%, 68%, 94%; 47 of 65 injection successes regressed. Read at full text (PMC) 2026-10-07
  - "https://search.pedro.org.au/search-results/record-detail/34833"  # Coombes BK, Bisset L, Brooks P, Khan A, Vicenzino B 2013, JAMA 309(5):461-469 -- 2x2 factorial RCT n=165, unilateral lateral epicondylalgia > 6 weeks: corticosteroid vs placebo injection, each with or without 8 weeks of physiotherapy (elbow manual therapy + exercise). At 1 year complete recovery or much improved: corticosteroid 83% vs placebo 96%; recurrence 54% vs 12%. Physiotherapy no 1-year difference (and at 26 weeks 71% vs 69%); at 4 weeks placebo + physio 39% vs placebo alone 10%. Read at abstract (PEDro record)
  - "https://bjsm.bmj.com/content/55/9/477"  # Karanasios S, Korakakis V, Whiteley R, Vasilogeorgis I, Woodbridge S, Gioftsos G 2021, Br J Sports Med 55(9):477-485 -- systematic review + meta-analysis, 30 RCTs, 2,123 participants: exercise vs passive care effective but small (low to very low certainty); vs corticosteroid injection better on most outcomes except short-term pain, pain-free grip differences 12-22 points (low certainty); vs wait-and-see significant only for short-term pain and disability (very low certainty); eccentric wrist-extensor strengthening better than other strengthening protocols; large heterogeneity in load, duration and frequency. Read at abstract
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC2971639"  # Tyler TF, Thomas GC, Nicholas SJ, McHugh MP 2010, J Shoulder Elbow Surg 19(6):917-922 -- RCT n=21 (stopped early, underpowered), chronic lateral epicondylosis, mean age 47-51: isolated eccentric wrist-extensor exercise with a rubber bar (FlexBar 'twist'), 3 x 15 daily, about 4 s eccentric, 30 s between sets, next-stiffer bar when 3 x 15 is easy, about 7 weeks, added to standard care vs standard care alone (stretching, ultrasound, friction massage, heat, ice). Pain improved 81% vs 22%, DASH 76% vs 13%, strength 79% vs 15%. Short-term only. Read at full text (PMC) 2026-10-07
  - "https://ujms.net/index.php/ujms/article/view/6062"  # Peterson M, Butler S, Eriksson M, Svärdsudd K 2011, Ups J Med Sci 116(4):269-279 -- RCT n=81, chronic lateral epicondylosis: daily home wrist-extensor exercise with a water-filled container as dumbbell, load raised weekly, 3 months, vs wait-list; greater and faster pain reduction during contraction and stretch with exercise; arm disability and quality of life not different. Read at abstract
  - "https://search.pedro.org.au/search-results/record-detail/39038"  # Peterson M, Butler S, Eriksson M, Svärdsudd K 2014, Clin Rehabil 28(9):862-872 -- RCT n=120, chronic tennis elbow: 3-month home eccentric vs concentric graded wrist-extensor exercise (seated, forearm supported, water-container dumbbell). Faster pain decrease and strength gain with eccentric from 2 months; no difference at 12 months in pain, function or quality of life. Read at abstract
  - "https://pure.ulster.ac.uk/en/publications/isometric-exercise-above-but-not-below-an-individuals-pain-thresh/"  # Coombes BK, Vicenzino B et al. 2016, Clin J Pain 32(12):1069-1075 -- randomised crossover, chronic lateral epicondylalgia: isometric wrist extension 10 x 15 s at 20% below vs 20% above the individual's pain threshold vs no exercise. Above-threshold raised pain during, immediately after and 30 min after; below-threshold was no different from no exercise (no analgesia). Read at abstract
  - "https://search.pedro.org.au/search-results/record-detail/58251"  # Vuvan V, Vicenzino B et al. 2020, Med Sci Sports Exerc 52(2):287-295 -- RCT n=40 (PEDro 8/10), lateral elbow tendinopathy > 6 weeks: one instruction session + 8 weeks unsupervised daily progressive isometric wrist-extensor exercise vs wait-and-see. PRTEE better (SMD -0.92, 95% CI -1.58 to -0.26); success 29% vs 26% (no difference); pain-free grip no difference. Authors: doubtful as a sole treatment. Read at abstract
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC9820871/"  # Stasinopoulos D 2022, J Clin Med 12(1):94 -- editorial on isometric exercise in lateral elbow tendinopathy: three studies, protocols vary (Park 2010 50 x 10 s holds four times a day pain-free; Bateman 2022 up to 60 s x 5 once a day); isometric not superior to isotonic. Read at full text (PMC) 2026-10-07
  - "https://doi.org/10.2519/jospt.2015.5841"  # Coombes BK, Bisset L, Vicenzino B 2015, J Orthop Sports Phys Ther 45(11):938-949 -- clinical commentary (expert opinion, not a trial): up to 90% improve on wait-and-see within a year, up to a third still have pain past a year, recurrence common; advice to avoid pain-provoking activity 'eg, by not lifting with a pronated forearm'; irritable cases: pain-free isometric wrist-extension holds 30-60 s daily (wrist 20-30 deg extension, elbow 90 deg), progressing to 90 s and to load; less irritable: slow concentric and eccentric (4 s each way) 2-3 x 10, progressed by load and by doing it with the elbow straighter; pain up to 3/10 during exercise acceptable but not the next morning; differential list (radial tunnel, posterior interosseous nerve, cervical referral, joint catching, posterolateral instability); 6-12 weeks before escalating. Read at full text 2026-10-07
  - "https://research.monash.edu/en/publications/orthotic-devices-for-tennis-elbow-a-systematic-review/"  # Struijs PA, Smidt N, Arola H, van Dijk CN, Buchbinder R, Assendelft WJ 2001, Br J Gen Pract 51(472):924-929 (Cochrane CD001821, 2002) -- five small RCTs (7-49 per group), not poolable: no definitive conclusion on orthoses (counterforce braces) for lateral epicondylitis. Read at abstract
  - "https://knova.um.edu.my/research_publications_2026_2030/99"  # See ZH, Loo CE, Jaafar Z 2026, Complement Ther Med 98:103364 -- systematic review, eccentric exercise for medial epicondylitis: 5 studies, 143 patients, within-group pain and function gains, one RCT showed a between-group benefit, no meta-analysis possible, overall certainty low. Read at record
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC4060314"  # Tyler TF, Nicholas SJ et al. 2014, Int J Sports Phys Ther 9(3):365-370 -- case series n=20 (age 49 +/- 12), chronic medial epicondylosis that failed physio, injection, PRP and NSAIDs: eccentric wrist-flexor rubber-bar exercise (reverse twist) 3 x 15 twice daily added to standard care. No control group. Read at record
  - "exercise/tendon-fascia-load-management-055"  # within-warehouse: load-don't-rest default and the outer pain ceiling (Achilles-derived, applied to other tendons by analogy)
  - "exercise/caution-severity-ladder-056"  # within-warehouse: the rungs every elbow_rules dose row keys to; tendon modifier
  - "exercise/injury-history-reinjury-risk-054"  # within-warehouse: elbow is one of the five common injury sites in weight-training sports (Keogh 2017); history weight
  - "exercise/pull-push-plane-balance-066"  # within-warehouse: the week still needs its pulls; swaps keep the plane, change the grip
  - "exercise/regional-bias-biceps-distal-012"  # within-warehouse: curl variants and what they bias, for the medial / biceps swap choices
  - "exercise/plantar-heel-pain-lifter-foot-rules-088"  # within-warehouse: the format and the 'protocol replaces, not adds' placement logic this row mirrors
  - "exercise/harm-route-boundary-031"  # within-warehouse: red flags and nerve symptoms stay with pain-triage
  - "framework:GRADE -- natural history and the injection harm rest on two well-run RCTs (n=198, 165) in non-lifting adults with lateral pain; the exercise effect is small and low certainty in a 30-trial meta-analysis with wildly varying doses; the eccentric and isometric questions rest on single trials (n=21, 40, 120) and a crossover; braces are unresolved. Medial elbow tendinopathy has five small studies and a case series. No trial in lifters; nothing tests grip swaps, straps, pulling variants or curl selection in elbow tendinopathy."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
elbow_rules:
  site:
    - side: lateral
      words: pain on the outside of the elbow, worse gripping, lifting with the palm down, opening jars, shaking hands
      tissue: wrist and finger extensor origin (extensor carpi radialis brevis)
      provocative_in_gym: pronated-grip pulls (overhand rows, pull-ups, pulldowns), reverse curls, deadlift and shrug grip, farmer's carries, wrist extension, thick grips
      basis: Coombes 2015 clinical picture
      basis_grade: D
    - side: medial
      words: pain on the inside of the elbow, worse with curls, chin-ups, heavy gripping or wrist curls
      tissue: wrist flexor / pronator origin (common flexor tendon)
      provocative_in_gym: supinated-grip pulls (chin-ups, underhand rows), straight-bar and heavy dumbbell curls, wrist curls, heavy grip work
      basis: anatomy; no lifter study
      basis_grade: D
    - side: other
      words: front-of-elbow pain after a heavy curl or chin-up, back-of-elbow pain, pain with numbness or tingling, catching or locking, swelling
      tissue: not covered by this row
      provocative_in_gym: n/a
      basis: exercise/harm-route-boundary-031; Coombes 2015 differential list
      basis_grade: D
  dose:
    - context: baseline
      rungs: [no-caution, mild, history-old]
      trigger: none -- no elbow-specific work added for prevention
      side: any
      slot: none
      exercise: ordinary program
      sets: program default
      reps: program default
      per_week_target: 0
      tempo: program default
      progression: program default
      pain_rule: none
      duration: none
      basis: no prevention trial of forearm work for elbow tendinopathy in lifters
      basis_grade: D
      transport_grade: D
    - context: history
      rungs: [history-recent, history-unknown]
      trigger: a named lateral or medial elbow tendinopathy episode, recovered, inside 12 months or timing unknown
      side: affected side
      slot: accessory, end of an upper-body pulling session
      exercise: lateral -- dumbbell wrist extension, forearm supported, palm down; medial -- dumbbell wrist flexion, forearm supported, palm up
      sets: 2-3
      reps: 10-15
      per_week_target: 2
      tempo: 3-4 s lowering
      progression: add load when all sets reach the top of the range
      pain_rule: 055 ceiling; a flare moves the user to current-load-pain
      duration: ongoing while the history weight lasts (056)
      basis: the current-load-pain exercise at a maintenance dose; product judgement
      basis_grade: D
      transport_grade: D
    - context: current-load-pain-irritable
      rungs: [current-load-pain]
      trigger: familiar elbow ache that is sharp with light gripping, lingers into the next day, or flares with any loading; no red flag; pain-triage has not flagged it
      side: affected side
      slot: daily at home, or before the main lifts as a short block
      exercise: isometric hold -- lateral wrist extension (medial wrist flexion), forearm supported, wrist about 20-30 deg, elbow bent 90 deg, against a dumbbell or band
      sets: 3-5 holds
      reps: 30-60 s each
      per_week_target: 7
      tempo: hold
      progression: lengthen holds toward 90 s, then add load; move to the isotonic row once gripping no longer flares
      pain_rule: below the pain threshold (pain-free or barely noticeable); holds above it raised pain in a crossover
      duration: until less irritable, usually 1-3 weeks; product judgement
      basis: Coombes 2015 (expert commentary); Coombes 2016 crossover (above-threshold holds raise pain)
      basis_grade: D
      transport_grade: D
    - context: current-load-pain
      rungs: [current-load-pain]
      trigger: familiar lateral or medial elbow ache with gripping or pulling, no red flag, not irritable; pain-triage has not flagged it
      side: affected side
      slot: accessory, end of the session, or a short standalone session at home
      exercise: lateral -- dumbbell (or water container) wrist extension, forearm supported on a bench or thigh, palm down, wrist straight in line with the middle finger; or eccentric rubber-bar twist (Tyler twist). Medial -- the same with wrist flexion, palm up; or reverse rubber-bar twist
      sets: 3
      reps: 10-15 (dumbbell 2-3 x 10 at 4 s each way; rubber bar 3 x 15)
      per_week_target: 7 (daily, as in the trials) -- at least 3
      tempo: about 4 s lowering; lifting phase may be assisted by the other hand
      progression: dumbbell -- raise load weekly while the pain rule holds; rubber bar -- next stiffer bar when 3 x 15 is easy; later do it with the elbow straighter
      pain_rule: about 3/10 during the exercise is acceptable; back to the usual level by the next morning; 055 ceiling as the outer limit for the gym lifts
      duration: 8-12 weeks, review at 12 weeks; 3 months in the dumbbell trials, about 7 weeks in the rubber-bar trial
      base_always: advice -- cut the gripping and palm-down lifting that provokes it, keep the rest of training; most cases settle within a year
      basis: lateral -- Tyler 2010, Peterson 2011, Peterson 2014, Karanasios 2021, Coombes 2015; medial -- mirrored (See 2026 low certainty, Tyler 2014 case series)
      basis_grade: C
      transport_grade: C (lateral) / D (medial)
    - context: closed
      rungs: [current-other, red-flag]
      trigger: elbow pain that is not the familiar lateral or medial ache -- after trauma, a pop, swelling or bruising, front-of-elbow pain after a heavy lowering, numbness or tingling, catching or locking, night or rest pain, pain from the neck, or pain that is unknown
      side: any
      slot: none
      exercise: none prescribed
      sets: 0
      reps: 0
      per_week_target: 0
      tempo: none
      progression: none
      pain_rule: pain-triage before any elbow prescription
      duration: none
      basis: exercise/harm-route-boundary-031; Coombes 2015 differential list
      basis_grade: D
      transport_grade: D
  swaps:
    - order: 1
      rule: change the GRIP before cutting the movement -- keep the pull, swap the provocative grip for the one that stays under the ceiling
      lateral: overhand rows, pull-ups and pulldowns -> neutral (hammer) grip first, then underhand; reverse curls -> hammer or regular curls
      medial: chin-ups, underhand rows and straight-bar curls -> neutral grip first, then overhand; straight bar -> EZ bar, dumbbell or cable with a free wrist
      basis_grade: D
      note: Coombes 2015 advises not lifting with a pronated forearm for lateral pain (expert advice); no trial of grip swaps in lifters; the week keeps its pulls (066)
    - order: 2
      rule: take grip load off the elbow -- lifting straps for deadlifts, rows, shrugs and heavy pulldowns; thick grips and fat-grip attachments off; farmer's carries and grip work paused
      basis_grade: D
      note: gripping is the provocative task in the clinical picture (Coombes 2015); straps are product judgement
    - order: 3
      rule: lower load, then sets, on the provocative pulls -- not the whole upper-body day
      basis_grade: D
      note: 055 step-back order applied to the elbow; no elbow trial
    - order: 4
      rule: machine or cable variants (chest-supported row, machine row with neutral handles, cable curl) when the free-weight version breaches the ceiling
      basis_grade: D
      note: product judgement; lets the user set the handle and wrist position
    - order: 5
      rule: pausing all pulling is the last step, only when every swap breaches the ceiling
      basis_grade: D
      note: wait-and-see advice in Bisset 2006 kept people 'as active as possible'
  placement:
    - rule: the wrist-extensor or wrist-flexor exercise REPLACES the program's wrist curls or forearm work on the affected side; it is not stacked on top
      basis_grade: D
      note: stacking doubles the site's load with no trial behind it (mirrors 088)
    - rule: the isotonic forearm exercise goes after the main pulls, never before them
      basis_grade: D
      note: keeps grip fresh for the main lifts; the irritable-phase isometric is the only exception
    - rule: no isometric hold as a pre-session painkiller
      basis_grade: C
      note: below-threshold holds gave no analgesia and above-threshold holds raised pain (Coombes 2016); doubtful as sole treatment (Vuvan 2020)
    - rule: heavy pulling days for the affected side at least one day apart
      basis_grade: D
      note: 055 spacing note (tendon collagen turnover); no elbow trial
  info_only:
    - rule: if the user raises a cortisone (steroid) injection, state the trade-off -- faster relief at about 6 weeks, worse 1-year recovery and more recurrence -- and leave the decision with their clinician
      basis_grade: B
      note: Bisset 2006; Coombes 2013 (recurrence 54% vs 12%)
    - rule: a counterforce strap or brace is optional comfort; never told it fixes the tendon
      basis_grade: C
      note: Struijs 2001 -- no definitive conclusion from five small trials
    - rule: set the clock -- about 9 in 10 lateral cases are much better within a year; exercise speeds the early weeks; up to a third still have some pain past a year
      basis_grade: B
      note: Bisset 2006 (90-94% at 52 weeks); Coombes 2015
refraction_notes:
  - note: >
      THE CLOCK IS MOSTLY ON THE USER'S SIDE. In tennis elbow trials about 9
      in 10 people were much better within a year even with only advice to
      stay active and avoid what provokes it. Exercise-based physiotherapy
      helped faster in the first 6 weeks but ended in the same place at a
      year. The engine speaks loading as "a way to keep training and settle
      it sooner", not "the cure", and expects months, not weeks.
    grade: B
  - note: >
      DON'T CHASE THE QUICK SHOT. A cortisone injection felt better at 6
      weeks, but a year later fewer people had recovered (83% vs 96%) and
      over half relapsed against about 1 in 8 on placebo. The engine does not
      recommend injections; if the user raises one, it states this trade-off
      and leaves the decision with their clinician.
    grade: B
  - note: >
      THE FOREARM DOSE. Exercise for the wrist extensors beats passive care
      by a small margin at low certainty, and trials used very different
      doses. The tested shapes: a light dumbbell or water container lifted
      daily with the forearm supported, load raised weekly, for 3 months; or
      a rubber-bar eccentric twist, 3 x 15 daily, about 4 s lowering, next
      bar when easy, for about 7 weeks. Stressing the lowering phase brought
      pain down faster but not further at a year, so eccentric is a
      preference, not a rule.
    grade: C
  - note: >
      ISOMETRICS ARE NOT A PAINKILLER HERE. Holds below the pain threshold
      did not relieve elbow pain, holds above it made it worse for at least
      half an hour, and 8 weeks of isometrics alone did not raise the share
      of people who felt better. The engine uses pain-free holds only as an
      entry step for an irritable elbow and moves on to full-range work.
    grade: C
  - note: >
      SWAP THE GRIP, KEEP THE PULL. Palm-down pulling and gripping provoke
      outside-elbow pain; palm-up chin-ups and curls tend to provoke the
      inside. The engine changes the grip (neutral first), adds straps and
      drops fat grips before it lowers load, and lowers load before it cuts
      sets; it pauses pulling only if every swap breaches the ceiling. No
      trial tests any of this in lifters.
    grade: D
  - note: >
      THE INSIDE ELBOW IS THINLY STUDIED. Golfer's elbow has five small
      studies and a case series; eccentric wrist-flexor work improved people
      within groups but rarely beat a comparison. The engine mirrors the
      outside-elbow protocol to the wrist flexors and labels it as borrowed.
    grade: C
  - note: >
      WHAT THIS ROW DOES NOT LICENSE. A pop or sudden weakness at the front
      of the elbow during a heavy curl or chin-up lowering, bruising or a
      changed biceps shape, swelling after a fall, numbness or tingling in
      the hand (ring and little finger, or the back of the hand), weak finger
      extension, catching or locking, pain at night or at rest, or pain that
      travels from the neck are not the familiar tendon picture. They go to
      the pain-triage skill first (031); a suspected biceps tear is urgent.
    grade: D
claim: >
  For a lifter with a familiar outside (lateral) or inside (medial) elbow
  ache from gripping and pulling, no red flags: keep training under the 055
  ceiling, change the provocative grip first (neutral grip; palm-up instead
  of palm-down for the outside elbow, the reverse for the inside), add
  straps and drop fat grips, then lower load, then sets; pause pulling only
  if every swap breaches the ceiling. Add a daily forearm exercise for the
  affected side (wrist extension for lateral, wrist flexion for medial,
  forearm supported, about 4 s lowering, 3 x 10-15, load raised as the pain
  rule allows, about 3/10 during and settled by morning) for 8-12 weeks; it
  replaces the program's forearm work and sits after the main pulls. An
  irritable elbow starts with pain-free 30-60 s holds; holds are not a
  painkiller. About 9 in 10 lateral cases are much better within a year
  whatever is done; exercise speeds the early weeks; a cortisone shot trades
  early relief for a worse year. Braces are unproven. The medial dose is
  borrowed from the lateral trials.
reasoning: >
  Bisset 2006 was read at full text for the success rates and the
  wait-and-see advice; Coombes 2013 at abstract for the injection harm and
  the null 1-year physiotherapy result. Together they set the natural
  history the engine must not oversell against. Karanasios 2021 supplies
  the size and certainty of the exercise effect (small, low) and the
  eccentric preference; Peterson 2014 bounds that preference (faster, not
  further). Tyler 2010 was read at full text for the rubber-bar dose;
  Peterson 2011 supplies the daily dumbbell shape. Coombes 2015 was read at
  full text and is the only source for the irritable-phase holds, the 3/10
  exercise pain rule and the palm-down advice; it is expert commentary, so
  every number it alone supplies stays D. Coombes 2016 and Vuvan 2020 keep
  isometrics out of the painkiller role. Struijs 2001 leaves braces
  unresolved. The medial rows rest on a 2026 review (low certainty) and a
  case series, so their dose is transported D. Every lifter-specific rule
  (grip order, straps, replace the forearm work, placement) has no trial and
  stays at the practitioner floor. The axis is hard with block_specifics
  because the rung (familiar tendon ache vs red flag, nerve sign or unknown
  elbow pain) decides whether any dose is given at all.
---

# exercise/elbow-tendinopathy-pulling-lifter-rules-089 -- 팔꿈치 바깥·안쪽 통증(테니스엘보·골프엘보)이 있는 사람의 당기기 운동·그립·전완 운동

**한 줄 그림:** 팔꿈치가 아파도 당기기는 계속한다. 먼저 그립을 바꾸고 스트랩을 쓰고, 그다음에 무게를 줄인다.
전완 운동을 매일 조금씩 하고, 몇 주가 아니라 몇 달을 본다.

## Site (engine-readable copy of `elbow_rules.site`)

| Side | User's words | Provocative in the gym |
|---|---|---|
| lateral (바깥쪽) | outside of the elbow, gripping, palm-down lifting | overhand rows / pull-ups / pulldowns, reverse curls, deadlift and shrug grip, carries, fat grips |
| medial (안쪽) | inside of the elbow, curls, chin-ups, heavy gripping | chin-ups, underhand rows, straight-bar and heavy dumbbell curls, wrist curls |
| other | front-of-elbow after a heavy curl, back of elbow, numbness, catching, swelling | not this row -> pain-triage (031) |

## Dose by rung (engine-readable copy of `elbow_rules.dose`)

| Context (056 rungs) | Slot | Exercise | Sets x reps | Per week | Basis |
|---|---|---|---|---|---|
| baseline (no caution, mild, history-old) | none | program as is | program default | -- | no prevention trial |
| history (recent, unknown) | end of a pulling day | wrist extension (lateral) / flexion (medial), forearm supported | 2-3 x 10-15, 3-4 s lowering | 2 | product judgement |
| current-load-pain, irritable | daily at home or before main lifts | isometric hold, wrist 20-30 deg, elbow 90 deg | 3-5 x 30-60 s, below pain threshold | 7 | expert commentary; crossover |
| current-load-pain | end of session or home | wrist extension / flexion, dumbbell or rubber-bar twist | 3 x 10-15, ~4 s lowering; ~3/10 during, settled by morning | daily (at least 3) | Tyler 2010; Peterson 2011/2014; Karanasios 2021; medial mirrored |
| closed (current-other, red-flag) | none | -- | -- | -- | pain-triage (031) |

Always with current-load-pain: advice to cut the provoking gripping and palm-down lifting while staying active.
Review at 12 weeks.

## Swap order and placement

| Rule | Basis |
|---|---|
| 1. Change the grip first (neutral, then the opposite grip); keep the pull | expert advice (palm-down) + product judgement |
| 2. Straps on deadlifts / rows / shrugs; fat grips, carries, grip work off | product judgement |
| 3. Lower load, then sets, on the provocative pulls only | 055 order, no elbow trial |
| 4. Machine / cable variant with neutral handles if free weight breaches | product judgement |
| 5. Pause pulling only if every swap breaches the ceiling | trial advice stayed active |
| Forearm exercise replaces the program's wrist curls on that side | product judgement |
| Isotonic forearm work after the main pulls | product judgement |
| No isometric hold as a pre-session painkiller | Coombes 2016; Vuvan 2020 |
| Heavy pulling days for the affected side a day apart | 055 spacing note |

## Evidence vs folklore

| Claim | State |
|---|---|
| Tennis elbow needs treatment to get better | About 9 in 10 much better within a year on advice alone |
| Exercise physio changes the 1-year result | Faster early, same at a year |
| A cortisone shot fixes it | Better at 6 weeks, worse at a year, more relapse |
| Eccentrics are the only way | Faster pain relief, same at 12 months |
| Isometric holds kill elbow pain before training | Below threshold no effect; above threshold worse |
| A tennis-elbow strap fixes it | No definitive evidence |
| Golfer's elbow has its own proven protocol | Low certainty; borrowed from tennis elbow |
| Swap to neutral grip / use straps | Sensible, untested in lifters |
| Stop all pulling until it heals | No trial; the trials kept people active |

## 한국어 요약 (답변용)

- 팔꿈치 바깥쪽(손바닥이 아래로 향한 채 들 때, 손으로 꽉 쥘 때 아픔)이나 안쪽(컬, 친업, 손목 컬 할 때
  아픔)이 익숙하게 시큰거리고 위험 신호가 없으면: 운동을 멈추지 않는다. 통증 기준(055: 운동 중·후 10점
  중 5점까지, 다음 날 아침 평소 수준으로 돌아옴, 아침 통증이 주마다 늘지 않음) 안에서 한다.
- 시간은 대체로 내 편이다. 테니스엘보 연구에서 "아픈 동작은 피하고 최대한 활동하라"는 조언만 받은 사람도
  1년 안에 10명 중 9명이 크게 좋아졌다. 운동 치료는 처음 6주를 더 빨리 좋게 했지만 1년 결과는 같았다.
  그래서 운동은 "훈련을 이어가며 더 빨리 가라앉히는 방법"으로 말하고, 몇 주가 아니라 몇 달을 본다.
- 바꾸는 순서: ① 그립부터 바꾼다. 바깥쪽이 아프면 오버핸드(손바닥 아래) 로우·풀업·랫풀다운을 뉴트럴
  그립(손바닥 마주 봄)으로, 그다음 언더핸드로. 리버스 컬은 해머 컬로. 안쪽이 아프면 친업·언더핸드 로우·
  스트레이트 바 컬을 뉴트럴 그립으로, 스트레이트 바는 EZ바·덤벨·케이블로. ② 데드리프트·로우·슈러그에
  스트랩을 쓰고, 두꺼운 그립·파머스 워크·악력 운동은 잠시 뺀다. ③ 그래도 아프면 그 당기기 동작의 무게를,
  그다음 세트를 줄인다. 상체 날 전체를 빼지 않는다. ④ 머신·케이블로 손잡이 각도를 맞춘다. ⑤ 모든 방법이
  기준을 넘을 때만 당기기를 쉰다. 이 순서를 리프터에게 시험한 연구는 없다(실무 판단).
- 전완 운동: 바깥쪽은 손바닥을 아래로, 안쪽은 손바닥을 위로 해서 팔뚝을 벤치나 허벅지에 올리고 가벼운
  덤벨(물병도 됨)로 손목을 올렸다 4초쯤 천천히 내린다. 올릴 때는 반대 손으로 도와도 된다. 3세트 10~15회,
  매일(최소 주 3회). 고무 막대를 비트는 방법(타일러 트위스트)은 매일 15회 3세트, 쉬워지면 더 단단한 막대로.
  운동 중 10점 중 3점 정도 통증은 괜찮고, 다음 날 아침엔 평소로 돌아와야 한다. 8~12주 하고 12주에 다시 본다.
  내리는 동작을 강조하면 통증이 더 빨리 줄었지만 1년 뒤 결과는 같았다.
- 이 전완 운동은 원래 프로그램의 손목 컬·전완 운동을 대신한다. 위에 더 얹지 않는다. 메인 당기기가 끝난
  뒤에 하고, 아픈 쪽에 무거운 당기기를 하는 날은 하루 띄운다.
- 가볍게 쥐기만 해도 찌릿하고 다음 날까지 남는 예민한 팔꿈치는 먼저 버티기(아이소메트릭)부터: 팔꿈치를
  90도로 굽히고 손목을 살짝 젖힌 채(안쪽이면 살짝 굽힌 채) 30~60초씩 3~5번, 아프지 않은 강도로 매일. 덜
  예민해지면 위의 전완 운동으로 넘어간다. 다만 운동 전에 버티기로 통증을 줄이려는 건 효과가 없었고,
  아플 만큼 세게 버티면 30분 넘게 더 아팠다.
- 주사(스테로이드)는 권하지 않는다. 사용자가 물으면: 6주쯤엔 좋아지지만 1년 뒤 회복이 더 적었고(83% 대
  96%) 절반 넘게 재발했다(가짜 주사는 8명 중 1명꼴). 결정은 담당 의사와 하도록 남긴다.
- 테니스엘보 밴드(팔꿈치 스트랩)는 편하면 써도 되지만, 힘줄을 고친다고 말하지 않는다. 효과는 확실히
  밝혀지지 않았다.
- 골프엘보(안쪽)는 연구가 아주 적다. 테니스엘보 방법을 손목 굽힘 쪽으로 뒤집어 빌려 쓴 것이라고 말한다.
- 무거운 컬이나 친업을 내리다 팔꿈치 앞쪽에서 "뚝" 소리나 갑자기 힘이 빠짐, 멍이나 이두근 모양 변화,
  넘어진 뒤 붓기, 손 저림(넷째·새끼손가락이나 손등), 손가락을 펴는 힘이 약해짐, 걸리거나 잠기는 느낌, 밤이나
  쉴 때도 아픈 통증, 목에서 내려오는 통증은 여기 해당하지 않는다. 먼저 통증 확인(pain-triage)으로 보내고,
  이두근 힘줄 파열이 의심되면 빨리 진료를 받게 한다.
