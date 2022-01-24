from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOSTNAME: str
    DB_PORT: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    SECRETE_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()
