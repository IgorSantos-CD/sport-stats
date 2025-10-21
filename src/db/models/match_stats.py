from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.db.base import Base

class MatchStat(Base):
    __tablename__ = "match_stats"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=False, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False, index=True)

    possession = Column(Float, nullable=True)
    shots_on_target = Column(Integer, nullable=True)
    shots_off_target = Column(Integer, nullable=True)
    corners = Column(Integer, nullable=True)
    tackles = Column(Integer, nullable=True)  # desarmes
    expected_goals = Column(Float, nullable=True)
    yellow_cards = Column(Integer, nullable=True)
    red_cards = Column(Integer, nullable=True)

    match = relationship("Match", back_populates="stats")