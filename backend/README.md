# fastapi-starter

A minimal FastAPI project template with CORS, rate limiting, and automatic route registration.

## Requirements

- Python 3.13+

## Setup

```bash
cp .env.example .env
uv sync
```

## Running

```bash
uv run python -m src.main
```

## Environment Variables

| Variable              | Default               | Description                                      |
|-----------------------|-----------------------|--------------------------------------------------|
| `APP_ENV`            | `development`         | Environment (`development`, `production`, `test`) |
| `PORT`                | `4000`                | Server port                                      |
| `ENABLE_CORS`         | `false`               | Enable CORS middleware                           |
| `ALLOWED_ORIGIN`      | `https://example.com` | Comma-separated list of allowed origins          |
| `ENABLE_RATE_LIMITER` | `false`               | Enable IP-based rate limiting                    |

## Project Structure

```
src/
├── config/         # Environment config
├── domains/        # Route domains (auto-registered)
│   └── ping/       # Example domain
├── exceptions/     # Custom exceptions
├── middlewares/    # CORS and rate limiter
├── utils/          # Route auto-registration
├── types.py        # Shared response types
└── main.py         # App entrypoint
```

## Adding a Domain

Create a folder under `src/domains/<name>/` with:

- `routes.py` — defines an `APIRouter` named `router`
- `handler.py` — async handler functions
- `schema.py` — Pydantic request/response models

The router is registered automatically at `/<name>` on startup. The `ping` domain is an exception and registers at `/`.

## Rate Limiter

When enabled, limits each IP to 10 requests per 10 seconds. After 5 violations, the IP is permanently banned for the lifetime of the process.

## Docker

```bash
docker build -t fastapi-starter .
docker run -p 4000:4000 fastapi-starter
```

# CI/CD
Uses GitHub Actions. See `.github/workflows/ci.yml`.
Pipeline runs on every push and pull request to `main`:

- Lint with ruff
- Run tests