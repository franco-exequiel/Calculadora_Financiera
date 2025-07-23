from fastapi import APIRouter
from app.models.calculo import CalculoRequest, CalculoResponse
from app.services.calculadora import calcular_interes_compuesto

router = APIRouter()

@router.post("/calcular", response_model=CalculoResponse)
def calcular(data: CalculoRequest):
    
    resultado = calcular_interes_compuesto(data)
    return resultado