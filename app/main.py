# app/main.py

from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.exception_handler import register_exception_handlers

app = FastAPI()
app.include_router(api_router)
register_exception_handlers(app) 

@app.get("/ping")
def ping():
    return {"message": "pong"}
