from django.core.management.base import BaseCommand
from orchestrator.services import PipelineOrchestrator

class Command(BaseCommand):
    help = 'Runs the full content pipeline: ingest -> evaluate -> match -> rewrite'

    def add_arguments(self, parser):
        parser.add_argument(
            '--mode',
            type=str,
            help='Run only a specific stage: ingest, evaluate, match, rewrite',
        )

    def handle(self, *args, **options):
        mode = options.get('mode')
        self.stdout.write(self.style.SUCCESS(f'Running pipeline (mode: {mode or "full"})'))
        
        orchestrator = PipelineOrchestrator()
        
        if mode == 'ingest':
            count = orchestrator.run_ingestion()
            self.stdout.write(f"Ingested: {count}")
        elif mode == 'evaluate':
            count = orchestrator.run_evaluation()
            self.stdout.write(f"Evaluated: {count}")
        elif mode == 'match':
            count = orchestrator.run_matching()
            self.stdout.write(f"Matched: {count}")
        elif mode == 'rewrite':
            count = orchestrator.run_rewrites()
            self.stdout.write(f"Rewritten: {count}")
        else:
            results = orchestrator.run_pipeline()
            self.stdout.write(f"Ingested: {results['ingestion']}")
            self.stdout.write(f"Evaluated: {results['evaluated']}")
            self.stdout.write(f"Matched: {results['matched']}")
            self.stdout.write(f"Rewritten: {results['rewritten']}")
        
        self.stdout.write(self.style.SUCCESS('Pipeline complete'))
