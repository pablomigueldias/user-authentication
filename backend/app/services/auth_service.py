from fastapi import HTTPException, status
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserLogin
from app.core.security import get_password_hash, verify_password

class AuthService:
    @staticmethod
    async def register_user(user_in: UserCreate) -> User:
        exist_user =  await User.find_one(User.email == user_in.email)

        if exist_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Email ja cadastrado no sistema.'
            )
        
        exist_username = await User.find_one(User.username==user_in.username)
        if exist_username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Username já está em uso.'
            )
        
        user = User(
            username=user_in.username,
            email=user_in.email,
            hashed_password=get_password_hash(user_in.password)
        )
        await user.insert()
        return user
    
    @staticmethod
    async def auhenticate_user(login_data: UserLogin):
        user = await User.find_one(User.email == login_data.email)

        if not user or not verify_password(login_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Email ou senha incorreto',
                headers={'WWW-Authenticate':'Bearer'},
            )
        
        return user
