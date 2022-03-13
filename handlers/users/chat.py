from loader import dp,bot,db
from aiogram.utils import exceptions
import asyncio
from aiogram.types import Message,CallbackQuery,ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext,filters
from states.admin_state import admin
from keyboards.default.chat_button import ChatEnd
from data.config import ADMINS

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('broadcast')

SIGNATURE='\n@Billurmebeluz\nhttps://vm.tiktok.com/ZSJfNkHYM/'

#start chat
@dp.callback_query_handler(text='ChatStart',user_id=ADMINS)
async def chat_start(call:CallbackQuery,state:FSMContext):
    await call.message.answer("<b>👩‍✈️Unutmang siz adminsiz‼️\nBu xizmat oddiy foydalanuvchilar uchun.</b>\nYordam:👉 /help")

@dp.callback_query_handler(text='ChatStart')
async def chat_start(call:CallbackQuery,state:FSMContext):
    await call.message.answer("✉️Xabar yuborishingiz mumkin",reply_markup=ChatEnd)
    await state.set_state(admin.CHAT_A)

#end admin chat
@dp.message_handler(text='📨Chatni yakunlash',state=admin.CHAT_A)
async def chat_start(msg:Message,state:FSMContext):
    await msg.answer("✅Chat yakunlandi.",reply_markup=ReplyKeyboardRemove())
    await state.finish()

#meessage handle
@dp.message_handler(state=admin.CHAT_A)
async def chat_start(msg:Message,state:FSMContext):
    user=msg.from_user.get_mention()
    await bot.send_message(chat_id=ADMINS[0],text=f"<b>🛎 Yangi xabar!!\nFoydalanuvchi {user}</b>")
    await bot.send_message(chat_id=ADMINS[0],text=f"<b>📄Xabar matni:</b>\n\n{msg.text}")
    await msg.answer(text="<b>Xabaringiz adminnga yetkazildi,admin javobini kuting.\nBoshqa xabar jo'natmasangiz chatni yakunlash tugmasini bosing</b>",parse_mode='HTML')


#reklama

@dp.message_handler(commands='rek',user_id=ADMINS)
async def send_message(msg:Message,state:FSMContext):
    await msg.answer("Matin,rasim yoki video yuborishingiz mumkin❗️")
    await state.set_state(admin.RekUsers)
    
        
#send text
@dp.message_handler(state=admin.RekUsers,user_id=ADMINS)
async def send_text_users(msg:Message,state:FSMContext):
    message=msg.text
    users = await db.select_all_users()
    for user in users:
        user_id = user[3]
        try:
            await bot.send_message(chat_id=user_id, text=f"{message}\n@sabina_mebel")
        except exceptions.BotBlocked:
            log.error(f"Target [ID:{user_id}]: blocked by user")
        except exceptions.ChatNotFound:
            log.error(f"Target [ID:{user_id}]: invalid user ID")
        except exceptions.RetryAfter as e:
            log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
            await asyncio.sleep(e.timeout)
            await bot.send_message(chat_id=user_id, text=f"{message}\n@sabina_mebel") # Recursive call
        except exceptions.UserDeactivated:
            log.error(f"Target [ID:{user_id}]: user is deactivated")
        except exceptions.TelegramAPIError:
            log.exception(f"Target [ID:{user_id}]: failed")
        else:
            log.info(f"Target [ID:{user_id}]: success")
            
    await msg.answer("✅Xabar barcha foydalanuvchilarga yuborildi")
    await state.finish()

#send photo
@dp.message_handler(content_types='photo',state=admin.RekUsers,user_id=ADMINS)
async def send_photo_users(msg:Message,state:FSMContext):
    photo=msg.photo[-1].file_id
    if msg.caption==None:
        caption=SIGNATURE
    else:
        caption=f"{msg.caption}\n{SIGNATURE}"
    users = await db.select_all_users()
    for user in users:
        user_id = user[3]
        try:
            await bot.send_photo(chat_id=user_id, photo=photo,caption=caption)
        except exceptions.BotBlocked:
            log.error(f"Target [ID:{user_id}]: blocked by user")
        except exceptions.ChatNotFound:
            log.error(f"Target [ID:{user_id}]: invalid user ID")
        except exceptions.RetryAfter as e:
            log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
            await asyncio.sleep(e.timeout)
            await bot.send_photo(chat_id=user_id, photo=photo,caption=caption) # Recursive call
        except exceptions.UserDeactivated:
            log.error(f"Target [ID:{user_id}]: user is deactivated")
        except exceptions.TelegramAPIError:
            log.exception(f"Target [ID:{user_id}]: failed")
        else:
            log.info(f"Target [ID:{user_id}]: success")
    await msg.answer("✅Rasim barcha foydalanuvchilarga yuborildi")
    await state.finish()

#send video

@dp.message_handler(content_types='video',state=admin.RekUsers,user_id=ADMINS)
async def send_photo_users(msg:Message,state:FSMContext):
    video=msg.video.file_id
    if msg.caption==None:
        caption=SIGNATURE
    else:
        caption=f"{msg.caption}\n{SIGNATURE}"
    users = await db.select_all_users()
    for user in users:
        user_id = user[3]
        try:
            await bot.send_video(chat_id=user_id,video=video,caption=caption)
        except exceptions.BotBlocked:
            log.error(f"Target [ID:{user_id}]: blocked by user")
        except exceptions.ChatNotFound:
            log.error(f"Target [ID:{user_id}]: invalid user ID")
        except exceptions.RetryAfter as e:
            log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
            await asyncio.sleep(e.timeout)
            await bot.send_video(chat_id=user_id,video=video,caption=caption) # Recursive call
        except exceptions.UserDeactivated:
            log.error(f"Target [ID:{user_id}]: user is deactivated")
        except exceptions.TelegramAPIError:
            log.exception(f"Target [ID:{user_id}]: failed")
        else:
            log.info(f"Target [ID:{user_id}]: success") 
    await msg.answer("✅Video barcha foydalanuvchilarga yuborildi")
    await state.finish()