from django.contrib import admin
from .models import PipelineRun

@admin.register(PipelineRun)
class PipelineRunAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'started_at', 'completed_at')
    list_filter = ('status',)
    readonly_fields = ('started_at',)
