from django.urls import path
from . import views

app_name = 'rewrites'

urlpatterns = [
    path('', views.RewriteListView.as_view(), name='list'),
    path('<int:pk>/', views.RewriteDetailView.as_view(), name='detail'),
    path('manual-generate/<int:story_id>/', views.manual_generate, name='manual_generate'),
]
