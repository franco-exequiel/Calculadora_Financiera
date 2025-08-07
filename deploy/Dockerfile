FROM python:3.12-slim

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar archivos del proyecto
COPY ./app /app/app


# Exponer el puerto por defecto de uvicorn
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]