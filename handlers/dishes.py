from aiogram import Router, types, F
from dp_config import database

dishes_router = Router()


@dishes_router.callback_query(F.data == "dishes")
async def dishes_handler(callback: types.CallbackQuery):
    await callback.message.answer("Наши блюдо")
    dishes_list = database.get_dishes()
    for dish in dishes_list:
        await callback.message.answer(f"Блюдо: {dish.get('name')} Цена: {dish.get('price')}")
