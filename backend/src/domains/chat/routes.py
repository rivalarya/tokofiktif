from fastapi import APIRouter

from .handler import chat
from .schema import ChatRequest, ChatResponse

router = APIRouter()

router.add_api_route("", chat, methods=["POST"], response_model=ChatResponse)
