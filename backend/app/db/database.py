from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings
from app.models.user_model import User 

async def init_db():
    client = AsyncIOMotorClient(str(settings.mongo_uri_computed))
    
    # Seleciona o banco de dados
    db = client[settings.MONGO_DB]
    
    # Inicializa o Beanie com os modelos
    await init_beanie(database=db, document_models=[User])