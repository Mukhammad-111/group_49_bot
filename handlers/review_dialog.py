from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

review_router = Router()


class CafeReview(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    extra_comments = State()


reviewed_users = []

@review_router.callback_query(F.data == "review")
async def start_review(callback: types.CallbackQuery, state: FSMContext):
    id_user = callback.from_user.id
    if id_user in reviewed_users:
        await callback.message.answer('Нельзя оставлять отзыв более одного раза')
        await state.clear()
        return
    await callback.message.answer("Как вас зовут?")
    await state.set_state(CafeReview.name)


@review_router.message(CafeReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await message.answer("Ваш номер телефона")
    await state.set_state(CafeReview.phone_number)


@review_router.message(CafeReview.phone_number)
async def process_number(message: types.Message, state: FSMContext):
    await message.answer("поставьте нам оценку от 1 до 5")
    await state.set_state(CafeReview.rate)


@review_router.message(CafeReview.rate)
async def process_rate(message: types.Message, state: FSMContext):
    await message.answer("Дополнительные комментарии или жалоба")
    await state.set_state(CafeReview.extra_comments)


@review_router.message(CafeReview.extra_comments)
async def process_comments(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за вашу отзыв")
    reviewed_users.append(message.from_user.id)
    await state.clear()
