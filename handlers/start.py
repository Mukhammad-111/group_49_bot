from aiogram import Router, types, F
from aiogram.filters import Command



start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.reply(f'Приветствую вас {name}, добро пожаловать в наш бот << кафе Лидера >> ')
    await message.answer(f'Наш график 08:00 - 23:00 без выходой')
    await message.answer(f'В нашем боте есть команды: ( /menu, /random_dishes ) ')
