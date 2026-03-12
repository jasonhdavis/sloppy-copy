# 007 — Rewrite Generation Engine

Generates rewritten articles using multiple source references and author-specific prompts.

---

## A. Intent

Process `Story` rows with `status = "matched"`.

The engine will:
1. Gather **multiple sources** related to the story (based on frequency analysis).
2. Load the matched `Author` and their **database-editable prompt**.
3. Load the **Editorial Style Sheet**.
4. Call the AI provider (OpenRouter) to generate the rewrite.
5. Transition story status to `rewritten`.

---

## B. Models

`Rewrite`
- `story`: FK to Story
- `author`: FK to Author
- `sources_used`: JSONField (List of URLs/Titles)
- `headline`: CharField
- `body`: TextField

---

## C. Service Design: RewriteGenerationService

Methods:
- `generate_rewrite(story)`:
    - Fetches related stories (same topic/frequency group).
    - Constructs prompt using `Author.persona_prompt` + `EditorialStyleSheet.rules`.
    - Sends firehose of source data to AI.
- `generate_batch(limit)`

---

## D. Prompt Design

The prompt is no longer a static file but a dynamic construction:
- **System**: Editorial Style Sheet rules.
- **User**: Author persona instructions + Multiple source summaries + Original story context.

Expected JSON output:
```json
{
  "headline": "The Great AI Delusion",
  "body": "In a world obsessed with silicon dreams...",
  "sources_cited": ["https://source1.com", "https://source2.com"]
}
```
