from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from accounting_bot.entity.reference.base_reference import BaseReference

from accounting_bot.entity.reference.currency_reference import CurrencyReference
from accounting_bot.entity.user_entity import UserEntity


class AccountEntity(BaseReference):
    __tablename__ = BaseReference.build_table_name("account")

    currency_id: Mapped[UUID] = mapped_column(ForeignKey(CurrencyReference.get_pk()))
    currency: Mapped["CurrencyReference"] = relationship(foreign_keys=currency_id)

    owner_id: Mapped[UUID] = mapped_column(ForeignKey(UserEntity.get_pk()))
    owner: Mapped["UserEntity"] = relationship(foreign_keys=owner_id)
