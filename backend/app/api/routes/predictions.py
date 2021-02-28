from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_predictions() -> List[dict]:
    predictions = [
        {"game_id": 1, "player_id": 1, "team_id": 1, "prediction": 30},
        {"game_id": 2, "player_id": 2, "team_id": 2, "prediction": 20},
    ]
    return predictions
