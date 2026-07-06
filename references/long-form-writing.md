# Long-Form Writing (X Articles)

Use this when the request is a long-form piece meant to be read as one continuous document — an X Article, a long-form post repurposed for X's article format, or any writing that runs past a few short paragraphs. For everything under that length, use the short-form rules in [x-copy-frameworks.md](x-copy-frameworks.md) and [anti-ai-polish.md](anti-ai-polish.md) instead — they are tuned for 280-character posts and actively wrong for this format.

## Scope

Handle:

- X Articles (long-form posts published through X's article feature)
- long-form pieces the user plans to publish elsewhere and link from X
- the "write the long version first" step of repurposing, before atomizing it into short posts

Do not use this file for single posts, threads, replies, or quote tweets — route those through the short-form writing loop.

## Why Short-Form Rules Invert Here

`anti-ai-polish.md` deliberately breaks several long-form humanizer conventions because X posts are short and candidate-isolated. None of those inversions apply to a long-form piece:

| Short-form rule (X posts) | Long-form reality |
|---|---|
| Drop headers and visual scaffolding | Headers and section breaks help a reader navigate and are expected, not a tell |
| Near-zero tolerance for one stock connector | One forgivable transition in 1,000+ words is not fatal; the reader has more runway to recover |
| Keep fragments and abrupt openers | A long piece still needs an entry point, but sentence fragments used throughout read as underdeveloped, not native voice |
| Kill meta-openers hard because characters are scarce | Characters are not scarce; the problem with a slow opener in long form is pacing, not space |

The things that do **not** change: fact lock, specificity upgrades, voice preservation, and evidence discipline all still apply exactly as in short form.

## Structure

A long-form piece is a sequence of sections, not one long paragraph and not a thread stretched into headers.

1. **Title**: state the concrete outcome or tension, not a vague topic label. Avoid clickbait that the body can't pay back.
2. **Open**: one to three short paragraphs that establish why this matters now and what the reader will get. Do not summarize the whole piece here — earn the read, don't front-load it.
3. **Context / setup**: only the background the reader needs to follow the rest. Cut anything decorative.
4. **Body sections**: one idea per section, each with its own natural sub-heading if the piece is long enough to need navigation (roughly 800+ words). Each section should stand on its own if someone jumps straight to it from a link.
5. **Evidence woven through, not dumped at the end**: numbers, examples, screenshots, or lived detail belong next to the claim they support.
6. **Synthesis**: what the sections add up to — the piece's actual point, not a restatement of the title.
7. **Close**: a real final thought, a next step, or an invitation to respond — not a generic summary paragraph.

## Section Design

- Give each section a job: it should teach, prove, complicate, or transition — never pad.
- Vary section length. A long-form piece with uniform section lengths reads mechanically.
- Use sub-headings as navigation aids for pieces long enough to need them, not as a way to avoid writing real transitions.
- If a section could be deleted without losing the argument, delete it.

## Anti-AI Pass for Long-Form

Run this instead of the X-specific pass in `anti-ai-polish.md` step 0 (everything else in that file — Fact Lock, Generic Voice Check, Specificity Upgrade, Voice Preservation, and the language-specific worked examples — still applies as written).

1. **Detect stock long-form openers**: "In today's fast-paced world," "在当今快速发展的时代," "As we all know," "Let's dive in." Cut them; start where the actual tension starts.
2. **Vary paragraph and section rhythm**: mix short punchy paragraphs with longer developed ones. Uniform paragraph length across a long piece is one of the strongest AI tells.
3. **Check transitions for function, not just presence**: a transition should connect two specific ideas. Cut any transition that would still make sense pasted into an unrelated piece ("Furthermore," "It is worth noting that," "In conclusion,").
4. **Verify the ending earns its place**: a summary paragraph that just restates each section heading is a tell. The close should add a thought the reader didn't already have.
5. **Second pass for residue**: reread once specifically for phrasing the rewrite itself introduced — long-form humanizing often leaves its own generic fingerprints if not checked twice.

## Output Contract

```text
Title:
[concrete, earns the read]

Article:
[full long-form text with natural section breaks]

Notes:
- Arc: [one line describing the reader's journey through sections]
- Evidence map: [where the proof lives, so nothing reads as unsupported]
- Risk check: [what was deliberately avoided]
```

## Repurposing Into Short Form

When a long-form piece needs to become short posts afterward (or vice versa — a short idea needs to become a long-form piece), use [x-copy-frameworks.md](x-copy-frameworks.md)'s "Repurposing Long-Form Content" extraction pass. Do not simply chop the long-form text into 280-character segments — that produces a thread that reads like an amputated article, not native short-form copy.
