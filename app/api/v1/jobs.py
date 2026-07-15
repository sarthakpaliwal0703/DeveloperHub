from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.job import JobCreate, JobResponse
from app.services.job_service import JobService
from app.database import get_db
from app.core.dependencies import require_company

router = APIRouter(prefix='/jobs', tags=['Jobs'])

@router.post('/create-job', response_model=JobResponse)
def create_job(job: JobCreate, current_company = Depends(require_company), db: Session = Depends(get_db)):
    service = JobService(db)
    return service.create_job(job, current_company)