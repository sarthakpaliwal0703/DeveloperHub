from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse, TokenResponse, UserLogin
from app.services.auth_service import AuthService
from app.database import get_db
from app.core.dependencies import get_current_user

router = APIRouter(prefix='/auth', tags=['Authentication'])

#Create user route
@router.post('/register-user', response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    service = AuthService(db)
    created_user = service.register_user(user)
    return created_user

#User Login route
@router.post('/login',response_model=TokenResponse)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.login_user(form_data)    

#Get profile route
@router.get('/me', response_model=UserResponse)
def get_my_profile(current_user = Depends(get_current_user)):
    return current_user