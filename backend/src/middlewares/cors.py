from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.config import config


def register_cors(app: FastAPI) -> None:
    if not config.ENABLE_CORS:
        return

    @app.middleware("http")
    async def cors_check(request: Request, call_next):
        origin = request.headers.get("origin", "")
        if origin and origin not in config.ALLOWED_ORIGIN:
            return JSONResponse(status_code=403, content={"message": "Not allowed", "data": {}})
        return await call_next(request)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.ALLOWED_ORIGIN,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
