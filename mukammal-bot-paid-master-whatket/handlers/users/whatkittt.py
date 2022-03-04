import pywhatkit
from aiogram.dispatcher.filters import Command

from aiogram import types
from loader import dp



@dp.message_handler(Command("Pywhatkit"))
async def bot_pyehat(message: types.Message):
    if message.text == "/Pywhatkit":
        await message.answer("Pywhatkit botga hush kelibsiz!\n"
                             "Matn kiriting!")



@dp.message_handler()
async def what(message: types.Message):
    #if message.text == "/Pywhatkit":
    pywhatkit.text_to_handwriting(message.text,
                        "c:/Users/User/Desktop/Botlar/mukammal-bot-paid-master-whatket/img/rasm1.png",rgb=(0,0,255))

    await message.answer("Rasm tayyor!\nRasmni olish -> /rasm")