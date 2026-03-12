# Sloppy Copy — Baseline Architecture

## Overview
Sloppy Copy is an AI-powered content pipeline that ingests news, evaluates it for newsworthiness using an "Editor AI" persona, and rewrites selected stories using distinct author personas guided by a central Editorial Style Sheet.

## Tech Stack
- **Backend**: [`Django 5.0`](https://docs.djangoproject.com/en/5.0/)
- **Database**: SQLite (for demo simplicity)
- **Frontend**: [`HTMX`](https://htmx.org/), [`Alpine.js`](https://alpinejs.dev/), [`Material Tailwind (HTML)`](https://www.material-tailwind.com/docs/html/installation)
- **Editor**: [`EasyMDE`](https://github.com/Ionaru/easy-markdown-editor) (Markdown editor for prompts and bios)
- **AI**: [`OpenRouter`](https://openrouter.ai/) (Primary gateway for Claude/GPT/Llama)
- **Ingestion**: [`feedparser`](https://pythonhosted.org/feedparser/)

## Project Structure
```
sloppy-copy/
├── ai/                 # AI provider abstraction (OpenRouter)
├── authors/            # Author persona models, prompts & matching
├── core/               # Dashboard, Editorial Style Sheet & base templates
├── orchestrator/       # Pipeline coordination & run tracking
├── rewrites/           # Assignment & rewrite models
├── sources/            # RSS/URL source management & Source Digest
└── stories/            # Story ingestion & Editor AI evaluation
```

## Core Pipeline Flow
1. **Ingestion**: `sources.services.FeedIngestionService` fetches RSS feeds.
2. **Source Digest**: A masonry-style UI for human review and feed testing.
3. **Evaluation (Editor AI)**: `stories.services.EditorService` analyzes headline/lede frequency across sources to determine story importance.
4. **Matching (Editor AI)**: `authors.services.AuthorMatchingService` assigns stories to the best-fit `Author` based on the Editorial Style Sheet.
5. **Generation**: `rewrites.services.RewriteGenerationService` produces the final article using multiple source references and author-specific prompts.

## Data Models
- `Source`: RSS feed metadata and testing status.
- `Story`: Ingested article data.
- `EditorialStyleSheet`: Global rules for the news organization.
- `Author`: Persona bio, beat, and database-editable prompt templates.
- `Assignment`: Link between multiple `Stories` and an `Author`.
- `Rewrite`: The AI-generated article (Headline, Dek, Body).
- `PipelineRun`: Logs for tracking automated runs.

## Development Workflow
- **Task-Based Development**: Each feature is implemented following the numbered tasks in `/tasks`.
- **Atomic Commits**: Every task completion (e.g., `001`, `002`) should be followed by a git commit referencing the task ID.
- **Verification**: No task is considered complete until its corresponding `.5` verification task passes.
