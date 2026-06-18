import time
from collections import defaultdict

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from src.config import config

banned_ips: set[str] = set()
request_counts: dict[str, list[float]] = defaultdict(list)

MAX_REQUESTS = 10
WINDOW_SECONDS = 10
BAN_AFTER_VIOLATIONS = 5
violation_counts: dict[str, int] = defaultdict(int)


def register_rate_limiter(app: FastAPI) -> None:
    if not config.ENABLE_RATE_LIMITER:
        return

    class RateLimitMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request: Request, call_next):
            client_ip = request.client.host if request.client else "unknown"

            if client_ip in banned_ips:
                return JSONResponse(
                    status_code=403, content={"message": "Your IP has been banned", "data": {}}
                )

            now = time.time()
            window_start = now - WINDOW_SECONDS
            request_counts[client_ip] = [t for t in request_counts[client_ip] if t > window_start]

            if len(request_counts[client_ip]) >= MAX_REQUESTS:
                violation_counts[client_ip] += 1
                if violation_counts[client_ip] >= BAN_AFTER_VIOLATIONS:
                    banned_ips.add(client_ip)
                    return JSONResponse(
                        status_code=403, content={"message": "Your IP has been banned", "data": {}}
                    )
                return JSONResponse(
                    status_code=429, content={"message": "Too many requests", "data": {}}
                )

            request_counts[client_ip].append(now)
            return await call_next(request)

    app.add_middleware(RateLimitMiddleware)
