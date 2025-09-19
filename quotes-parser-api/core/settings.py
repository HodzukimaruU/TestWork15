from pydantic_settings import BaseSettings
from pydantic import Field
from pathlib import Path


class Settings(BaseSettings):
    app_name: str = Field(..., env="APP_NAME")
    debug: bool = Field(..., env="DEBUG")

    mongo_host: str = Field(..., env="MONGO_HOST")
    mongo_port: int = Field(..., env="MONGO_PORT")
    mongo_db: str = Field(..., env="MONGO_DB")

    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: int = Field(..., env="REDIS_PORT")
    redis_db_broker: int = Field(..., env="REDIS_DB_BROKER")
    redis_db_backend: int = Field(..., env="REDIS_DB_BACKEND")


    @property
    def mongo_url(self) -> str:
        return f"mongodb://{self.mongo_host}:{self.mongo_port}"

    class Config:
        env_file = Path(__file__).resolve().parents[2] / ".env"
        print(env_file)

settings = Settings()
