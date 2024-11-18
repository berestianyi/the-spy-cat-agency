from pydantic import BaseModel, Field


class TargetBase(BaseModel):
    name: str = Field(..., example="Target A")
    country: str = Field(..., example="USA")
    notes: str = Field(default="", example="Initial observation notes")
    is_completed: bool = Field(default=False, example=False)


class TargetCreate(TargetBase):
    pass


class TargetUpdate(BaseModel):
    notes: str = Field(..., example="Updated observation notes")
    is_completed: bool = Field(..., example=True)


class TargetRead(TargetBase):
    id: int = Field(..., example=1)

    class Config:
        orm_mode = True