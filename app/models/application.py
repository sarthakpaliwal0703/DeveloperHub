from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey

from app.models.base_model import BaseModel
from app.core.enums import ApplicationStatus

class Application(BaseModel):
    __tablename__ = "applications"

    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id"),nullable=False)
    developer_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)
    resume: Mapped[str] = mapped_column(nullable=False)
    cover_letter: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[ApplicationStatus] = mapped_column(
    default=ApplicationStatus.PENDING
    )

    job = relationship("Job",
                       back_populates="applications")
    developer = relationship("User",
                        back_populates="applications")