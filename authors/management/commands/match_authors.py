from django.core.management.base import BaseCommand
from authors.services import AuthorMatchingService
from stories.models import Story

class Command(BaseCommand):
    help = 'Matches evaluated stories to authors'

    def add_arguments(self, parser):
        parser.add_argument('--limit', type=int, default=10, help='Limit the number of stories to match')

    def handle(self, *args, **options):
        limit = options['limit']
        service = AuthorMatchingService()
        
        self.stdout.write(f"Starting matching for up to {limit} stories...")
        
        assignments = service.match_batch(limit=limit)
        
        self.stdout.write(self.style.SUCCESS(f"Successfully created {len(assignments)} assignments."))
        for assignment in assignments:
            self.stdout.write(f" - {assignment.story.title} -> {assignment.author.name}")
