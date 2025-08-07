import pytest
from decimal import Decimal
from app.models.calculo import CalculoRequest, PeriodoCapitalizacion, FrecuenciaAporte

@pytest.fixture
def calculo_request_valido():
    return CalculoRequest(
        capital_inicial=Decimal("10000"),
        tasa_interes_anual=Decimal("12"),
        anios=10,
        tipo_capitalizacion=PeriodoCapitalizacion.semestral,
        aportes_periodicos=Decimal("1000"),
        cada_cuanto_aporta=FrecuenciaAporte.semestral
    )

@pytest.fixture
def payload_valido():
    return {
        "capital_inicial": 10000,
        "tasa_interes_anual": 12,
        "anios": 10,
        "tipo_capitalizacion": "semestral",
        "aportes_periodicos": 1000,
        "cada_cuanto_aporta": "semestral"
    }