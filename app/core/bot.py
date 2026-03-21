import anyio
import discord
from discord.ext import commands
from loguru import logger

from app.core.command_tree import CommandTree


class MyBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        super().__init__(
            command_prefix=commands.when_mentioned, intents=intents, tree_cls=CommandTree
        )

    async def _load_cogs(self) -> None:
        async for filepath in anyio.Path("app/cogs").glob("**/*.py"):
            cog_name = filepath.stem

            try:
                await self.load_extension(f"app.cogs.{cog_name}")
                logger.info(f"Loaded cog {cog_name!r}")
            except Exception:
                logger.exception(f"Failed to load cog {cog_name!r}")

        await self.load_extension("jishaku")

    async def setup_hook(self) -> None:
        await self._load_cogs()
