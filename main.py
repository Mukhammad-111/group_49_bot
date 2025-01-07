from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
from dotenv import dotenv_values
import logging
from random import choice


token = dotenv_values(".env")["TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()


ides = []
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    id = message.from_user.id
    global ides
    name = message.from_user.first_name
    if id is not ides:
        ides.append(id)
        await message.answer(f'Привет, {name},наш бот обслуживает уже {len(ides)} пользователя')
    else:
        await message.answer(f'Привет, {name},наш бот обслуживает уже {len(ides)} пользователя')



@dp.message(Command("myinfo"))
async def info_handler(message: types.Message):
    id = message.from_user.id
    first_name = message.from_user.first_name
    user_name = message.from_user.username
    await message.answer(f"Ваш id: {id}")
    await message.answer(f"Ваш firstname(имя): {first_name}")
    if user_name is not None:
        await message.answer(f"Ваш username(имя пользователя): {user_name}")
    else:
        await message.answer(f"Ваш username(имя пользователя): Not")


@dp.message(Command("random"))
async def random_handler(message: types.Message):
    names = ['Li', 'Bob', 'Shrek', 'Kisame', 'Itachi', 'Gaara', 'Obito']
    await message.answer(f"Рандомное имя: {choice(names)}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())