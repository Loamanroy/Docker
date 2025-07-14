# docker-nginx-site
# Фикс запуска CI
⚙️ Мини-инфраструктура из 3 контейнеров (frontend + backend + PostgreSQL + nginx) на Docker Compose.

## 🔧 Запуск

```bash
git clone https://github.com/ТВОЙ_АКК/docker-nginx-site.git
cd docker-nginx-site
sudo docker compose up --build -d

🧪 Проверка

    http://localhost:8080 — frontend

    http://localhost:5000/api/hello — backend

    http://localhost:5000/api/users — PostgreSQL API
