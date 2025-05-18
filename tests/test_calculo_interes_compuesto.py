from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calculo_interes_compuesto():
    payload = {
        "capital_inicial": 10000,
        "interes_anual": 10,
        "frecuencia_capitalizacion": "mensual",
        "agregado_extra": 500,
        "frecuencia_agregado": "mensual",
        "duracion_anios": 1
    }

    response = client.post("/api/v1/calcular", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "monto_final" in data
    assert "detalle" in data
    assert isinstance(data["detalle"], list)
    assert len(data["detalle"]) == 12  # 12 meses