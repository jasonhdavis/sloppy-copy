# Task 012: Author Persona Injection

## Objective
Implement a mechanism to seed author personas from Markdown files in the `docs/` directory.

## Context
M'Lord wants to be able to inject seed personas like `docs/author-Elias-Cartwright.md` into the system as authors.

## Required Files
- `authors/management/commands/seed_authors_from_docs.py` (New)
- `authors/models.py`
- `authors/services.py`

## Implementation Steps

### 1. Management Command
- Create `seed_authors_from_docs.py`.
- The command should scan `docs/` for files matching `author-*.md`.
- Parse the Markdown content to extract:
  - Name (from the first heading or filename).
  - Bio (from the "Bio" section).
  - Style Guide/Voice (from the "Style Guide" section).
  - Other characteristics.
- Create or update `Author` records in the database.

### 2. Model/Service Updates
- Ensure `Author` model has fields to store the parsed persona data (Bio, Style Guide, etc.).
- Update `AuthorService` if necessary to handle the creation/update logic.

## Verification Commands
- `python manage.py seed_authors_from_docs`
- Check Django Admin or `/authors/` list to see the new author.

## Success Criteria
- [x] `Dr. Elias Cartwright` is successfully created as an author.
- [x] The author's bio and style guide are correctly populated from the Markdown file.
- [x] The command is idempotent (can be run multiple times without duplicates).
