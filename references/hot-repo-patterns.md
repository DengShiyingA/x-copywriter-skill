# Hot Repository Patterns

**Scope:** this file covers *writing and workflow lessons* to borrow from popular projects — how to structure the copywriting process and judge output quality. For the *tooling layer* (algorithm code, scrapers, MCP servers, data access, automation safety), use [x-open-source-ecosystem.md](x-open-source-ecosystem.md) instead. The two files intentionally do not repeat each other's repo lists.

Use this reference when the user asks to learn from popular open-source projects around AI skills, writing quality, and marketing skill systems. Do not copy README language, prompts, examples, or code. Extract operating patterns only.

## Hot Project Clusters (writing & workflow)

Star counts and rankings change fast; treat every repo as directional and re-check GitHub if exact ranking matters. The point is the *pattern*, not the specific project.

| Cluster | Example repos | The pattern worth borrowing |
|---|---|---|
| X-native staged pipelines | `kangarooking/x-skills`, `PHY041/claude-skill-twitter` | The strongest X skills split the work into discrete gated stages (collect → score topics → create → critic → draft) instead of one mega-prompt, with a weighted topic filter and a forced-rewrite critic before output. |
| Algorithm-mechanics framing | `alirezarezvani/claude-skills` (x-growth) | Encode ranking reality as hard constraints (conversation weighted above likes, link-in-first-reply, length caps) rather than generic "post consistently" advice. |
| Broad marketing skill suites | `coreyhaines31/marketingskills`, `zubair-trabzada/ai-marketing-claude` | Separate context, strategy, creation, review, and reporting; load one shared product/audience context doc that every sub-skill reads first. |
| Hidden analysis layer | `nashsu/Viral_Writer_Skill`, `yabasha/copywrite-skill` | Run an internal analysis pass (audience awareness level, emotional trigger, quotable anchors) that shapes depth without appearing in the output; tag each variant with the rhetorical mechanism it uses. |
| Anchored, voice-matched generation | `oaker-io/wewrite` | Anchor claims to real searched material to prevent invented stats, and extract a few-shot "style fingerprint" from the user's own samples instead of a generic voice. |
| Adversarial review | `aaaronmiller/create-viral-content` | Stress-test a draft from several reader personas (skeptic, expert, fast scroller) before shipping; delegate de-slop to a dedicated pass. |
| Real-time social research | `mvanhorn/last30days-skill`, `Panniantong/agent-reach` | Inspect recent X/Reddit/YouTube/GitHub discourse before writing; agent-reach is read-only, which is the safe research posture. |
| Anti-AI writing cleanup | `blader/humanizer`, `op7418/Humanizer-zh`, `MrGeDiao/shuorenhua`, `conorbronsdon/avoid-ai-writing` | Quality is judged by fact preservation, rhythm, specificity, and voice fidelity; the second residue pass is what separates strong humanizers from word-swappers. |
| Multilingual anti-slop polish | `devswha/patina`, `Aboudjem/humanizer-skill`, `adenaufal/anti-slop-writing` | Per-language tell-lists and protected-span rules; a fidelity score that gates on meaning, treated as an editing signal, not an authorship verdict. |
| Persona / voice analysis | `wordware-ai/twitter` | Analyze an account as a voice/personality system before producing in its register — learn the grammar of the voice, then write new sentences in it. |
| Modular social media skill packs | `blacktwist/social-media-skills`, `chencore/tweet-skills` | Split into context, topic research, hook writing, post writing, polish, calendar, and performance analysis. |
| Long-form repurposing | `megastep/codex-skills/blog-repurpose` and similar | Decompose source into thesis, proof, examples, and platform-specific atoms before writing X-native posts. |

> Tooling-heavy clusters (official algorithm code, scrapers, alternative front ends, MCP servers, automation frameworks) live in [x-open-source-ecosystem.md](x-open-source-ecosystem.md). Findings here are from a June 2026 sweep; the landscape churns, so re-verify before citing any single repo.

## Patterns to Bring Into X Copywriting

### 1. Research before writing

For trend-sensitive posts, inspect recent discourse before drafting. Look for:

- repeated pain points
- words the audience actually uses
- contrarian angles that already have traction
- unanswered questions
- recurring objections
- proof styles the niche accepts

Then write a fresh post from the user's actual point of view.

### 2. Separate the workflow

Do not treat "write a tweet" as one step. Route through:

1. context
2. research
3. angle
4. hook
5. body
6. polish
7. distribution check
8. performance feedback

Skip steps only when the user already supplied enough context.

### 3. Preserve voice

Popular writing-quality projects converge on the same lesson: generic AI tone is the failure mode. Preserve:

- sentence length patterns
- vocabulary level
- favorite phrases
- tolerated sharpness
- humor or lack of humor
- level of self-disclosure
- Chinese/English code-switching habits

### 4. Build collection value

Chinese tweet-writing systems often optimize for "worth saving." Useful checks:

- Does the post contain a non-obvious judgment?
- Does it include a concrete number, example, or mechanism?
- Can the reader reuse the idea later?
- Is there one memorable sentence?
- Did the reader learn something they did not know before?

### 5. Add tool awareness without tool dependency

Many hot projects are tool-heavy: they fetch tweets, search multiple platforms, monitor mentions, or publish automatically. This skill should remain a writing skill:

- Suggest research/fetching when it improves the answer.
- Do not require automation tools for normal drafting.
- Do not post, like, follow, scrape, or monitor unless the user explicitly asks and the relevant tool is available.
- If using external examples, synthesize patterns and cite sources when appropriate.

## Red Flags from Popular Projects

- "Viral" claims without proof.
- Hard-coded engagement hierarchies presented as timeless facts.
- Over-reliance on templates that erase the user's voice.
- Automation before strategy.
- Copying competitor hooks too closely.
- Producing many variants without explaining which one to use.
- Treating likes as the only success signal.

## Strong Default Behavior

When the user asks for X copy informed by hot projects:

1. Briefly state the pattern being borrowed.
2. State what will not be copied.
3. Produce fresh copy.
4. Include one line explaining the intended signal: dwell, reply, repost, quote, follow, or click.
