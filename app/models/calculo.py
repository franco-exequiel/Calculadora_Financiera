from pydantic import BaseModel, Field
from enum import Enum

class FrecuenciaCapitalizacion(str, Enum):
    anual = "anual"
    semestral = "semestral"
    trimestral = "trimestral"
    mensual = "mensual"
    diaria = "diaria"

class FrecuenciaExtra(str, Enum):
    anual = "anual"
    mensual = "mensual"
    trimestral = "trimestral"
    ninguna = "ninguna"

class CalculoRequest(BaseModel):
    capital_inicial: float = Field(..., gt=0)
    interes_anual: float = Field(..., gt=0)
    duracion_anios: float = Field(..., gt=0)
    frecuencia_capitalizacion: FrecuenciaCapitalizacion
    agregado_extra: float = Field(default=0.0, ge=0)
    frecuencia_agregado: FrecuenciaExtra = FrecuenciaExtra.ninguna

class CalculoResponse(BaseModel):
    monto_final: float
    detalle: list[dict]  # Puede ajustarse a un modelo futuro