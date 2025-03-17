# 🚍 Sistema de Transporte Público

## 📌 Descripción
Este proyecto es un sistema de gestión de transporte público basado en **Django Rest Framework (DRF)** para el backend y **Angular** para el frontend. Incluye autenticación JWT, almacenamiento en **AWS S3**, caché con **Redis**, y despliegue con **Docker y AWS EC2**.

---

## 🚀 Tecnologías

### **Backend** (Django + DRF)
- Django Rest Framework
- PostgreSQL
- Redis (caché y optimización)
- AWS S3 (almacenamiento de archivos)
- Docker + Docker Compose

### **Frontend** (Angular)
- Angular 16+
- Tailwind CSS (estilos)
- Angular Material (componentes UI)

### **Infraestructura y Despliegue**
- Docker + Docker Compose
- AWS EC2 (despliegue backend)
- AWS S3 (almacenamiento de archivos)
- AWS RDS (PostgreSQL en la nube)
- CI/CD con GitHub Actions

---

## 🔧 Instalación y Configuración

### **1️⃣ Clonar el repositorio**
```bash
git clone https://github.com/MrVelartt/transporte-publico.git
cd transporte-publico
```

### **2️⃣ Configurar el entorno**
Crea un archivo `.env` en el backend con las variables de entorno necesarias:
```env
SECRET_KEY=tu_secreto
debug=True
DB_NAME=transporte_db
DB_USER=admin
DB_PASSWORD=adminpassword
DB_HOST=localhost
DB_PORT=5432
REDIS_URL=redis://localhost:6379
AWS_ACCESS_KEY_ID=tu_key
AWS_SECRET_ACCESS_KEY=tu_secret
```

### **3️⃣ Construir y levantar los contenedores con Docker**
```bash
docker-compose up --build
```
Esto iniciará **Django + PostgreSQL + Redis**.

### **4️⃣ Aplicar migraciones y cargar datos**
```bash
docker exec -it backend python manage.py migrate
docker exec -it backend python manage.py createsuperuser
```

---

## 🌍 Despliegue en AWS EC2

### **1️⃣ Crear una instancia EC2**
- **Tipo:** t2.micro (gratis por 1 año)
- **Sistema:** Ubuntu 22.04 LTS
- **Reglas de seguridad:** Abrir puertos `80`, `443`, `22`, `5432`, `6379`

### **2️⃣ Instalar dependencias en EC2**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io docker-compose -y
```

### **3️⃣ Clonar el repositorio en EC2 y levantar el proyecto**
```bash
git clone https://github.com/MrVelartt/transporte-publico.git
cd transporte-publico
docker-compose up --build -d
```

### **4️⃣ Configurar Nginx como proxy inverso (Opcional)**
Instalar y configurar Nginx para redirigir tráfico al backend.
```bash
sudo apt install nginx -y
```
Configurar el archivo `/etc/nginx/sites-available/default`.
```nginx
server {
    listen 80;
    server_name tu_dominio.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```
Reiniciar Nginx:
```bash
sudo systemctl restart nginx
```

---

## ✅ CI/CD con GitHub Actions
Para automatizar despliegues, configura un workflow en `.github/workflows/deploy.yml`:
```yaml
name: Deploy to AWS EC2
on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      
      - name: Deploy with SSH
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.EC2_HOST }}
          username: ubuntu
          key: ${{ secrets.EC2_SSH_KEY }}
          script: |
            cd transporte-publico
            git pull origin main
            docker-compose up --build -d
```

---

## 📌 Próximos pasos
✔ Integración con WebSockets (Django Channels)
✔ Mejorar logs con AWS CloudWatch
✔ Implementación de FastAPI para nuevos microservicios

---

📌 **Autor:** MrVelartt 🚀
📌 **Repositorio:** [GitHub](https://github.com/MrVelartt/transporte-publico)
