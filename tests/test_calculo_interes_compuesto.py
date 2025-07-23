from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calculo_endpoint_con_aportes():
    payload = {
        "capital_inicial": 10000,
        "tasa_interes_anual": 10,
        "tipo_capitalizacion": "mensual",
        "aportes_periodicos": 500,
        "cada_cuanto_aporta": "mensual",
        "anios": 1
    }

    response = client.post("/api/v1/calcular", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "capital_final" in data
    assert "ganancia_total" in data
    assert "detalle" in data
    assert isinstance(data["detalle"], list)
    assert len(data["detalle"]) == 13
    assert data["detalle"][0]["periodo"] == "Inicial"

