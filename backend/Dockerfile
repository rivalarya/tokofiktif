FROM python:3.13-slim AS builder
WORKDIR /app
COPY backend/pyproject.toml backend/uv.lock ./
RUN pip install --no-cache-dir uv \
 && uv sync --no-dev --frozen --no-install-project --python 3.13
FROM python:3.13-slim AS runner
WORKDIR /app
ENV APP_ENV=production

RUN addgroup --system --gid 1001 fastapi-starter \
 && adduser --uid 1001 --gid 1001 --home /home/appuser --no-create-home --disabled-password --gecos "" appuser \
 && mkdir -p /home/appuser /app/qdrant_db \
 && chown -R appuser:fastapi-starter /app \
 && chown -R appuser:fastapi-starter /home/appuser

COPY --chown=appuser:fastapi-starter --from=builder /app/.venv ./.venv
COPY --chown=appuser:fastapi-starter backend/ .
COPY --chown=appuser:fastapi-starter data/ /data/

ENV PATH="/app/.venv/bin:$PATH"

USER appuser
EXPOSE 4000
ENV PORT=4000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "4000"]
