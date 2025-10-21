from pydantic import BaseModel
from typing import Optional

class EventCreate(BaseModel):
    match_id: int
    minute: Optional[int]
    team_id: Optional[int]
    player_name: Optional[str]
    event_type: str
    description: Optional[str]

class EventOut(EventCreate):
    id: int

    class Config:
        orm_mode = True

