import time
import json
from .types import AIResponse
from .providers import BaseProvider

class MockAIProvider(BaseProvider):
    """
    Mock provider for testing without API keys.
    """
    def generate(self, request):
        content = "{}"
        
        # Simple heuristic to return relevant mock data
        if "evaluations" in request.prompt:
            # Editor evaluation
            content = json.dumps({
                "evaluations": [
                    {"story_id": 2, "score": 8, "reasoning": "High impact story."},
                    {"story_id": 3, "score": 7, "reasoning": "Relevant to current trends."}
                ]
            })
        elif "author_id" in request.prompt:
            # Author matching
            content = json.dumps({
                "author_id": 1,
                "assignment_rationale": "Matches author beat."
            })
        elif "headline" in request.prompt and "body" in request.prompt:
            # Rewrite generation
            content = json.dumps({
                "headline": "Mocked Headline",
                "dek": "Mocked dek for the story.",
                "body": "This is a mocked body content for the rewrite."
            })

        return AIResponse(
            content=content,
            raw_response={},
            model=request.model,
            usage={},
            latency=0.1
        )
