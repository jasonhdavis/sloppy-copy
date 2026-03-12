from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List

@dataclass
class AIResponse:
    """
    Standardized response from any AI provider.
    """
    content: str
    raw_response: Dict[str, Any]
    model: str
    usage: Dict[str, int] = field(default_factory=dict)
    latency: float = 0.0
    parsed_json: Optional[Dict[str, Any]] = None

@dataclass
class AIRequest:
    """
    Standardized request to an AI provider.
    """
    prompt: str
    system: Optional[str] = None
    model: Optional[str] = None
    temperature: float = 0.0
    response_format: Optional[Dict[str, Any]] = None
    max_tokens: Optional[int] = None
