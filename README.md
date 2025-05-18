# 📈 API Calculadora Financiera (v0.1.0)

API REST que calcula interés compuesto incluyendo aportes periódicos opcionales.

## 🚀 Cómo correr el proyecto

### Opción 1: Localmente (sin Docker)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```


### Opción 2: Usando Docker
```bash
cd deploy
docker-compose up --build
```
# API disponible en: http://localhost:8000/docs

### 📬 Endpoint
POST /api/v1/calcular
Body JSON: capital inicial, tasa anual, duración, frecuencia, etc.
Devuelve el monto final y el detalle por período.


### 🧪 Tests
```bash
pytest
```

### 🧠 Visión a Futuro
* Exportar resultados a Excel o CSV.
* Agregar simulaciones con inflación.
* Frontend con Streamlit o React.
* Deploy en la nube.