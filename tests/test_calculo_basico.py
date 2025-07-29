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

    # Validaciones generales
    assert resultado["capital_final"] > 10000
    assert resultado["ganancia_total"] > 0

    # Validar que se devuelva una lista de dicts con el detalle
    detalle = resultado.get("detalle")
    assert isinstance(detalle, list)
    assert len(detalle) > 0
    assert isinstance(detalle[0], dict)
    assert "capital_final" in detalle[0]
    assert "ganancia_total" in detalle[0]