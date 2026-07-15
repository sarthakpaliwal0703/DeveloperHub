from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime
from datetime import datetime, UTC
from app.database import Base

class BaseModel(Base):
    __abstract__ = True # If we don't want to make table of this model
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
        ) 

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default= lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC)
        )