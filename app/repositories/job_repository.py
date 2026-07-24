from sqlalchemy.orm import Session

from app.models.job import Job

class JobRepository:

    def __init__(self, db:Session):
        self.db = db

    def get_all_jobs(self):
        return(
            self.db.query(Job).all()
        )

    def get_job_by_id(self, job_id: int):
        return(
            self.db.query(Job).filter(Job.id == job_id).first()
        )

    def create_job(self, job:Job):
       self.db.add(job)
       self.db.commit()
       self.db.refresh(job)
       return job
    
    #This is for updating a specific field in job
    def update_specific_field(self, job:Job):
        self.db.commit()
        self.db.refresh(job)
        return job