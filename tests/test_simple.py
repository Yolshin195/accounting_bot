import asyncio

from accounting_bot.db import async_session
from accounting_bot.repository import CurrencyReferenceRepository
from accounting_bot.entity import CurrencyReference


async def async_main():
    async with async_session() as session:
        currency_reference_repository = CurrencyReferenceRepository(session)

        rub = CurrencyReference(code="RUB", name="RUB", created_by="admin")

        await currency_reference_repository.add_one(rub)

        all_list = await currency_reference_repository.find_all()
        for c in all_list:
            print(f"{c.code} - {c.name}")


if __name__ == "__main__":
    asyncio.run(async_main())
