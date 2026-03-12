from django.core.management.base import BaseCommand
from rewrites.services import RewriteGenerationService

class Command(BaseCommand):
    help = 'Generates rewrites for pending assignments'

    def add_arguments(self, parser):
        parser.add_argument(
            '--limit',
            type=int,
            default=10,
            help='Limit the number of assignments to process'
        )

    def handle(self, *args, **options):
        limit = options['limit']
        self.stdout.write(f"Starting rewrite generation for up to {limit} assignments...")
        
        service = RewriteGenerationService()
        service.process_pending_assignments(limit=limit)
        
        self.stdout.write(self.style.SUCCESS("Successfully processed assignments."))
