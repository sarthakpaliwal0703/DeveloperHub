from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.exceptions.handlers import AppException, exception_handler

app = FastAPI()

app.add_exception_handler(AppException, exception_handler)

app.include_router(auth_router)

