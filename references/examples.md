# X Copywriter Examples

Use these examples to calibrate output shape and quality. Do not treat them as fixed templates. Preserve the user's context, voice, language, and evidence.

## Example 1: Chinese Single Post

User intent:

```text
给一个 AI 编程工具写中文推文，面向独立开发者，不要太营销。
```

Good output shape:

```text
很多独立开发者用 AI 编程工具的方式错了。

不是让它“帮我写个功能”。
而是让它先把问题拆成：

1. 哪些文件会被影响
2. 哪些状态会被打破
3. 哪些测试能证明没坏

AI 真正省时间的地方，不是多打几行代码。
是少走三次错路。

Notes:
- Hook logic: 第一句直接挑战默认用法，独立开发者会下意识对号入座。
- Interaction path: 可保存/转发——清单本身有复用价值。
- Risk check: 没有吹产品功效，只讲使用方式，规避无源夸大。
```

This shows the full Single Post contract: ready-to-post copy first, then the `Notes` block (hook logic / interaction path / risk check).

Why it works:

- Names a specific reader: independent developers.
- Uses a tension pair: common use vs better use.
- Avoids unsupported product claims.
- Creates save/repost value through a reusable checklist.

## Example 2: Thread for Product Launch

User intent:

```text
Write a launch thread for a tool that turns customer interviews into product insights.
Audience: early-stage founders. Proof: processed 42 interviews in beta.
```

Good output shape:

```text
Thread arc:
Show founders that the bottleneck is not collecting interviews; it is turning scattered notes into decisions.

Posts:
1/ Founders do not have a customer interview problem.

They have a synthesis problem.

You can record 20 calls and still walk away with a folder full of quotes, no roadmap signal, and 3 conflicting opinions.

2/ We built [product] for the moment after the call ends.

It takes interview notes and pulls out:
- repeated pains
- buying triggers
- objections
- feature requests
- exact customer language

3/ In beta, teams used it across 42 interviews.

The surprising part: the biggest value was not "summaries."

It was seeing which customer comments belonged to the same decision.

4/ If your roadmap is being pulled by the loudest recent call, this gives you a calmer view.

Not perfect truth.
Better signal.

End:
We're opening access this week. Reply "interviews" and I'll send the beta link.
```

Why it works:

- Opens with a reframed problem.
- Uses available proof without exaggerating it.
- Avoids claiming the product replaces judgment.
- CTA fits conversation instead of forcing a hard sell.

## Example 3: Rewrite

Weak draft:

```text
Our platform is revolutionary and helps teams unlock next-level productivity with AI-powered insights.
```

Better rewrite:

```text
Most teams do not need more AI dashboards.

They need one clear answer:

"What changed this week, and what should we do next?"

That's the job our product is built for.
```

Why it works:

- Replaces hype with a concrete job.
- Uses a quotable line.
- Creates a clearer reader payoff.

## Example 4: Quote Tweet or Reply

User intent:

```text
Reply to someone saying "founders should post every day."
Tone: thoughtful disagreement.
```

Good output:

```text
Daily posting helps only after you know what you are trying to be known for.

Before that, it often just creates a larger pile of unclear signals.

I'd rather see founders post 3x/week around one sharp thesis than 7x/week around random updates.
```

Why it works:

- Disagrees without dunking.
- Adds a condition instead of a blanket rule.
- Gives a concrete alternative.

## Example 5: Research Synthesis

User intent:

```text
Research what AI app builders are talking about this week and write a post for my devtool.
```

Good output shape:

```text
Patterns found:
- Builders are comparing "fast prototype" with "maintainable product."
- The strongest posts use concrete failure stories, not generic AI optimism.
- Comments cluster around debugging, deployment, and code review trust.

Use:
Frame the devtool as a way to make AI-generated work reviewable.

Avoid:
Do not claim it makes engineers obsolete or ships production code untouched.

Draft:
The AI app builder bottleneck moved.

Last year it was:
"Can I make a prototype?"

Now it is:
"Can I trust this code enough to keep building on it?"

The tools that win will not just generate more code.
They will make the code easier to inspect, test, and change.
```

Why it works:

- Separates research patterns from final copy.
- Does not imitate source posts.
- Turns trend research into a specific thesis.

## Example 6: Content Plan

User intent:

```text
I'm a solo founder building an open-source dev tool. Give me a posting plan
so my account stops being random updates. 3-4 lanes, realistic cadence.
```

Good output shape:

```text
Post lanes:
1. Build notes - show the work, earn trust - "What broke this week and the fix that stuck."
2. Sharp opinion - stake a thesis, invite replies - "Why most CLI tools lose users at install, not usage."
3. User-shaped proof - turn real usage into authority - "A maintainer used it to cut CI time; here's the before/after."
4. Quiet offer - convert without hype - "Made this for X devs; here's the one job it does well."

Cadence:
- 3-4 posts/week, not daily.
- Rotate lanes so no two consecutive posts share a job.
- Opinion + build notes mid-week; proof/offer when you actually have evidence.
- Reply inside your niche on off days instead of forcing a new post.
```

Why it works:

- Lanes are repeatable jobs, not a list of topics.
- Each lane states a purpose and a concrete example angle.
- Cadence is realistic and tied to having real proof, not a fixed quota.

## Example 7: Audit

User intent:

```text
Audit this draft before I post it:
"Our AI platform is a game changer that helps teams unlock 10x productivity. Try it now!"
```

Good output shape:

```text
Verdict:
Rework before posting.

Scores:
- Audience fit: 1/5 - "teams" could be anyone; no role or situation.
- First line: 2/5 - "game changer" is generic; nobody stops scrolling.
- Payoff: 1/5 - no information, only an adjective.
- Evidence: 1/5 - "10x productivity" is an unsupported number.
- Action path: 2/5 - "Try it now" is premature with no native value first.
- Trust / negative-feedback risk: 1/5 - reads as inflated AI copy; high skip/mute risk.
- Account fit: 2/5 - says nothing repeatable about what the account stands for.

Weakest lever:
Evidence. The "10x" claim is fabricated and poisons trust; everything else follows from having no concrete proof.

Suggested rewrite:
Most teams don't need another AI dashboard.

They need one answer: "What changed this week, and what do we do next?"

That's the only job we built this for.
```

Why it works:

- Leads with a verdict, not a wall of scores.
- Each score has a one-line reason tied to a lever.
- Fixes the weakest lever (fabricated proof) instead of polishing surface wording.

## Example 8: Internal Process (Hook Tournament + Critic Gate)

This example shows the machinery that normally stays hidden. The user only receives the final post; the scoring below is what happens internally before delivery.

User intent:

```text
Single post. Audience: indie devs shipping with AI coding tools.
Claim: the bottleneck is reviewing AI output, not generating it.
Voice: blunt, lowercase, no emoji. Proof: my own week, ~30 PRs.
```

Internal — hook tournament (draft several mechanisms, score Stop / Stake / Specificity / Truth, 1-5):

```text
A. "AI can write code faster than you can read it."        Stop 4 Stake 4 Spec 3 Truth 5  = strong
B. "The bottleneck moved and most devs didn't notice."     Stop 3 Stake 3 Spec 2 Truth 4  = vague
C. "I shipped 30 PRs with AI last week. 25 were the easy part." Stop 4 Stake 3 Spec 5 Truth 5 = strong, specific
D. "Stop generating code. Start reviewing it."             Stop 3 Stake 2 Spec 2 Truth 3  = preachy, thin
E. "Your AI tool is fast. Your review process is not."     Stop 3 Stake 3 Spec 3 Truth 4  = ok

Pick: C as the lead (highest specificity, true to the proof), A's framing folded into the body.
```

Internal — critic gate on the drafted post (1-5; rewrite anything 1-2):

```text
Hook 5 - concrete number + tension in line one.
One idea 5 - stays on "review is the real work."
Proof 4 - uses the real 30-PR week without inflating it.
Action fit 4 - invites replies from devs with the same experience.
Voice 3 -> fix: first draft had a capitalized sentence and a tidy summary line; both off-voice. Lowercase it, cut the summary.
```

Delivered post (what the user sees):

```text
i shipped 30 PRs with AI last week. 25 of them were the easy part.

generating the code took minutes. reading it closely enough to trust it took the rest of the week.

the tool didn't make me faster. it moved the slow part from typing to reviewing.

curious if other people feel this or if i'm just slow at review.
```

Why it works:

- The tournament kept the most specific true hook instead of the catchiest vague one.
- The critic gate caught a voice slip (capitalization + summary ending) and forced the fix before delivery, not after.
- The close invites `P(reply)` honestly — a real question, not engagement bait.
- The proof is the user's actual week, never inflated.
