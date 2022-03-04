from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

boshsahifa = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="/Qullanma"),
            KeyboardButton(text="/Pywhatkit")
        ],
        [
            KeyboardButton(text="Admin")
        ],
    ],
    resize_keyboard=True
)
