from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.config import config
from src.middlewares import register_cors, register_rate_limiter
from src.utils import register_all_routes

app = FastAPI()

register_rate_limiter(app)
register_cors(app)
register_all_routes(app)


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422, content={"message": "A validation error occurred", "data": exc.errors()}
    )


@app.exception_handler(Exception)
async def generic_error_handler(request: Request, exc: Exception):
    from fastapi import HTTPException

    if isinstance(exc, HTTPException):
        message = exc.detail if config.APP_ENV != "production" else "An error occurred"
        return JSONResponse(status_code=exc.status_code, content={"message": message, "data": {}})
    message = str(exc) if config.APP_ENV != "production" else "An error occurred"
    return JSONResponse(status_code=500, content={"message": message, "data": {}})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host="0.0.0.0", port=config.PORT, reload=True)
