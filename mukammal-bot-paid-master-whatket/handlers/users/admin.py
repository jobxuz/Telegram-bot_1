import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = await db.select_all_users()
    await message.answer(users)


@dp.message_handler(text="/count", user_id=ADMINS)
async def get_countt_users(message: types.Message):
    count = await db.count_users()
    await message.answer(f"Botda {count} ta foydalanuvchi bor")



@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        # print(user[3])
        user_id = user[4]
        await bot.send_message(chat_id=user_id, text="@SariqDev kanaliga obuna bo'ling!")
        await asyncio.sleep(0.05)

