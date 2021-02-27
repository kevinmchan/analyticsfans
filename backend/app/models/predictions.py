from .core import CoreModel
from typing import List, Optional
from datetime import datetime


class Prediction(CoreModel):
    player_id: int
    game_id: int
    team_id: int
    opponent_team_id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    start_time: Optional[datetime] = None
    team_abbr: Optional[str] = None
    opponent_team_abbr: Optional[str] = None
    home_away: Optional[str] = None
    prediction: Optional[float] = None


class PredictionsList(CoreModel):
    predictions: List[Prediction]