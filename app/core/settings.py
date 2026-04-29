from typing import Literal

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    discord_token: str
    env: Literal["dev", "prod"]

    postgres_password: str
    postgres_db: str = "bot"
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_user: str = "postgres"

    @property
    def database_url(self) -> str:
        return f"asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"

    @property
    def is_dev(self) -> bool:
        return self.env == "dev"


load_dotenv()
SETTINGS = Settings()  # pyright: ignore[reportCallIssue]
