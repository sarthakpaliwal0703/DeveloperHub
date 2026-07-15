# Contain all authentication dependencies
#like get_current_user(), get_current_admin()

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.core.security import decode_access_token
from app.repositories.user_repository import UserRepository
from app.exceptions.handlers import AppException
from app.core.enums import UserRole

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Current user nikalne ke liye
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    repo = UserRepository(db)
    current_user = decode_access_token(token)
    user_id = current_user.get("id")    
    user = repo.get_user_by_id(user_id)
    if not user:
        raise AppException(
            status_code=401,
            message="Unauthorized"
        )
    return user

def require_company(current_user = Depends(get_current_user)):
    if current_user.role != UserRole.COMPANY:
        raise AppException(
            status_code=403,
            message="Only company can perform this action"
        )
    return current_user