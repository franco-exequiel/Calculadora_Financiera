from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints.v1 import calculadora, exportar

app = FastAPI(
    title="API Calculadora Financiera",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Podés usar ["*"] en desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calculadora.router, prefix="/api/v1", tags=["calculadora"])
app.include_router(exportar.router, prefix="/api/v1", tags=["exportar"])