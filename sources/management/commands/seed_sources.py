from django.core.management.base import BaseCommand
from django.utils.text import slugify
from sources.models import Source

class Command(BaseCommand):
    help = 'Seeds the database with initial sources'

    def handle(self, *args, **options):
        sources_data = [
            {
                'name': 'BBC News',
                'feed_url': 'https://feeds.bbci.co.uk/news/rss.xml',
                'source_type': 'rss',
                'is_active': True
            },
            {
                'name': 'NPR News',
                'feed_url': 'https://feeds.npr.org/1001/rss.xml',
                'source_type': 'rss',
                'is_active': True
            },
            {
                'name': 'NPR Business',
                'feed_url': 'https://feeds.npr.org/1003/rss.xml',
                'source_type': 'rss',
                'is_active': True
            },
            {
                'name': 'NPR Health',
                'feed_url': 'https://feeds.npr.org/1004/rss.xml',
                'source_type': 'rss',
                'is_active': True
            },
            {
                'name': 'AP News (Google)',
                'feed_url': 'https://news.google.com/rss/search?q=when:24h+allinurl:apnews.com',
                'source_type': 'rss',
                'is_active': True
            },
            {
                'name': 'Bloomberg (Google)',
                'feed_url': 'https://news.google.com/rss/search?q=when:24h+allinurl:bloomberg.com',
                'source_type': 'rss',
                'is_active': True
            },
        ]

        # Deactivate old sources
        Source.objects.all().update(is_active=False)

        for data in sources_data:
            source, created = Source.objects.update_or_create(
                slug=slugify(data['name']),
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created source: {source.name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated source: {source.name}'))
