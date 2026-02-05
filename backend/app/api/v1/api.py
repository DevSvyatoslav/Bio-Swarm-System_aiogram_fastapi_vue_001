from fastapi import APIRouter
from app.api.v1.endpoints import users # <--- Импортируем файл users

api_router = APIRouter()

# Включаем рубильник
api_router.include_router(users.router, prefix="/users", tags=["users"])