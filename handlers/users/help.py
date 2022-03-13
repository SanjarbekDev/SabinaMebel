from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from data.config import ADMINS

from loader import dp

#command help admin
@dp.message_handler(CommandHelp(),user_id=ADMINS)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/add_pic  - Rasmlar qo'shish",
            "/rek - Azolarga xabar yuborrish",
            "/menu - Rasmlarni tekshirish",
            "/clear_data - Malumotlarni tozalash")
    
    await message.answer("\n".join(text))

#command help users
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/menu - Menyuni ko'rish")
    
    await message.answer("\n".join(text))