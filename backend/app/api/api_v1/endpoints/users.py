from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserResponse
from app.models.user_model import User
from app.api.deps import get_current_user
from typing import Any


router = APIRouter()

@router.get('/me', response_model=UserResponse)
async def read_user_me(
    current_user: User = Depends(get_current_user)
) -> Any:
    return current_user