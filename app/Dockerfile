#Usar imagen oficial de Python
FROM python:3.10-slim

#Establecer directorio de trabajo
WORKDIR /app

#Copiar archivos
COPY . .

#Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

#Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
