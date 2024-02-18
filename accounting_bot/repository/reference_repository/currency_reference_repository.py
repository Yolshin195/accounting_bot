from accounting_bot.entity import CurrencyReference
from accounting_bot.repository.reference_repository.base_reference_repository import BaseReferenceRepository


class CurrencyReferenceRepository(BaseReferenceRepository):
    model: CurrencyReference = CurrencyReference
