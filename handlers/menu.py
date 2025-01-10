from aiogram import Router, types
from aiogram.filters import Command

menu_router = Router()


@menu_router.message(Command("menu"))
async def menu_handler(message: types.Message):
    await message.answer(f'Блюдо 1: "Беш-бармак", "Плов", "Куурдак", "Манты"')
    await message.answer(f'Блюдо 2: "Суп говядина", "Пельмен", "Борш"')
    await message.answer(f'Салаты : "Аливия", "Фруктовый", "Марковный", "Шакарап"')
    await message.answer(f'Напитки : "Черный чай", "Зеленный чай", "Чай с молоком", "Кофе"')

