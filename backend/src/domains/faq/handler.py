import json
import os

from fastapi.responses import JSONResponse

from src.utils import config


async def get_faqs() -> JSONResponse:
    faq_path = os.path.join(config.DATA_DIR, "faq.json")
    with open(faq_path, encoding="utf-8") as f:
        faqs = json.load(f)
    return JSONResponse(content=faqs)
