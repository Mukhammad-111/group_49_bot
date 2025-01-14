from aiogram import Router, F, types


about_as_router = Router()


@about_as_router.callback_query(F.data == "about_as")
async def about_as_handler(callback: types.CallbackQuery):
    await callback.message.answer("""
    Мы - кафе <<Лидер>> 
    Адрес: улица Пушкина 18
    График: 08:00 - 23:00 без выходной""")
