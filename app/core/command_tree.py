from typing import TYPE_CHECKING

from discord import app_commands

from app.core.error_handler import handle_error

if TYPE_CHECKING:
    from app.types import Interaction


class CommandTree(app_commands.CommandTree):
    async def on_error(
        self, i: Interaction, error: app_commands.AppCommandError
    ) -> None:
        await handle_error(i, error)
