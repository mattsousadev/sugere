
from typing import Any
from pydantic import BaseModel


class BaseResponse(BaseModel):
    success:bool = True
    data: Any
