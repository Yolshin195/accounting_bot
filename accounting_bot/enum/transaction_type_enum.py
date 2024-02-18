from enum import Enum


class TransactionTypeEnum(Enum):
    EXPENSE = "expense"
    INCOME = "income"
    TRANSFER = "transfer"
