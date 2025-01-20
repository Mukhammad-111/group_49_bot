from aiogram import Router, types, F

menu_router = Router()


@menu_router.callback_query(F.data == "menu")
async def menu_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("""
    Блюдо 1: "Беш-бармак", "Плов", "Куурдак", "Манты"
    Блюдо 2: "Суп говядина", "Пельмен", "Борш"
    Салаты : "Аливия", "Фруктовый", "Марковный", "Шакарап"
    Напитки : "Черный чай", "Зеленный чай", "Чай с молоком", 'Кофе'""")
