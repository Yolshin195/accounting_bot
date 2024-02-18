from dataclasses import dataclass
from decimal import Decimal


@dataclass
class ExpenseCommand:
    telegram_id: int
    category_code: str
    value: Decimal
    comment: str | None


class ExpenseTransactionService:

    def __init__(self, command: ExpenseCommand):
        self.command = command

    def execute(self):
        user = self.get_user(self.command.telegram_id)
        pass

    def get_user(self, telegram_id: int):
        pass

    def get_category(self, ):
        pass

    def create_transaction(self):
        pass
