# syntax=docker/dockerfile:1
FROM python:3.9-slim

# Crea un directorio de trabajo
WORKDIR /app

# Copia requirements y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto de FastAPI
EXPOSE 8000

# Comando por defecto: arranca uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
