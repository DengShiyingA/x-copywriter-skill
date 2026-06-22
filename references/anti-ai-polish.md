# Anti-AI Polish for X Copy

Use this as the final pass for X posts, threads, replies, and launch copy. It distills common lessons from popular humanizer, avoid-AI-writing, anti-slop, "说人话", and multilingual polish skills into a narrow X-writing workflow. Do not copy their rules wholesale; apply the underlying editing moves.

## Popular Project Baseline

Prioritize patterns from popular, active repositories before using long-tail derivatives. Tiers below are directional (most → least adopted at the time of writing); re-check GitHub if exact ranking matters.

| Repo | Tier | Why it matters |
|---|---|---|
| `blader/humanizer` | flagship | The dominant Claude/OpenCode humanizer skill; emphasizes voice calibration, AI-sign audit, and a second rewrite pass. |
| `op7418/Humanizer-zh` | flagship (zh) | High-signal Chinese adaptation of humanizer-style rules; useful for Chinese AI tone cleanup. |
| `conorbronsdon/avoid-ai-writing` | established | Strong audit/rewrite structure with detect, rewrite, edit, voice profile, and second-pass verification modes. |
| `MrGeDiao/shuorenhua` | established (zh) | Chinese-first "说人话" skill; strong on preserving facts while removing Chinese AI tone, translationese, and over-formal posture. |
| `inhouseseo/superseo-skills` | niche | Shows anti-AI-slop rules embedded inside production SEO/content workflows rather than used as a standalone gimmick. |
| `devswha/patina` | niche (multilingual) | Multilingual deterministic polish across Korean, English, Chinese, and Japanese with meaning-preservation constraints. |
| `jalaalrd/anti-ai-slop-writing` | niche | Compact anti-slop writing skill focused on banned phrases, structural tells, punctuation tells, and accuracy failures. |
| `Aboudjem/humanizer-skill` | niche | Pattern scoring approach with voice profiles and an explicit "AI-tell" score. |
| `adenaufal/anti-slop-writing` | niche | Universal anti-slop prompt, useful for multilingual plainness and naturalness constraints. |

Treat smaller language-specific forks as supporting evidence only when the user's language or domain matches.

## Source Pattern Summary

Open-source anti-AI writing projects converge on a few ideas:

- Preserve meaning before changing style.
- Detect patterns before rewriting.
- Match a real voice, not a generic "natural" voice.
- Remove inflated language, empty transitions, and overexplained structure.
- Vary sentence rhythm.
- Replace abstract claims with concrete details.
- Do a second pass because the first rewrite often leaves AI residue.
- Treat each language and locale differently; Chinese, English, and bilingual accounts have extra notes because they are common X use cases.

Representative hot projects include `blader/humanizer`, `op7418/Humanizer-zh`, `conorbronsdon/avoid-ai-writing`, `MrGeDiao/shuorenhua`, `devswha/patina`, `jalaalrd/anti-ai-slop-writing`, `Aboudjem/humanizer-skill`, and `adenaufal/anti-slop-writing`.

## X-Specific Anti-AI Pass

Run these checks after the post already has a clear idea.

### 0. X is not long-form — invert some rules

Most humanizer tools are tuned for articles. Several of their "AI tells" are correct for essays but wrong for X, and a few X-native moves get falsely flagged. Adjust before applying any long-form ruleset:

- **Keep fragments and one-line punches.** On X a sentence fragment or an abrupt opener is native voice, not a defect. Long-form tools that "fix" staccato rhythm will flatten good X copy.
- **Drop the visual-structure category.** Headers, bold scaffolding, and decorative formatting are long-form slop signals; on X they barely apply, and an emoji is a voice choice, not automatically a tell.
- **Residue tolerance is near zero.** In 280 characters, one stock connector or one "not X, but Y" reads as obviously AI. A tell that's forgivable in a 1,000-word piece is fatal in a post.
- **Fact-lock matters more, not less.** With little surrounding context, a flipped number or polarity is more damaging and harder for the reader to recover.
- **Kill meta-openers hard.** "Let's dive in", "在这个…的时代", throat-clearing windups — they waste scarce characters and signal a template. Start at the tension.

### 1. Fact Lock

Before polishing, mark facts that must not change:

- numbers
- names
- dates
- product claims
- customer evidence
- technical terms
- quote wording
- risk disclaimers
- causal relationships

If the draft lacks evidence, do not invent it during polish.

### 2. Generic Voice Check

Flag lines that could appear in any AI-generated founder post:

- "This is a game changer"
- "In today's fast-paced world"
- "Unlock the power of"
- "It's not just X, it's Y"
- "The future of [category] is here"
- "Here's why it matters"
- "Let's dive in"
- "Hope this helps"
- "Comment below"

Replace with a concrete observation, a specific reader situation, or a sharper close.

### 3. Rhythm Check

AI drafts often sound too even. For X:

- Mix short and medium lines.
- Let one sentence stand alone when it carries the point.
- Remove symmetrical three-part lists unless each item matters.
- Cut filler transitions.
- Avoid overusing em dashes, semicolons, and polished paragraph cadence.

Good X rhythm often feels like thinking in public, not presenting a memo.

When a line reads as AI, **rebuild the sentence, do not swap words.** Replacing one flagged word with a synonym leaves the AI sentence *shape* intact, and both readers and detectors still catch it. Recast the whole structure instead.

### 4. Specificity Upgrade

Replace:

- "teams" with a real role or stage
- "productivity" with the task that got faster
- "insights" with what the user can decide
- "AI-powered" with what the model actually does
- "seamless" with the friction removed
- "innovative" with the mechanism

### 5. Voice Preservation

If the user provides prior posts or a voice sample, extract:

- sentence length
- directness
- tolerated slang
- punctuation habits
- Chinese/English mix
- how personal they get
- how hard they sell
- whether they use humor

Do not "professionalize" a casual voice or "casualize" a precise technical voice unless asked.

## Language-Specific Pass

Use [language-adaptation.md](language-adaptation.md) for target-language selection, translation/adaptation, locale, and code-switching. This file focuses on polish after the language choice is clear.

### Universal Method (works for any language)

The named lists below are **worked examples, not a privileged set of languages**. For any target language, run the same four steps:

1. **Find this language's stock openers** — the phrases AI uses to warm up before the point (the equivalent of "In today's..." or "在当今...").
2. **Find translationese** — sentence shapes imported from English that a native writer would not use.
3. **Find inflated register** — adjectives, business jargon, or over-formal posture heavier than the audience speaks.
4. **Find mechanical connective tissue** — symmetric lists, even rhythm, and empty transitions.

Then rewrite by starting closer to the point, keeping one clear judgment, using native word order, and ending with a real thought instead of a summary. If you are not fluent in the tells of a given language, write plainer and simpler rather than guessing at idiom. The worked examples below show what this looks like for the most common X languages; apply the same lens to Spanish, Japanese, Arabic, French, Portuguese, and any other.

### Worked example: any non-English copy

For any non-English X copy:

- Watch for literal English translation structure.
- Use local syntax and punctuation conventions.
- Prefer plain, native-sounding verbs over imported business jargon.
- Keep standard English product/category terms only if the audience actually uses them.
- Do not add slang unless the user's voice supports it.
- If uncertain, write cleaner and simpler rather than more idiomatic.

### Worked example: Chinese "说人话"

For Chinese X copy, watch for:

- 过度承接: "首先/其次/最后/值得注意的是"
- 宏大铺垫: "在当今快速发展的时代"
- 互联网黑话: "赋能/闭环/抓手/沉淀/认知升级"
- 翻译腔: "这不仅是 A，更是 B"
- 工程汇报腔: "根因坐实/差异收窄/链路打通"
- 小红书 AI 腔: "你不是 X，你只是 Y"
- 无源权威: "越来越多的人意识到"

Rewrite by:

- starting closer to the point
- keeping one clear judgment
- using normal spoken Chinese when appropriate
- preserving technical facts, commands, versions, and responsibility
- cutting performative empathy or fake certainty

### Worked example: English

For English X copy:

- Prefer plain verbs.
- Avoid corporate adjectives.
- Keep claims smaller and sharper.
- Replace summary endings with a concrete final line.
- Avoid formulaic "not X, but Y" unless the contrast is genuinely useful.
- **Never use "X" as a placeholder variable when the platform is X.** Phrases like "it's not just X, it's Y" collide with the platform name and erase it from the post. Use "A/B", "this/that", or concrete nouns instead, so every "X" in the copy reads as the platform.
- Use contractions only if they fit the user's voice.
- Do not add emojis by default.

### Worked example: Spanish

For Spanish X copy, watch for:

- inflated openers: "En el mundo actual...", "Hoy en día..."
- empty connectives: "Es importante destacar que...", "Cabe mencionar que..."
- imported business jargon: "potenciar", "revolucionario", "solución integral"
- translationese: literal "no es solo X, sino Y" carried over from English
- over-formal "usted" register when the audience speaks informally

Rewrite toward the audience's real register (tú vs. usted by market), plain verbs, and a concrete first line.

### Worked example: Japanese

For Japanese X copy, watch for:

- stock openers: "近年", "現代社会において", "皆さんは〜でしょうか"
- over-polite scaffolding that buries the point under keigo when X expects a sharper voice
- mechanical connectives: "まず／次に／最後に", "〜と言えるでしょう"
- inflated katakana buzzwords used only to sound advanced
- translationese from English marketing phrasing

Rewrite by leading with the claim, matching the account's politeness level (plain vs. です・ます), and cutting filler sentence-enders.

### Worked example: bilingual / code-switching

For Chinese-English X accounts (the same logic applies to any language pair):

- Keep standard product terms in English when the audience expects them.
- Do not translate technical terms into awkward Chinese.
- Do not sprinkle English to look sophisticated.
- Use English only when it improves precision, searchability, or community fit.

## Two-Pass Polish

1. **Detection pass**: list only the top 3 AI tells.
2. **Rewrite pass**: fix them with minimal changes.
3. **Residue pass**: reread the result and remove any new generic phrasing introduced by the rewrite.

For short X posts, return only the final copy unless the user asks for diagnosis. For audits or rewrites, include the top issues and why the rewrite is stronger.

## Quick Score

Score each 0-2:

| Area | 0 | 1 | 2 |
|---|---|---|---|
| Fact fidelity | changes or invents facts | mostly preserved | fully preserved |
| Specificity | abstract | partly concrete | concrete and situated |
| Rhythm | uniform | some variation | natural variation |
| Voice fit | generic | acceptable | clearly fits user/account |
| AI residue | obvious | minor | clean |

Rewrite until no area is 0.
