import datetime

from app.constants import UTC8


def get_utc8_now() -> datetime.datetime:
    return datetime.datetime.now(UTC8)
