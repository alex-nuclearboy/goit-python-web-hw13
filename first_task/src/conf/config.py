from pydantic_settings import BaseSettings
from pydantic import EmailStr


class Settings(BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str = 'localhost'
    postgres_port: int = 5432
    sqlalchemy_database_url: str
    secret_key: str
    algorithm: str
    mail_username: str
    mail_password: str
    mail_from: EmailStr
    mail_port: int
    mail_server: str
    redis_host: str = 'localhost'
    redis_port: int = 6379

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
