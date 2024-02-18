from sqlalchemy.orm import Mapped, mapped_column

from accounting_bot.entity.base_entity import BaseEntity


class UserEntity(BaseEntity):
    __tablename__ = BaseEntity.build_table_name("user")

    telegram_id: Mapped[int] = mapped_column(unique=True, index=True, nullable=False)
    username: Mapped[str]
