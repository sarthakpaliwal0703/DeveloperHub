from sqlalchemy.orm import Session

from app.repositories.application_repository import ApplicationRepository
from app.repositories.job_repository import JobRepository
from app.schemas.application import ApplicationCreate, ApplicationResponse
from app.exceptions.handlers import AppException
from app.models.application import Application

class ApplicationService:
    def __init__(self, db: Session):
        self.application_repo = ApplicationRepository(db)
        self.job_repo = JobRepository(db)

    def apply_job(self, application: ApplicationCreate, current_developer):
        job = self.job_repo.get_job_by_id(application.job_id)
        if not job:
            raise AppException(
                status_code=404,
                message="Job not found"
            )

        existing_application = self.application_repo.get_application_by_job_and_developer(
            application.job_id,
            current_developer.id
        )
        if existing_application:
            raise AppException(
                status_code= 400,
                message="You have already applied for this position."
            )
        
        new_application = Application(
            job_id = application.job_id,
            developer_id = current_developer.id,
            resume = application.resume,
            cover_letter = application.cover_letter,
        )
        
        return self.application_repo.create_application(new_application)
    
    def get_applications_by_job(self, job_id: int, current_company):
        job = self.job_repo.get_job_by_id(job_id)
        if not job:
            raise AppException(
                status_code=404,
                message="Job not found"
            )
        if job.company_id != current_company.id:
            raise AppException(
                status_code=403,
                message="You are not allowed to view these applications"
            )
        applications = self.application_repo.get_application_by_job_id(job_id)

        return applications