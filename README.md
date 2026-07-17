# Sample Backend

FastAPI application for the DevOps deployment lab. Part of a pipeline: GitHub Actions -> Docker Context -> Remote Docker Engine.

## Run Locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

Swagger docs at `http://localhost:8000/docs`.

## Docker

```bash
# Build and run (includes PostgreSQL)
docker compose up --build

# Stop
docker compose down

# Stop and remove volumes
docker compose down -v
```

## Environment Variables

| Variable | Description | Default |
|---|---|---|
| `APP_NAME` | Application name | `sample-backend` |
| `APP_ENV` | Environment name | `development` |
| `APP_VERSION` | App version | `0.0.0` |
| `PG_HOST` | PostgreSQL host | `localhost` |
| `PG_PORT` | PostgreSQL port | `5432` |
| `PG_USER` | PostgreSQL user | `postgres` |
| `PG_PASSWORD` | PostgreSQL password | `postgres` |
| `PG_DB` | PostgreSQL database | `sample_db` |

## API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/api/v1/health` | Health check |
| GET | `/api/v1/version` | App version info |
| GET | `/docs` | Swagger UI |

## Deployment

Two GitHub Actions workflows:

- **deploy-qa.yml** - Triggers on push to `stage` branch
- **deploy-prod.yml** - Manual trigger via `workflow_dispatch`

Both run on the `athena-deployer` runner.

### Docker Context Architecture

```
GitHub Actions (CI)
       |
       v
  Docker Context
       |
       v
  Remote Docker Engine
```

The pipeline builds the Docker image, establishes a Docker context to the remote engine, and deploys the container there. This keeps the build environment separate from the target deployment host.
# sample-backend
