# Lint & Format

This project has Python and front-end formatting configured.

- Python: ruff (lint, import sort) + black (format)
- Front-end: js-beautify for HTML/CSS/JS in `templates/` and `static/`

## Install tools

Use the existing VS Code task or run in the active environment:

- pip install -r requirements.txt
- npm install

## Run formatters

- Python (check): ruff check .
- Python (fix): ruff check . --fix && black .
- Front-end (fix): npm run format

## Notes

- Virtualenv and node_modules are excluded from linting.
- EditorConfig enforces LF and common indentation.
