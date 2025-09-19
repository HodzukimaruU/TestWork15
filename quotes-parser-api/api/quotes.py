from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from typing import List
from core.mongo_db import mongo_db
from tasks.quotes import parse_quotes
from repositories.quotes_repository import QuotesRepository
from models.quotes import Quote


router = APIRouter()
repository = QuotesRepository(mongo_db)

@router.post("/parse-quotes-task/")
async def create_parse_task():
    task = parse_quotes.delay()
    return {"task_id": task.id}

@router.get("/quotes/", response_model=List[Quote])
async def get_quotes(
    author: str | None = Query(None),
    tag: str | None = Query(None),
    page: int | None = Query(None, ge=1),
    page_size: int | None = Query(None, ge=1, le=100),
):
    quotes = await repository.get_quotes(
        author=author,
        tag=tag,
        page=page,
        page_size=page_size,
    )

    if not quotes:
        return JSONResponse(
            status_code=404,
            content={"detail": "Цитаты по заданным критериям не найдены"}
        )
    return quotes
