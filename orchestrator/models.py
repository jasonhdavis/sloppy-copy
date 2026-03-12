from django.db import models

class PipelineRun(models.Model):
    STATUS_CHOICES = [
        ('running', 'Running'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='running')
    
    stories_ingested = models.IntegerField(default=0)
    stories_evaluated = models.IntegerField(default=0)
    stories_assigned = models.IntegerField(default=0)
    rewrites_generated = models.IntegerField(default=0)
    
    error_log = models.TextField(null=True, blank=True)
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Run {self.id} ({self.status})"
