# 📈 Financial Calculator API

Financial Calculator API is a REST service developed in Python with FastAPI. It allows the calculation of capital growth through compound interest, including optional periodic contributions. It returns the final amount, total gain, and a period-by-period breakdown. It also offers export functionalities and a basic frontend.

Ideal for investment simulations, financial education, or personal planning. Includes frontend, backend with FastAPI, and result export to CSV and Excel.

---

## 🚀 Features

- Compound interest calculation:
  - With or without periodic contributions
  - Compounding: monthly, quarterly, semiannual, annual
- Simple embedded frontend with theme selector (light/dark)
- Result export:
  - CSV (`.csv`)
  - Excel (`.xlsx`)
- Automatically documented RESTful API (Swagger/OpenAPI)

---

## 🛠️ Technologies

- **Backend**: FastAPI + Pydantic + Pandas
- **Frontend**: HTML + Vanilla JS
- **In-memory persistence** (no DB)
- **Tests**: `pytest` + `TestClient`
- **Containerization**: Docker + Uvicorn

---

## 🚀 How to Run the Project

### ✅ Option 1: Locally (without Docker)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 🐳 Option 2: Using Docker

```bash
cd deploy
docker-compose up --build
```

Once running, access:

- API: http://localhost:8000/docs
- Frontend: http://localhost:8000

---

### Access

- [http://localhost:8000](http://localhost:8000) → Frontend
- [http://localhost:8000/docs](http://localhost:8000/docs) → Swagger UI 

---

### Compound Interest Calculation (POST `/api/v1/calcular`)

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

### Export result as CSV

```
POST /api/v1/calcular/csv?descargar=true
```

### Export result as Excel

```
POST /api/v1/calcular/excel?descargar=true
```

---

## 🧪 Tests

```bash
pytest tests/
```

Includes tests for:
- Basic and periodic contribution calculation logic.
- CSV Export
- Excel Export

✔️ **Test Coverage: 100%**

---

## 💻 Static Frontend

Located at `app/frontend/index.html`, this simple form allows testing the API from the browser.

Includes:
- Calculation inputs.
- Optional contribution selector.
- Light/Dark theme toggle button (🌙 / ☀️).
- Custom styles from `app/frontend/statics/css/styles.css`.
- Logic in `app/frontend/statics/js/main.js`.

---

## 📂 Project Structure

```bash
.
├── github/
│   ├── workflows/
│   │   └── ci.yml
├── app/
│   ├── main.py
│   ├── api/
│   │   └── endpoints/
│   │       └── v1/
│   │           ├── calculadora.py
│   │           └── exportar.py
│   ├── models/
│   │   ├── calculo.py
│   ├── services/
│   │   ├── calculadora.py
│   │   └── exportador.py
│   ├── frontend/
│   │    ├── index.html
│   │    └── statics/
│   │        ├── css/
│   │        │   └── styles.css
│   │        └── js/
│   │            └── main.js
│   ├── deploy/
│   │   ├── .dockerignore
│   │   ├── docker-compose.yml
│   │   └── Dockerfile
├── tests/
│   ├── conftest.py
│   ├── test_calculo_basico.py
│   ├── test_calculo_interes_compuesto.py
│   └── test_exportar_csv.py
│   └── test_exportar_excel.py
│   └── test_exportar_validaciones.py
├── deploy/
│   └── docker-compose.yml
├── requirements.txt
├── pytest.ini
└── DEVELOPER_GUIDE_en.md
└── README_en.md
```

---

## 🧠 Future Vision

- 📊 Charts with Chart.js or similar.
- 🔐 JWT authentication once integrated with HomeBanking API.

---

## ✨ Author

**Franco Exequiel**  
Python Backend Developer | REST API | Automation | Clean Code & Scalability focused 🚀

---
For technical details, see [DEVELOPER_GUIDE_en.md](./DEVELOPER_GUIDE_en.md)