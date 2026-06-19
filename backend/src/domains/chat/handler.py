from src.utils.generator import generate

from .schema import ChatRequest, ChatResponse


async def chat(body: ChatRequest) -> ChatResponse:
    result = generate(body.question, body.with_rag)
    return ChatResponse(answer=result["content"], usage=result.get("usage", {}))
