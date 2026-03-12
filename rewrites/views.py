from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Rewrite, Assignment
from stories.models import Story
from authors.models import Author
from .services import RewriteGenerationService

class RewriteListView(ListView):
    model = Rewrite
    template_name = 'rewrites/list.html'
    context_object_name = 'rewrites'
    ordering = ['-created_at']

class RewriteDetailView(DetailView):
    model = Rewrite
    template_name = 'rewrites/detail.html'
    context_object_name = 'rewrite'

def manual_generate(request, story_id):
    """
    Manually trigger a rewrite for a specific story and author.
    """
    if request.method == 'POST':
        story = get_object_or_404(Story, id=story_id)
        author_id = request.POST.get('author_id')
        author = get_object_or_404(Author, id=author_id)
        
        # Create assignment
        assignment = Assignment.objects.create(
            story=story,
            author=author,
            match_rationale="Manual assignment by editor.",
            status='pending'
        )
        
        # Generate rewrite
        service = RewriteGenerationService()
        rewrite = service.generate_rewrite(assignment)
        
        if rewrite:
            return HttpResponse(f"Successfully generated rewrite: {rewrite.headline}")
        else:
            return HttpResponse("Failed to generate rewrite.", status=500)
            
    return HttpResponse("Method not allowed.", status=405)
