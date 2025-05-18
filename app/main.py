from fastapi import FastAPI
from app.api.endpoints.v1 import calculadora, exportar

app = FastAPI(
    title="API Calculadora Financiera",
    version="0.1.0"
)

app.include_router(calculadora.router, prefix="/api/v1", tags=["calculadora"])
app.include_router(exportar.router, prefix="/api/v1", tags=["exportar"])