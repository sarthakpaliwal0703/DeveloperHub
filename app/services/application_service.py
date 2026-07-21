from sqlalchemy.orm import Session

from app.repositories.application_repository import ApplicationRepository
from app.repositories.job_repository import JobRepository
from app.schemas.application import ApplicationCreate, ApplicationDetailsResponse, ApplicationStatusUpdate
from app.exceptions.handlers import AppException
from app.models.application import Application
from app.core.enums import ApplicationStatus

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
    

    #This route is for getting all applicants using job id who applied for a particular job 
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
        response = []
        applications = self.application_repo.get_application_by_job_id(job_id)
        for application in applications:
            response.append(
                ApplicationDetailsResponse(
                    id = application.id,
                    resume = application.resume,
                    cover_letter = application.cover_letter,
                    status = application.status,
                    developer_id = application.developer_id,
                    developer_name = application.developer.full_name,
                    developer_email = application.developer.email,
                    created_at = application.created_at,
                    updated_at = application.updated_at
                )
            )
        return response
    
    #This is for updating status 
    def update_status(self,application_id:int,current_company, status_update: ApplicationStatusUpdate):
        application = self.application_repo.get_application_by_id(application_id)
        if not application:
            raise AppException(
                status_code=404,
                message="Application not found"
            )
        if application.job.company_id != current_company.id:
            raise AppException(
                status_code=403,
                message="You are not allowed to view these applications"
            )
        if application.status == status_update.status:
            raise AppException(
                status_code=400,
                message=f"Application is already {application.status.value.lower()}"
            )
        application.status = status_update.status
        updated_application = self.application_repo.update_application(application)

        return updated_application