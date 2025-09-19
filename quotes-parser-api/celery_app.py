from celery import Celery
from core.settings import settings

app = Celery(
    "quotes_parser",
    broker=f"redis://{settings.redis_host}:{settings.redis_port}/{settings.redis_db_broker}",
    backend=f"redis://{settings.redis_host}:{settings.redis_port}/{settings.redis_db_backend}",
    include=["tasks.quotes"]
)

app.conf.update(
    result_expires=3600,
    task_track_started=True
)
