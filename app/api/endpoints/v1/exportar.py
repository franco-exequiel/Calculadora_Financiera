from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.models.calculo import CalculoRequest
from app.services.exportador import generar_csv
from datetime import datetime

router = APIRouter()

@router.post("/exportar")
def exportar_csv(data: CalculoRequest):
    csv_bytes = generar_csv(data)
    filename = f"calculo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    return StreamingResponse(io.BytesIO(csv_bytes),
                             media_type="text/csv",
                             headers={"Content-Disposition": f"attachment; filename={filename}"})