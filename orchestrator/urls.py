from django.urls import path
from . import views

app_name = 'orchestrator'

urlpatterns = [
    path('run/', views.run_pipeline_view, name='run_pipeline'),
]
