from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

from accounting_bot.repository import UserRepository


class CurrentUserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        telegram_user: User = data["event_from_user"]
        user_repository = UserRepository(data['session'])
        data["current_user"] = await user_repository.get_or_create(telegram_id=telegram_user.id,
                                                                   username=telegram_user.username)
        return await handler(event, data)
