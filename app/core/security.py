from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, UTC
from app.core.config import settings
from app.exceptions.handlers import AppException

#Password Hashing and Verifying
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)


#Creating Access token
def create_access_token(data:dict):
    data = data.copy()

    expire = datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    data.update({"exp": expire})

    token = jwt.encode(
        data,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return token

def decode_access_token(token:str):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        user_id = payload.get("id")
        if user_id is None:
            raise AppException(
                status_code=401,
                message="Invalid or Expired token"
            )
        username = payload.get("username")
        role = payload.get("role")
        token_type = payload.get("type")
        return{
            "id": user_id,
            "username": username,
            "role": role,
            "type": token_type
        }
    except JWTError:
        raise AppException(
            status_code=401,
            message="Invalid or Expired token"
        )

