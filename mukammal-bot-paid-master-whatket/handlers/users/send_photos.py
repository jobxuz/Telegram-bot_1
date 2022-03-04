from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp ,bot


@dp.message_handler(Command("rasm"))
async def rasm(message: types.Message):
    photo_fild = InputFile(path_or_bytesio="img/rasm1.png")
    await message.reply_photo(photo_fild,caption="Siz kiritgan matn!")