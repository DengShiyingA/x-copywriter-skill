# Topic Scoring and Variants

Use this reference when the user has multiple possible topics, wants A/B variants, asks for a more rigorous draft pass, or needs machine-readable output for a feedback loop. This borrows the useful structure from staged X-skill pipelines while keeping `x-copywriter` as a writing skill, not an automation system.

## Topic Scoring

Score topics before writing when the user provides several candidates or asks "which should I post?"

| Criterion | Weight | Ask |
|---|---:|---|
| Heat / trend | 0-3 | Is this live now for the intended audience? |
| Value density | 0-3 | Does it teach, reveal, explain, or help someone act? |
| Discussion potential | 0-2 | Can reasonable people reply, disagree, extend, or add examples? |
| Account fit | 0-2 | Does this strengthen the account's repeatable topic identity? |
| Freshness bonus | -1 to +1 | Is it timely or stale? |
| Repetition penalty | 0 to -2 | Is it too similar to recent posts or rejected ideas? |

Default threshold:

- **8+**: write now
- **6-7**: keep as backup or narrow the angle
- **5 or below**: skip unless the user has a strategic reason

Return a compact table:

```text
Topic scores:
1. [topic] - n/10 - [why]
2. [topic] - n/10 - [why]
3. [topic] - n/10 - [why]

Pick:
[topic] because [single decisive reason]
```

## Repetition Check

If the user supplies prior posts, rejected topics, or analytics, compare new candidates against them.

Reject or penalize:

- same claim with a new wrapper
- same source repeated too often
- same post shape repeated too often
- same CTA repeated too often
- topic that already attracted negative feedback

If no history is available, do not pretend to know. Use a soft note: "No posting history supplied, so repetition risk is unknown."

## A/B Variant Strategy

Generate A/B variants when:

- the post is for a launch or offer
- the user asks for options
- there are two plausible angles
- the topic is sensitive or high-risk
- the best action path is unclear

Default split:

| Variant | Job |
|---|---|
| A | More direct, higher contrast, stronger first-line tension. |
| B | More evidence-led, structured, nuanced, and lower risk. |

Do not make A and B tiny wording changes. They should test different strategic angles.

## Critic Score

Score each variant 0-10 after anti-AI polish.

| Dimension | Weight | Question |
|---|---:|---|
| Hook | 2 | Would the target reader stop? |
| Payoff | 2 | Does the post reward attention? |
| Proof | 2 | Is there evidence, mechanism, example, or honest limit? |
| Action path | 2 | Is one response likely and earned? |
| Voice / trust | 2 | Does it sound like the account and avoid overclaiming? |

If both variants score below 7, rewrite once from a sharper angle before showing the final.

Use this compact output unless the user asks for full scoring:

```text
Critic:
- A: 8/10 - stronger hook, slightly higher disagreement risk.
- B: 7/10 - clearer proof, less memorable opening.

Selected: A, because the topic needs contrast more than explanation.
```

## Machine-Readable Output

Only include JSON when useful for automation, logging, analytics, or handoff. Do not include JSON in normal casual drafting.

### Topic Score JSON

```json
X_TOPIC_SCORE_JSON
{
  "schema_version": "x_copywriter.topic_score.v1",
  "language": "...",
  "topics": [
    {
      "topic": "...",
      "scores": {
        "heat": 0,
        "value_density": 0,
        "discussion": 0,
        "account_fit": 0,
        "freshness_bonus": 0,
        "repetition_penalty": 0
      },
      "final_score_0_10": 0,
      "recommendation": "write_now|backup|skip",
      "reason": "..."
    }
  ],
  "selected_topic": "..."
}
```

### Draft JSON

```json
X_COPYWRITER_JSON
{
  "schema_version": "x_copywriter.create.v1",
  "language": "...",
  "topic": "...",
  "post_type": "single|thread|reply|quote|plan|audit",
  "intended_action": "reply|repost|quote|follow|click|bookmark",
  "variants": [
    {"id": "A", "score_0_10": 0, "text": "..."},
    {"id": "B", "score_0_10": 0, "text": "..."}
  ],
  "selected": "A|B",
  "risk_flags": ["..."],
  "notes": ["..."]
}
```

## Feedback Loop

When the user reports outcomes, store the lesson in prose unless a real state store exists.

Capture:

- topic
- language
- post shape
- intended action
- result signal
- what changed in the final edit
- whether to repeat, revise, or avoid this lane

Useful feedback prompts:

```text
What happened after posting?
- impressions:
- replies:
- reposts/quotes:
- follows/profile clicks:
- negative feedback:
- your own rating:
```

Use the next draft to test one variable at a time: hook, topic, proof, CTA, or format.
