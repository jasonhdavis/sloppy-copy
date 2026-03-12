# Task 009: Application UI (Legacy)

> [!IMPORTANT]
> This task has been superseded by **Task 011: UI Refactor & CMS Separation**. 
> The original requirements for a unified dashboard were found to be insufficient for a professional separation of public and editorial concerns.

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
1. **Base Template & Editor**: Set up the canonical layout.
2. **Dashboard & Source Digest**: Implement stats and firehose.
3. **List & Detail Views**: Implement side-by-side comparison for Rewrites.

## Success Criteria
- [ ] All pages render without template errors.
- [ ] HTMX buttons on the dashboard trigger backend actions and update the UI.
- [ ] The UI matches the "credible and authoritative" look of the style guide.
