#This model is for jobs
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseModel
from app.core.enums import EmploymentType

class Job(BaseModel):
    __tablename__ = "jobs"

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    salary: Mapped[float] = mapped_column(nullable=False)
    experience: Mapped[int] = mapped_column(nullable=False)
    skills: Mapped[str] = mapped_column(nullable=False)
    employment_type: Mapped[EmploymentType] = mapped_column(nullable=False)
    is_active: Mapped[bool]= mapped_column(default=True)
    company_id: Mapped[int] = mapped_column(nullable=False)
