from typing import Sequence
from bson import ObjectId
from models.quotes import Quote

class QuotesRepository:
    def __init__(self, db):
        self.collection = db["quotes"]

    async def insert_many_unique(self, quotes: Sequence[Quote]) -> list[ObjectId]:
        inserted_ids: list[ObjectId] = []

        for quote in quotes:
            quote_dict = quote.model_dump()
            exists = await self.collection.find_one({
                "quote": quote_dict["quote"],
                "author": quote_dict["author"]
            })
            if not exists:
                result = await self.collection.insert_one(quote_dict)
                inserted_ids.append(result.inserted_id)

        return inserted_ids
    
    async def get_quotes(
        self,
        author: str | None = None,
        tag: str | None = None,
        page: int | None = None,
        page_size: int | None = None,
    ):
        query = {}
        if author:
            query["author"] = author
        if tag:
            query["tags"] = tag

        cursor = self.collection.find(query)

        # применяем пагинацию только если page и page_size переданы
        if page is not None and page_size is not None:
            skip = (page - 1) * page_size
            cursor = cursor.skip(skip).limit(page_size)
            results = await cursor.to_list(length=page_size)
        else:
            results = await cursor.to_list(length=None)

        return results