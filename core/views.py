from django.shortcuts import render
from stories.models import Story
from rewrites.models import Rewrite
from authors.models import Author
from orchestrator.models import PipelineRun

def dashboard(request):
    stats = {
        'total_stories': Story.objects.count(),
        'selected_stories': Story.objects.filter(ai_score__gte=0.7).count(),
        'total_rewrites': Rewrite.objects.count(),
        'total_authors': Author.objects.count(),
    }
    
    latest_run = PipelineRun.objects.order_by('-started_at').first()
    
    # For the Source Digest (Masonry)
    stories = Story.objects.order_by('-published_at')[:20]
    
    context = {
        'stats': stats,
        'latest_run': latest_run,
        'stories': stories,
    }
    return render(request, 'core/dashboard.html', context)
