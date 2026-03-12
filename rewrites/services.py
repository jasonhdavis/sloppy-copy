import logging
from typing import List, Dict, Any, Optional
from django.db import transaction
from django.conf import settings
from .models import Assignment, Rewrite
from stories.models import Story
from authors.models import Author, EditorialStyleSheet
from ai.client import AIClient

logger = logging.getLogger(__name__)

class RewriteGenerationService:
    """
    Service for generating article rewrites using assigned authors and editorial style sheets.
    """
    def __init__(self, ai_client: AIClient = None):
        self.ai_client = ai_client or AIClient()

    def get_related_stories(self, story: Story) -> List[Story]:
        """
        Fetches related stories based on topic tags.
        In a real scenario, this would use vector search or more complex grouping.
        """
        if not story.topic_tags:
            return []
        
        # Find stories with overlapping topic tags, excluding the current story
        related = Story.objects.filter(
            topic_tags__overlap=story.topic_tags
        ).exclude(id=story.id).order_by('-ai_score')[:5]
        
        return list(related)

    def generate_rewrite(self, assignment: Assignment) -> Optional[Rewrite]:
        """
        Generates a rewrite for a specific assignment.
        """
        story = assignment.story
        author = assignment.author
        
        logger.info(f"Generating rewrite for story: {story.title} by author: {author.name}")
        
        # 1. Load Editorial Style Sheet
        style_sheet = EditorialStyleSheet.objects.filter(is_active=True).first()
        style_rules = style_sheet.rules if style_sheet else "Standard news reporting."
        
        # 2. Gather related sources
        related_stories = self.get_related_stories(story)
        sources_context = []
        for s in related_stories:
            sources_context.append({
                "title": s.title,
                "summary": s.summary,
                "url": s.url
            })
            
        # 3. Load prompt template
        try:
            with open("prompts/author_rewrite.md", "r") as f:
                prompt_template = f.read()
        except FileNotFoundError:
            logger.error("Author rewrite prompt template not found.")
            return None

        context = {
            "author": author,
            "style_sheet": style_rules,
            "story": story,
            "related_sources": sources_context
        }

        try:
            # 4. Call AI Client
            response_data = self.ai_client.generate(
                prompt=prompt_template,
                context=context,
                response_format={"type": "json_object"}
            )
            
            # 5. Create Rewrite record
            with transaction.atomic():
                rewrite = Rewrite.objects.create(
                    assignment=assignment,
                    headline=response_data.get("headline", story.title),
                    dek=response_data.get("dek", ""),
                    body=response_data.get("body", ""),
                    model_used=self.ai_client.default_model,
                    status='draft'
                )
                
                # Update assignment status
                assignment.status = 'completed'
                assignment.save()
                
                # Update story status
                story.status = 'rewritten'
                story.save()
                
                logger.info(f"Successfully generated rewrite for assignment {assignment.id}")
                return rewrite
                
        except Exception as e:
            logger.error(f"Error generating rewrite for assignment {assignment.id}: {str(e)}")
            assignment.status = 'failed'
            assignment.save()
            return None

    def process_pending_assignments(self, limit: int = 10):
        """
        Processes a batch of pending assignments.
        """
        assignments = Assignment.objects.filter(status='pending').select_related('story', 'author')[:limit]
        
        if not assignments:
            logger.info("No pending assignments to process.")
            return
            
        logger.info(f"Processing {len(assignments)} pending assignments.")
        
        for assignment in assignments:
            # Mark as in_progress to avoid double processing
            assignment.status = 'in_progress'
            assignment.save()
            
            self.generate_rewrite(assignment)
