import logging
import traceback
from django.utils import timezone
from .models import PipelineRun
from sources.services import FeedIngestionService
from stories.services import EditorService
from authors.services import AuthorMatchingService
from rewrites.services import RewriteGenerationService

logger = logging.getLogger(__name__)

class PipelineOrchestrator:
    """
    Coordinates the full content pipeline end-to-end.
    """

    def run_pipeline(self):
        """
        Runs the entire pipeline in sequence: ingest -> evaluate -> match -> rewrite.
        """
        run = PipelineRun.objects.create(status='running')
        
        try:
            # 1. Ingestion
            run.stories_ingested = self.run_ingestion()
            run.save()

            # 2. Evaluation
            run.stories_evaluated = self.run_evaluation()
            run.save()

            # 3. Matching
            run.stories_assigned = self.run_matching()
            run.save()

            # 4. Rewrites
            run.rewrites_generated = self.run_rewrites()
            
            run.status = 'completed'
        except Exception as e:
            logger.error(f"Pipeline run {run.id} failed: {str(e)}")
            run.status = 'failed'
            run.error_log = f"{str(e)}\n\n{traceback.format_exc()}"
        finally:
            run.completed_at = timezone.now()
            run.save()

        return {
            "ingestion": run.stories_ingested,
            "evaluated": run.stories_evaluated,
            "matched": run.stories_assigned,
            "rewritten": run.rewrites_generated
        }

    def run_ingestion(self):
        """
        Calls FeedIngestionService.ingest_all_sources()
        """
        results = FeedIngestionService.ingest_all_sources()
        total_created = sum(r.get('created', 0) for r in results if r.get('status') == 'success')
        print(f"Ingested: {total_created}")
        return total_created

    def run_evaluation(self):
        """
        Calls EditorService.process_batch()
        """
        service = EditorService()
        # We need to know how many were evaluated. 
        # process_batch doesn't return count, so we'll check before/after or modify it if possible.
        # For now, let's assume we process a batch of 50.
        from stories.models import Story
        before_count = Story.objects.filter(status='evaluated').count()
        service.process_batch(limit=50)
        after_count = Story.objects.filter(status='evaluated').count()
        count = max(0, after_count - before_count)
        print(f"Evaluated: {count}")
        return count

    def run_matching(self):
        """
        Calls AuthorMatchingService.match_batch()
        """
        service = AuthorMatchingService()
        assignments = service.match_batch(limit=50)
        count = len(assignments)
        print(f"Matched: {count}")
        return count

    def run_rewrites(self):
        """
        Calls RewriteGenerationService.process_pending_assignments()
        """
        service = RewriteGenerationService()
        from rewrites.models import Rewrite
        before_count = Rewrite.objects.count()
        service.process_pending_assignments(limit=50)
        after_count = Rewrite.objects.count()
        count = max(0, after_count - before_count)
        print(f"Rewritten: {count}")
        return count
