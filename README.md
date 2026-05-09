# WOWproject

WOWproject is a civic transparency web application created by Kevin Harper, Darron McIntyre, and Mallah-Divine Mallah.

The project helps community members search public civilian complaint data connected to New York City police officers. The goal is to support transparency between the community and law enforcement by making officer complaint information easier to access and understand.

## Current functionality

- Search for officers by last name or badge number.
- Return matching officer records from the project database.
- Support partial-name searches when the exact spelling is unknown.

## Technology stack

### Backend

- Python 3.11
- Flask
- Flask-SQLAlchemy
- PostgreSQL
- Gunicorn

### Frontend

- HTML
- CSS
- JavaScript

## Data note

The project uses public CCRB data released in 2020. The database connection information is intentionally not committed to the repository.

## Local setup

From the repository root:

```bash
cd BaseCode
python -m pip install --upgrade pip pipenv
pipenv install --dev
pipenv shell
```

## Running the app locally

After installing dependencies, run the main application file from the directory where the Flask app is located:

```bash
python application.py
```

Depending on your local environment, you may need to set database environment variables before the app can connect to PostgreSQL.

## Development checks

Compile the Python files to catch syntax errors:

```bash
cd BaseCode
pipenv run python -m compileall .
```

## Security and configuration

Do not commit database credentials, API keys, `.env` files, or local virtual environments. Use environment variables for private configuration.
