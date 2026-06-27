# X Copywriter

An original, multilingual copywriting skill for X/Twitter. It drafts, rewrites, critiques, and plans posts in **any language the user writes in** — single posts, threads, replies, quote tweets, launch copy, founder-voice content, content calendars, long-form repurposing, and anti-AI-tone polishing.

The skill applies marketing strategy, audience psychology, evidence discipline, language-specific voice adaptation, and a writer-facing read of public X algorithm signals — without copying external templates or claiming to game the feed.

## What makes it different

- **Writes for the right action, not just "engagement."** Maps copy to the actions X actually rewards (reply, quote, profile-click-then-stay) and away from the ones it taxes (mute, block, report).
- **Hook tournament.** Drafts several hooks across distinct mechanisms, scores them on stop / stake / specificity / truth, and ships the strongest — never the first catchy-but-vague line.
- **Critic gate.** Every draft passes a skeptical pre-delivery review (hook, one idea, proof, action fit, voice); weak dimensions are rewritten before you see the copy.
- **Topic scoring and A/B variants.** For higher-stakes work, it scores topic candidates, tests two distinct angles, critiques both, and selects the stronger final.
- **Voice fingerprint.** Matches your real voice from samples instead of flattening everything into generic founder-speak.
- **Anti-AI polish tuned for X.** Inverts long-form humanizer rules — keeps fragments and punchy one-liners, drops article-style scaffolding, and holds near-zero tolerance for AI tells in 280 characters.
- **Genuinely language-neutral.** Output matches the user's language by default. Chinese and English appear as worked examples of a universal method, not a privileged pair.
- **Evidence discipline.** Never fabricates numbers, testimonials, logos, stories, or platform rules.
- **X appeals with factual continuity.** Drafts account, post, feature, and monetization review requests in any requested language while checking prior submissions for contradictions and unsupported claims.

## Structure

```
SKILL.md                          # entry point: rules, task router, strategy card, writing loop, output contracts
references/
  x-algorithm-principles.md       # writer-facing read of the public X ranking pipeline
  x-copy-frameworks.md            # hooks, awareness calibration, voice fingerprint, threads, offers, critic gate
  hot-repo-patterns.md            # writing/workflow patterns to borrow from popular projects
  x-open-source-ecosystem.md      # X tooling, data access, and automation safety limits
  topic-scoring-and-variants.md   # topic scoring, A/B tests, critic scores, optional JSON output
  x-appeals.md                    # X enforcement and eligibility appeals, multilingual
  anti-ai-polish.md               # final-pass humanization, multilingual
  language-adaptation.md          # writing/adapting across languages
  examples.md                     # calibrated examples, including the internal tournament + critic-gate flow
agents/claude.yaml                # interface metadata
```

## Installation

This is a [Claude Code](https://claude.com/claude-code) agent skill. Install it by cloning the repo into a skills directory, using the **skill name** (`x-copywriter`) as the folder name.

**Personal (available in every project):**

```bash
git clone https://github.com/DengShiyingA/x-copywriter-skill.git ~/.claude/skills/x-copywriter
```

**Project-scoped (checked in with one repo):**

```bash
git clone https://github.com/DengShiyingA/x-copywriter-skill.git .claude/skills/x-copywriter
```

To update later:

```bash
git -C ~/.claude/skills/x-copywriter pull
```

Claude Code auto-discovers any directory under a skills path that contains a `SKILL.md`, so no further configuration is needed. Verify it loaded by running `/help` (it should appear in the skills list) or just by asking for X copy.

## Using it

Once installed, invoke it by asking for X/Twitter copy — drafting, rewriting, threads, launches, content plans, audits, or anti-AI polish, in any language. The skill triggers on requests like "write an X thread", "rewrite this tweet", "推文改写", or "founder launch post".

## On the algorithm references

The algorithm notes are a *writer-facing interpretation* of public open-source material (e.g. `xai-org/x-algorithm`, the older `twitter/the-algorithm-ml` weights, and Community Notes ranking). They improve audience fit, first-line clarity, and negative-feedback avoidance. They are **not** a reach guarantee — production ranking is retuned and not fully published, so the skill treats signal *ordering* as durable guidance, never as deterministic outcomes.

## License

[MIT](LICENSE).
