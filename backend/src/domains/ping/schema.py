from pydantic import BaseModel


class PostPingBody(BaseModel):
    message: str
