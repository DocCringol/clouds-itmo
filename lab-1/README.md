# Лабораторная 1 - Настройка nginx

## Добавление сервисов

TBD

## Простая контейнеризация сервисов

TBD

```yaml
services:
  project-1:
    build: ./project-1

  project-2:
    build: ./project-2
```

## Простая настройка nginx для http

TBD

```yaml
services:
  project-1:
    build: ./project-1
    networks:
      - nginx-network


  project-2:
    build: ./project-2
    networks:
      - nginx-network

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - project-1
      - project-2
    networks:
      - nginx-network


networks:
  nginx-network:
    driver: bridge
```

```nginx
events {}

http {
    upstream project1 {
        server project-1:8080;
    }

    upstream project2 {
        server project-2:8080;
    }

    server {
        listen 80;

        location /cats {
            proxy_pass http://project1/random-cat;
        }

        location /dogs {
            proxy_pass http://project2/random-dog;
        }

        location / {
            return 404 "Not Found";
        }
    }
}
```