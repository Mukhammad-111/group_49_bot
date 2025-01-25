import asyncio
import logging

from handlers.start import start_router
from handlers.menu import menu_router
from handlers.random_dishes import random_dishes_router
from dp_config import dp, bot, database
from handlers.about_as import about_as_router
from handlers.order_food import order_food_router
from handlers.review_dialog import review_router
from aiogram import Bot
from handlers.food_management import food_admin_router
from handlers.dishes import dishes_router


async def on_startup(bot: Bot):
    database.create_tables()


async def main():
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(random_dishes_router)
    dp.include_router(about_as_router)
    dp.include_router(order_food_router)
    dp.include_router(review_router)
    dp.startup.register(on_startup)
    dp.include_router(food_admin_router)
    dp.include_router(dishes_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
