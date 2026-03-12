from django.contrib import admin
from .models import Assignment, Rewrite

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('story', 'author', 'status', 'match_score')
    list_filter = ('status', 'author')
    search_fields = ('story__title', 'author__name')

@admin.register(Rewrite)
class RewriteAdmin(admin.ModelAdmin):
    list_display = ('headline', 'status', 'created_at')
    list_filter = ('status', 'assignment__author')
    search_fields = ('headline', 'body')
