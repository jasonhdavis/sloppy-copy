# Sloppy Copy

AI-powered content pipeline that ingests news, evaluates it for newsworthiness using an "Editor AI" persona, and rewrites selected stories using distinct author personas guided by a central Editorial Style Sheet.

## Features

- **RSS Ingestion**: Automated fetching of news from multiple sources.
- **Editor AI**: Intelligent evaluation of story importance based on frequency and relevance.
- **Author Personas**: Distinct writing styles for different authors, managed via the admin.
- **Editorial Style Sheet**: Global rules that guide all AI rewrites.
- **Pipeline Orchestration**: End-to-end automation from ingestion to rewrite.
- **Modern UI**: Built with Django, HTMX, and Material Tailwind.

## Tech Stack

- **Backend**: Django 5.0
- **Database**: SQLite
- **Frontend**: HTMX, Alpine.js, Material Tailwind (HTML)
- **AI**: OpenRouter (Claude/GPT/Llama)
- **Markdown**: EasyMDE

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd sloppy-copy
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Copy `.env.example` to `.env` and fill in your `OPENROUTER_KEY`.
   ```bash
   cp .env.example .env
   ```

5. **Initialize the database**:
   ```bash
   python manage.py migrate
   ```

6. **Seed initial data**:
   ```bash
   python manage.py seed_sources
   python manage.py seed_authors
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Usage

- **Dashboard**: Access the main dashboard at `http://127.0.0.1:8000/`.
- **Admin**: Manage sources, authors, and style sheets at `http://127.0.0.1:8000/admin/`.
- **Run Pipeline**: Trigger the full pipeline via the management command:
  ```bash
  python manage.py run_pipeline
  ```

## Architecture Overview

- `ai/`: AI provider abstraction layer.
- `authors/`: Author persona management and matching logic.
- `core/`: Dashboard and global editorial settings.
- `orchestrator/`: Pipeline coordination and logging.
- `rewrites/`: Rewrite generation and assignment tracking.
- `sources/`: RSS feed management and ingestion.
- `stories/`: Story storage and Editor AI evaluation.

## License

MIT
