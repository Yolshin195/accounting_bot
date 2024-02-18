from .base_reference import BaseReference


class CurrencyReference(BaseReference):
    __tablename__ = BaseReference.build_table_name("currency_reference")
