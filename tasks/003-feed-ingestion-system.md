# 003 — Feed Ingestion System (RSS)

## A. Task Intent Summary

Implement the **first pipeline stage** responsible for importing external RSS feed content into the system.

The ingestion system must:

- Retrieve RSS feeds from configured `Source` records
- Parse entries deterministically
- Normalize fields into the internal `Story` model format
- Prevent duplicate records
- Persist new stories with `status="ingested"`

This stage **does not perform AI processing** and **must not call prompts or LLM providers**.

All ingestion logic must live in the **service layer** of the `sources` Django app.

The system must be **idempotent**, safe to run repeatedly, and resilient to malformed feeds.

---

## B. Architectural Context

Defined in [`plans/PLANNING.md`](plans/PLANNING.md).

Pipeline overview:

1. RSS Feed Ingestion ← **THIS TASK**
2. Story Evaluation
3. Author Matching
4. Rewrite Generation
5. UI Presentation

The ingestion system is the **entry point of the pipeline**.

Responsibilities:

- Fetch external data
- Normalize to internal models
- Create `Story` records

Responsibilities explicitly excluded:

- AI evaluation
- author matching
- rewriting
- orchestration logic

These occur in later pipeline stages.

---

## C. Models Used

Models are defined in the core architecture task:

- [`tasks/002-core-django-architecture.md`](tasks/002-core-django-architecture.md)

### Source

Expected fields:

```
name
rss_url
is_active
last_fetched_at
created_at
updated_at
```

### Story

Expected fields:

```
title
url
source (ForeignKey → Source)
summary
published_at
status
created_at
updated_at
```

During ingestion all created records must use:

```
status = "ingested"
```

---

## D. Modules and Files

### Services

File: `sources/services.py`

Functions:

- `ingest_all_sources()`
- `ingest_source(source)`
- `fetch_feed(url)`
- `parse_feed_entries(feed_data)`
- `normalize_entry(entry)`
- `create_story_if_new(source, normalized_entry)`

### Selectors

File: `sources/selectors.py`

Functions:

- `get_active_sources()`
- `story_exists_by_url(url)`

### Optional CLI Command

File: `sources/management/commands/ingest_feeds.py`

Run via:

```
python manage.py ingest_feeds
```

---

## E. External Dependencies

Required libraries:

- `feedparser`
- `requests`
- `python-dateutil`

All timestamps must be converted to **UTC timezone-aware datetimes**.

---

## F. Feed Ingestion Workflow

1. Load active `Source` records

```
Source.objects.filter(is_active=True)
```

2. Fetch RSS feed using `requests`.

3. Parse feed using `feedparser.parse()`.

4. Normalize each entry to fields:

```
title
url
summary
published_at
```

5. Deduplicate using `Story.url`.

6. Insert new `Story` rows with:

```
status="ingested"
```

---

## G. Data Normalization Rules

### Title

Priority:

```
entry.title
entry.get("title")
"Untitled"
```

### URL

Priority:

```
entry.link
entry.id
```

Entries without URL must be skipped.

### Summary

Priority:

```
entry.summary
entry.description
entry.content
```

Maximum length: 2000 characters.

### Published Date

Priority:

```
entry.published
entry.updated
entry.published_parsed
```

Fallback:

```
timezone.now()
```

---

## H. Deduplication and Idempotency

Deduplication key:

```
Story.url
```

Running ingestion multiple times must **not create duplicates**.

Recommended database constraint:

```
unique=True on Story.url
```

---

## I. Error Handling

### Feed Fetch Failure

Log error and continue to next source.

### Feed Parsing Failure

Skip feed and continue.

### Entry Processing Failure

Skip entry and continue loop.

---

## J. Logging

Recommended fields:

- source_name
- source_url
- stories_created
- entries_processed
- errors

Optional integration with `PipelineLog`.

---

## K. Deterministic Implementation Plan

1. Implement selectors in `sources/selectors.py`.
2. Implement feed fetch logic.
3. Implement parser.
4. Implement normalization rules.
5. Implement deduplication.
6. Implement story creation.
7. Implement `ingest_source()`.
8. Implement `ingest_all_sources()`.
9. Implement CLI command.

---

## L. Expected Artifacts

Database rows created:

```
Story(status="ingested")
```

Example:

```
Title: "New AI Model Released"
URL: https://example.com/article
Source: TechCrunch
Status: ingested
```

---

## M. CLI Verification

Create test source:

```
python manage.py shell
```

```
from sources.models import Source
Source.objects.create(
    name="Example Feed",
    rss_url="https://example.com/rss",
    is_active=True
)
```

Run ingestion:

```
python manage.py ingest_feeds
```

Verify:

```
from stories.models import Story
Story.objects.count()
```

---

## N. Failure Scenarios

Feed Offline

→ log error and continue.

Malformed Feed

→ skip feed.

Duplicate Stories

→ skip duplicate URL.

Partial Feed Failures

→ skip entry and continue.

---

## O. Dot‑Notation Execution Plan

```
003.sources.selectors.get_active_sources
003.sources.selectors.story_exists_by_url

003.sources.services.fetch_feed
003.sources.services.parse_feed_entries
003.sources.services.normalize_entry
003.sources.services.create_story_if_new
003.sources.services.ingest_source
003.sources.services.ingest_all_sources

003.sources.management.commands.ingest_feeds.handle
```

Execution order:

```
get_active_sources
→ ingest_source
→ fetch_feed
→ parse_feed_entries
→ normalize_entry
→ create_story_if_new
```

---

End of specification.
