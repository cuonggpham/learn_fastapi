from fastapi import FastAPI
from app.core.init_app import startup_event, shutdown_event
from app.core.config import settings
from app.api.v1.api import api_router

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup():
    await startup_event()

@app.on_event("shutdown")
async def shutdown():
    await shutdown_event()

app.include_router(api_router, prefix=settings.API_V1_STR)
