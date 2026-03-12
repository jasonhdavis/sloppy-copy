# Agent Rules

## 🔄 Project Awareness & Context
- **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Check project `tasks` folder** before starting, ensure you are referencing the appropriate task file. Ask the user, or infer from the tasks folder based on `@git-changes` or most recently modified file. If you don't see a matching file, prepare a brief description and ask if the user would like the task written into the suggested file.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.

## 🧱 Code Structure & Modularity
- **Organize code into clearly separated modules**, grouped by feature or responsibility.
- **Follow Python and Django best practice**, utilize built-in features and prefer industry-standard implementations when available.
- **Always include documentation** describing the code to a mid-level developer.

## 🧩 Task Decomposition & Dot Notation
- **Use dot notation for all task references**:  
  - `X.Y.Z`  
    - **X = file**  
    - **Y = module/class**  
    - **Z = function/method**
- **Work systematically down the chain**:  
  1. Confirm file exists  
  2. Confirm module/class exists  
  3. Implement/modify the function  
- Add new TODO items using the same dot notation.

## 🧪 Testing & Reliability
- After implementing a feature, **test with the user using live terminal commands**.
- After initial debugging, **ask if the user wants formal tests**.
- Tests should include:
  - One expected-use case  
  - One edge case  
  - One failure case  
- Place tests inside `tests.py` or a `tests/` folder within the app.

## ✅ Task Completion
- **Mark tasks complete** in the `/tasks` folder as soon as they are finished.
- **Atomic Git Commits**: After completing a task (e.g., `001`, `002`), perform a git commit referencing the task ID.
- Add new subtasks or TODOs to `/tasks/BACKLOG.md` with a date and contextual reference.

## 📎 Style & Conventions
- Use **Python** as primary language.
- Use **Material Tailwind** for all UI components in Django templates.
- Use **EasyMDE** for all markdown-enabled text fields in the UI.
- **Always reference [`STYLE_GUIDE.md`](../../STYLE_GUIDE.md) before implementing any UI feature.**

## 🎨 UI Development Rules
- **Read the Style Guide first**: Before implementing UI, review [`STYLE_GUIDE.md`](../../STYLE_GUIDE.md).
- **Use Material Tailwind components**: Reference [`/docs/material-tailwind-html/`](../../docs/material-tailwind-html/) for all component implementations.
- **Follow the canonical layout**: All pages use header + cards structure.
- **HTMX-first interactions**: Use inline edits and modals—no standalone edit pages.
- **Reuse existing patterns**: When unsure, copy an existing screen.
- **No custom components**: Unless reused ≥ 3 times and documented in [`/templates/components/`](../../templates/components/).
- **Follow template structure**: Respect the organization defined in [`docs/TEMPLATE_STRUCTURE.md`](../../docs/TEMPLATE_STRUCTURE.md).

### UI Anti-Patterns (Never Do These)
- ❌ Craft standalone `/edit/` routes
- ❌ Build custom button or form components
- ❌ Create layouts with raw Tailwind utility soup
- ❌ Mix component libraries or icon families
- ❌ Make "just this once" UI exceptions

### Build boring, familiar UI
The best UI is invisible. Users should focus on their work, not on figuring out your interface.

## 📚 Documentation & Explainability
- Update `README.md` when features or dependencies change.
- Comment non-obvious code.
- For complex logic, include an inline `# Reason:` comment explaining *why* something is done.

## 🧠 AI Behavior Rules
- **Never assume missing context. Ask questions if uncertain.**
- **Never hallucinate libraries or functions.**
- **Always confirm file paths and modules** exist before referencing them.
- **Never delete or overwrite code** unless instructed or part of a formal task.
- **Do not summarize or remove code** when making edits — provide full functions.
- **Always provide adiquite context** when delivering subtasks to new agent context windows, always provide extensive context, file references with paths, and rational with both positive and negative prompting to ensure agent compliance. 

## 👑 About The User
- Refer to the user as **M'Lord** whenever the request is understood.
- Before completing a task, **ask if M'Lord considers the task complete**, and provide a **0–10 confidence rating**.
- Ask M'Lord to verify functionality by loading a page or running a command.
- The user is technically skilled and can run shell commands; feel free to request logs, errors, or code context.
