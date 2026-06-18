from fastapi import APIRouter

from src.schemas import StandardResponse

from .handler import get_ping, post_ping

router = APIRouter()

router.add_api_route("/ping", get_ping, methods=["GET"], response_model=StandardResponse)
router.add_api_route("/ping", post_ping, methods=["POST"], response_model=StandardResponse)
