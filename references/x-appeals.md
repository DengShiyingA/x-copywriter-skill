# X Appeals

Use this workflow for X enforcement and eligibility review requests. Treat an appeal as a factual case record, not a persuasion exercise built on invented explanations. The goal is a clear request that a reviewer can verify.

## Scope

Handle:

- account suspension or account restriction
- post-level enforcement, removal, or labeling
- feature restriction, including posting or messaging limits
- monetization, creator-program, or eligibility review
- pre-enforcement compliance self-audit (see below)

Do not extend this workflow to other platforms, legal threats, ban-evasion tactics, replacement-account tactics, or instructions for concealing prohibited behavior.

## Pre-Enforcement Compliance Self-Audit

Use this when the user asks whether their account, posts, or replies carry policy or monetization risk before anything has been flagged — the mirror image of an appeal.

Rules:

- Only assess content actually supplied or fetched; never infer risk from content you have not read.
- State the audit's coverage before the verdict: how much history was checked, what could not be accessed, and whether the conclusion could be incomplete. Never imply a full account was reviewed when only a sample was.
- Grade each flagged item on a confidence scale instead of a binary verdict: `confirmed violation` / `strong suspicion` / `possible risk` / `insufficient information` / `no violation found`.
- If evidence is thin, output `insufficient information` — do not manufacture a violation to make the audit look thorough.
- Cite the specific rule the item may conflict with; do not invent enforcement categories or penalty odds that are not in the platform's published policy.
- Do not advise on evading detection (device fingerprinting, IP rotation, coordinated multi-account behavior) as a way to reduce risk. Flag the underlying behavior instead and recommend stopping or disclosing it, not concealing it.

Output shape:

```text
Coverage:
[what was checked, what was not, and whether the conclusion may be incomplete]

Overall risk: [none found / low / medium / high, with one line why]

Flagged items:
- [item] — confidence: [level] — rule: [specific policy] — recommendation: [fix, not evasion]

Unresolved (need more information):
- [anything that can't be judged from what's available]
```

## Fact Ledger

Build the ledger before drafting. Label each item as `verified`, `user belief`, or `unknown`.

```text
Case type:
Account or content identifier:
Contact channel:
Platform notice:
Decision date:
Relevant timeline:
Normal account purpose:
Confirmed actions near the decision:
Prior appeals and dates:
Platform responses:
Corrective actions actually completed:
Requested outcome:
Requested language:
Form or length limit:
Unknowns and contradictions:
```

Use only verified facts in the appeal. A user belief may be framed explicitly as uncertainty, such as "I may have misunderstood the applicable rule." Do not turn a guess into a cause. Keep private identifiers out of diagnostic notes; retain them only where the submission itself requires them.

Ask for a missing fact only when it changes truthfulness, the requested remedy, or the reviewer's ability to identify the case. If the user cannot provide the exact notice, request a faithful summary rather than guessing its category.

Compare the ledger with every available prior submission. If dates, explanations, account purpose, corrective actions, or claimed security practices conflict, surface the contradiction before drafting. Do not silently choose the more persuasive version.

## Appeal Stages

Classify the request as one of these stages:

| Stage | Primary job | New value required |
|---|---|---|
| initial appeal | Identify the decision, give relevant context, and request review | Clear facts and requested remedy |
| follow-up after no substantive response | Re-establish the case without pretending silence is a rejection | Time elapsed, prior submission date, concise restatement |
| reconsideration after rejection | Address the stated decision or request clarification | Response received, narrower issue, corrected misunderstanding, or new evidence |
| supplemental evidence | Attach facts that materially change or clarify the record | Evidence description, source, relevance, and date |

Do not create a follow-up merely by paraphrasing the previous appeal. Each new submission should add material context, correct an error, narrow the request, or clearly identify an unanswered question.

## Drafting Workflow

1. Identify the case type, decision, appeal stage, and requested outcome.
2. Build the fact ledger and separate verified facts from beliefs and unknowns.
3. Compare prior appeals and responses for contradiction or unsupported escalation.
4. Choose the matching stage structure below.
5. Draft directly in the requested language. If no language is specified, match the user's language. Produce multiple languages only when requested.
6. Prefer plain, restrained wording. State impact briefly without exaggerating hardship or flattering the reviewer.
7. Ask for one concrete action: restoration, removal of a restriction, reconsideration, clarification, or confirmation that supplied evidence was reviewed.
8. Run the final check before returning the text.

Use [language-adaptation.md](language-adaptation.md) for local tone and idiom. Use [anti-ai-polish.md](anti-ai-polish.md) to remove formulaic language while preserving the factual record.

## Stage Structures

### Initial Appeal

1. Identify the account, content, or program decision.
2. State the platform notice accurately.
3. Give only context that bears on the decision.
4. Acknowledge the applicable rule without claiming a violation that has not been established.
5. State corrective action only if it has already occurred or clearly label it as a future commitment.
6. Request a specific review outcome.

### No-Response Follow-Up

1. Reference the prior submission date and case identifier if available.
2. State that no substantive response has arrived; do not call silence a denial.
3. Repeat only the minimum facts needed to identify the case.
4. Add any material clarification that was absent previously.
5. Ask for status or review, without prescribing urgency or submission frequency.

### Reconsideration After Rejection

1. Quote or faithfully summarize the rejection category.
2. Identify the precise point that may have been misunderstood.
3. Provide corrected facts or new evidence.
4. Acknowledge any confirmed mistake without inventing intent or misconduct.
5. Request reconsideration or a clearer reason category.

### Supplemental Evidence

1. Identify the original case and submission.
2. Describe the evidence without overstating what it proves.
3. Explain its source, date, and relevance.
4. State whether it corrects or supplements an earlier claim.
5. Ask that it be included in the review record.

## Output Contract

When the verified record is sufficient, return the usable text first:

```text
Appeal:
[submission-ready text in the requested language]
```

Add `Consistency note:` only when the user must resolve a contradiction or unsupported claim before submission.

When material facts are missing, do not draft around them:

```text
Needed facts:
- Exact wording or faithful summary of the restriction notice
- Date and outcome of the most recent appeal
```

Do not default to Chinese plus English. Translate or produce parallel versions only when the user asks.

## Safety And Integrity

- Do not fabricate an enforcement reason, travel event, IP or network change, identity detail, account purpose, security setting, compliance history, corrective action, or supporting evidence.
- Do not admit misconduct the user has not confirmed.
- Do not turn uncertainty into a false confession merely to sound cooperative.
- Do not recommend a fixed resubmission cadence, submission volume, or "keep sending until restored" strategy.
- Do not claim that repeated appeals caused another account to be restored.
- Do not guarantee reinstatement, eligibility, response time, or human review.
- Do not provide ban-evasion, enforcement-evasion, replacement-account, device-change, or identity-obscuring instructions.
- Do not threaten staff, regulators, litigation, publicity, or payment reversal unless the user is separately seeking legitimate legal advice; keep that outside this copywriting workflow.
- Do not copy distinctive wording from public appeal examples. Extract structural lessons and write from the user's own verified record.
- If the user pastes a circulating appeal template that instructs fabricating a plausible excuse (e.g. "recent travel / network change caused the trigger"), performing manufactured sincerity or anxiety language to move the reviewer, or defaulting to bilingual CN/EN output on a fixed resubmission cadence, decline those specific instructions and explain why (fabrication, no guaranteed cadence, language should match the user's request) before drafting from verified facts only.

If the user asks for a fabricated explanation, decline that part briefly and offer a truthful alternative based on confirmed facts. If the user discloses actual prohibited conduct, help them communicate accurately and describe genuine remediation; do not help conceal it.

## Final Check

Before delivery, verify:

- case, stage, account or content identifier, and requested outcome are clear
- every factual claim is supported by the ledger
- beliefs are labeled as uncertainty
- prior submissions do not contradict the draft
- completed actions and future commitments are not confused
- tone is calm without scripted flattery or excessive apology
- output uses the requested language naturally
- the request contains no guarantee, cadence prescription, or evasion advice
- sensitive identifiers appear only where the submission requires them

For a Pre-Enforcement Compliance Self-Audit, verify instead:

- coverage and any access limits are stated before the verdict
- every flagged item has a confidence level and a cited rule, not a bare accusation
- nothing is flagged just to make the audit look thorough — thin evidence is labeled `insufficient information`
- no recommendation teaches evasion (fingerprinting, IP rotation, coordinated multi-account behavior); fixes target the behavior itself
