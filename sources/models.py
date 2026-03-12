from django.db import models

class Source(models.Model):
    SOURCE_TYPES = [
        ('rss', 'RSS'),
        ('api', 'API'),
        ('manual', 'Manual'),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    source_type = models.CharField(max_length=20, choices=SOURCE_TYPES)
    feed_url = models.URLField(null=True, blank=True)
    homepage_url = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    last_checked_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
