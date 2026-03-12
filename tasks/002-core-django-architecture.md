# Task 002: Core Django Architecture

## Objective
Implement the data models for all apps and register them with the Django Admin.

## Context
This task establishes the database schema for sources, stories, authors, rewrites, and orchestration.

## Required Files
- `sources/models.py`, `sources/admin.py`
- `stories/models.py`, `stories/admin.py`
- `authors/models.py`, `authors/admin.py`
- `rewrites/models.py`, `rewrites/admin.py`
- `orchestrator/models.py`, `orchestrator/admin.py`

## Implementation Steps

### 1. Sources App
- Define [`Source`](sources/models.py) model.

Recommended schema:

- `name` – CharField(255)
- `slug` – SlugField(unique=True)
- `source_type` – CharField with choices:
  - `rss`
  - `api`
  - `manual`
- `feed_url` – URLField(null=True, blank=True)
- `homepage_url` – URLField(null=True, blank=True)
- `is_active` – BooleanField(default=True)
- `last_checked_at` – DateTimeField(null=True, blank=True)
- `created_at` – DateTimeField(auto_now_add=True)
- `updated_at` – DateTimeField(auto_now=True)

Admin Requirements:

- Register [`SourceAdmin`](sources/admin.py)
- `list_display`: name, source_type, is_active, last_checked_at
- `search_fields`: name, feed_url
- `list_filter`: source_type, is_active

### 2. Stories App
- Define [`Story`](stories/models.py) model.

Recommended schema:

- `source` – ForeignKey(Source, on_delete=CASCADE, related_name="stories")
- `external_id` – CharField(255, null=True, blank=True)
- `title` – CharField(500)
- `url` – URLField(unique=True)
- `summary` – TextField(null=True, blank=True)
- `published_at` – DateTimeField(null=True, blank=True)
- `ingested_at` – DateTimeField(auto_now_add=True)

Evaluation Fields:

- `status` – CharField with choices:
  - `new`
  - `evaluated`
  - `assigned`
  - `rewritten`
  - `rejected`
- `ai_score` – FloatField(null=True, blank=True)
- `ai_rationale` – TextField(null=True, blank=True)
- `topic_tags` – JSONField(default=list, blank=True)

Admin Requirements:

- Register [`StoryAdmin`](stories/admin.py)
- `list_display`: title, source, status, ai_score, published_at
- `search_fields`: title, url
- `list_filter`: source, status

### 3. Authors App
- Define [`Author`](authors/models.py) model.

Recommended schema:

- `name` – CharField(255)
- `slug` – SlugField(unique=True)
- `bio` – TextField(blank=True)
- `avatar_url` – URLField(null=True, blank=True)

Editorial Identity:

- `beat_description` – TextField
- `style_guide` – TextField
- `writing_voice` – CharField(255)
- `tone_keywords` – JSONField(default=list, blank=True)
- `persona_prompt` – TextField (Database-editable prompt for the rewrite engine)

Operational Fields:

- `is_active` – BooleanField(default=True)
- `created_at` – DateTimeField(auto_now_add=True)
- `updated_at` – DateTimeField(auto_now=True)

### 3.5 Core App (Editorial)
- Define [`EditorialStyleSheet`](core/models.py) model.

Schema:
- `name` – CharField(255)
- `rules` – TextField (Global rules for the organization)
- `is_active` – BooleanField(default=True)

Admin Requirements:

- Register [`AuthorAdmin`](authors/admin.py)
- `list_display`: name, slug, is_active
- `search_fields`: name, slug
- `list_filter`: is_active

### 4. Rewrites App
- Define [`Assignment`](rewrites/models.py) model.

Assignment schema:

- `story` – ForeignKey(Story, on_delete=CASCADE, related_name="assignments")
- `author` – ForeignKey(Author, on_delete=CASCADE, related_name="assignments")
- `match_score` – FloatField(null=True, blank=True)
- `match_rationale` – TextField(null=True, blank=True)
- `assigned_at` – DateTimeField(auto_now_add=True)
- `status` – CharField with choices:
  - `pending`
  - `in_progress`
  - `completed`
  - `failed`

Define [`Rewrite`](rewrites/models.py) model.

Rewrite schema:

- `assignment` – ForeignKey(Assignment, on_delete=CASCADE, related_name="rewrites")
- `headline` – CharField(500)
- `dek` – CharField(500, blank=True)
- `body` – TextField
- `model_used` – CharField(255, null=True, blank=True)
- `prompt_version` – CharField(100, null=True, blank=True)
- `status` – CharField with choices:
  - `draft`
  - `review`
  - `approved`
  - `rejected`
- `created_at` – DateTimeField(auto_now_add=True)
- `updated_at` – DateTimeField(auto_now=True)

Admin Requirements:

- Register [`AssignmentAdmin`](rewrites/admin.py)
- Register [`RewriteAdmin`](rewrites/admin.py)
- `RewriteAdmin list_display`: headline, status, created_at
- `AssignmentAdmin list_display`: story, author, status, match_score

### 5. Orchestrator App
- Define [`PipelineRun`](orchestrator/models.py) model.

Recommended schema:

- `started_at` – DateTimeField(auto_now_add=True)
- `completed_at` – DateTimeField(null=True, blank=True)
- `status` – CharField with choices:
  - `running`
  - `completed`
  - `failed`
- `stories_ingested` – IntegerField(default=0)
- `stories_evaluated` – IntegerField(default=0)
- `stories_assigned` – IntegerField(default=0)
- `rewrites_generated` – IntegerField(default=0)
- `error_log` – TextField(null=True, blank=True)
- `metadata` – JSONField(default=dict, blank=True)

Admin Requirements:

- Register [`PipelineRunAdmin`](orchestrator/admin.py)
- `list_display`: id, status, started_at, completed_at
- `list_filter`: status

### 6. Migrations
- Run `python manage.py makemigrations` for all apps.
- Run `python manage.py migrate`.

## Verification Commands
- `python manage.py check`
- `python manage.py showmigrations`

## Success Criteria
- [ ] All models are defined according to the architecture spec.
- [ ] Migrations are created and applied without errors.
- [ ] Admin interface shows all models.
