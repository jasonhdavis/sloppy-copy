from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Rewrite

class RewriteListView(ListView):
    model = Rewrite
    template_name = 'rewrites/list.html'
    context_object_name = 'rewrites'
    ordering = ['-created_at']

class RewriteDetailView(DetailView):
    model = Rewrite
    template_name = 'rewrites/detail.html'
    context_object_name = 'rewrite'
