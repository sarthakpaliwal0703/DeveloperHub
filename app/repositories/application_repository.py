from sqlalchemy.orm import Session

from app.models.application import Application

class ApplicationRepository:
    def __init__(self, db:Session):
        self.db = db

    #This is for checking that person has applied once for job
    def get_application_by_job_and_developer(self, job_id:int, developer_id: int):
        return(
            self.db.query(Application).filter(
                Application.job_id == job_id,
                Application.developer_id == developer_id
                ).first()
        )
    
    #This is for fetching job by id
    def get_application_by_id(self, application_id:int):
        return(
            self.db.query(Application).filter(
                Application.job_id == application_id
            ).first()
        )
    
    #This is for creating application data
    def create_application(self, application: Application):
        self.db.add(application)
        self.db.commit()
        self.db.refresh(application)
        return application
    
    #This is for getting all applicants 
    def get_application_by_job_id(self, job_id:int):
        return(
            self.db.query(Application).filter(Application.job_id == job_id).all()
        )