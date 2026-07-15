from sqlalchemy.orm import Session
from fastapi import Depends

from app.schemas.job import JobCreate, JobResponse
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