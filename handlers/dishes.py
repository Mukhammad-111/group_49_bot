from aiogram import Router, types, F
from dp_config import database
from aiogram_widgets.pagination import TextPaginator


dishes_router = Router()


@dishes_router.callback_query(F.data == "dishes_with_photo")
async def dishes_with_photo_handler(callback: types.CallbackQuery):
    await callback.message.answer("Наши блюдо")
    dishes_list = database.get_dishes()
    for dish in dishes_list:
        photo = dish.get("photo")

        kb = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text="В избранный", callback_data=f"favourite{dish['id']}"
                    )
                ]
            ]
        )
        await callback.message.answer_photo(
            photo=photo,
            caption= f"Название: {dish.get('name', 'Без название')}\nЦена: {dish.get('price')}\nОписание:"
                     f" {dish.get('description')}\nКатегория: {dish.get('category')}", reply_markup=kb
        )


@dishes_router.callback_query(F.data == "dishes_with_pagination")
async def dishes_with_pagination_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Наши блюдо")
    dishes_list = database.get_dishes()
    text_data = [
        f"Название: {dish.get('name', 'Без название')}\nЦена: {dish.get('price')}\nОписание:"
        f" {dish.get('description')}\nКатегория: {dish.get('category')}" for dish in dishes_list
    ]
    paginator = TextPaginator(data=text_data, router=dishes_router, per_page=1)
    current_text_chunk, reply_markup = paginator.current_message_data
    await callback.message.answer(
        text=current_text_chunk,
        reply_markup=reply_markup
    )
