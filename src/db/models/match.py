from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, func
from sqlalchemy.orm import relationship 
import enum
from src.db.base import Base

class MatchStatus(str, enum.Enum):
    scheduled = "scheduled"
    live = "live"
    finished = "finished"

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    home_team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    away_team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    match_date = Column(DateTime(timezone=True), nullable=False)
    competition = Column(String(100), nullable=True)
    venue = Column(String(100), nullable=True)
    status = Column(Enum(MatchStatus), default=MatchStatus.scheduled, nullable=False)
    home_score = Column(Integer, nullable=True)
    away_score = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    home_team = relationship("Team", foreign_keys=[home_team_id], lazy="joined")
    away_team = relationship("Team", foreign_keys=[away_team_id], lazy="joined")
    events = relationship("Event", back_populates="match", cascade="all, delete-orphan")
    stats = relationship("MatchStat", back_populates="match", cascade="all, delete-orphan")