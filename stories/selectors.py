from .models import Story

def get_unevaluated_stories(limit: int = 20):
    """
    Returns a queryset of stories that have been ingested but not yet evaluated.
    """
    return Story.objects.filter(status='ingested')[:limit]
