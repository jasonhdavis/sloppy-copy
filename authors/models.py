from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    bio = models.TextField(blank=True)
    avatar_url = models.URLField(null=True, blank=True)

    # Editorial Identity
    beat_description = models.TextField()
    style_guide = models.TextField()
    writing_voice = models.CharField(max_length=255)
    tone_keywords = models.JSONField(default=list, blank=True)
    persona_prompt = models.TextField(help_text="Database-editable prompt for the rewrite engine")

    # Operational Fields
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
