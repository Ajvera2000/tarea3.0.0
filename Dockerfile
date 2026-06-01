#paso1 : Usar una imagen base oficial de Python ligera
FROM python:3.11-slim

#paso2 : Configurar el directorio de trabajo
WORKDIR /app

#paso3 : Copiar el archivo de requerimientos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#paso4 : Copiar el código de la aplicación y las pruebas
COPY app/ ./app/
COPY tests/ ./tests/

#paso5 : Variable de entorno para evitar que Python escriba archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#paso6 : Comando por defecto para ejecutar la aplicación
CMD ["python", "app/main.py"]