from django.shortcuts import render
from django.http import HttpResponse
from stories.models import Story
from rewrites.models import Rewrite
from authors.models import Author
from core.models import EditorialStyleSheet
from orchestrator.models import PipelineRun

def dashboard(request):
    """
    Public Front End Dashboard - Shows final Rewrites.
    """
    rewrites = Rewrite.objects.filter(status='approved').order_by('-created_at')[:10]
    # Fallback to draft if no approved ones yet for the demo
    if not rewrites.exists():
        rewrites = Rewrite.objects.order_by('-created_at')[:10]
        
    authors = Author.objects.filter(is_active=True)[:5]
    
    context = {
        'rewrites': rewrites,
        'authors': authors,
    }
    return render(request, 'core/dashboard.html', context)

def cms_dashboard(request):
    """
    Editorial CMS Dashboard - Operational stats and controls.
    """
    stats = {
        'total_stories': Story.objects.count(),
        'selected_stories': Story.objects.filter(ai_score__gte=0.7).count(),
        'total_rewrites': Rewrite.objects.count(),
        'total_authors': Author.objects.count(),
    }
    
    latest_run = PipelineRun.objects.order_by('-started_at').first()
    
    context = {
        'stats': stats,
        'latest_run': latest_run,
    }
    return render(request, 'cms/dashboard.html', context)

def cms_digest(request):
    """
    Source Digest - The "firehose" of raw ingested stories.
    """
    stories = Story.objects.order_by('-published_at')[:50]
    authors = Author.objects.filter(is_active=True)
    
    context = {
        'stories': stories,
        'authors': authors,
    }
    return render(request, 'cms/digest.html', context)

def cms_authors(request):
    """
    CMS Author Management - List and manage author personas.
    """
    style_sheet = EditorialStyleSheet.objects.filter(is_active=True).first()
    
    if request.method == 'POST':
        default_model = request.POST.get('default_model')
        if default_model and style_sheet:
            style_sheet.default_model = default_model
            style_sheet.save()
            return HttpResponse(f"Model updated to {default_model}")

    authors = Author.objects.all().order_by('-is_active', 'name')
    
    context = {
        'authors': authors,
        'style_sheet': style_sheet,
    }
    return render(request, 'cms/authors.html', context)
