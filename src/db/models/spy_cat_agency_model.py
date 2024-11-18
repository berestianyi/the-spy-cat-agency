from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.db.config import Base


class SpyCat(Base):
    __tablename__ = "spy_cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    years_of_experience = Column(Integer, nullable=False)
    breed = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

    missions = relationship("Mission", back_populates="spy_cat")


class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer, ForeignKey("spy_cats.id"), nullable=True)
    is_completed = Column(Boolean, default=False)

    spy_cat = relationship("SpyCat", back_populates="missions")
    targets = relationship("Target", back_populates="mission")


class Target(Base):
    __tablename__ = "targets"

    id = Column(Integer, primary_key=True, index=True)
    mission_id = Column(Integer, ForeignKey("missions.id"), nullable=False)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False)

    mission = relationship("Mission", back_populates="targets")