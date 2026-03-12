from django.http import HttpResponse
from django.views.decorators.http import require_POST
from orchestrator.services import PipelineOrchestrator

@require_POST
def run_pipeline_view(request):
    service = PipelineOrchestrator()
    try:
        # We run it in the background or just wait if it's fast enough for demo
        service.run_pipeline()
        return HttpResponse('<p class="text-green-500 text-xs">Pipeline run triggered successfully.</p>')
    except Exception as e:
        return HttpResponse(f'<p class="text-red-500 text-xs">Error: {str(e)}</p>')
