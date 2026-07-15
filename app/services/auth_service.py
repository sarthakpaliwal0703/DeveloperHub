from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.user import UserCreate, UserLogin
from app.exceptions.handlers import AppException

class AuthService:
    
    def __init__(self, db:Session):
        self.user_repo = UserRepository(db)


    def register_user(self, user: UserCreate):
        existing_email = self.user_repo.get_user_by_email(user.email)
        if existing_email:
            raise AppException(
                status_code=409,
                message="Email already exists"
            )
        existing_username = self.user_repo.get_user_by_username(user.username)
        if existing_username:
            raise AppException(
                status_code=409,
                message="Username already exists"
            )
        
        hashed_password = hash_password(user.password)

        new_user = User(
            username = user.username,
            email = user.email,
            hashed_password = hashed_password,
            full_name = user.full_name
        )
        
        return self.user_repo.create_user(new_user)
    
    def login_user(self, user: UserLogin):
        verify_user = self.user_repo.get_user_by_email(user.email)
        if not verify_user:
            raise AppException(
                status_code=401,
                message="Invalid email or password"
            )
        if not verify_password(user.password, verify_user.hashed_password):
            raise AppException(
                status_code=401,
                message="Invalid email or password"
            )
        
        token = create_access_token(
            {
                "id": verify_user.id,
                "username": verify_user.username,
                "role": verify_user.role.value,
                "type": "access"
            }
        )

        return{
            "access_token": token,
            "token_type": "bearer"
        }