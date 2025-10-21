from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str | None = None
    db_user: str | None = None
    db_pass: str | None = None
    db_host: str | None = None
    db_port: int | None = None
    db_name: str | None = None

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"

settings = Settings()