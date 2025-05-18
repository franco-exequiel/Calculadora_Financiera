FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY ./app /app/app
COPY ./requirements.txt /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto por defecto de uvicorn
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]