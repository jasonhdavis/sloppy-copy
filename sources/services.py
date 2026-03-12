import logging
import feedparser
import requests
from django.utils import timezone
from dateutil import parser as date_parser
from sources.models import Source
from stories.models import Story
from sources.selectors import get_active_sources, story_exists_by_url

logger = logging.getLogger(__name__)

class FeedIngestionService:
    @staticmethod
    def ingest_all_sources():
        """
        Ingests stories from all active sources.
        """
        sources = get_active_sources()
        results = []
        for source in sources:
            try:
                count = FeedIngestionService.ingest_source(source)
                results.append({
                    'source': source.name,
                    'created': count,
                    'status': 'success'
                })
            except Exception as e:
                logger.error(f"Failed to ingest source {source.name}: {str(e)}")
                results.append({
                    'source': source.name,
                    'error': str(e),
                    'status': 'error'
                })
        return results

    @staticmethod
    def ingest_source(source: Source):
        """
        Ingests stories from a single source.
        """
        if not source.feed_url:
            logger.warning(f"Source {source.name} has no feed URL.")
            return 0

        feed_data = FeedIngestionService.fetch_feed(source.feed_url)
        if not feed_data:
            return 0

        entries = FeedIngestionService.parse_feed_entries(feed_data)
        created_count = 0
        for entry in entries:
            normalized = FeedIngestionService.normalize_entry(entry)
            if normalized:
                story = FeedIngestionService.create_story_if_new(source, normalized)
                if story:
                    created_count += 1
        
        source.last_checked_at = timezone.now()
        source.save(update_fields=['last_checked_at'])
        
        return created_count

    @staticmethod
    def fetch_feed(url):
        """
        Fetches the feed content from the given URL.
        """
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            return response.content
        except Exception as e:
            logger.error(f"Error fetching feed from {url}: {str(e)}")
            return None

    @staticmethod
    def parse_feed_entries(feed_data):
        """
        Parses the feed data using feedparser.
        """
        parsed = feedparser.parse(feed_data)
        if parsed.bozo:
            logger.warning(f"Feedparser reported an error: {parsed.bozo_exception}")
        return parsed.entries

    @staticmethod
    def normalize_entry(entry):
        """
        Normalizes a feed entry into a standard format.
        """
        # URL is mandatory
        url = entry.get('link') or entry.get('id')
        if not url:
            return None

        # Title
        title = entry.get('title', 'Untitled')

        # Summary
        summary = entry.get('summary') or entry.get('description') or entry.get('content', [{}])[0].get('value', '')
        if summary:
            # Truncate to 2000 chars as per spec
            summary = summary[:2000]

        # Published Date
        published_at = None
        date_str = entry.get('published') or entry.get('updated')
        if date_str:
            try:
                published_at = date_parser.parse(date_str)
                if timezone.is_naive(published_at):
                    published_at = timezone.make_aware(published_at, timezone.utc)
            except Exception:
                published_at = timezone.now()
        else:
            published_at = timezone.now()

        return {
            'title': title,
            'url': url,
            'summary': summary,
            'published_at': published_at,
            'external_id': entry.get('id')
        }

    @staticmethod
    def create_story_if_new(source, normalized_entry):
        """
        Creates a new Story record if it doesn't already exist.
        """
        if story_exists_by_url(normalized_entry['url']):
            return None

        try:
            story = Story.objects.create(
                source=source,
                title=normalized_entry['title'],
                url=normalized_entry['url'],
                summary=normalized_entry['summary'],
                published_at=normalized_entry['published_at'],
                external_id=normalized_entry['external_id'],
                status='ingested'
            )
            return story
        except Exception as e:
            logger.error(f"Error creating story {normalized_entry['url']}: {str(e)}")
            return None
