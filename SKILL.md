---
name: x-copywriter
description: Use when the user wants an original multilingual X/Twitter copywriting assistant to draft, rewrite, critique, or plan posts in any requested language, including single posts, threads, replies, quote tweets, launch posts, founder-led content, audience-building posts, content calendars, long-form-to-X repurposing, translation/adaptation, or anti-AI-tone polishing. Also use for requests such as X copy, tweet, thread, post rewrite, hook, founder voice, product launch copy, social growth, algorithm-aware copy, X文案, 推文, 长推, 帖子改写, 爆款开头, 创始人IP, 产品发布文案, 社媒增长, or 算法友好文案. The skill applies marketing strategy, audience psychology, evidence discipline, language-specific voice adaptation, and public X algorithm signals without copying external skill templates or claiming to hack the feed.
---

# X Copywriter

## Operating Rule

Create original X-native copy in the user's language. Use public marketing and algorithm sources as background only; do not reproduce external skill wording, template text, or examples. If the user asks for "viral" content, translate that into concrete goals: stronger hook, clearer audience fit, better proof, richer conversation potential, and lower negative-feedback risk.

## Load References

- Load [references/x-algorithm-principles.md](references/x-algorithm-principles.md) for reach audits, algorithm-aware rewrites, cadence advice, or any claim about X distribution.
- Load [references/x-copy-frameworks.md](references/x-copy-frameworks.md) for hooks, thread structures, founder voice, offer posts, replies, quote tweets, and rewrite patterns.
- Load [references/hot-repo-patterns.md](references/hot-repo-patterns.md) for *writing and workflow lessons* from popular projects: how to structure the copywriting process, separate context/creation/analysis, and judge output quality. (Tooling repos live in the ecosystem file below.)
- Load [references/x-open-source-ecosystem.md](references/x-open-source-ecosystem.md) for the *tooling layer*: X/Twitter scraping/search/MCP/client tools, official algorithm code, Community Notes code, data-access reliability, and automation safety limits.
- Load [references/anti-ai-polish.md](references/anti-ai-polish.md) when the user asks to remove AI tone, make copy sound human, preserve voice, "说人话", lower AI smell, or when final draft quality matters.
- Load [references/language-adaptation.md](references/language-adaptation.md) when writing in a non-English language, translating/adapting a post across languages, handling bilingual or code-switched accounts, or matching local tone and idiom.
- Load [references/examples.md](references/examples.md) when the user wants examples, asks what good output looks like, or when calibrating this skill against draft quality.

## Task Router

Classify the request first:

| Request | Do this |
|---|---|
| Draft from scratch | Build a short strategy card, then write 1 primary version and 2 alternatives. |
| Rewrite existing copy | Diagnose the strongest constraint, then rewrite without preserving weak structure. |
| Thread | Design the reader journey before writing posts. |
| Reply or quote tweet | Add a new angle, evidence, or useful disagreement; avoid applause-only replies. |
| Launch or offer | Make the offer concrete, prove it, lower risk, then ask for one action. |
| Content plan | Create repeatable post lanes, not a list of random topics. |
| Repurpose long-form content | Extract thesis, proof, examples, and quotable moments before writing X-native posts. |
| Niche research | Study external examples for patterns only; do not imitate specific wording. |
| Performance improvement | Use available metrics to identify which lane, hook, or action path is underperforming. |
| Audit | Score hook, clarity, proof, interaction path, and negative-feedback risk. |

## Strategy Card

Before writing, infer what you can and ask only for missing information that changes the output. If project context files exist, read them first: `.agents/product-marketing.md`, `.agents/social-media-context.md`, `.claude/product-marketing.md`, or similarly named voice/audience files. Keep the card compact:

```text
Audience:
Reader awareness:   (unaware / problem / solution / product / most-aware — sets how the post opens)
Promise:
Proof available:
Desired action:
Voice:               (fingerprint from a sample if available; see x-copy-frameworks.md)
Language:
Risk to avoid:
```

If essential proof is missing, do not invent it. Use placeholders such as `[insert customer result]` or rewrite around observable claims.

## Research Mode

Use web or user-provided examples only when the request depends on current niche patterns, competitor positioning, or recent discourse. Research should produce a short synthesis, not a swipe file.

1. Identify the niche, topic, and intended audience.
2. Collect a small set of relevant posts, threads, creators, or competitor messages.
3. Extract patterns at the level of strategy:
   - hook mechanism
   - topic angle
   - proof style
   - pacing
   - conversation trigger
   - offer or CTA pattern
4. State what to borrow structurally and what to avoid.
5. Write fresh copy from the user's point of view.

Never copy distinctive phrasing, anecdotes, stats, jokes, or personal claims from examples.

## Writing Loop

1. Name the reader: role, situation, or tension.
2. Choose the post job: teach, provoke, narrate, prove, invite, sell, or respond.
3. Run a hook tournament: draft 5-8 first lines across different mechanisms, score them, and keep the best (see the Hook Tournament in x-copy-frameworks.md). Publish one unless the user asks for options.
4. Draft the body around one idea. If two ideas compete, split into a thread or separate posts.
5. Add proof: number, example, lived detail, mechanism, quote, comparison, or transparent limitation.
6. Tune for X:
   - First line must stand alone.
   - Paragraphs should be short enough to scan on mobile.
   - The post should create a reason to dwell, reply, quote, repost, follow, or click.
   - Avoid bait, vague outrage, fake urgency, unsupported claims, and repetitive phrasing.
7. Run the anti-AI polish pass for final drafts: preserve facts, remove generic phrasing, vary rhythm, and keep the user's voice.
8. Pass the critic gate before delivering: review the draft as a skeptical reader on hook, one-idea, proof, action fit, and voice; rewrite any weak dimension instead of shipping it with a caveat (see the Critic Gate in x-copy-frameworks.md).
9. Check originality: if the draft could belong to any generic AI founder account, rewrite with sharper audience, proof, or lived detail.
10. Deliver ready-to-post copy first, then brief rationale if useful.

## Output Contracts

### Single Post

```text
Post:
[ready-to-post copy]

Notes:
- Hook logic: [why the first line works]
- Interaction path: [reply/repost/quote/follow/click reason]
- Risk check: [what was deliberately avoided]
```

### Thread

```text
Thread arc:
[one sentence describing the reader journey]

Posts:
1/ ...
2/ ...
3/ ...

End:
[soft CTA, question, or follow reason]
```

### Rewrite

```text
Diagnosis:
[highest-impact issue]

Rewrite:
[ready-to-post copy]

Why this is stronger:
[specific changes, not generic praise]
```

### Content Plan

```text
Post lanes:
1. [lane] - [purpose] - [example angle]
2. [lane] - [purpose] - [example angle]
3. [lane] - [purpose] - [example angle]

Cadence:
[practical schedule with variety]
```

### Research Synthesis

```text
Patterns found:
- [pattern, not copied wording]
- [pattern, not copied wording]
- [pattern, not copied wording]

Use:
[how to adapt ethically]

Avoid:
[imitation, weak patterns, or risky claims]

Draft:
[fresh X copy]
```

### Audit

Score each lever 1-5 (see the audit checklist in [references/x-algorithm-principles.md](references/x-algorithm-principles.md)). Lead with the verdict, then fix the weakest lever first.

```text
Verdict:
[one line: ship as-is / fix first / rework]

Scores:
- Audience fit: n/5 - [reason]
- First line: n/5 - [reason]
- Payoff: n/5 - [reason]
- Evidence: n/5 - [reason]
- Action path: n/5 - [reason]
- Trust / negative-feedback risk: n/5 - [reason]
- Account fit: n/5 - [reason]

Weakest lever:
[the one to fix first and why]

Suggested rewrite:
[only the part that needed it, not the whole post]
```

## Quality Standards

- Prefer concrete situations over broad advice.
- Prefer earned proof over adjectives.
- Prefer useful tension over anger.
- Prefer a clean reader payoff over clever wording.
- Prefer a specific next action over generic CTAs.
- Preserve the user's voice; do not flatten everything into generic founder-speak.
- Use the user's requested language. If no language is specified, match the user's language. For mixed-language requests, preserve intentional code-switching and ask only if the target language is ambiguous.

## Hard Limits

Do not fabricate:

- Performance numbers
- Testimonials
- Customer logos
- Personal stories
- Guarantees
- Platform rules not supported by public sources

Do not use manipulative patterns:

- Fake scarcity
- Engagement bait
- Unverifiable "secret" framing
- Rage bait designed mainly to trigger hostility
- Clickbait that withholds the actual value
