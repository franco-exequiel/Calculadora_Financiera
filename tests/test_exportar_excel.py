from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calcular_y_exportar_excel_descarga():
    payload = {
        "capital_inicial": 10000,
        "tasa_interes_anual": 10,
        "tipo_capitalizacion": "mensual",
        "aportes_periodicos": 500,
        "cada_cuanto_aporta": "mensual",
        "anios": 1
    }

    response = client.post("/api/v1/calcular/excel?descargar=true", json=payload)

    # Verificar el status code
    assert response.status_code == 200

    # Validar el tipo de contenido
    assert response.headers["content-type"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    # Verificar que tiene el header de descarga
    assert "attachment; filename=calculo_resultado.xlsx" in response.headers.get("content-disposition", "")

    # Validar que el contenido no esté vacío
    assert len(response.content) > 0
def test_exportar_excel_sin_descargar_devuelve_streamingresponse():
    """
    Valida que el endpoint /calcular/excel devuelva un StreamingResponse válido
    cuando 'descargar=False' (por defecto).
    """
    payload = {
        "capital_inicial": 10000,
        "tasa_interes_anual": 10,
        "tipo_capitalizacion": "mensual",
        "aportes_periodicos": 100,
        "cada_cuanto_aporta": "mensual",
        "anios": 1
    }

    response = client.post("/api/v1/calcular/excel", json=payload)
    
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    assert len(response.content) > 0  # Asegura que hay contenido binario