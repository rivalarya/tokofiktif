from pydantic import BaseModel


class FaqItem(BaseModel):
    id: int
    category: str
    question: str
    answer: str
