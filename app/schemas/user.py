from pydantic import BaseModel, EmailStr, Field, model_validator, ConfigDict
from typing import Annotated, Optional
from app.core.enums import UserRole
from datetime import datetime

#For Register (New User)
class UserCreate(BaseModel):
    username: Annotated[str, Field(min_length=5, max_length=30)]
    email: EmailStr
    password: Annotated[str, Field(min_length=8)]
    confirm_password: Annotated[str, Field(min_length=8)]
    full_name: str

    @model_validator(mode="after")
    def check_password(self):
        if self.password != self.confirm_password:
            raise ValueError(
                "Password do not match!!"
            )
        return self
    
#For User Login 
class UserLogin(BaseModel):
    email: EmailStr
    password: Annotated[str, Field(min_length=8)]

#For Giving Response of user information
class UserResponse(BaseModel):
    id: int
    username: Annotated[str, Field(min_length=5, max_length=30)]
    email: EmailStr
    full_name: str
    role: UserRole
    bio: Optional[str]
    profile_image: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )

#For token response
class TokenResponse(BaseModel):
    access_token: str
    token_type: str