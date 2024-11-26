import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config import TOKEN_API
from telegram_bot.app.handlers.user_handlers import register_user_handlers


def register_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)


async def main() -> None:
    bot = Bot(token=TOKEN_API, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    register_handlers(dp)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as _ex:
        print(f'There is an exception - {_ex}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
