from sqlalchemy.orm import Mapped

from accounting_bot.entity.base_entity import BaseEntity


class BaseReference(BaseEntity):
    __abstract__ = True

    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]
