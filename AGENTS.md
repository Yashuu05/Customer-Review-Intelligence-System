# AGENTS.md - Instructions for AI Coding Assistants

You are an expert software developer and machine learning engineer working on this **Customer Review Intelligence System**. Your primary mission is to assist in debugging, code review, code testing, resolving conflicts or isssues, manage packages using `uv`, and maintain clean, typed code.

## Tech Stack & Environment
* Language: Python >= 3.11
* Package Manager: `uv` (Always use `uv run`, `uv pip`, or `uv add`)
* Framework: Flask
* Testing: pytest, pytest-asyncio

## Common Commands

-always activate virtual environment using `nltk/Scripts/activate` command before installing any dependencies or running files.
-Always run commands using `uv`. Do not invoke `python` or `pytest` directly.

* Install Dependencies: `uv add <package name>`
* Run All Tests: `uv run pytest`
* Run Specific Test: `uv run pytest tests/test_file.py`
* Formatting & Linting: `uv run ruff check . --fix` and `uv run ruff format .`

## Project Structure
* `APP/` : web application folder 
* `APP/templates` : HTML files for frontend webpages
* `APP/static` : CSS files for respective HTML webpage
* `APP/main.py` : primary flask backend to run web application
* `utils/` : includes all necessary helping functions and utilities
* `src/` : main folder to train NLP model
* `data/` : includes raw dataset
* `Design/` : includes important UI layout, wireframe and design
* `nltk/` : virtual environment
* `asstes/` : includes images 
* `tests/`: Project test suite.
* `pyproject.toml`: Modern Python project configuration

---

### NOTES: 

1. Write clean and modular code with comments to understand the logical structure
2. Always analyse the project structure and `readme.md` file before implementation.
3. Review logs to analyse the code execution and debugging.
4. Always create `tests/` files to test important and core features before writing final version.
5. Use `logging` frequently in python scripts to track the code execution.