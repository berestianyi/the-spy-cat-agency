from pydantic import BaseModel, Field, field_validator
from typing import Optional
from src.utils.breed_validator import fetch_breeds


class SpyCatBase(BaseModel):
    name: str = Field(..., example="Whiskers")
    years_of_experience: int = Field(..., example=5)
    breed: str = Field(...)
    salary: float = Field(..., example=50000.0)

    @field_validator("breed", mode="before")
    async def validate_breed(cls, value):
        allowed_breeds = await fetch_breeds()
        if value not in allowed_breeds:
            raise ValueError(f"Invalid breed '{value}'. Allowed breeds are: {', '.join(allowed_breeds)}.")
        return value


class SpyCatCreate(SpyCatBase):
    pass


class SpyCatUpdate(BaseModel):
    salary: Optional[float] = Field(None, example=60000.0)


class SpyCatRead(SpyCatBase):
    id: int = Field(..., example=1)

    class Config:
        orm_mode = True
