from django.urls import path
from sources.views import SourceDigestView, StoryDetailView, ingest_feeds_view, test_feed_view

app_name = 'sources'

urlpatterns = [
    path('digest/', SourceDigestView.as_view(), name='source_digest'),
    path('story/<int:pk>/', StoryDetailView.as_view(), name='story_detail'),
    path('ingest/', ingest_feeds_view, name='ingest_feeds'),
    path('test-feed/', test_feed_view, name='test_feed'),
]
