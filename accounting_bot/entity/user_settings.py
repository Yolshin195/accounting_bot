from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .user_entity import UserEntity
from .account_entity import AccountEntity
from .base_entity import BaseEntity


class UserSettings(BaseEntity):
    __tablename__ = BaseEntity.build_table_name("user_settings")

    owner_id: Mapped[UUID] = mapped_column(ForeignKey(UserEntity.get_pk()))
    owner: Mapped["UserEntity"] = relationship(foreign_keys=owner_id)

    current_account_id: Mapped[UUID] = mapped_column(ForeignKey(AccountEntity.get_pk()))
    current_account: Mapped["AccountEntity"] = relationship(foreign_keys=current_account_id)
