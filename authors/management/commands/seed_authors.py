from django.core.management.base import BaseCommand
from authors.models import Author

class Command(BaseCommand):
    help = 'Seeds the database with initial authors'

    def handle(self, *args, **options):
        authors_data = [
            {
                'name': 'Alex Tech',
                'slug': 'alex-tech',
                'beat_description': 'Artificial intelligence and developer tools',
                'writing_voice': 'Technical and analytical',
                'style_guide': 'Focus on technical accuracy and developer experience.',
                'is_active': True
            },
            {
                'name': 'Morgan Policy',
                'slug': 'morgan-policy',
                'beat_description': 'Technology policy and regulation',
                'writing_voice': 'Formal and investigative',
                'style_guide': 'Focus on legal implications and societal impact.',
                'is_active': True
            },
            {
                'name': 'Riley Startup',
                'slug': 'riley-startup',
                'beat_description': 'Startups, venture capital, and product launches',
                'writing_voice': 'Energetic and business-focused',
                'style_guide': 'Focus on market trends and funding rounds.',
                'is_active': True
            },
            {
                'name': 'Jordan Consumer',
                'slug': 'jordan-consumer',
                'beat_description': 'Consumer technology and gadgets',
                'writing_voice': 'Relatable and practical',
                'style_guide': 'Focus on user experience and daily utility.',
                'is_active': True
            },
            {
                'name': 'Taylor Future',
                'slug': 'taylor-future',
                'beat_description': 'Future trends, science, and emerging technology',
                'writing_voice': 'Visionary and speculative',
                'style_guide': 'Focus on long-term impact and scientific breakthroughs.',
                'is_active': True
            },
        ]

        for data in authors_data:
            author, created = Author.objects.update_or_create(
                slug=data['slug'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created author: {author.name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated author: {author.name}'))
