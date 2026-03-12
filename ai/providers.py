import time
import logging
import requests
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from django.conf import settings
from .types import AIRequest, AIResponse

logger = logging.getLogger(__name__)

class BaseProvider(ABC):
    """
    Abstract base class for AI providers.
    """
    @abstractmethod
    def generate(self, request: AIRequest) -> AIResponse:
        pass

class OpenRouterProvider(BaseProvider):
    """
    Implementation for OpenRouter API.
    """
    def __init__(self):
        self.api_key = getattr(settings, "OPENROUTER_API_KEY", None)
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        
        if not self.api_key:
            logger.warning("OPENROUTER_API_KEY not found in settings.")

    def generate(self, request: AIRequest) -> AIResponse:
        if not self.api_key:
            raise ValueError("OpenRouter API key is required.")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/scrummage/sloppy-copy", # Optional, for OpenRouter rankings
            "X-Title": "Sloppy Copy",
        }

        messages = []
        if request.system:
            messages.append({"role": "system", "content": request.system})
        messages.append({"role": "user", "content": request.prompt})

        payload = {
            "model": request.model or getattr(settings, "DEFAULT_AI_MODEL", "anthropic/claude-3-haiku"),
            "messages": messages,
            "temperature": request.temperature,
        }

        if request.response_format:
            payload["response_format"] = request.response_format
        
        if request.max_tokens:
            payload["max_tokens"] = request.max_tokens

        start_time = time.time()
        try:
            response = requests.post(
                self.base_url,
                headers=headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            data = response.json()
            latency = time.time() - start_time

            content = data["choices"][0]["message"]["content"]
            usage = data.get("usage", {})

            return AIResponse(
                content=content,
                raw_response=data,
                model=payload["model"],
                usage=usage,
                latency=latency
            )
        except Exception as e:
            logger.error(f"OpenRouter API error: {str(e)}")
            raise
