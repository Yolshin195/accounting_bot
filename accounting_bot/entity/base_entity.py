from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
from uuid import UUID
from uuid import uuid4

from accounting_bot.config import DB_PREFIX


class BaseEntity(DeclarativeBase):

    id: Mapped["UUID"] = mapped_column(primary_key=True, default=uuid4)

    created_by: Mapped[str]
    created_date: Mapped[datetime] = mapped_column(default=datetime.now())

    last_modified_by: Mapped[str | None]
    last_modified_date: Mapped[datetime | None]

    deleted_by: Mapped[str | None]
    deleted_date: Mapped[datetime | None]

    version: Mapped[int] = mapped_column(default=1)

    @staticmethod
    def build_table_name(table_name: str) -> str:
        return f'{DB_PREFIX}_{table_name}'

    @classmethod
    def get_pk(cls):
        return f'{cls.__tablename__}.id'
