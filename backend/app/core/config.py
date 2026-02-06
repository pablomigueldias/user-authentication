from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import MongoDsn, computed_field
from typing import Optional



class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file='.env',
        env_ignore_empty=True,
        extra='ignore'
    )

    SECRET_KEY: str = "admin123"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    MONGO_URI: Optional[str] = None

    MONGO_HOST: str = "localhost"
    MONGO_PORT: int = 27017
    MONGO_USER: str = "admin"
    MONGO_PASS: str = "password"
    MONGO_DB: str = "auth_db"

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Auth System"

    @computed_field
    def mongo_uri_computed(self) -> MongoDsn:
        if self.MONGO_URI:
            return self.MONGO_URI #type: ignore

        return MongoDsn.build(
            scheme='mongodb',
            username=self.MONGO_USER,
            password=self.MONGO_PASS,
            host=self.MONGO_HOST,
            port=self.MONGO_PORT,
            path=f'{self.MONGO_DB}?authSource=admin',
        )


settings = Settings()
