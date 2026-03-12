from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author

class AuthorListView(ListView):
    model = Author
    template_name = 'authors/list.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/detail.html'
    context_object_name = 'author'
