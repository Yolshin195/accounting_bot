from decimal import Decimal
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from accounting_bot.entity.base_entity import BaseEntity

from accounting_bot.entity.user_entity import UserEntity
from accounting_bot.entity.account_entity import AccountEntity
from accounting_bot.entity.reference.transaction_type_reference import TransactionTypeReference
from accounting_bot.entity.reference.category_reference import CategoryReference


class TransactionEntity(BaseEntity):
    __tablename__ = BaseEntity.build_table_name("transaction")

    owner_id: Mapped[UUID] = mapped_column(ForeignKey(UserEntity.get_pk()))
    owner: Mapped["UserEntity"] = relationship(foreign_keys=owner_id)

    type_id: Mapped[UUID] = mapped_column(ForeignKey(TransactionTypeReference.get_pk()))
    type: Mapped["TransactionTypeReference"] = relationship(foreign_keys=type_id)

    category_id: Mapped[UUID] = mapped_column(ForeignKey(CategoryReference.get_pk()))
    category: Mapped["CategoryReference"] = relationship(foreign_keys=category_id)

    account_id: Mapped[UUID | None] = mapped_column(ForeignKey(AccountEntity.get_pk()))
    account: Mapped["AccountEntity"] = relationship(foreign_keys=account_id)

    value: Mapped[Decimal] = mapped_column(default=lambda: Decimal("0.0"))

    comment: Mapped[str | None]
