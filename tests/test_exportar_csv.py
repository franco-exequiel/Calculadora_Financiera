from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calcular_y_exportar_csv_texto():
    payload = {
        "capital_inicial": 10000,
        "tasa_interes_anual": 10,
        "tipo_capitalizacion": "mensual",
        "aportes_periodicos": 500,
        "cada_cuanto_aporta": "mensual",
        "anios": 1
    }

    response = client.post("/api/v1/calcular/csv?descargar=false", json=payload)
    
    # Verificar el status code
    assert response.status_code == 200
    
    # Validar el tipo de contenido
    assert response.headers["content-type"] == "text/plain; charset=utf-8"
    
    csv_text = response.text
    
    # Validar que los encabezados estén presentes
    assert "anio" in csv_text
    assert "capital_actual" in csv_text
    
    # Debe haber más de una línea (header + filas)
    assert len(csv_text.splitlines()) > 1


def test_calcular_y_exportar_csv_descarga():
    payload = {
        "capital_inicial": 10000,
        "tasa_interes_anual": 10,
        "tipo_capitalizacion": "mensual",
        "aportes_periodicos": 500,
        "cada_cuanto_aporta": "mensual",
        "anios": 1
    }

    response = client.post("/api/v1/calcular/csv?descargar=true", json=payload)

    # Verificar el status code
    assert response.status_code == 200

    # Validar el tipo de contenido
    assert response.headers["content-type"] == "text/csv; charset=utf-8"
    
    # Verificar que tiene el header de descarga
    assert "attachment; filename=calculo_resultado.csv" in response.headers.get("content-disposition", "")

    csv_text = response.text
    # Validar contenido
    assert "anio" in csv_text