# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del microservicio al contenedor
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir flask

# Exponer el puerto 5000 para Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "microservicio.py"]
