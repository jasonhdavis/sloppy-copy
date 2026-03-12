from django.contrib import admin
from .models import Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'status', 'ai_score', 'published_at')
    search_fields = ('title', 'url')
    list_filter = ('source', 'status')
    readonly_fields = ('ingested_at',)
