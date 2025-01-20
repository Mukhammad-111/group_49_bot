from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database import Database
from dp_config import database

review_router = Router()


class CafeReview(StatesGroup):
    name = State()
    date = State()
    phone_number = State()
    rate = State()
    extra_comments = State()


@review_router.message(Command("stop"))
@review_router.message(F.text == "стоп")
async def stop_dialog(message: types.Message, state: FSMContext):
    await message.answer("Диалог остановлен")
    await state.clear()


reviewed_users = []


@review_router.callback_query(F.data == "review")
async def start_review(callback: types.CallbackQuery, state: FSMContext):
    id_user = callback.from_user.id
    if id_user in reviewed_users:
        await callback.message.answer('Нельзя оставлять отзыв более одного раза')
        await state.clear()
        return
    await callback.message.answer("Оставьте отзыв ответив на несколько вопросов. Можете остановить "
                                  "диалог с ботом введя '/stop' или 'стоп'")
    await callback.message.answer("Как вас зовут?")
    await state.set_state(CafeReview.name)


@review_router.message(CafeReview.name)
async def process_number(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Напишите сегодняшнюю дату")
    await state.set_state(CafeReview.date)

@review_router.message(CafeReview.date)
async def process_number(message: types.Message, state: FSMContext):
    date = message.text
    await state.update_data(date=date)
    await message.answer("Напишите вашу номер телефона")
    await state.set_state(CafeReview.phone_number)


@review_router.message(CafeReview.phone_number)
async def process_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="1", callback_data="rating:1"
                ),
                types.InlineKeyboardButton(
                    text="2", callback_data="rating:2"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="3", callback_data="rating:3"
                ),
                types.InlineKeyboardButton(
                    text="4", callback_data="rating:4"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="5", callback_data="rating:5"
                )
            ]
        ]
    )
    await message.answer("поставьте нам оценку от 1 до 5", reply_markup=kb)
    await state.set_state(CafeReview.rate)


@review_router.callback_query(F.data.startswith("rating:"))
async def process_rate(callback: types.CallbackQuery, state: FSMContext):
    rate = int(callback.data.split(":")[1])
    await state.update_data(rate=rate)
    await callback.message.answer("Дополнительные комментарии или жалоба")
    await state.set_state(CafeReview.extra_comments)


@review_router.message(CafeReview.extra_comments)
async def process_comments(message: types.Message, state: FSMContext):
    extra_comments = message.text
    await state.update_data(extra_comments=extra_comments)
    data = await state.get_data()
    await message.answer("Спасибо за вашу отзыв")
    reviewed_users.append(message.from_user.id)
    print(data)
    database.save_reviews(data)
    await state.clear()
