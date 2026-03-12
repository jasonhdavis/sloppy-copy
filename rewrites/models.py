from django.db import models
from stories.models import Story
from authors.models import Author

class Assignment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="assignments")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="assignments")
    match_score = models.FloatField(null=True, blank=True)
    match_rationale = models.TextField(null=True, blank=True)
    assigned_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.story.title} -> {self.author.name}"

class Rewrite(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('review', 'Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="rewrites")
    headline = models.CharField(max_length=500)
    dek = models.CharField(max_length=500, blank=True)
    body = models.TextField()
    model_used = models.CharField(max_length=255, null=True, blank=True)
    prompt_version = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline
