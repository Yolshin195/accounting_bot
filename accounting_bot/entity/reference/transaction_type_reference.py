from accounting_bot.entity.reference.base_reference import BaseReference


class TransactionTypeReference(BaseReference):
    __tablename__ = BaseReference.build_table_name("transaction_type_reference")
