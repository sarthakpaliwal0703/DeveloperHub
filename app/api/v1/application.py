from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.application import ApplicationResponse, ApplicationCreate, ApplicationDetailsResponse, ApplicationStatusUpdate
from app.database import get_db
from app.core.dependencies import required_developer, require_company
from app.services.application_service import ApplicationService

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("/apply", response_model=ApplicationResponse)
def create_application(application: ApplicationCreate, current_developer = Depends(required_developer), db: Session = Depends(get_db)):
    service = ApplicationService(db)
    return service.apply_job(application, current_developer)

@router.get('/job/{job_id}', response_model=List[ApplicationDetailsResponse])
def get_applications(job_id: int, current_company = Depends(require_company), db: Session = Depends(get_db)):
    service = ApplicationService(db)
    return service.get_applications_by_job(job_id, current_company)

#Route for updating status
@router.patch("/{application_id}/status", response_model=ApplicationResponse)
def update_status(application_id: int, status_update: ApplicationStatusUpdate, current_company = Depends(require_company), db: Session = Depends(get_db)):
    service = ApplicationService(db)
    return service.update_status(application_id, current_company, status_update)