import asyncio
import logging

from handlers.start import start_router
from handlers.menu import menu_router
from handlers.random_dishes import random_dishes_router
from dp_config import dp, bot


async def main():
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(random_dishes_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
