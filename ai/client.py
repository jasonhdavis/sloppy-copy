import json
import logging
import re
from typing import Dict, Any, Optional, Union
from django.conf import settings
from django.template import Template, Context
from .providers import OpenRouterProvider
from .types import AIRequest, AIResponse

logger = logging.getLogger(__name__)

class AIClient:
    """
    Unified client for AI interactions.
    Handles prompt loading, rendering, execution, and JSON parsing.
    """
    def __init__(self, provider=None):
        from core.models import EditorialStyleSheet
        if provider:
            self.provider = provider
        elif getattr(settings, "USE_MOCK_AI", False):
            from .mock_provider import MockAIProvider
            self.provider = MockAIProvider()
        else:
            self.provider = OpenRouterProvider()
        
        # Try to get model from active style sheet
        style_sheet = EditorialStyleSheet.objects.filter(is_active=True).first()
        if style_sheet and style_sheet.default_model:
            self.default_model = style_sheet.default_model
        else:
            self.default_model = getattr(settings, "DEFAULT_AI_MODEL", "anthropic/claude-3-haiku")

    def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        model: Optional[str] = None,
        temperature: float = 0.0,
        response_format: Optional[Dict[str, Any]] = None,
        max_retries: int = 3,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        High-level method to generate a response and parse it as JSON.
        """
        # Render prompt if context is provided
        rendered_prompt = self.render_prompt(prompt, context) if context else prompt
        rendered_system = self.render_prompt(system, context) if system and context else system

        # Ensure we are asking for JSON if response_format is set or by default
        if response_format and "json" not in rendered_prompt.lower():
            rendered_prompt += "\n\nIMPORTANT: Your response must be a valid JSON object."

        request = AIRequest(
            prompt=rendered_prompt,
            system=rendered_system,
            model=model or self.default_model,
            temperature=temperature,
            response_format=response_format
        )

        attempts = 0
        last_error = None

        while attempts < max_retries:
            attempts += 1
            try:
                response = self.provider.generate(request)
                parsed = self.parse_json(response.content)
                
                # Log success
                logger.info(
                    f"AI Generation Success: model={response.model}, "
                    f"latency={response.latency:.2f}s, attempts={attempts}"
                )
                
                return parsed
            except (json.JSONDecodeError, ValueError) as e:
                last_error = e
                logger.warning(f"AI JSON parse error (attempt {attempts}): {str(e)}")
                # On retry, we might want to append a hint to the prompt, 
                # but for now we just retry.
            except Exception as e:
                last_error = e
                logger.error(f"AI Provider error (attempt {attempts}): {str(e)}")
                if attempts >= max_retries:
                    raise

        raise ValueError(f"Failed to get valid JSON response after {max_retries} attempts. Last error: {str(last_error)}")

    def render_prompt(self, template_str: str, context: Dict[str, Any]) -> str:
        """
        Renders a Django-style template string with the provided context.
        Disables auto-escaping for AI prompts.
        """
        template = Template("{% autoescape off %}" + template_str + "{% endautoescape %}")
        return template.render(Context(context))

    def parse_json(self, text: str) -> Dict[str, Any]:
        """
        Extracts and parses JSON from a string.
        Handles cases where the model might wrap JSON in markdown blocks.
        """
        # Try direct parsing first
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # Try to find JSON in markdown code blocks
        match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                pass

        # Try to find anything that looks like a JSON object
        match = re.search(r"(\{.*\})", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                pass

        raise json.JSONDecodeError("Could not find valid JSON in response", text, 0)
