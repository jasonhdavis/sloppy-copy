import os
import re
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from authors.models import Author

class Command(BaseCommand):
    help = 'Seed author personas from Markdown files in the docs/ directory'

    def handle(self, *args, **options):
        docs_dir = 'docs'
        if not os.path.exists(docs_dir):
            self.stdout.write(self.style.ERROR(f"Directory {docs_dir} not found."))
            return

        # Deactivate existing authors to "remove" them as requested
        Author.objects.all().update(is_active=False)

        for filename in os.listdir(docs_dir):
            if filename.lower().startswith('author-') and filename.endswith('.md'):
                filepath = os.path.join(docs_dir, filename)
                self.stdout.write(f"Processing {filepath}...")
                
                with open(filepath, 'r') as f:
                    content = f.read()

                # Basic parsing logic
                # Extract Name from the first line or a specific pattern
                name_match = re.search(r'^Author Persona\n(.+)', content)
                if not name_match:
                    # Fallback to filename
                    name = filename.replace('author-', '').replace('.md', '').replace('-', ' ').title()
                else:
                    name = name_match.group(1).strip()
                    # Remove titles like "Dr. " for the slug if needed, but slugify handles it
                    if " — " in name:
                        name = name.split(" — ")[0]

                # Extract Bio
                bio_match = re.search(r'Bio\n\n(.*?)(?=\n\nStyle Guide|\Z)', content, re.DOTALL)
                bio = bio_match.group(1).strip() if bio_match else ""

                # Extract Style Guide
                style_guide_match = re.search(r'Style Guide\n(.*?)(?=\n\nWriting Characteristics|\Z)', content, re.DOTALL)
                style_guide = style_guide_match.group(1).strip() if style_guide_match else ""

                # Extract Writing Characteristics for beat/voice
                writing_chars_match = re.search(r'Writing Characteristics\n(.*?)(?=\n\nCommon Geological References|\Z)', content, re.DOTALL)
                writing_chars = writing_chars_match.group(1).strip() if writing_chars_match else ""

                # Create or update Author
                author, created = Author.objects.update_or_create(
                    slug=slugify(name),
                    defaults={
                        'name': name,
                        'bio': bio,
                        'style_guide': style_guide,
                        'beat_description': writing_chars,
                        'writing_voice': "See Style Guide",
                        'persona_prompt': content, # Use full content as prompt for now
                        'is_active': True,
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created author: {author.name}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"Updated author: {author.name}"))
