from discord import Embed


class DefaultEmbed(Embed):
    def __init__(
        self, *, title: str | None = None, description: str | None = None, url: str | None = None
    ) -> None:
        super().__init__(color=0x57AEC2, title=title, description=description, url=url)


class ErrorEmbed(Embed):
    def __init__(
        self, *, title: str | None = None, description: str | None = None, url: str | None = None
    ) -> None:
        super().__init__(color=0xCF3055, title=title, description=description, url=url)
