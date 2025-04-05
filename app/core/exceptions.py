# app/core/exceptions.py

class CustomException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code


class ResourceNotFoundException(CustomException):
    def __init__(self, resource: str = "Resource"):
        super().__init__(message=f"{resource} not found", status_code=404)
