FROM nginx:latest

# Заменяем конфиг
COPY nginx.conf /etc/nginx/nginx.conf

# Копируем всё содержимое в html
COPY . /usr/share/nginx/html

EXPOSE 80
