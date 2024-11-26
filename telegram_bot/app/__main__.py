import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from app.config.config import TOKEN_API
from app.handlers.user_handlers import register_user_handlers







def register_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)


async def main() -> None:
    bot = Bot(token=TOKEN_API, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    register_handlers(dp)

    try:
        await dp.start_polling(bot)
    except Exception as _ex:
        print(f'There is an exception - {_ex}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
