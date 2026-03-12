from django.core.management.base import BaseCommand
from django.utils.text import slugify
from sources.models import Source

class Command(BaseCommand):
    help = 'Seeds the database with initial sources'

    def handle(self, *args, **options):
        sources_data = [
            {
                'name': 'TechCrunch',
                'feed_url': 'https://techcrunch.com/feed/',
                'source_type': 'rss',
                'is_active': True
            },
            {
                'name': 'Hacker News',
                'feed_url': 'https://hnrss.org/frontpage',
                'source_type': 'rss',
                'is_active': True
            },
            {
                'name': 'The Verge',
                'feed_url': 'https://www.theverge.com/rss/index.xml',
                'source_type': 'rss',
                'is_active': True
            },
        ]

        for data in sources_data:
            source, created = Source.objects.update_or_create(
                slug=slugify(data['name']),
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created source: {source.name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated source: {source.name}'))
