from pydantic import BaseModel, ConfigDict
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