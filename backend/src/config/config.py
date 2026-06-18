import os

from dotenv import load_dotenv

_env_file = ".env.test" if os.getenv("APP_ENV") == "test" else ".env"
load_dotenv(_env_file)


def _parse_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.lower() == "true"


def _parse_origins(value: str | None) -> list[str]:
    if not value:
        return ["https://example.com"]
    return [o.strip() for o in value.split(",")]


APP_ENV = os.getenv("APP_ENV", "development")

_is_test = APP_ENV == "test"


class _Config:
    PORT: int = int(os.getenv("PORT", "4000"))
    APP_ENV: str = APP_ENV
    ENABLE_CORS: bool = _parse_bool(os.getenv("ENABLE_CORS")) or _is_test
    ALLOWED_ORIGIN: list[str] = _parse_origins(os.getenv("ALLOWED_ORIGIN"))
    ENABLE_RATE_LIMITER: bool = _parse_bool(os.getenv("ENABLE_RATE_LIMITER")) or _is_test


config = _Config()
