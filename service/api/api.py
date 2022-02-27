from fastapi import APIRouter

from .endpoints.encrypt import router as encrypt_router
from .endpoints.tokenize import router as tokenize_router


router = APIRouter()
router.include_router(encrypt_router)
router.include_router(tokenize_router)
