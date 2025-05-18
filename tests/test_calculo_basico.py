from app.models.calculo import CalculoRequest
from app.services.calculadora import calcular_interes_compuesto


def test_calculo_basico():
    req = CalculoRequest(
        capital_inicial=10000,
        interes_anual=12,
        duracion_anios=1,
        frecuencia_capitalizacion="mensual",
        agregado_extra=0,
        frecuencia_agregado="ninguna"
    )
    resultado = calcular_interes_compuesto(req)
    assert resultado["monto_final"] > 10000
    assert len(resultado["detalle"]) == 12



