from sources.models import Source
from stories.models import Story

def get_active_sources():
    """
    Returns all active sources.
    """
    return Source.objects.filter(is_active=True)

def story_exists_by_url(url):
    """
    Checks if a story with the given URL already exists.
    """
    return Story.objects.filter(url=url).exists()
