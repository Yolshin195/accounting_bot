from .base_reference_repository import BaseReferenceRepository
from accounting_bot.entity import CategoryReference


class CategoryReferenceRepository(BaseReferenceRepository):
    model: CategoryReference = CategoryReference
