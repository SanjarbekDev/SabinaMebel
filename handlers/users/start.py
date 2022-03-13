import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.container import container_user
from aiogram.dispatcher import FSMContext
import logging as log

from loader import dp, db, bot
from data.config import ADMINS

#command start admin
@dp.message_handler(CommandStart(),user_id=ADMINS)
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    count = await db.count_users()
    await message.answer(f"Xush kelibsiz Admin!\nBotda {count}ta foydalanuvchi bor")

#menu command
@dp.message_handler(commands='menu')
async def menu(msg:types.Message):
    await msg.answer(text='Kategoryani tanlang',reply_markup=container_user)

#command start users
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    first_name=message.from_user.first_name
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer(f"<b>🧑‍✈️Assalomu aleykum {first_name} botga xush kelibsiz!\n📋Menyuni tanlang</b>",reply_markup=container_user)

    # ADMINGA xabar beramiz
    count = await db.count_users()
    msg = f"{user[1]} Botga qo'shildi.\nBotda {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

#info file
@dp.callback_query_handler(text='container1')
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    try:
        photos=await db.select_all_capture1()
        for photo in photos:
            file_id=photo[1]
            text=photo[2]
            try:
                await call.message.answer_photo(photo=file_id,caption=text)
            except:
                log.info(f"filed id:{file_id}")
        await call.message.answer('Kategoriyani tanlang',reply_markup=container_user)
        await call.answer(cache_time=60)
    except asyncpg.exceptions.UndefinedTableError:
        await call.answer("Kechirasiz malumot hali mavjud emas",cache_time=60)
        
@dp.callback_query_handler(text='container2')
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    try:
        photos=await db.select_all_capture2()
        for photo in photos:
            file_id=photo[1]
            text=photo[2]
            try:
                await call.message.answer_photo(photo=file_id,caption=text)
            except:
                log.info(f"filed id:{file_id}")
        await call.message.answer('Kategoriyani tanlang',reply_markup=container_user)
        await call.answer(cache_time=60)
    except asyncpg.exceptions.UndefinedTableError:
        await call.answer("Kechirasiz malumot hali mavjud emas",cache_time=60)
        
@dp.callback_query_handler(text='container3')
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    try:
        photos=await db.select_all_capture3()
        for photo in photos:
            file_id=photo[1]
            text=photo[2]
            try:
                await call.message.answer_photo(photo=file_id,caption=text)
            except:
                log.info(f"filed id:{file_id}")
        await call.message.answer('Kategoriyani tanlang',reply_markup=container_user)
        await call.answer(cache_time=60)
    except asyncpg.exceptions.UndefinedTableError:
        await call.answer("Kechirasiz malumot hali mavjud emas",cache_time=60)
        
@dp.callback_query_handler(text='container4')
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    try:
        photos=await db.select_all_capture4()
        for photo in photos:
            file_id=photo[1]
            text=photo[2]
            try:
                await call.message.answer_photo(photo=file_id,caption=text)
            except:
                log.info(f"filed id:{file_id}")
        await call.message.answer('Kategoriyani tanlang',reply_markup=container_user)
        await call.answer(cache_time=60)
    except asyncpg.exceptions.UndefinedTableError:
        await call.answer("Kechirasiz malumot hali mavjud emas",cache_time=60)

@dp.callback_query_handler(text='container5')
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    try:
        photos=await db.select_all_capture5()
        for photo in photos:
            file_id=photo[1]
            text=photo[2]
            try:
                await call.message.answer_photo(photo=file_id,caption=text)
            except:
                log.info(f"filed id:{file_id}")
        await call.message.answer('Kategoriyani tanlang',reply_markup=container_user)
        await call.answer(cache_time=60)
    except asyncpg.exceptions.UndefinedTableError:
        await call.answer("Kechirasiz malumot hali mavjud emas",cache_time=60)
        
@dp.callback_query_handler(text='container6')
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    try:
        photos=await db.select_all_capture6()
        for photo in photos:
            file_id=photo[1]
            text=photo[2]
            try:
                await call.message.answer_photo(photo=file_id,caption=text)
            except:
                log.info(f"filed id:{file_id}")
        await call.message.answer('Kategoriyani tanlang',reply_markup=container_user)
        await call.answer(cache_time=60)
    except asyncpg.exceptions.UndefinedTableError:
        await call.answer("Kechirasiz malumot hali mavjud emas",cache_time=60)

@dp.callback_query_handler(text='container7')
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    try:
        photos=await db.select_all_capture7()
        for photo in photos:
            file_id=photo[1]
            text=photo[2]
            try:
                await call.message.answer_photo(photo=file_id,caption=text)
            except:
                log.info(f"filed id:{file_id}")
        await call.message.answer('Kategoriyani tanlang',reply_markup=container_user)
        await call.answer(cache_time=60)
    except asyncpg.exceptions.UndefinedTableError:
        await call.answer("Kechirasiz malumot hali mavjud emas",cache_time=60)

@dp.callback_query_handler(text='container8')
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    try:
        photos=await db.select_all_capture8()
        for photo in photos:
            file_id=photo[1]
            text=photo[2]
            try:
                await call.message.answer_photo(photo=file_id,caption=text)
            except:
                log.info(f"filed id:{file_id}")
        await call.message.answer('Kategoriyani tanlang',reply_markup=container_user)
        await call.answer(cache_time=60)
    except asyncpg.exceptions.UndefinedTableError:
        await call.answer("Kechirasiz malumot hali mavjud emas",cache_time=60)

@dp.callback_query_handler(text='container9')
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    try:
        photos=await db.select_all_capture9()
        for photo in photos:
            file_id=photo[1]
            text=photo[2]
            try:
                await call.message.answer_photo(photo=file_id,caption=text)
            except:
                log.info(f"filed id:{file_id}")
        await call.message.answer('Kategoriyani tanlang',reply_markup=container_user)
        await call.answer(cache_time=60)
    except asyncpg.exceptions.UndefinedTableError:
        await call.answer("Kechirasiz malumot hali mavjud emas",cache_time=60)


