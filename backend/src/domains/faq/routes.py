from fastapi import APIRouter

from .handler import get_faqs

router = APIRouter()

router.add_api_route("", get_faqs, methods=["GET"])
