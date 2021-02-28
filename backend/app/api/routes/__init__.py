from fastapi import APIRouter
from .predictions import router as predictions_router


router = APIRouter()

router.include_router(
    predictions_router,
    prefix="/predictions",
    tags=["predictions"],
)
