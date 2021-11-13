from fastapi import APIRouter
from service.core.models.tokenize import (
    TokenizeInput, TokenizeOutput
)
from service.core.libs.commons import validate_value
from service.core.libs.tokenize_lib import (
    tokenize_values, detokenize_values
)


router = APIRouter()

@router.post("/tokenize", response_model=TokenizeOutput, tags=["Tokenize Post"])
def tokenize_endpoint(body: TokenizeInput):
    value = validate_value(body.value)
    table_name = body.table_name
    result = tokenize_values(value, table_name)
    result = [{"value": val[0], "token": val[1]} for val in result]
    return TokenizeOutput(value=result)

@router.post("/detokenize", response_model=TokenizeOutput, tags=["Detokenize Post"])
def detokenize_endpoint(body: TokenizeInput):
    value = validate_value(body.value)
    table_name = body.table_name
    result = detokenize_values(value, table_name)
    result = [{"value": val[0], "token": val[1]} for val in result]
    return TokenizeOutput(value=result)
