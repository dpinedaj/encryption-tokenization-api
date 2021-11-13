from hashlib import new
from fastapi import APIRouter
from typing import Dict, Any
from service.core.libs.commons import validate_value
from service.core.models.encrypt import (
    EncryptInput, EncryptOutput
)
from service.core.libs.encrypt_lib import (
    encrypt_text, decrypt_text
)
from service.core.handlers import KeyHandler


router = APIRouter()

def IApi(service: str, value: Any) -> str:
    keys = KeyHandler()
    key = keys.encryption_key
    iv = keys.encryption_iv
    value = validate_value(value)
    if not value or len(value) == 0:
        return value

    if service == 'encrypt':
        return [encrypt_text(val, iv, key) for val in value]\
            if type(value) in (list, tuple) \
            else encrypt_text(value, iv, key)
    elif service == 'decrypt':
        return [decrypt_text(val, iv, key) for val in value]\
            if type(value) in (list, tuple) \
            else decrypt_text(value, iv, key)


@router.post("/encrypt", response_model=EncryptOutput, tags=["Encrypt Post"])
def encrypt_endpoint(body: EncryptInput) -> Dict[Any, Any]:
    value = body.value
    service = "encrypt"
    new_value = IApi(service, value)

    return EncryptOutput(value=new_value)


@router.post("/decrypt", response_model=EncryptOutput, tags=["Decrypt Post"])
def encrypt_endpoint(body: EncryptInput) -> Dict[Any, Any]:
    value = body.value
    service = "decrypt"
    new_value = IApi(service, value)

    return EncryptOutput(value=new_value)
