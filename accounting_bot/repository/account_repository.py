from accounting_bot.entity import AccountEntity
from accounting_bot.repository.base_repository import BaseRepository


class AccountRepository(BaseRepository):
    model: AccountEntity = AccountEntity
