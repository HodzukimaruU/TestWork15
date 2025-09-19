from fastapi import FastAPI
from core.mongo_db import mongo_db
from core.settings import settings

from api.quotes import router

app = FastAPI(title=settings.app_name, debug=settings.debug)

# Подключаем роутер
app.include_router(router, prefix="")

# Зависимость для роутеров
async def get_mongo():
    return mongo_db

@app.get("/")
async def root():
    return {"message": f"{settings.app_name} is running 🚀"}
