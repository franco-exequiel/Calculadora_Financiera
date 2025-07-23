from app.models.calculo import CalculoRequest, PeriodoCapitalizacion
from app.services.calculadora import calcular_interes_compuesto


def test_calculo_sin_aportes():
    req = CalculoRequest(
        capital_inicial=10000,
        tasa_interes_anual=12,
        anios=1,
        tipo_capitalizacion=PeriodoCapitalizacion.mensual,
        aportes_periodicos=None,
        cada_cuanto_aporta=None
    )
    resultado = calcular_interes_compuesto(req)
    assert resultado["capital_final"] > 10000
    assert "detalle" not in resultado or len(resultado["detalle"]) == 0