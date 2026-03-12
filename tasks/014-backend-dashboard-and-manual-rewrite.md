# Task 014: Backend Dashboard and Manual Rewrite

## Objective
Implement the "Source News Feed" dashboard in the CMS with a "Rewrite" button and modal for manual assignment.

## Context
M'Lord wants a way to manually trigger a rewrite for a specific source story, selecting the author via a modal.

## Required Files
- `templates/cms/digest.html`
- `rewrites/views.py`
- `rewrites/urls.py`
- `rewrites/services.py`

## Implementation Steps

### 1. Source News Feed Dashboard
- Refactor the "Source Digest" into a professional editorial dashboard.
- Each story card should have a "Rewrite" button.

### 2. Rewrite Modal (HTMX)
- Clicking "Rewrite" should open an HTMX-powered modal.
- The modal should list available `Authors`.
- Selecting an author and clicking "Generate" should trigger the `RewriteGenerationService` for that specific story and author.

### 3. Manual Rewrite Logic
- Create a view in `rewrites/views.py` to handle the manual rewrite request.
- Ensure it returns a success message or redirects to the new `Rewrite` page.

## Verification Commands
- Visit `/cms/digest/`.
- Click "Rewrite" on a story.
- Select an author and confirm.
- Verify the rewrite is generated and visible.

## Success Criteria
- [x] "Rewrite" button is functional on all source stories in the CMS.
- [x] Modal allows selecting an author.
- [x] Manual rewrite generation works as expected.
