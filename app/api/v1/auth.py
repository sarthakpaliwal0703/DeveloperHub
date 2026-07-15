from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, TokenResponse, UserLogin
from app.services.auth_service import AuthService
from app.database import get_db

router = APIRouter(prefix='/auth', tags=['Authentication'])

#Create user route
@router.post('/register-user', response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    service = AuthService(db)
    created_user = service.register_user(user)
    return created_user

#User Login route
@router.post('/login',response_model=TokenResponse)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.login_user(user)    