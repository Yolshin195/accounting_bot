from accounting_bot.entity import TransactionEntity
from accounting_bot.repository.base_repository import BaseRepository


class TransactionRepository(BaseRepository):
    model: TransactionEntity = TransactionEntity