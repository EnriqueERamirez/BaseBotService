# Usa una imagen base de Python 3
FROM python:3.9-slim

# Establece un directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos al contenedor
COPY requirements.txt ./

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código al contenedor
COPY . .

# Ejecuta main.py cuando se inicie el contenedor
CMD [ "python", "./main.py" ]
