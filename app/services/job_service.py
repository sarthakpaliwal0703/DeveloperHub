from sqlalchemy.orm import Session
from fastapi import Depends

from app.schemas.job import JobCreate, JobResponse, JobUpdate
from app.core.dependencies import require_company
from app.repositories.job_repository import JobRepository 
from app.exceptions.handlers import AppException
from app.models.job import Job

class JobService:

    def __init__(self, db: Session):
        self.job_repo = JobRepository(db)

    def create_job(self, job: JobCreate, current_company):

        new_job = Job(
            title = job.title,
            description = job.description,
            location = job.location,
            salary = job.salary,
            experience = job.experience,
            skills = job.skills,
            employment_type = job.employment_type,
            company_id = current_company.id
        )
        return self.job_repo.create_job(new_job)
    
    #This is for updating specific field
    def update_specific_job(self, job_id: int, update_job: JobUpdate,current_company):
        job = self.job_repo.get_job_by_id(job_id)
        if not job:
            raise AppException(
                status_code=404,
                message="Job not found"
            )
        if job.company_id != current_company.id:
            raise AppException(
                status_code=403,
                message="You are not allowed to update this job"
            )
        # if update_job.title is not None:
        #     job.title = update_job.title
        # if update_job.description is not None:
        #     job.description = update_job.description
        # if update_job.location is not None:
        #     job.location = update_job.location
        # if update_job.salary is not None:
        #     job.salary = update_job.salary
        # if update_job.experience is not None:
        #     job.experience = update_job.experience
        # if update_job.skills is not None:
        #     job.skills = update_job.skills
        # if update_job.employment_type is not None:
        #     job.employment_type = update_job.employment_type
        # if update_job.is_active is not None:
        #     job.is_active = update_job.is_active

        #If we do not want to use this much if statements then...
        update_data = update_job.model_dump(exclude_unset = True)
        if not update_data:
            raise AppException(
                status_code=400,
                message="No fields provided for update"
            )
        for key, value in update_data.items():
            setattr(job, key, value)
        updated_job = self.job_repo.update_specific_field(job)
        return updated_job