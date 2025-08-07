# 📈 Financial Calculation Engine - Microservice

Python microservice that calculates compound interest, with or without periodic contributions, and exports the results to formats like CSV or Excel.

This engine was designed as a reusable service for applications such as a HomeBanking system, an investment platform, or an educational financial simulator.

---

## 🚀 Technologies Used

- ✅ Python 3.11
- ✅ FastAPI
- ✅ Pandas
- ✅ Docker + Docker Compose
- ✅ GitHub Actions (CI)
- ✅ pytest
- ✅ HTML + JS (optional simple frontend)

---

## 🧪 Run Tests

```bash
make test
# or directly
pytest
```

---

## 🐳 Docker

### Start the service with Docker

```bash
make up
# or
docker-compose -f deploy/docker-compose.yml up --build
```

### Stop

```bash
make down
```

---

## 📬 Available Endpoints

| Method | Endpoint                  | Description                                 |
|--------|---------------------------|---------------------------------------------|
| POST   | `/api/v1/calculadora`     | Interest calculation (with/without contrib) |
| POST   | `/api/v1/calcular/csv`    | Export calculation to CSV file              |
| POST   | `/api/v1/calcular/excel`  | Export calculation to Excel file            |

---

## 🧠 Example Body for POST `/api/v1/calculadora`

```json
{
  "monto_inicial": 10000,
  "tasa_anual": 10,
  "anios": 5,
  "aporte_periodico": 1000,
  "frecuencia_aporte": "mensual"
}
```

---

## 🔧 Environment Variables

No database or external credentials required. Fully stateless service.

---

## 📦 Project Structure

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

## 📣 License and Use

This microservice can be integrated into any system requiring financial calculations.

---

🔙 Back to [Main README_en](./README_en.md)