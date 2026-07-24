from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated, Optional
from datetime import datetime

from app.core.enums import EmploymentType

class JobCreate(BaseModel):
    title: Annotated[str, Field(min_length=5, max_length=100)]
    description: str
    location: str
    salary: Annotated[float, Field(gt=0)]
    experience: Annotated[int, Field(ge=0)]
    skills: str
    employment_type: EmploymentType

class JobResponse(BaseModel):
    id: int
    title: Annotated[str, Field(min_length=5, max_length=100)]
    description: str
    location: str
    salary: Annotated[float, Field(gt=0)]
    experience: Annotated[int, Field(ge=0)]
    skills: str
    employment_type: EmploymentType
    is_active: bool
    company_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )

#This is for updating specific field in a job
class JobUpdate(BaseModel):
    title: Annotated[Optional[str], Field(min_length=5, max_length=100)] = None
    description: Optional[str] = None
    location: Optional[str] = None
    salary: Annotated[Optional[float], Field(gt=0)] = None
    experience: Annotated[Optional[int], Field(ge=0)] = None
    skills: Optional[str] = None
    employment_type: Optional[EmploymentType] = None
    is_active: Optional[bool] = None