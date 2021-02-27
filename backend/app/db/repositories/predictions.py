from .base import BaseRepository
from ...models.predictions import Prediction, PredictionsList


GET_PREDICTIONS_QUERY = """
    select
        mf.player_id
        , mf.game_id
        , mf.team_id
        , case
            when mf.team_id = gm.hometeam_id then gm.awayteam_id
            when mf.team_id = gm.awayteam_id then gm.hometeam_id
            end as opponent_team_id
        , pl.firstname as first_name
        , pl.lastname as last_name
        , gm.starttime at time zone 'EST' as start_time
        , case
            when mf.team_id = gm.hometeam_id then gm.hometeam_abbreviation
            when mf.team_id = gm.awayteam_id then gm.awayteam_abbreviation
            end as team_abbr
        , case
            when mf.team_id = gm.hometeam_id then gm.awayteam_abbreviation
            when mf.team_id = gm.awayteam_id then gm.hometeam_abbreviation
            end as opponent_team_abbr
        , case
            when mf.team_id = gm.hometeam_id then 'home'
            when mf.team_id = gm.awayteam_id then 'away'
            end as home_away
        , mf.prediction
    from public.dfs_model_features as mf
    left join public.games as gm
        on gm.id = mf.game_id
    left join public.players as pl
        on pl.id = mf.player_id
    order by mf.game_id, mf.team_id, pl.firstname
    ;
"""


class PredictionsRepository(BaseRepository):
    async def get_predictions(self) -> PredictionsList:
        predictions = await self.db.fetch_all(query=GET_PREDICTIONS_QUERY)
        return PredictionsList(predictions=[Prediction(**p) for p in predictions])