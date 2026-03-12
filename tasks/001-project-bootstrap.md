# Task 001: Project Bootstrap

## Objective
Initialize the Django project, virtual environment, and install core dependencies.

## Context
This is the first step in building Sloppy Copy. We need a clean Django environment with all necessary apps and libraries.

## Required Files
- `requirements.txt`
- `.env` (from `.env.example`)
- `sloppycopy/settings.py`
- `sloppycopy/urls.py`

## Implementation Steps

### 1. Environment Setup
- Create a virtual environment: `python3 -m venv venv`
- Activate it: `source venv/bin/activate`
- Create `requirements.txt` with the following content:
```txt
Django==5.0.1
python-dotenv==1.0.0
feedparser==6.0.10
requests==2.31.0
anthropic==0.18.1
openai==1.12.0
python-dateutil==2.8.2
```
- Install dependencies: `pip install -r requirements.txt`

### 2. Django Initialization
- Start the project: `django-admin startproject sloppycopy .`
- Create the following apps (exact names):
  - `core`
  - `sources`
  - `stories`
  - `authors`
  - `rewrites`
  - `orchestrator`

Command example:

```
python manage.py startapp core
python manage.py startapp sources
python manage.py startapp stories
python manage.py startapp authors
python manage.py startapp rewrites
python manage.py startapp orchestrator
```

Create the AI module structure:

```
ai/
  __init__.py
  client.py
  providers.py
  types.py
```

Create prompt directory:

```
prompts/
```

Expected project structure after bootstrap:

```
sloppycopy/
  settings.py
  urls.py
  asgi.py
  wsgi.py

core/
sources/
stories/
authors/
rewrites/
orchestrator/

ai/
prompts/
```

### 3. Configuration
- Create `.env` based on `.env.example`.
- Update [`sloppycopy/settings.py`](sloppycopy/settings.py) to:

Load environment variables:

```
from dotenv import load_dotenv
load_dotenv()
```

Register apps in `INSTALLED_APPS`:

```
core
sources
stories
authors
rewrites
orchestrator
```

Configure SQLite database:

```
DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
  }
}
```

Environment variables expected:

```
OPENAI_API_KEY
ANTHROPIC_API_KEY
DEFAULT_AI_PROVIDER
```

These values will later be used by [`AIClient`](ai/client.py:1).

## Verification Commands
- `python manage.py check`
- `python manage.py runserver`

## Success Criteria
- [x] Virtual environment is active and dependencies are installed.
- [x] Django project and all apps are created.
- [x] `python manage.py check` returns no issues.
- [ ] Development server starts without errors.
