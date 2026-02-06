from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings
from app.models.user_model import User


async def init_db():

    client = AsyncIOMotorClient(str(settings.mongo_uri))
    
    
    await init_beanie(
        database=client[settings.MONGO_DB], #type: ignore
        document_models=[
            User,
        ]
    )
