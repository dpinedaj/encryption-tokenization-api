from pydantic import BaseModel
from typing import Union, List, Any


class EncryptInput(BaseModel):
    value: Any

class EncryptOutput(BaseModel):
    value: Union[str, List[Any], int, bool]

