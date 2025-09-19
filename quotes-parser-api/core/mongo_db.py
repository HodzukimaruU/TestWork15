from motor.motor_asyncio import AsyncIOMotorClient
from core.settings import settings

mongo_client = AsyncIOMotorClient(settings.mongo_url)
mongo_db = mongo_client[settings.mongo_db]