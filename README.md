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

### 💻 Frontend mínimo para testing manual
Puedes testear la API usando un archivo HTML estático que haga peticiones fetch.

### 🔧 Cómo probar localmente
Serví el HTML con Python:

```bash
cd frontend/
python -m http.server 5500
Accedé desde tu navegador a: http://localhost:5500
```

### 🌐 Importante: CORS
Para permitir llamadas del frontend, se configuró en main.py:

```bash python
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
Si cambias de puerto o hacés deploy, asegurate de actualizar esto.

