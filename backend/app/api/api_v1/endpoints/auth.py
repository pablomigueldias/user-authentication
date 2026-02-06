from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user_schema import UserCreate, UserResponse, Token, UserLogin
from app.services.auth_service import AuthService
from app.core.security import create_access_token

router = APIRouter()


@router.post('/signup', response_model=UserResponse, status_code=201)
async def create_user_signup(user_in: UserCreate) -> Any:
    user = await AuthService.register_user(user_in)
    return user


@router.post('/login', response_model=Token)
async def login_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:

    user = await AuthService.auhenticate_user(
        UserLogin(email=form_data.username, password=form_data.password)
    )

    access_token = create_access_token(subject=user.email)

    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }
