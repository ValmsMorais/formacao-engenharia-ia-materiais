from fastapi import FastAPI
from app.routers import status

app = FastAPI(title="API de Transações", version="1.0.0")
app.include_router(status.router, prefix="/api/v1")
