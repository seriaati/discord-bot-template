from tortoise import Tortoise

from app.core.settings import SETTINGS

TORTOISE_ORM = {
    "connections": {"default": SETTINGS.database_url},
    "apps": {
        "models": {
            "models": ["app.db.models"],
            "default_connection": "default",
            "migrations": "migrations",
        }
    },
    "use_tz": True,
    "timezone": "Asia/Taipei",
}


class Database:
    async def connect(self) -> None:
        await Tortoise.init(TORTOISE_ORM)

    async def close(self) -> None:
        await Tortoise.close_connections()

    async def __aenter__(self) -> Database:
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:  # noqa: ANN001
        await self.close()
