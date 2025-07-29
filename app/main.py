from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints.v1 import calculadora, exportar
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title="API Calculadora Financiera",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ["http://localhost:5500"] Podés usar ["*"] en desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calculadora.router, prefix="/api/v1", tags=["calculadora"])
app.include_router(exportar.router, prefix="/api/v1", tags=["exportar"])
app.mount("/", StaticFiles(directory="app/frontend", html=True), name="frontend")

# Servir frontend y archivos estáticos
app.mount("/static", StaticFiles(directory="app/frontend/statics"), name="static")
