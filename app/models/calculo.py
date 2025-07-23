from pydantic import BaseModel, Field, model_validator, ConfigDict
from typing import Optional, List, Annotated,Union
from decimal import Decimal
from enum import Enum

class PeriodoCapitalizacion(str, Enum):
    mensual = "mensual"
    trimestral = "trimestral"
    semestral = "semestral"
    anual = "anual"

class FrecuenciaAporte(str, Enum):
    mensual = "mensual"
    bimestral = "bimestral"
    trimestral = "trimestral"
    cuatrimestral = "cuatrimestral"
    semestral = "semestral"
    anual = "anual"  

class CalculoRequest(BaseModel):
    capital_inicial: Annotated[Decimal, Field(gt=0,description="Capital inicial invertido")]
    tasa_interes_anual: Annotated[Decimal, Field(gt=0, description="Tasa de interés anual en porcentaje (Ej: 10.5)")]
    anios: Annotated[int, Field(gt=0, description="Cantidad de períodos (meses o años)")] 
    tipo_capitalizacion: PeriodoCapitalizacion
    aportes_periodicos: Optional[Annotated[Decimal, Field(ge=0, description="Monto a aportar en cada período")]]
    cada_cuanto_aporta: Optional[FrecuenciaAporte] = None
    
    @model_validator(mode='after')
    def validar_dependencia_aportes(cls, values):
        if values.aportes_periodicos is not None and values.cada_cuanto_aporta is None:
            raise ValueError("Si se indica 'aportes_periodicos', también debe indicarse 'cada_cuanto_aporta'")
        if values.aportes_periodicos is None and values.cada_cuanto_aporta is not None:
            raise ValueError("No puede indicarse 'cada_cuanto_aporta' sin 'aportes_periodicos'")
        return values

    model_config = ConfigDict(
        json_schema_extra= {
            "example": {
                "capital_inicial": 10000,
                "tasa_interes_anual": 10.5,
                "anios": 20,
                "tipo_capitalizacion": "semestral",
                "aportes_periodicos": 500,
                "cada_cuanto_aporta": "mensual"
            }
        }
    )

class DetallePeriodo(BaseModel):
    anio: int
    periodo: Union[int, str]
    capital_actual: float
    interes_generado: float
    interes_acumulado: float
    monto_agregado: float

#

class CalculoResponse(BaseModel):
    capital_final: Decimal
    ganancia_total: Decimal
    detalle: Optional[List[DetallePeriodo]] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "capital_final": 25500.50,
                "ganancia_total": 5500.50,
                "detalle": [
                    {
                        "periodo": 1,
                        "anio": 1,
                        "capital_actual": 11000.00,
                        "interes_generado": 100.00,
                        "interes_acumulado": 100.00,
                        "monto_agregado": 1000.00
                    }
                ]
            }
        }
    )