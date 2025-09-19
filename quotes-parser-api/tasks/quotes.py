import asyncio
import logging
from celery_app import app
from parser.quotes_parser import fetch_quotes
from core.mongo_db import mongo_db
from services.quotes_service import QuotesUseCase
from repositories.quotes_repository import QuotesRepository
from models.quotes import Quote
from bson import ObjectId

logger = logging.getLogger(__name__)

@app.task(bind=True)
def parse_quotes(self) -> list[str]:
    logger.info(f"Task {self.request.id} started")

    quotes: list[Quote] = fetch_quotes()
    logger.info(f"Parsed {len(quotes)} quotes")

    repository = QuotesRepository(mongo_db)
    service = QuotesUseCase(repository)

    loop = asyncio.get_event_loop()
    inserted_ids: list[ObjectId] = loop.run_until_complete(service.save_quotes(quotes))
    inserted_ids_str: list[str] = [str(_id) for _id in inserted_ids]

    logger.info(f"Task {self.request.id} finished, {len(inserted_ids)} new quotes saved")
    return inserted_ids_str

