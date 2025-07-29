from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse, PlainTextResponse
from app.models.calculo import CalculoRequest
from app.services.calculadora import calcular_interes_compuesto
from app.services.exportador import ExportadorService

router = APIRouter()

@router.post("/calcular/csv")
def calcular_y_exportar_csv(
    req: CalculoRequest,
    descargar: bool = Query(False, description="Si es True, fuerza la descarga del archivo")
):
    """
    Calcula el interés compuesto y exporta el detalle en CSV.
    """
    resultado = calcular_interes_compuesto(req)

    # Si el modelo simple no trae detalle, devolvemos CSV vacío o error claro
    detalle = resultado.get("detalle") or []
    #Validamos que haya datos para exportar
    if not detalle:
        raise ValueError("No hay datos detallados para exportar.")
    # Si es una lista de modelos Pydantic, convertirlos a dict
    detalle = [d if isinstance(d, dict) else d.model_dump() for d in detalle]
    
    csv_buffer = ExportadorService.generar_csv(detalle)
    print("Detalle:", detalle)
    print("📄 Filas para exportar:", len(detalle))
    if descargar:
        return StreamingResponse(
            iter([csv_buffer.getvalue()]),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=calculo_resultado.csv"}
        )
    else:
        return PlainTextResponse(csv_buffer.getvalue(), media_type="text/plain")
    

@router.post("/calcular/excel")
def calcular_y_exportar_excel(
    req: CalculoRequest,
    descargar: bool = Query(False, description="Si es True, fuerza la descarga del archivo")
):
    """
    Calcula el interés compuesto y exporta el detalle en Excel.
    """
    resultado = calcular_interes_compuesto(req)

    detalle = resultado.get("detalle") or []
    if not detalle:
        raise ValueError("No hay datos detallados para exportar.")
    
    detalle = [d if isinstance(d, dict) else d.model_dump() for d in detalle]
    excel_buffer = ExportadorService.generar_excel(detalle)

    if descargar:
        return StreamingResponse(
            iter([excel_buffer.getvalue()]),
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": "attachment; filename=calculo_resultado.xlsx"}
        )
    else:
        return StreamingResponse(
            iter([excel_buffer.getvalue()]),
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )