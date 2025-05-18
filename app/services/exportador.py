import csv
import io
from app.models.calculo import CalculoRequest
from app.services.calculadora import calcular_interes_compuesto

def generar_csv(data: CalculoRequest) -> bytes:
    resultado = calcular_interes_compuesto(data)
    detalle = resultado["detalle"]

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["periodo", "interes_generado", "capital_total"])
    writer.writeheader()
    writer.writerows(detalle)

    return output.getvalue().encode("utf-8")