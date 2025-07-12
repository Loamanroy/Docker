# Базовый образ
FROM nginx:latest

# Копируем наш сайт внутрь nginx
COPY index.html /usr/share/nginx/html/index.html

# Указываем, что контейнер слушает 80 порт
EXPOSE 80
