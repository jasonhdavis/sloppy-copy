# 006 — Editor AI Matching Engine

Matches evaluated stories to the most relevant `Author` profiles using the "Editor AI" and the global **Editorial Style Sheet**.

---

## A. Intent

Process `Story` rows with `status = "evaluated"`.

The "Editor AI" will:
1. Review the story's importance and topic.
2. Consult the **Editorial Style Sheet** for organizational rules.
3. Select the best `Author` based on their persona and current workload/beat.
4. Transition story status to `matched`.

---

## B. Models

`Story`
- `matched_author`
- `status`

`EditorialStyleSheet` (New Model)
- `rules`: TextField (Global guidelines)
- `is_active`: Boolean

`Author`
- `persona_prompt`: TextField (Database editable)
- `expertise_tags`: JSONField

---

## C. Matching Strategy

The "Editor AI" acts as a human editor, making a qualitative decision based on:
- **Author Persona**: Does this story fit the author's unique voice?
- **Style Sheet**: Does this assignment follow organizational rules?
- **Topic Relevance**: Direct match between story tags and author expertise.

---

## D. Service Design: AuthorMatchingService

Methods:
- `match_story(story)`: Calls Editor AI with story context, author list, and style sheet.
- `match_batch(limit)`

Expected JSON output from Editor AI:
```json
{
  "author_id": 123,
  "assignment_rationale": "Fits the author's cynical tech-skeptic persona perfectly."
}
```
