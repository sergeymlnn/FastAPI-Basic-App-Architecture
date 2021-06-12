import logging.config

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.settings import settings


app = FastAPI(version=settings.api_version)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
logger = logging.getLogger(__name__)


@app.on_event("startup")
async def startup_event():
    """On application startup"""
    logging.config.dictConfig(settings.logger_config)


@app.on_event("shutdown")
async def app_shutdown():
    """On application shutdown"""
    pass


@app.get("/version")
async def _version():
    """"""
    return {"API Version": app.version}



@app.get("/health")
async def _health():
    """"""
    return {"Response": "OK"}



@app.get("/")
async def main():
    """"""
    return {"message": "Hello, World!"}



@app.get("/test")
async def test():
    """Route for different tests"""
    return {"message": "Test Route"}