from aiogram import Router, types, F
from aiogram.filters import Command
from datetime import timedelta


group_router = Router()
group_router.message.filter(F.chat.type != "private")


FORBIDDEN_WORDS = ("жирный", "мырк", "неуклюжий", "сирота")


@group_router.message(Command("ban", prefix="!"))
@group_router.message(F.text == "ban")
async def command_handler(message: types.Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        await message.chat.ban(
            user_id=user.id,
            until_date=timedelta(days=1, hours=3, weeks=3, minutes=10)
        )


@group_router.message(F.text)
async def text_ban_handler(message: types.Message):
    for word in FORBIDDEN_WORDS:
        if word in message.text.lower():
            autor_id = message.from_user.id
            autor_name = message.from_user.first_name
            await message.answer(f"{autor_name},вы были забанены за такое слова {word}")
            await message.chat.ban(autor_id)
