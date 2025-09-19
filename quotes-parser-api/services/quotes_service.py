from typing import Sequence
from repositories.quotes_repository import QuotesRepository
from models.quotes import Quote
from bson import ObjectId

class QuotesUseCase:
    def __init__(self, repository: QuotesRepository):
        self.repository = repository

    async def save_quotes(self, quotes: Sequence[Quote]) -> list[ObjectId]:
        return await self.repository.insert_many_unique(quotes)
