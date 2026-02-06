from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings
from app.db.database import init_db
from app.api.api_v1.router import api_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    print('Inicializando Database...')
    await init_db()
    print('Database Conectado!')
    yield
    print('Encerrando aplicação...')

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f'{settings.API_V1_STR}/openapi.json',
    lifespan=lifespan
)

app.include_router(api_router,prefix=settings.API_V1_STR)

@app.get('/')
async def root():
    return{'message':'Sistema de Auth Operancional'}