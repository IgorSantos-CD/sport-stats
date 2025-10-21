from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from src.db.base import Base

class EventType:
    GOAL = "goal"
    YELLOW = "yellow_card"
    RED = "red_card"
    SUB = "substitution"

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=False)
    minute = Column(Integer, nullable=True)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=True)
    player_name = Column(String(100), nullable=True)
    event_type = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)

    match = relationship("Match", back_populates="events")