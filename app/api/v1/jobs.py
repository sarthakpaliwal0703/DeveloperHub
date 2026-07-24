from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.job import JobCreate, JobResponse, JobUpdate
from app.services.job_service import JobService
from app.database import get_db
from app.core.dependencies import require_company

router = APIRouter(prefix='/jobs', tags=['Jobs'])

@router.post('/create-job', response_model=JobResponse)
def create_job(job: JobCreate, current_company = Depends(require_company), db: Session = Depends(get_db)):
    service = JobService(db)
    return service.create_job(job, current_company)

#This is for updating specific job field
@router.patch('/jobs/{job_id}', response_model=JobResponse)
def update_specific_field(job_id: int, update_job: JobUpdate, current_company = Depends(require_company), db: Session = Depends(get_db)):
    service = JobService(db)
    return service.update_specific_job(job_id, update_job, current_company)