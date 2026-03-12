from django.core.management.base import BaseCommand
from sources.services import FeedIngestionService

class Command(BaseCommand):
    help = 'Ingests stories from all active RSS feeds'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting feed ingestion...'))
        
        results = FeedIngestionService.ingest_all_sources()
        
        for result in results:
            if result['status'] == 'success':
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully ingested {result['source']}: {result['created']} new stories.")
                )
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to ingest {result['source']}: {result['error']}")
                )
        
        self.stdout.write(self.style.SUCCESS('Feed ingestion complete.'))
