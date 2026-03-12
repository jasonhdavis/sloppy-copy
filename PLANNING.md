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

## UI Architecture (Revised)
The system is split into two distinct interfaces to separate public consumption from editorial operations.

### 1. Public Front End (`/`)
- **Aesthetic**: High-end digital newspaper (NYT/WSJ style).
- **Focus**: Displaying the final `Rewrites`.
- **Routes**:
  - `/`: Homepage featuring top AI-generated stories.
  - `/authors/`: Public list of author personas.
  - `/authors/<slug>/`: Author profile and their generated articles.
  - `/rewrites/<id>/`: Full article view.

### 2. Editorial CMS (`/cms/`)
- **Aesthetic**: Operational dashboard, dense information, control-focused.
- **Focus**: Managing the pipeline, reviewing raw feeds, and controlling AI runs.
- **Features**:
  - **Source News Feed Dashboard**: A "firehose" of raw ingested stories.
  - **Manual Rewrite**: A "Rewrite" button + modal on each source story that lets an editor select an author to write it.
  - **Markdown Editor**: EasyMDE integration for reviewing and editing copy.
- **Routes**:
  - `/cms/`: Operational dashboard with pipeline stats and controls.
  - `/cms/digest/`: The "Source Digest" firehose of raw ingested stories.
  - `/cms/sources/`: Management of RSS feeds and testing.
  - `/cms/pipeline/`: Detailed logs of `PipelineRuns`.

## Content Handling & AI
- **Source Parsing**: Ensure source material is parsed correctly, stripping or interpreting HTML and handling images.
- **AI Output**: Ensure proper AI output that includes formatting (Markdown) and images.
- **Author Personas**: Seed personas can be injected from markdown files (e.g., `docs/author-*.md`).

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
