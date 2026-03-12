# 005 — Editor AI Evaluation Engine

Evaluates ingested stories using the "Editor AI" persona. Instead of subjective scoring, the engine focuses on **frequency analysis** and **editorial importance** across the firehose of news.

---

## A. Intent

Process `Story` rows with `status = "ingested"`.

The "Editor AI" will:
- Analyze headlines and ledes from a batch of stories.
- Identify recurring themes and frequency of topics.
- Determine "Importance" based on how often a story or topic appears across different sources.
- Transition story status to `evaluated`.

---

## B. Models

Model: `Story`

Relevant fields:
- `title`
- `summary`
- `importance_score` (derived from frequency/relevance)
- `editor_rationale`
- `status`

---

## C. Service Design: EditorService

Primary class: `EditorService`

Methods:
- `analyze_frequency(stories)`: Groups stories by topic and counts occurrences.
- `evaluate_importance(story, context_batch)`: Uses AI to determine if a story is a "must-cover" based on the current news cycle.
- `process_batch(limit)`

### Evaluation Logic
1. **Frequency Check**: If a topic appears in >X% of sources, it is flagged as high importance.
2. **Editor AI Review**: The AI acts as a Managing Editor, reviewing the "firehose" and selecting stories that fit the organization's **Editorial Style Sheet**.

---

## D. AI Prompt (Database Editable)

The prompt for the Editor AI is stored in the database (e.g., in a `SystemConfig` or `EditorProfile` model) to allow for real-time tuning of the "editorial voice."

Expected JSON output:
```json
{
  "importance": 0.9,
  "rationale": "Topic appearing across 5 major feeds; high public interest.",
  "tags": ["Politics", "Breaking"]
}
```
