from sqlalchemy.orm import mapped_column, Mapped

from app.models.base_model import BaseModel
from app.core.enums import ApplicationStatus

class Application(BaseModel):
    __tablename__ = "applications"

    job_id: Mapped[int] = mapped_column(nullable=False)
    developer_id: Mapped[int] = mapped_column(nullable=False)
    resume: Mapped[str] = mapped_column(nullable=False)
    cover_letter: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[ApplicationStatus] = mapped_column(
    default=ApplicationStatus.PENDING
)