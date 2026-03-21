from typing import TYPE_CHECKING

from loguru import logger

from app.core.embeds import ErrorEmbed

if TYPE_CHECKING:
    from app.types import Interaction


async def handle_error(i: Interaction, error: Exception) -> None:
    original = getattr(error, "original", None)
    e = original or error
    logger.exception("Error occurred", exc_info=e)
    embed = ErrorEmbed(
        title="發生錯誤了",
        description="發生了一些預期之外的錯誤, 請稍後再試一次\n如果問題持續存在, 請聯繫開發者",
    )

    if i.response.is_done():
        await i.followup.send(embed=embed, ephemeral=True)
    else:
        await i.response.send_message(embed=embed, ephemeral=True)
