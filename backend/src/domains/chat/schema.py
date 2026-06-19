from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str
    with_rag: bool = True


class ChatResponse(BaseModel):
    answer: str
    usage: dict
