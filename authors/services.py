import logging
from typing import List, Optional
from django.db import transaction
from ai.client import AIClient
from stories.models import Story
from authors.models import Author, EditorialStyleSheet
from rewrites.models import Assignment

logger = logging.getLogger(__name__)

class AuthorMatchingService:
    def __init__(self, ai_client: Optional[AIClient] = None):
        self.ai_client = ai_client or AIClient()
        try:
            with open("prompts/author_matching.md", "r") as f:
                self.prompt_template = f.read()
        except FileNotFoundError:
            logger.error("Author matching prompt template not found.")
            self.prompt_template = ""

    def match_story(self, story: Story) -> Optional[Assignment]:
        """
        Matches a single story to an author using AI.
        """
        if not self.prompt_template:
            return None

        authors = Author.objects.filter(is_active=True)
        if not authors.exists():
            logger.warning("No active authors available for matching.")
            return None

        style_sheet = EditorialStyleSheet.objects.filter(is_active=True).first()
        style_sheet_text = style_sheet.rules if style_sheet else "No specific style rules defined."

        context = {
            "story": story,
            "authors": authors,
            "style_sheet": style_sheet_text,
        }

        try:
            result = self.ai_client.generate(
                prompt=self.prompt_template,
                context=context,
                response_format={"type": "json_object"}
            )

            author_id = result.get("author_id")
            rationale = result.get("assignment_rationale")

            if not author_id:
                logger.error(f"AI failed to provide author_id for story {story.id}")
                return None

            author = Author.objects.get(id=author_id)

            with transaction.atomic():
                assignment = Assignment.objects.create(
                    story=story,
                    author=author,
                    match_rationale=rationale,
                    status='pending'
                )
                story.status = 'matched'
                story.save()

            logger.info(f"Successfully matched story {story.id} to author {author.name}")
            return assignment

        except Author.DoesNotExist:
            logger.error(f"AI suggested non-existent author ID {author_id}")
            return None
        except Exception as e:
            logger.error(f"Error matching story {story.id}: {str(e)}")
            return None

    def match_batch(self, limit: int = 10) -> List[Assignment]:
        """
        Matches a batch of evaluated stories.
        """
        stories = Story.objects.filter(status='evaluated')[:limit]
        assignments = []

        for story in stories:
            assignment = self.match_story(story)
            if assignment:
                assignments.append(assignment)

        return assignments
