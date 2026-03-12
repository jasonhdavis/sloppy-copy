# Task 011: UI Refactor & CMS Separation

## Objective
Separate the public-facing "Front End" from the operational "Editorial CMS" and implement the core CMS dashboard features.

## Context
M'Lord has identified that the current UI conflates public consumption with backend operations. We need a clear separation of concerns and a more professional "Newspaper" feel for the public site. The CMS needs to be a powerful tool for editors.

## Required Files
- `sloppycopy/urls.py`
- `core/urls.py`, `core/views.py`
- `templates/base.html`
- `templates/cms_base.html` (New)
- `templates/core/dashboard.html` (Refactor to Public Home)
- `templates/cms/dashboard.html` (New)
- `templates/cms/digest.html` (New)

## Implementation Steps

### 1. URL Restructuring
- Move operational routes (ingest, run pipeline, test feed) under a `/cms/` prefix.
- Ensure `/` is reserved for the public-facing newspaper front end.

### 2. Base Template Split
- **`templates/base.html`**: Public newspaper style. Clean, typography-focused, no operational buttons. Use Material Tailwind for a polished look.
- **`templates/cms_base.html`**: Operational style. Sidebar-driven, dense stats, pipeline controls.

### 3. Public Front End (`/`)
- Refactor `core/views.py:dashboard` to only show `Rewrites` (the final product).
- Use a classic newspaper layout (Lead story, secondary stories, sidebar).
- Ensure `Author` profiles are public-facing.

### 4. Editorial CMS (`/cms/`)
- Create `cms/` views for:
  - **Operational Dashboard**: Pipeline stats, latest runs, quick controls.
  - **Source Digest**: The masonry "firehose" of raw `Stories`.
  - **Source Management**: List and test RSS feeds.
- **Markdown Editor**: Integrate `EasyMDE` for all text areas where copy is reviewed or edited.
- **HTML Fix**: Ensure `Story.summary` and `Rewrite.body` respect HTML formatting using the `|safe` filter.

### 5. Navigation Update
- Public header: Home, Authors, About.
- CMS header/sidebar: Dashboard, Source Digest, Sources, Pipeline Logs, Back to Site.

## Verification Commands
- `python manage.py runserver`
- Visit `/` -> Should see only Rewrites.
- Visit `/cms/` -> Should see operational controls and Source Digest.

## Success Criteria
- [x] Public site feels like a credible news publication.
- [x] CMS feels like a professional editorial tool.
- [x] No operational buttons (Fetch, Run) are visible on the public site.
- [x] HTML content in stories/rewrites renders correctly.
- [x] EasyMDE is active on editorial fields.
