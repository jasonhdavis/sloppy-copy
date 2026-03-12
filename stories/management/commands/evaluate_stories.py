from django.core.management.base import BaseCommand
from stories.services import EditorService

class Command(BaseCommand):
    help = 'Evaluates ingested stories using the Editor AI'

    def add_arguments(self, parser):
        parser.add_argument(
            '--limit',
            type=int,
            default=20,
            help='Limit the number of stories to process',
        )

    def handle(self, *args, **options):
        limit = options['limit']
        self.stdout.write(f"Starting evaluation for up to {limit} stories...")
        
        service = EditorService()
        service.process_batch(limit=limit)
        
        self.stdout.write(self.style.SUCCESS("Evaluation complete."))
