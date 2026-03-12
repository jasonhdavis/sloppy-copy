# Task 009: Application UI

## Objective
Implement the web interface for the dashboard, stories, authors, and rewrites.

## Context
The UI should follow the "New York Times (Digital)" aesthetic defined in `STYLE_GUIDE.md` using Material Tailwind components and HTMX.

## Required Files
- `core/views.py`, `core/templates/core/base.html`, `core/templates/core/dashboard.html`
- `stories/views.py`, `stories/templates/stories/list.html`, `stories/templates/stories/detail.html`
- `authors/views.py`, `authors/templates/authors/list.html`, `authors/templates/authors/detail.html`
- `rewrites/views.py`, `rewrites/templates/rewrites/list.html`, `rewrites/templates/rewrites/detail.html`

## Implementation Steps

### 1. Base Template & Editor
- Set up the canonical layout: Header + Main Content + Footer.
- Include HTMX, Alpine.js, and Material Tailwind.
- **Markdown Editor**: Integrate [`EasyMDE`](https://github.com/Ionaru/easy-markdown-editor) for all `TextField` inputs related to prompts, bios, and style guides.
- Apply the typography and color palette from `STYLE_GUIDE.md`.

### 2. Dashboard & Source Digest
- Implement stats cards (Total Stories, Selected, Rewrites, Authors).
- **Source Digest**: A masonry-style block layout showing the "firehose" of ingested news.
- **Filters**: Add filters for Source, Date, and Importance.
- **Feed Testing**: Add a UI component to input a new RSS feed URL and "Test" it (showing a preview of parsed stories before saving).
- Add HTMX buttons to trigger "Fetch Stories" and "Run Pipeline".
- Show the latest `PipelineRun` status.

### 3. List & Detail Views
- Implement list views for Stories, Authors, and Rewrites.
- Use the "Example Card Structure" from `STYLE_GUIDE.md`.
- Implement detail views with side-by-side comparison for Rewrites (Original vs. AI).

## Verification Commands
- `python manage.py runserver`

## Success Criteria
- [x] All pages render without template errors.
- [x] HTMX buttons on the dashboard trigger backend actions and update the UI.
- [x] The UI matches the "credible and authoritative" look of the style guide.
