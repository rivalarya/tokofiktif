from src.schemas import StandardResponse

from .schema import PostPingBody


async def get_ping() -> StandardResponse:
    return StandardResponse(message="Pong", data={})


async def post_ping(body: PostPingBody) -> StandardResponse:
    return StandardResponse(message=body.message, data={})
