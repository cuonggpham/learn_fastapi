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

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",  
    "http://localhost",       
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          
    allow_credentials=True,         
    allow_methods=["*"],           
    allow_headers=["*"],            
)