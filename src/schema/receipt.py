
from typing import Any, Optional
from pydantic import BaseModel


class BaseResponse(BaseModel):
    success:bool = True
    data: Any


class ReceiptSchema(BaseModel):
    id: int
    description: Optional[str]
    quantity: Optional[float]
    unit: Optional[str]
    unit_value: Optional[float]
    value: Optional[float]