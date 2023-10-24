from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    POSTGRES_USER: str
    POSTGRES_HOST: str
    POSTGRES_DB: str

    class Config:
        env_file = ".env"


settings = Settings()
