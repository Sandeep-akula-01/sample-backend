import os

from fastapi import APIRouter

router = APIRouter()

APP_NAME = os.getenv("APP_NAME", "sample-backend")
APP_ENV = os.getenv("APP_ENV", "development")
APP_VERSION = os.getenv("APP_VERSION", "0.0.0")


@router.get("/api/v1/health")
async def health():
    return {"status": "healthy"}


@router.get("/api/v1/version")
async def version():
    return {
        "application": APP_NAME,
        "environment": APP_ENV,
        "version": APP_VERSION,
    }
