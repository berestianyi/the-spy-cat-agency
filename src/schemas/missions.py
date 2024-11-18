from pydantic import BaseModel, Field
from typing import List, Optional
from src.schemas.targets import TargetCreate, TargetRead


class MissionBase(BaseModel):
    is_completed: bool = Field(default=False, example=False)


class MissionCreate(MissionBase):
    targets: List[TargetCreate] = Field(..., min_items=1, max_items=3)


class MissionUpdate(BaseModel):
    is_completed: Optional[bool] = Field(None, example=True)


class MissionRead(MissionBase):
    id: int = Field(..., example=1)
    targets: List[TargetRead]

    class Config:
        orm_mode = True
