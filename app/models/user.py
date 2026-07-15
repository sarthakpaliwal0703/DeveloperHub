from sqlalchemy.orm import Mapped, mapped_column
from app.models.base_model import BaseModel
from app.core.enums import UserRole
from typing import Optional


class User(BaseModel):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    full_name: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[UserRole] = mapped_column(default=UserRole.DEVELOPER)
    bio: Mapped[Optional[str]] = mapped_column(nullable=True)
    profile_image: Mapped[str] = mapped_column(default="default-avatar.png")
    is_active: Mapped[bool] = mapped_column(default=True)
    is_verified: Mapped[bool] = mapped_column(default=False)