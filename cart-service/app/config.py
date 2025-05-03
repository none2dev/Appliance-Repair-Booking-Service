from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, Field, field_validator
from typing import Optional, Any


class Settings(BaseSettings):
    # Database settings
    POSTGRES_HOST: str = Field(..., env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(..., env="POSTGRES_PORT")
    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field(..., env="POSTGRES_DB")
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    
    # Auth settings
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = Field(default="HS256", env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    ADMIN_CREATION_SECRET: str = Field(..., env="ADMIN_CREATION_SECRET")
    ALLOW_ADMIN_CREATION: bool = Field(default=False, env="ALLOW_ADMIN_CREATION")

    # App settings
    DEBUG: bool = Field(default=False, env="DEBUG")

    @field_validator("DATABASE_URL", mode='before')
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], values: dict) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            username=values["POSTGRES_USER"],
            password=values["POSTGRES_PASSWORD"],
            host=values["POSTGRES_HOST"],
            port=values["POSTGRES_PORT"],
            path=f"/{values.get('POSTGRES_DB', '')}",
        )


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()