from typing import List
from fastapi import APIRouter, Depends

from ..dependencies.database import get_repository
from ...db.repositories.predictions import PredictionsRepository
from ...models.predictions import PredictionsList


router = APIRouter()


@router.get("/latest", response_model=PredictionsList, name="predictions:get-predictions")
async def get_latest_predictions(
    predictions_repo: PredictionsRepository = Depends(get_repository(PredictionsRepository)),
) -> PredictionsList:
    predictions = await predictions_repo.get_predictions()
    return predictions