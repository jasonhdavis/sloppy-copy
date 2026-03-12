# 008 — Pipeline Orchestrator

Coordinates the full content pipeline end‑to‑end using deterministic stage execution.

Stages orchestrated:

1. Feed Ingestion
2. Story Evaluation
3. Author Matching
4. Rewrite Generation

Primary service: [`PipelineOrchestrator`](orchestrator/services.py:1)

---

## A. Intent

Provide a single entrypoint that runs the entire pipeline in sequence.

Stages must execute in this exact order:

```
ingest → evaluate → match → rewrite
```

Each stage is idempotent and processes only eligible rows.

---

## B. Modules

Service implementation:

```
orchestrator/services.py
```

CLI command:

```
orchestrator/management/commands/run_pipeline.py
```

Imported services:

• [`FeedIngestionService`](sources/services.py:1)

• [`StoryEvaluationService`](stories/services.py:1)

• [`AuthorMatchingService`](authors/services.py:1)

• [`RewriteGenerationService`](rewrites/services.py:1)

---

## C. Service Design

Class:

```
PipelineOrchestrator
```

Methods:

```
run_pipeline()
run_ingestion()
run_evaluation()
run_matching()
run_rewrites()
```

---

### run_pipeline

Execution order:

1. `run_ingestion()`
2. `run_evaluation()`
3. `run_matching()`
4. `run_rewrites()`

Each step prints summary metrics.

Example return:

```
{
 ingestion: 12,
 evaluated: 10,
 matched: 8,
 rewritten: 8
}
```

---

### run_ingestion

Calls:

[`FeedIngestionService.ingest_all()`](sources/services.py:1)

---

### run_evaluation

Calls:

[`StoryEvaluationService.evaluate_batch()`](stories/services.py:1)

---

### run_matching

Calls:

[`AuthorMatchingService.match_batch()`](authors/services.py:1)

---

### run_rewrites

Calls:

[`RewriteGenerationService.generate_batch()`](rewrites/services.py:1)

---

## D. CLI Execution

Run the entire pipeline:

```
python manage.py run_pipeline
```

Example output:

```
Running pipeline
Ingested: 12
Evaluated: 10
Matched: 8
Rewritten: 8
Pipeline complete
```

CLI handler:

[`run_pipeline`](orchestrator/management/commands/run_pipeline.py:1)

---

## E. Idempotency

Running the pipeline repeatedly should only process new work.

Reason:

Each stage filters by status:

```
ingested → evaluated → matched → rewritten
```

---

## F. Error Handling

If a stage fails:

• log error

• continue remaining stages

Example:

Evaluation failure should not block ingestion next run.

---

## G. Observability

Each stage should log:

• items processed

• execution time

• errors

Logging location:

```
core/logging.py
```

---

## H. Verification

Run pipeline:

```
python manage.py run_pipeline
```

Verify database states:

```
Story.objects.filter(status="rewritten")
```

Confirm rewrites exist:

```
Rewrite.objects.count()
```

---

## I. Dot Execution Plan

```
008.orchestrator.run_pipeline

008.stage.ingestion
008.stage.evaluation
008.stage.matching
008.stage.rewrites
```

---

End specification.
