import asyncio
import asyncpg

from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from loader import dp, db, bot
from keyboards.inline.container import container_key,ClearButton
from states.admin_state import admin
from aiogram.dispatcher.filters import Text

#add picture command
@dp.message_handler(commands="add_pic", user_id=ADMINS)
async def send_ad_to_all(message: types.Message ,state:FSMContext):
    try:
        await message.answer('Kategoryani tanlang',reply_markup=container_key)
        await admin.select_container.set()
    except:
        await message.answer("Bir daqiqa kuting")
        await message.answer('Kategoryani tanlang',reply_markup=container_key)

@dp.message_handler(state=admin.select_container)
async def not_allowed(msg:types.Message):
    await msg.reply('Kategoriyani tanlashingiz kerak yoki,\nBekor qilishnni bosing!!',reply_markup=container_key)

#cancel commands
@dp.callback_query_handler(text='cancel_add',state='*')
async def cancel_state(call: types.CallbackQuery, state: FSMContext):
    """
    Allow user to cancel any action
    """
    try:
        current_state = await state.get_state()
        if current_state is None:
            return

       # Cancel state and inform user about it
        await state.finish()
       # And remove keyboard (just in case)
        await call.answer('Bekor qilindi')
        await call.message.delete()
        await call.message.answer("<b>Rasim qo'shish uchun /add_pic komandasini qayta yozing!</b>")

    except Exception as e:
        print(e)

#wipe data

@dp.message_handler(commands="clear_data", user_id=ADMINS)
async def clear(message: types.Message ,state:FSMContext):
    await message.answer(text="Qaysi kategoriya malumotlarini o'chiray ?",reply_markup=container_key)
    await state.set_state(admin.ClearData)


#seleect dell container
@dp.callback_query_handler(text='container1',state=admin.ClearData)
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Malumotlarni rostdanxam o'chiraymi ?",reply_markup=ClearButton)
    await state.update_data(
        {
            "action":'container1'
        }
    )
    await state.set_state(admin.ConfirmClear)

@dp.callback_query_handler(text='container2',state=admin.ClearData)
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Malumotlarni rostdanxam o'chiraymi ?",reply_markup=ClearButton)
    await state.update_data(
        {
            "action":'container2'
        }
    )
    await state.set_state(admin.ConfirmClear)

@dp.callback_query_handler(text='container3',state=admin.ClearData)
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Malumotlarni rostdanxam o'chiraymi ?",reply_markup=ClearButton)
    await state.update_data(
        {
            "action":'container3'
        }
    )
    await state.set_state(admin.ConfirmClear)

@dp.callback_query_handler(text='container4',state=admin.ClearData)
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Malumotlarni rostdanxam o'chiraymi ?",reply_markup=ClearButton)
    await state.update_data(
        {
            "action":'container4'
        }
    )
    await state.set_state(admin.ConfirmClear)

@dp.callback_query_handler(text='container5',state=admin.ClearData)
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Malumotlarni rostdanxam o'chiraymi ?",reply_markup=ClearButton)
    await state.update_data(
        {
            "action":'container5'
        }
    )
    await state.set_state(admin.ConfirmClear)

@dp.callback_query_handler(text='container6',state=admin.ClearData)
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Malumotlarni rostdanxam o'chiraymi ?",reply_markup=ClearButton)
    await state.update_data(
        {
            "action":'container6'
        }
    )
    await state.set_state(admin.ConfirmClear)

@dp.callback_query_handler(text='container7',state=admin.ClearData)
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Malumotlarni rostdanxam o'chiraymi ?",reply_markup=ClearButton)
    await state.update_data(
        {
            "action":'container7'
        }
    )
    await state.set_state(admin.ConfirmClear)

@dp.callback_query_handler(text='container8',state=admin.ClearData)
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Malumotlarni rostdanxam o'chiraymi ?",reply_markup=ClearButton)
    await state.update_data(
        {
            "action":'container8'
        }
    )
    await state.set_state(admin.ConfirmClear)

@dp.callback_query_handler(text='container9',state=admin.ClearData)
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer("Malumotlarni rostdanxam o'chiraymi ?",reply_markup=ClearButton)
    await state.update_data(
        {
            "action":'container9'
        }
    )
    await state.set_state(admin.ConfirmClear)
        
#cleared
@dp.callback_query_handler(text='clear_confirm',state=admin.ConfirmClear,user_id=ADMINS)
async def clear(call:types.CallbackQuery,state:FSMContext):
    data=await state.get_data()
    try:
        try:
            if data.get('action')=='container1':
                await db.drop_capture1()
            if data.get('action')=='container2':
                await db.drop_capture2()
            if data.get('action')=='container3':
                await db.drop_capture3()
            if data.get('action')=='container4':
                await db.drop_capture4()
            if data.get('action')=='container5':
                await db.drop_capture5()
            if data.get('action')=='container6':
                await db.drop_capture6()
            if data.get('action')=='container7':
                await db.drop_capture7()
            if data.get('action')=='container8':
                await db.drop_capture8()
            if data.get('action')=='container9':
                await db.drop_capture9()
            await call.answer("🗑 Malumotlar tozalandi")
            await call.message.delete()
            await state.reset_state()
        except asyncpg.exceptions.ConnectionDoesNotExistError:
            await call.message.answer("Ulanishda xatolik /clear_data ni qayta yuboring!!")
            await asyncio.sleep(60)
            await state.reset_state()
    except asyncpg.exceptions.UndefinedTableError:
        await call.answer("Malumot topilmadi!!")
        await call.message.delete()
        await state.reset_state()

#cancell confirm
@dp.callback_query_handler(text='cancel',state=admin.ConfirmClear,user_id=ADMINS)
async def clear(call:types.CallbackQuery,state:FSMContext):
    await call.answer('Bekor qilindi!!')
    await call.message.answer("Malumot uchun: /help ")
    await call.message.delete()
    await state.reset_state()
