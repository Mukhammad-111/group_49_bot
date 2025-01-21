from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


order_food_router = Router()


class Order(StatesGroup):
    name = State()
    tel_number = State()
    address = State()
    order_food = State()


@order_food_router.callback_query(F.data == "order_food")
async def start_order(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Как вас зовут?")
    await state.set_state(Order.name)


@order_food_router.message(Order.name)
async def process_name(message: types.Message, state: FSMContext):
    await message.answer("Напишите номер телефона:")
    await state.set_state(Order.tel_number)


@order_food_router.message(Order.tel_number)
async def process_tel_number(message: types.Message, state: FSMContext):
    await message.answer("Напишите пожалюста адрес которую мы доставим еду")
    await state.set_state(Order.address)


@order_food_router.message(Order.address)
async def process_address(message: types.Message, state: FSMContext):
    await message.answer("Что вы хотите заказать")
    await state.set_state(Order.order_food)


@order_food_router.message(Order.order_food)
async def process_order_food(message: types.Message, state: FSMContext):
    await message.answer("Ваш заказ принято, ваш заказ бутдет отправлено через 15 минут")
    await state.clear()


