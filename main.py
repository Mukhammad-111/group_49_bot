import asyncio
import logging

from handlers.start import start_router
from handlers.menu import menu_router
from handlers.random_dishes import random_dishes_router
from dp_config import dp, bot
from handlers.about_as import about_as_router
from handlers.order_food import order_food_router
from handlers.review_dialog import review_router


async def main():
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(random_dishes_router)
    dp.include_router(about_as_router)
    dp.include_router(order_food_router)
    dp.include_router(review_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
