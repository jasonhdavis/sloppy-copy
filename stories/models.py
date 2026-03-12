from django.db import models
from sources.models import Source

class Story(models.Model):
    STATUS_CHOICES = [
        ('ingested', 'Ingested'),
        ('evaluated', 'Evaluated'),
        ('matched', 'Matched'),
        ('assigned', 'Assigned'),
        ('rewritten', 'Rewritten'),
        ('rejected', 'Rejected'),
    ]

    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name="stories")
    external_id = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=500)
    url = models.URLField(unique=True)
    summary = models.TextField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    ingested_at = models.DateTimeField(auto_now_add=True)

    # Evaluation Fields
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ingested')
    ai_score = models.FloatField(null=True, blank=True)
    ai_rationale = models.TextField(null=True, blank=True)
    topic_tags = models.JSONField(default=list, blank=True)

    class Meta:
        verbose_name_plural = "Stories"

    def __str__(self):
        return self.title
