from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

til = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="🇺🇿 uz"),
            KeyboardButton(text="🇷🇺 ru"),
            KeyboardButton(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 eng")
        ],

    ],
    resize_keyboard=True
)

