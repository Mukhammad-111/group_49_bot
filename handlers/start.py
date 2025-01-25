from aiogram import Router, types, F
from aiogram.filters import Command



start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Наше местоположение",
          url="https://2gis.ru/firm/70000001080310560/66.495202%2C55.273873?m=66.495146%2C55.274057%2F15.87")
            ],
            [
                types.InlineKeyboardButton(
                    text="Меню", callback_data="menu"
                ),
                types.InlineKeyboardButton(
                    text="Рандомные блюдо", callback_data="random_dish"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="О нас", callback_data="about_as"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Заказать еду", callback_data="order_food"
                ),
                types.InlineKeyboardButton(
                    text="Оставить отзыв", callback_data="review"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Наши блюдо", callback_data="dishes"
                )
            ]
        ]
    )
    await message.answer(f'Приветствую вас {name}, добро пожаловать в наш бот << кафе Лидера >>',
                         reply_markup=keyboard)

