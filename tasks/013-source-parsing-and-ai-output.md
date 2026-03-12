# Task 013: Source Parsing and AI Output

## Objective
Improve the parsing of source material (HTML/Images) and ensure AI output includes proper formatting and images.

## Context
M'Lord wants to ensure that raw source material is cleaned up (HTML stripped or interpreted) and that the AI-generated rewrites are rich with formatting and images.

## Required Files
- `sources/services.py` (FeedIngestionService)
- `rewrites/services.py` (RewriteGenerationService)
- `prompts/author_rewrite.md`

## Implementation Steps

### 1. Source Parsing Improvements
- Update `FeedIngestionService` to better handle HTML in `Story.summary` and `Story.content`.
- Use `BeautifulSoup` or similar to strip unwanted tags while preserving structure if needed.
- Extract image URLs from the source feed and store them in the `Story` model (may need a new field or JSON field).

### 2. AI Prompting for Rich Output
- Update `prompts/author_rewrite.md` to explicitly instruct the AI to:
  - Use Markdown for formatting (bold, italics, lists, subheadings).
  - Suggest placement for images (e.g., `[IMAGE: description]`).
  - Maintain the author's specific voice and style.

### 3. Rewrite Generation
- Update `RewriteGenerationService` to handle the rich output.
- If the AI suggests images, try to match them with images extracted from the source or use placeholders.

## Verification Commands
- `python manage.py ingest_feeds`
- `python manage.py generate_rewrites`
- View a `Rewrite` in the CMS or Front End to check formatting and images.

## Success Criteria
- [x] Source stories have clean, readable summaries.
- [x] AI-generated rewrites use Markdown formatting.
- [x] Images from sources are preserved or referenced in the rewrites.
