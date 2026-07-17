from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.application import ApplicationResponse, ApplicationCreate
from app.database import get_db
from app.core.dependencies import required_developer
from app.services.application_service import ApplicationService

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("/apply", response_model=ApplicationResponse)
def create_application(application: ApplicationCreate, current_developer = Depends(required_developer), db: Session = Depends(get_db)):
    service = ApplicationService(db)
    return service.apply_job(application, current_developer)