# AI-Driven-Interview-Bot

AI-Driven-Interview-Bot is a Python project that helps simulate technical interview conversations using AI. This README provides quick setup, usage, development, and contribution information so you can get started fast.

## Features

- Interactive interview simulations with configurable prompts
- Role-based interviewer and candidate modes
- Save and review past interview sessions
- Extensible: add new question sets and evaluation metrics

## Requirements

- Python 3.10 or newer
- pip

Optional (recommended): create an isolated virtual environment (`venv` or `virtualenv`).

## Installation

1. Clone the repository:

    git clone https://github.com/your-org/AI-Driven-Interview-Bot.git
    cd AI-Driven-Interview-Bot

2. Create and activate a virtual environment:

    python -m venv .venv
    # On Windows (PowerShell)
    .venv\Scripts\Activate.ps1
    # On macOS / Linux
    source .venv/bin/activate

To deactivate virtual env when done:

    deactivate

3. Install dependencies:

    pip install -r requirements.txt

If this project does not yet include `requirements.txt`, install packages as needed (for example `openai`, `pytest`, etc.).

## Quickstart

Adjust the module or entrypoint below to match the project's layout. Example commands:

    # Run the main program (replace with your entry module/file)
    uvicorn app.main:app --reload

## Configuration

- Add API keys or other secrets to environment variables before running (for example `OPENAI_API_KEY`).
- Consider using a `\.env` file and `python-dotenv` during local development.

## PostgreSQL setup (local development)

This project can use PostgreSQL for local development. Steps performed on Windows:

- Install PostgreSQL using the official installer or use WSL. Ensure the `psql` client is available on `PATH`.
  - Example PATH on Windows: `C:\Program Files\PostgreSQL\<version>\bin` — add that directory to system/user PATH if `psql` is not recognized.
- Start the PostgreSQL service (or use pgAdmin/Service manager).
- Connect locally with `psql`:

    psql -U postgres -h localhost -p 5432

- Change the `postgres` user password:
  - Interactive method inside `psql`:

      \password postgres

  - Or via SQL:

      ALTER USER postgres WITH PASSWORD 'new_secure_password';

Notes:
- If `psql` is not recognized on Windows, either add the `bin` folder to `PATH` or open the "SQL Shell (psql)" shipped with the installer.
- If a `\.env` containing secrets was committed, rotate the exposed credentials immediately (DB password, API keys, etc.).

## Environment files and secrets

- Create local `\.env` from `\.env.example` for development only and do not commit `\.env`.

Example workflow:

    cp .env.example .env

Add to `\.gitignore` if not already:

    .env

### `\.env.example`

Use `\.env.example` to document required keys without real secrets. Example entries:

    # Database
    DATABASE_URL=postgresql://user:password@localhost:5432/ai_interview
    PGHOST=localhost
    PGPORT=5432
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=

    # OpenAI
    OPENAI_API_KEY=

    # Other keys...
    # Add other required keys here, leave values empty for local setup.

### Loading variables in Python (development only)

    from dotenv import load_dotenv
    import os

    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")

## If `\.env` was already committed

Remove it from the index, commit the change, push, and rotate secrets immediately:

    git rm --cached .env
    git commit -m "Remove .env from repository"
    git push origin feature/STORY-AI-003-PostgreSQL-Database-Setup

If secrets were exposed, rotate DB passwords and API keys and update any consumers.

## Test db connection

run test_db_connection.py to verify the connection to PostgreSQL is working correctly:

    python test_db_connection.py

## Development

- Use a consistent formatter (e.g., `black`) and linter (e.g., `flake8`).

    pip install -U black flake8
    black .
    flake8

## Testing

If tests exist, run them with `pytest`:

    pip install -U pytest
    pytest

## Contributing

- Open an issue to discuss larger changes before implementing.
- Fork the repo, create a feature branch, and submit a pull request with a clear description and tests where applicable.

## License

This project is provided under the MIT License unless otherwise noted in repository metadata.

## Notes

- Branch used for the PostgreSQL setup: `feature/STORY-AI-003-PostgreSQL-Database-Setup`
- Remote: `origin`
