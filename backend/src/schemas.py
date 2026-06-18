from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class StandardResponse(BaseModel, Generic[T]):
    message: str
    data: T
