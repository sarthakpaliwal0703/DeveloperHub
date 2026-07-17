from sqlalchemy.orm import Session

from app.models.application import Application

class ApplicationRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_application_by_job_and_developer(self, job_id:int, developer_id: int):
        return(
            self.db.query(Application).filter(
                Application.job_id == job_id,
                Application.developer_id == developer_id
                ).first()
        )
    
    def get_application_by_id(self, application_id:int):
        return(
            self.db.query(Application).filter(
                Application.job_id == application_id
            ).first()
        )
    
    def create_application(self, application: Application):
        self.db.add(application)
        self.db.commit()
        self.db.refresh(application)
        return application