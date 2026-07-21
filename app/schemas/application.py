from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime

from app.core.enums import ApplicationStatus

class ApplicationCreate(BaseModel):
    job_id: int
    resume: str
    cover_letter: str

class ApplicationResponse(BaseModel):
    id: int
    job_id: int
    developer_id: int
    resume: str
    cover_letter: str
    status: ApplicationStatus
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )

class ApplicationDetailsResponse(BaseModel):
    id: int
    resume: str
    cover_letter: str
    status: ApplicationStatus
    developer_id: int
    developer_name: str
    developer_email: EmailStr
    created_at: datetime
    updated_at: datetime

class ApplicationStatusUpdate(BaseModel):
    status: ApplicationStatus


#This is for seeing all application(job applied) by a developer
class AllApplicationResponse(BaseModel):
    title: str
    full_name: str
    status: ApplicationStatus
    created_at: datetime