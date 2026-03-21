from typing import TYPE_CHECKING, Any

import discord
from discord import ui

from app.core.error_handler import handle_error

if TYPE_CHECKING:
    from app.types import Interaction


class LayoutView(ui.LayoutView):
    async def on_error(
        self, i: Interaction, error: Exception, _item: ui.Item[Any]
    ) -> None:
        return await handle_error(i, error)


class View(ui.View):
    async def on_error(
        self, i: Interaction, error: Exception, _item: ui.Item[Any]
    ) -> None:
        return await handle_error(i, error)


class Container[V: LayoutView](ui.Container):
    view: V

    def __init__(
        self,
        *children: ui.Item[Any],
        spoiler: bool = False,
        id: int | None = None,  # noqa: A002
    ) -> None:
        super().__init__(
            *children, accent_colour=discord.Color.blurple(), spoiler=spoiler, id=id
        )


class Modal(ui.Modal):
    async def on_error(self, i: Interaction, error: Exception) -> None:
        return await handle_error(i, error)


class Label[C: ui.Item[Any]](ui.Label):
    component: C


class TextDisplay(ui.TextDisplay):
    pass


class TextInput(ui.TextInput):
    pass


class Button(ui.Button):
    pass


class Select(ui.Select):
    pass


class ActionRow(ui.ActionRow):
    pass


class FileUpload(ui.FileUpload):
    pass


class ChannelSelect(ui.ChannelSelect):
    pass
