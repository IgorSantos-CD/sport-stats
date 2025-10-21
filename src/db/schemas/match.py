from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from src.db.models.match import MatchStatus

class MatchBase(BaseModel):
    match_date: datetime
    competition: Optional[str] = None
    venue: Optional[str] = None

class MatchCreate(MatchBase):
    home_team_id: int
    away_team_id: int

class MatchOut(MatchBase):
    id: int
    home_team_id: int
    away_team_id: int
    status: MatchStatus
    home_score: Optional[int] = None
    away_score: Optional[int] = None
    created_at: datetime

    class Config:
        orm_mode = True