# X Algorithm Principles for Writers

Use this as a writer-facing interpretation of the public `xai-org/x-algorithm` repository (the open-sourced "For You" feed pipeline). It is not a feed-hacking recipe. The useful lesson is that distribution depends on candidate sourcing, predicted user actions, negative-feedback avoidance, and author diversity over time. Source: https://github.com/xai-org/x-algorithm — re-check the README if exact terminology matters.

## What the Public Repo Actually Describes

The repo lays out a sequential pipeline orchestrated by a service called **Home Mixer** (exposes a gRPC `ScoredPostsService`):

1. **Query Hydration**: fetch user context (engagement history, following list).
2. **Candidate Sourcing**: retrieve posts from two sources —
   - **Thunder**: in-memory store of *in-network* posts (accounts you follow).
   - **Phoenix**: ML retrieval that pulls *out-of-network* posts from a global corpus via similarity search.
3. **Candidate Hydration**: enrich candidates with extra data.
4. **Pre-Scoring Filters**: drop ineligible content (see filter list below).
5. **Scoring**: a **Grok-based transformer** (ported from the Grok-1 release, adapted for recsys) predicts engagement probabilities per post.
6. **Selection**: sort by score, take top K.
7. **Post-Selection Filters**: final validation, safety, conversation dedup.

### The score

```text
Final Score = Σ (weight_i × P(action_i))
```

Positive actions carry positive weights; negative actions carry negative weights that push the post down. The model predicts these probabilities (exact names from the repo):

`P(favorite)`, `P(reply)`, `P(repost)`, `P(quote)`, `P(click)`, `P(profile_click)`, `P(video_view)`, `P(photo_expand)`, `P(share)`, `P(dwell)`, `P(follow_author)`, `P(not_interested)`, `P(block_author)`, `P(mute_author)`, `P(report)`.

Two retrieval towers feed sourcing: a **user tower** encodes who the viewer is and what they engage with, a **candidate tower** encodes each post, and out-of-network reach is won when those two embeddings land close. Plain-language consequence: a post travels beyond your followers only when it clearly resembles the kind of thing its ideal reader already opens — vague, audience-less posts have nothing to match against.

### Candidate isolation (important for writers)

During inference, candidates **cannot attend to each other — only to the user context**. A post's score does not depend on which other posts are in the batch. Writer implication: **every post is scored on its own merit.** You cannot lean on a strong thread to drag a weak post 1 along; each tweet has to earn its own predicted actions.

### Not all actions weigh the same

The score is a weighted sum, and the weights are not equal. The older public release of the heavy ranker (`twitter/the-algorithm-ml`, documented around early 2023) is the only place exact numbers were ever printed, and X has said production weights are retuned and no longer published — so treat the *ordering* as the durable lesson, not the figures:

- **A reply the author then replies back to** sat far above everything else. Conversation you actually join beats one-way broadcast.
- **Replies outranked reposts, which outranked likes.** A like is cheap signal; a reply is expensive signal.
- **A profile click that leads somewhere** (the viewer stays) was rewarded — a hook that makes people check who you are pays off.
- **Report was catastrophic** — a single report cost more than dozens of likes earned. Mute and block were also heavily negative.

Writer translation: design for the expensive actions you can honestly earn (reply, quote, profile-click-then-stay), and treat anything that risks a report/mute/block as a direct score tax, not just a vibe.

## Mental Model

Collapse the pipeline into four things a writer can actually influence:

1. **Sourcing**: in-network reach comes from followers (Thunder); out-of-network reach is earned when the post looks similar to things a viewer already engages with (Phoenix). Clear topic identity helps both.
2. **Predicted positive actions**: the score is a weighted sum of `P(action)`; write deliberately for the actions your post can plausibly earn.
3. **Negative feedback**: `not_interested`, `block`, `mute`, `report` carry negative weight. Avoiding these is as valuable as earning likes.
4. **Survival through filters**: freshness, dedup, already-seen/served, muted keywords, and safety filters can quietly remove a post regardless of quality.

Writing cannot control the whole system. It can improve the content's odds by making the right reader understand, care, and act without feeling tricked.

## Writer-Controlled Levers

### 1. Relevance

Help the model and the reader understand who the post is for.

Use:

- Specific audience labels: "solo founder", "B2B SaaS PMM", "AI app builder"
- Specific situations: "before launch", "after churn spikes", "when demos are not converting"
- Recognizable vocabulary from the community

Avoid:

- Generic advice that could apply to anyone
- Hashtag stuffing as a substitute for clear subject matter
- Switching topics so often the account has no recognizable surface area

### 2. Dwell

The public repo names dwell-related predictions. For copy, dwell comes from readable density.

Use:

- A first line that creates tension or a concrete promise
- Short paragraphs
- Sequenced reveals
- Examples after claims
- Lists only when each item adds information

Avoid:

- Long setup before the point
- Dense blocks
- Vague motivational phrasing
- Threads where post 1 overpromises and the body underdelivers

### 3. Positive Actions

The scorer predicts a fixed set of actions, each with its own weight. Design each post for the actions it can plausibly earn, mapped to the exact repo signals.

| Desired action | Repo signal | Write for |
|---|---|---|
| Reply | `P(reply)` | A question with context, tradeoff, or lived experience. |
| Repost | `P(repost)` | A useful frame the reader wants their audience to see. |
| Quote | `P(quote)` | A strong claim with room for agreement, dissent, or extension. |
| Like | `P(favorite)` | A clean, true, resonant line. |
| Share | `P(share)` | Something worth sending to one specific person privately. |
| Profile click | `P(profile_click)` | A post that signals repeat expertise, not a one-off trick. |
| Follow | `P(follow_author)` | A recognizable point of view repeated across related topics. |
| Click | `P(click)` | Native value first, link second. |
| Dwell | `P(dwell)` | Readable density that rewards stopping (see Dwell above). |
| Media expand / view | `P(photo_expand)`, `P(video_view)` | Media that is worth opening for proof or demo, not decoration. |
| Bookmark | not named in the public repo, but the live Posts API exposes `bookmark_count` as its own metric, separate from `like_count`/`repost_count` | Reference-shaped copy the reader wants to find later: numbered breakdowns, frameworks, concrete before/after figures. Live sampling (2026-07) on high-reach accounts shows posts with a numbered comparison or a specific figure routinely pull bookmark counts several times higher than same-account posts that are pure observation/humor, even at similar or lower like counts. |

### 4. Negative Feedback

The scorer predicts `P(not_interested)`, `P(block_author)`, `P(mute_author)`, and `P(report)`, each with a **negative weight** that directly subtracts from the score. A post can get attention and still train the system that many viewers dislike it.

Common copy risks:

- Rage bait without substance
- Claims that sound fake or inflated
- Repeated self-promotion
- Misleading hooks
- Polarizing language outside the user's brand
- Excessive posting of near-duplicates
- Sensitive claims without support

### 5. Variety

The repo includes an **`Author Diversity Scorer`** that attenuates repeated scores from the same author, plus `PreviouslySeenPostsFilter` and `PreviouslyServedPostsFilter` that remove posts a viewer has already encountered, and `DropDuplicatesFilter` / `RepostDeduplicationFilter` / `DedupConversationFilter` that strip near-duplicates. Writer implication: posting the same angle repeatedly competes against your own earlier posts and gets attenuated. Vary formats and angles.

Rotate:

- Observation
- Story
- Mini-framework
- Build-in-public note
- Product lesson
- Customer insight
- Quote-tweet analysis
- Reply that adds expertise
- Offer or launch post

### 6. Freshness and Timing

The pipeline includes an **`AgeFilter`** in pre-scoring, so stale candidates can be dropped before they are ever scored. Note also a **`MutedKeywordFilter`** — words a viewer muted remove your post for that viewer regardless of quality, so avoid gratuitous trigger words. Timing is not a substitute for quality. Use timing as a distribution assist:

- Post when the intended audience is likely to be active.
- Avoid dropping a high-effort thread when you cannot reply for the first stretch.
- For launches, schedule supporting posts before and after the main announcement.
- Do not overfit to universal "best times"; audience behavior matters more.

### 7. Media and Native Value

The public scorer includes media-adjacent actions such as expansion and video view signals. Use media when it makes the idea easier to inspect:

- screenshots for proof
- diagrams for frameworks
- short clips for demos
- carousels when a thread would be visually easier

Do not add visuals as decoration. A weak idea with an image is still a weak idea.

## Audit Checklist

Score each from 1-5:

| Check | Question |
|---|---|
| Audience fit | Is the reader unmistakable? |
| First line | Would the target reader stop scrolling? |
| Payoff | Does the post reward attention quickly? |
| Evidence | Is there proof, mechanism, example, or honest limitation? |
| Action path | Is one likely action clear: reply, repost, quote, follow, click? |
| Trust | Does anything feel inflated, manipulative, or unsupported? |
| Account fit | Does this strengthen the account's long-term topic identity? |
| Format fit | Would text, image, video, poll, or thread carry this idea best? |

Rewrite the weakest area first.
