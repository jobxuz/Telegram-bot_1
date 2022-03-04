import asyncpg
from aiogram import types
from aiogram.dispatcher.filters import Command,Text
from aiogram.types import Message , ReplyKeyboardRemove
from keyboards.default.anketaKeyboard import anketa

from loader import dp, db, bot

@dp.message_handler(text="🇺🇿 uz")
async def tilfunc(message: Message):
    await message.answer(f" {message.from_user.first_name} @RizqimUZbot ga hush kelibsiz")


