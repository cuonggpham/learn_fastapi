# app/core/exception_handler.py

from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions import CustomException

def register_exception_handlers(app):
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.message},
        )
