from .base_reference import BaseReference


class CategoryReference(BaseReference):
    __tablename__ = BaseReference.build_table_name("category_reference")
