# QuotesParser API

## Документация API

Документация к эндпоинтам также доступна через Swagger UI после запуска приложения по URL: `http://localhost:8000/docs#/`

### 1. Запуск парсера

Реализован эндпоинт, который запускает celery задачу, которая запускает парсер, после чего распаршенная дата сохораняется в MongoDB.

#### Запрос

**Метод:** `POST`

**URL:** `http://localhost:8000/parse-quotes-task/`

**Ответ:**

```ini
{
    "task_id": "0295390d-9d7e-42b3-8f18-18b966e046b7"
}
```

---

### 2. Получение данных из MongoDB.

Реализован endpoint для получения данных из MongoDB с фильтрацией по автору и тегу, а также с пагинацией.

#### Запрос

**Метод:** `GET`

**URL:** `http://localhost:8000/quotes/`

**Примеры URL c фильтрацией и пагинацией:**

- `http://localhost:8000/quotes/?page=1&page_size=10`
- `http://localhost:8000/quotes/?author=Albert Einstein&tag=life`
- `http://localhost:8000/quotes/?tag=life`
- `http://localhost:8000/quotes/?page=1&page_size=10&uthor=Albert Einstein`

**Ответ:**

```ini
[
    {
        "quote": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
        "author": "Albert Einstein",
        "tags": [
            "change",
            "deep-thoughts",
            "thinking",
            "world"
        ],
        "created_at": "2025-09-20T13:43:12.352000"
    },
    {
        "quote": "“It is our choices, Harry, that show what we truly are, far more than our abilities.”",
        "author": "J.K. Rowling",
        "tags": [
            "abilities",
            "choices"
        ],
        "created_at": "2025-09-20T13:43:12.353000"
    },
    ...
]
```

---

## Запуск и настройка

### Требования

- **Docker**
- **Docker Compose**

### Конфигурация `.env`

Создайте файл `.env` на одном уровне с docker-compose.yaml (пример содержимого в .env.example):

```ini
APP_NAME=Quotes Parser
DEBUG=True

MONGO_HOST=mongo
MONGO_PORT=27017
MONGO_DB=quotes_db

REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB_BROKER=0
REDIS_DB_BACKEND=1
```

---

## Инструкция по запуску

1. **Клонируйте репозиторий:**

   ```sh
   git clone <ссылка на репозиторий>
   ```

2. **Зайдите в склонированный репозиторий:**

   ```sh
   cd <название репозитория>
   ```

3. **Запустите сервисы с помощью Docker Compose:**

   ```sh
   docker compose up -d
   ```
