from app.models.calculo import CalculoRequest

def calcular_interes_compuesto(data: CalculoRequest) -> dict:
    # Mapear frecuencias a cantidad de períodos por año
    map_periodos = {
        "anual": 1,
        "semestral": 2,
        "trimestral": 4,
        "mensual": 12,
        "diaria": 365
    }

    n = map_periodos[data.frecuencia_capitalizacion]
    t = data.duracion_anios
    r = data.interes_anual / 100
    P = data.capital_inicial
    extra = data.agregado_extra
    freq_extra = map_periodos.get(data.frecuencia_agregado, 0)

    total_periodos = int(n * t)
    periodo_extra = n // freq_extra if freq_extra else None

    detalle = []
    capital = P

    for i in range(1, total_periodos + 1):
        interes = capital * (r / n)
        capital += interes

        if freq_extra and i % periodo_extra == 0:
            capital += extra

        detalle.append({
            "periodo": i,
            "interes_generado": round(interes, 2),
            "capital_total": round(capital, 2)
        })

    return {
        "monto_final": round(capital, 2),
        "detalle": detalle
    }