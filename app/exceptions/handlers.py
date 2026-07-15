from fastapi import Request
from fastapi.responses import JSONResponse

class AppException(Exception):
    def __init__(self, message:str, status_code:int):
        self.message = message
        self.status_code = status_code

async def exception_handler(request: Request, ecx: AppException):
    return JSONResponse(
        status_code= ecx.status_code,
        content={
            "error": ecx.message
        }
    )