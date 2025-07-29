
# 📈 API de Calculadora Financiera

Calculadora Financiera API es un servicio REST desarrollado en Python con FastAPI. Permite calcular el crecimiento del capital a través del interés compuesto, incluyendo aportes periódicos opcionales. Devuelve el monto final, la ganancia total y un desglose por período. También ofrece funcionalidades de exportación y un frontend básico.

Ideal para simulaciones de inversión, educación financiera o planificación personal. Incluye frontend, backend con FastAPI y exportación de resultados a CSV y Excel.

---


## 🚀 Características

- Cálculo de interés compuesto:
  - Con o sin aportes periódicos
  - Capitalización: mensual, trimestral, semestral, anual
- Frontend simple embebido con selector de tema (claro/oscuro)
- Exportación de resultados:
  - CSV (`.csv`)
  - Excel (`.xlsx`)
- API RESTful documentada automáticamente (Swagger/OpenAPI)

---

## 🛠️ Tecnologías

- **Backend**: FastAPI + Pydantic + Pandas
- **Frontend**: HTML + JS Vanilla
- **Persistencia en memoria** (sin DB)
- **Tests**: `pytest` + `TestClient`
- **Contenerización**: Docker + Uvicorn

---

## 🧪 Ejemplo de uso
## 🚀 Cómo correr el proyecto

### ✅ Opción 1: Localmente (sin Docker)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 🐳 Opción 2: Usando Docker

```bash
cd deploy
docker-compose up --build
```

Una vez iniciado, accedé a:

- API: http://localhost:8000/docs
- Frontend: http://localhost:8000

---

### Acceder

- [http://localhost:8000](http://localhost:8000) → Frontend
- [http://localhost:8000/docs](http://localhost:8000/docs) → Swagger UI 

---

### Cálculo de interés compuesto (POST `/api/v1/calcular`)

```json
{
  "capital_inicial": 10000,
  "tasa_interes_anual": 10.5,
  "anios": 20,
  "tipo_capitalizacion": "semestral",
  "aportes_periodicos": 500,
  "cada_cuanto_aporta": "mensual"
}
```

### Exportar resultado en CSV

```
POST /api/v1/calcular/csv?descargar=true
```

### Exportar resultado en Excel

```
POST /api/v1/calcular/excel?descargar=true
```

---

## 🧪 Tests

```bash
pytest tests/
```

Incluye tests para:
- Lógica de cálculo simple y con aportes.
- Exportación CSV
- Exportación Excel

---
## 💻 Frontend Estático

Ubicado en `app/frontend/index.html`, este formulario simple permite probar la API desde el navegador.

Incluye:
- Inputs de cálculo.
- Selector de aportes opcionales.
- Botón de cambio de tema claro/oscuro (🌙 / ☀️).
- Estilos personalizados desde `app/frontend/statics/css/styles.css`.
- Lógica en `app/frontend/statics/js/main.js`.

---
## 📂 Estructura del Proyecto

```bash
.
├── app/
│   ├── main.py
│   ├── api/
│   │   └── endpoints/v1/
│   │       ├── calculadora.py
│   │       └── exportar.py
│   ├── services/
│   │   ├── calculadora.py
│   │   └── exportador.py
│   └── frontend/
│       ├── index.html
│       └── statics/
│           ├── css/
│           │   └── styles.css
│           └── js/
│               └── main.js
├── tests/
│   ├── test_calculo_basico.py
│   ├── test_calculo_interes_compuesto.py
│   └── test_exportar_csv.py
├── deploy/
│   └── docker-compose.yml
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🧠 Visión a Futuro

- 📊 Gráficos con Chart.js o similar.
- 🔐 Autenticación JWT una vez integrada con HomeBanking API.

---



## ✨ Autor

**Franco Exequiel**  
Desarrollador backend Python | API REST | Automatización | Enfoque en clean code y escalabilidad 🚀
