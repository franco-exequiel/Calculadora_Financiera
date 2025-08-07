# 📈 Motor de Cálculo Financiero - Microservicio

Microservicio en Python que permite calcular interés compuesto, con o sin aportes periódicos, y exportar los resultados a formatos como CSV o Excel.

Este motor fue diseñado como servicio reutilizable para aplicaciones como un sistema HomeBanking, una plataforma de inversión o un simulador financiero educativo.

---

## 🚀 Tecnologías utilizadas

- ✅ Python 3.11
- ✅ FastAPI
- ✅ Pandas
- ✅ Docker + Docker Compose
- ✅ GitHub Actions (CI)
- ✅ pytest
- ✅ HTML + JS (Frontend simple opcional)

---

## 🧪 Correr tests

```bash
make test
# o directamente
pytest
```

---

## 🐳 Docker

### Levantar el servicio con Docker

```bash
make up
# o
docker-compose -f deploy/docker-compose.yml up --build
```

### Apagar

```bash
make down
```

---

## 📬 Endpoints disponibles

| Método | Endpoint                     | Descripción                              |
|--------|------------------------------|------------------------------------------|
| POST   | `/api/v1/calculadora`        | Cálculo de interés (con/sin aportes)     |
| POST   | `/api/v1/calcular/csv`       | Exportación de cálculo a archivo CSV     |
| POST   | `/api/v1/calcular/excel`     | Exportación de cálculo a archivo Excel   |

---

## 🧠 Ejemplo de cuerpo para POST `/api/v1/calculadora`

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

## 🔧 Variables de entorno

No requiere base de datos ni credenciales externas. Servicio completamente stateless.

---

## 📦 Estructura del proyecto

```bash
.
├── app/
│   ├── api/endpoints/v1/
│   ├── services/
│   ├── models/
│   └── main.py
├── frontend/
│   └── index.html
├── tests/
├── deploy/
│   ├── docker-compose.yml
│   └── Dockerfile
├── .github/workflows/ci.yml
├── requirements.txt
├── Makefile
└── README.md
```

---

## 📣 Licencia y uso

Este microservicio puede integrarse en cualquier sistema que requiera cálculos financieros.

---

🔙 Volver al [README principal](./README.md)