import pytest
from decimal import Decimal
from app.models.calculo import CalculoRequest, PeriodoCapitalizacion, FrecuenciaAporte

def test_validacion_correcta_con_aportes():
    req = CalculoRequest(
        capital_inicial=Decimal("10000"),
        tasa_interes_anual=Decimal("10"),
        anios=5,
        tipo_capitalizacion=PeriodoCapitalizacion.mensual,
        aportes_periodicos=Decimal("500"),
        cada_cuanto_aporta=FrecuenciaAporte.mensual
    )
    assert req.aportes_periodicos == Decimal("500")
    assert req.cada_cuanto_aporta == FrecuenciaAporte.mensual

def test_error_si_aportes_sin_frecuencia():
    with pytest.raises(ValueError, match="también debe indicarse 'cada_cuanto_aporta'"):
        CalculoRequest(
            capital_inicial=Decimal("10000"),
            tasa_interes_anual=Decimal("10"),
            anios=5,
            tipo_capitalizacion=PeriodoCapitalizacion.mensual,
            aportes_periodicos=Decimal("500"),
            cada_cuanto_aporta=None
        )

def test_error_si_frecuencia_sin_aportes():
    with pytest.raises(ValueError, match="sin 'aportes_periodicos'"):
        CalculoRequest(
            capital_inicial=Decimal("10000"),
            tasa_interes_anual=Decimal("10"),
            anios=5,
            tipo_capitalizacion=PeriodoCapitalizacion.mensual,
            aportes_periodicos=None,
            cada_cuanto_aporta=FrecuenciaAporte.mensual
        )