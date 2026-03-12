from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cms/', views.cms_dashboard, name='cms_dashboard'),
    path('cms/digest/', views.cms_digest, name='cms_digest'),
    path('cms/authors/', views.cms_authors, name='cms_authors'),
]
