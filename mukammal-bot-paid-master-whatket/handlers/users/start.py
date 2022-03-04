import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.tilKeyboard import til
from keyboards.default.Boshsahifa import boshsahifa
from handlers.users.menu import tilfunc

from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    #await message.answer("Tilni tanlang", reply_markup=til)
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username,
                                 languag=message.from_user.language_code)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    #await message.answer("Xush kelibsiz!")
    await message.answer(f"Salom {message.from_user.first_name} @RizqimUZbot da Pywhatkit funksiyasidan foydalanishingiz mumkun", reply_markup=boshsahifa)

    # ADMINGA xabar beramiz
    count = await db.count_users()
    msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

