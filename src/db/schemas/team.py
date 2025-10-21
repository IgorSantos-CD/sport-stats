from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TeamBase(BaseModel):
    name: str
    country: Optional[str] = None
    founded_year: Optional[int] = None

class TeamCreate(TeamBase):
    pass

class TeamOut(TeamBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True