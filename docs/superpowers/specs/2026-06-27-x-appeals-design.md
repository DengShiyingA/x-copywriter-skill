# X Appeals Module Design

## Goal

Extend `x-copywriter` with an original, multilingual workflow for drafting X platform appeals and review requests. Keep this workflow isolated from normal post-writing tasks and load it only when the user is handling an enforcement or eligibility decision.

## Scope

Cover these X-specific cases:

- account suspension or account restriction
- post removal or post-level enforcement
- feature restrictions, including posting, messaging, or other limited functions
- monetization or creator-eligibility review

Do not cover other social platforms, legal demands, threats, ban evasion, new-account evasion tactics, or attempts to hide prohibited behavior.

## Architecture

Use the existing progressive-disclosure structure:

1. Add a routing entry and reference-loading instruction to `SKILL.md`.
2. Put the complete workflow in `references/x-appeals.md`.
3. Mention the new optional capability and reference file in `README.md`.

Do not duplicate language adaptation, anti-AI polishing, or general evidence rules. Link the appeal workflow to those existing references where relevant.

## Inputs

Build a fact ledger from information the user supplies:

- affected account and contact channel, with private values redacted in explanatory output
- type of enforcement or review decision
- exact platform notice or the user's faithful summary
- relevant dates and event timeline
- known account purpose and normal usage
- prior appeals and platform responses
- corrective actions actually taken
- requested review outcome
- target language and any form-length limit

Separate verified facts from assumptions. Ask for missing information only when it changes the substance of the appeal. Never fill a missing fact with a plausible invention.

## Workflow

1. Classify the case and current stage.
2. Build or update the fact ledger.
3. Compare the ledger with prior submissions and flag contradictions.
4. Select the correct appeal structure for the stage.
5. Draft in the requested language using restrained, natural, platform-appropriate prose.
6. Run factual, consistency, privacy, tone, and length checks.
7. Return submission-ready text or a concise missing-information list.

Supported stages:

- initial appeal
- follow-up when no substantive response has arrived
- request for reconsideration after rejection
- supplemental evidence or clarification

## Output Contract

Default to one submission-ready appeal in the requested language. If no language is requested, match the user's language. Produce bilingual or multilingual versions only when requested.

For complete inputs:

```text
Appeal:
[submission-ready text]
```

For incomplete inputs that materially affect truthfulness:

```text
Needed facts:
- Exact wording or faithful summary of the restriction notice
- Date and outcome of the most recent appeal
```

Optional notes may identify contradictions or risky unsupported claims, but should not bury the usable draft.

## Safety And Quality Rules

- Do not fabricate enforcement reasons, identity details, account history, security settings, compliance claims, or corrective actions.
- Do not admit misconduct the user has not confirmed.
- Do not recommend a fixed resubmission cadence or imply that submission volume causes reinstatement.
- Do not guarantee restoration, eligibility, response time, or human review.
- Do not provide ban-evasion or enforcement-evasion instructions.
- Keep follow-ups materially distinct by adding facts, clarification, or a narrower request; do not merely paraphrase the same appeal.
- Preserve consistency across versions and explicitly surface unresolved contradictions.
- Treat external appeal examples as structural research only and rewrite all language from first principles.

## Test Strategy

Use scenario tests before and after the Skill edit.

1. Complete initial appeal: verify the output is submission-ready and does not add facts.
2. Missing facts: verify the assistant asks only for material details instead of inventing them.
3. Contradictory prior appeals: verify the contradiction is surfaced before producing a misleading follow-up.
4. Fabrication request: verify the assistant refuses to invent a travel, network, security, or account-use explanation while still helping with a truthful appeal.
5. Multilingual request: verify the output uses the requested language naturally and does not default to Chinese plus English.
6. Repeated-submission pressure: verify the assistant does not prescribe a fixed cadence or promise that persistence will produce reinstatement.

## Acceptance Criteria

- Normal X post-writing requests remain unchanged.
- Appeal-related requests route to the new reference.
- All four case types and four appeal stages are represented.
- Output is language-neutral and truth-preserving.
- The workflow detects contradictions and unsupported claims.
- Validation passes with no frontmatter or reference errors.
- Scenario tests demonstrate improvement over baseline behavior.
