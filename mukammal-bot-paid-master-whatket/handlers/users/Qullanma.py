from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from keyboards.default.anketaKeyboard import anketa
from keyboards.default.Boshsahifa import boshsahifa


@dp.message_handler(Command("Qullanma"))
async def bot_echo(message: types.Message):
    text = f"Salom {message.from_user.first_name}\n" \
           f"Pywhatkit orqali kiritgan matningizni qulda yozilgan matn qilib tahrirlashingiz mumkun.Matn rasm ko'rinshda qaytariladi"
    await message.answer(text)



@dp.message_handler(text="Admin")
async def anketaa(message: types.Message):
    text = "Admin bilan bog'lanish uchun form ni bosing va suralgan narsalarni kiriting:"
    await message.answer(text,reply_markup=anketa)


@dp.message_handler(text="Orqaga")
async def orqaga(message: types.Message):
    text = "Bosh menu"
    await message.answer(text,reply_markup=boshsahifa)