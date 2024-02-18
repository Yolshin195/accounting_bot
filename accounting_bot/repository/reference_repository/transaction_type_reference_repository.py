from accounting_bot.entity import TransactionTypeReference
from accounting_bot.enum.transaction_type_enum import TransactionTypeEnum
from accounting_bot.repository.reference_repository.base_reference_repository import BaseReferenceRepository


class TransactionTypeReferenceRepository(BaseReferenceRepository):
    model: BaseReferenceRepository = TransactionTypeReference

    async def find_by_type(self, transaction_type: TransactionTypeEnum):
        return await self.find_by_code(transaction_type.value)
