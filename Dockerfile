#1 buscar una imagen base
FROM python:3.12-alpine

#2 crear directorio de trabajo en el contenedor
WORKDIR /app

#3 copiar el archivo de dependencias
COPY requirements.txt /app

#4 instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt


#5 copiar el codigo fuente, si se usa el . en lugar de app.py, se copiaran todos los archivos del directorio actual al contenedor
COPY app.py /app

#6 exponer el puerto que usara la aplicacion
EXPOSE 5000

#7 comando para ejecutar la aplicacion
CMD ["python", "app.py"]