from pydantic import BaseModel
from typing import Optional

class MatchStatBase(BaseModel):
    possession: Optional[float]
    shots_on_target: Optional[int]
    shots_off_target: Optional[int]
    corners: Optional[int]
    tackles: Optional[int]
    expected_goals: Optional[float]
    yellow_cards: Optional[int]
    red_cards: Optional[int]

class MatchStatCreate(MatchStatBase):
    match_id: int
    team_id: int

class MatchStatOut(MatchStatBase):
    id: int

    class Config:
        orm_mode = True