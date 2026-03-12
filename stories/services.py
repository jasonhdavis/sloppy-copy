import logging
from typing import List, Dict, Any
from django.db import transaction
from .models import Story
from .selectors import get_unevaluated_stories
from core.models import EditorialStyleSheet
from ai.client import AIClient

logger = logging.getLogger(__name__)

class EditorService:
    """
    Service for evaluating stories using the Editor AI persona.
    Focuses on frequency analysis and editorial importance.
    """
    def __init__(self, ai_client: AIClient = None):
        self.ai_client = ai_client or AIClient()

    def analyze_frequency(self, stories: List[Story]) -> Dict[int, float]:
        """
        Groups stories by topic and counts occurrences to determine frequency-based importance.
        For now, we'll use a simple keyword-based overlap or just return a baseline.
        In a real scenario, this might use embeddings or TF-IDF.
        """
        # Simple frequency analysis: count how many stories share similar words in titles
        # This is a placeholder for more complex grouping logic
        frequency_map = {}
        all_titles = [s.title.lower() for s in stories]
        
        for story in stories:
            count = 0
            words = set(story.title.lower().split())
            # Filter out common stop words if needed
            words = {w for w in words if len(w) > 3}
            
            for other_title in all_titles:
                other_words = set(other_title.split())
                if words & other_words: # Intersection
                    count += 1
            
            # Normalize score (count / total stories in batch)
            frequency_map[story.id] = count / len(stories) if stories else 0
            
        return frequency_map

    def evaluate_importance(self, stories: List[Story]) -> List[Dict[str, Any]]:
        """
        Uses AI to determine if stories are "must-cover" based on the current news cycle.
        """
        style_sheet = EditorialStyleSheet.objects.filter(is_active=True).first()
        style_rules = style_sheet.rules if style_sheet else "Standard news reporting."

        # Load prompt template
        try:
            with open("prompts/editor_evaluation.md", "r") as f:
                prompt_template = f.read()
        except FileNotFoundError:
            logger.error("Editor evaluation prompt template not found.")
            return []

        context = {
            "style_sheet": style_rules,
            "stories": stories
        }

        try:
            response = self.ai_client.generate(
                prompt=prompt_template,
                context=context,
                response_format={"type": "json_object"}
            )
            return response.get("evaluations", [])
        except Exception as e:
            logger.error(f"Error during AI evaluation: {str(e)}")
            return []

    def process_batch(self, limit: int = 20):
        """
        Main entry point for processing a batch of ingested stories.
        """
        stories = list(get_unevaluated_stories(limit=limit))
        if not stories:
            logger.info("No stories to evaluate.")
            return

        logger.info(f"Processing batch of {len(stories)} stories.")

        # 1. Frequency Analysis (Internal logic)
        frequency_scores = self.analyze_frequency(stories)

        # 2. AI Evaluation
        evaluations = self.evaluate_importance(stories)
        eval_map = {e['story_id']: e for e in evaluations}

        # 3. Update Database
        with transaction.atomic():
            for story in stories:
                eval_data = eval_map.get(story.id)
                freq_score = frequency_scores.get(story.id, 0)
                
                if eval_data:
                    # Combine frequency score with AI score (e.g., weighted average)
                    # AI score is 1-10, freq_score is 0-1
                    ai_score_raw = eval_data.get('score', 5)
                    
                    # Final score calculation: 70% AI, 30% Frequency (scaled to 10)
                    final_score = (ai_score_raw * 0.7) + (freq_score * 10 * 0.3)
                    
                    story.ai_score = round(final_score, 2)
                    story.ai_rationale = eval_data.get('reasoning', '')
                    story.status = 'evaluated'
                    
                    # If score is very low, we might mark as rejected, but for now just evaluate
                    if final_score < 3:
                        # Optional: story.status = 'rejected'
                        pass
                else:
                    # Fallback if AI failed for this specific story
                    story.ai_score = round(freq_score * 10, 2)
                    story.ai_rationale = "Evaluated based on frequency analysis only (AI fallback)."
                    story.status = 'evaluated'
                
                story.save()

        logger.info(f"Successfully evaluated {len(stories)} stories.")
