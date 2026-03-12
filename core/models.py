from django.db import models

class EditorialStyleSheet(models.Model):
    """
    Global rules for the organization.
    """
    name = models.CharField(max_length=255)
    rules = models.TextField(help_text="Global rules for the organization")
    default_model = models.CharField(max_length=255, default="anthropic/claude-3-haiku", help_text="OpenRouter model ID")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
