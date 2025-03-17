# Usa una imagen oficial de Python
FROM python:3.11

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000
EXPOSE 8000

# Comando por defecto
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]