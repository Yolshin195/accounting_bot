from accounting_bot.repository import UserRepository
from accounting_bot.service.entity_service.base_entity_service import BaseEntityService


class UserEntityService(BaseEntityService):
    def __init__post__(self):
        self.user_repository = UserRepository(self.session)

