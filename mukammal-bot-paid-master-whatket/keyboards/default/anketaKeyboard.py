from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

anketa = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="/form")
        ],
        [
          KeyboardButton(text="Orqaga")
        ],
    ],
    resize_keyboard=True
)