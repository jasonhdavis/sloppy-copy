from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from sources.models import Source
from stories.models import Story
from sources.services import FeedIngestionService

class SourceDigestView(ListView):
    model = Story
    template_name = 'sources/source_digest.html'
    context_object_name = 'stories'
    paginate_by = 24

    def get_queryset(self):
        return Story.objects.filter(status='ingested').order_by('-published_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_sources'] = Source.objects.filter(is_active=True)
        return context

def ingest_feeds_view(request):
    """
    HTMX view to trigger feed ingestion.
    """
    if request.method == 'POST':
        results = FeedIngestionService.ingest_all_sources()
        return render(request, 'sources/partials/ingestion_results.html', {'results': results})
    return HttpResponse(status=405)

class StoryDetailView(DetailView):
    model = Story
    template_name = 'sources/story_detail.html'
    context_object_name = 'story'
