from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup

from database import Database
from dp_config import database

food_admin_router = Router()


class Food(StatesGroup):
    name = State()
    price = State()
    description = State()
    category = State()
    serving_options = State()


@food_admin_router.message(Command("new_food"))
async def new_food(message: types.Message, state: FSMContext):
    await message.answer("Напишите название блюда(напитка)")
    await state.set_state(Food.name)


@food_admin_router.message(Food.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Введите цену блюда(напитка)")
    await state.set_state(Food.price)


@food_admin_router.message(Food.price)
async def process_price(message: types.Message, state: FSMContext):
    price = message.text
    if not price.isdigit():
        await message.answer("Введите только цифру !")
        return
    await state.update_data(price=price)
    await message.answer("Напишите описание")
    await state.set_state(Food.description)


@food_admin_router.message(Food.description)
async def process_description(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description)
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Первое", callback_data="first"
                ),
                types.InlineKeyboardButton(
                    text="Второе", callback_data="second"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Горячие напитки", callback_data="hot_drinks"
                ),
                types.InlineKeyboardButton(
                    text="Холодные напитки", callback_data="cold_drinks"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Салаты", callback_data="salads"
                ),
                types.InlineKeyboardButton(
                    text="Пицца", callback_data="pizza"
                )
            ]
        ]
    )
    await message.answer("Выберите категорию", reply_markup=keyboard)
    await state.set_state(Food.category)


@food_admin_router.callback_query(Food.category)
async def process_category(callback: types.CallbackQuery, state: FSMContext):
    category = callback.data
    await state.update_data(category=category)
    await callback.message.answer("Варианты порций")
    await state.set_state(Food.serving_options)


@food_admin_router.message(Food.serving_options)
async def process_serving_options(message: types.Message, state: FSMContext):
    serving_options = message.text
    await state.update_data(serving_options=serving_options)
    await message.answer("Новое блюдо(напиток) успешно сохранено")
    data = await state.get_data()
    print(data)
    database.save_dishes(data)
    await state.clear()