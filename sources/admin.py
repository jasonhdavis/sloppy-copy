from django.contrib import admin
from .models import Source

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'source_type', 'is_active', 'last_checked_at')
    search_fields = ('name', 'feed_url')
    list_filter = ('source_type', 'is_active')
    prepopulated_fields = {"slug": ("name",)}
