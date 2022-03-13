import asyncpg
from aiogram import types
from loader import dp,db
from states.admin_state import admin
from data.config import ADMINS
from aiogram.dispatcher import FSMContext
from keyboards.default.Save_button import SaveButton
from aiogram.dispatcher.filters import Text
from keyboards.inline.container import cancel

#select contiener
@dp.callback_query_handler(text='container1',state=admin.select_container,user_id=ADMINS)
async def add_pic(call: types.CallbackQuery,state:FSMContext):
    await call.message.answer('Rasm yuboring',reply_markup=cancel)
    await call.answer(text='🏚Yotoqxona kampilekt tanlandi',cache_time=60)
    await state.set_state(admin.container1)

@dp.callback_query_handler(text='container2',state=admin.select_container,user_id=ADMINS)
async def add_pic(call:types.CallbackQuery,state:FSMContext):
    await call.message.answer('Rasm yuboring',reply_markup=cancel)
    await call.answer('🛌Divan kreslo tanlandi',cache_time=60)
    await state.set_state(admin.container2)

@dp.callback_query_handler(text='container3',state=admin.select_container,user_id=ADMINS)
async def add_pic(call:types.CallbackQuery,state:FSMContext):
    await call.message.answer('Rasm yuboring',reply_markup=cancel)
    await call.answer('📐Ugalog tanlandi',cache_time=60)
    await state.set_state(admin.container3)

@dp.callback_query_handler(text='container4',state=admin.select_container,user_id=ADMINS)
async def add_pic(call:types.CallbackQuery,state:FSMContext):
    await call.message.answer('Rasm yuboring',reply_markup=cancel)
    await call.answer('🪟Penal kamot tanlandi',cache_time=60)
    await state.set_state(admin.container4)

@dp.callback_query_handler(text='container5',state=admin.select_container,user_id=ADMINS)
async def add_pic(call:types.CallbackQuery,state:FSMContext):
    await call.message.answer('Rasm yuboring',reply_markup=cancel)
    await call.answer('🗄Gorka tanlandi',cache_time=60)
    await state.set_state(admin.container5)

@dp.callback_query_handler(text='container6',state=admin.select_container,user_id=ADMINS)
async def add_pic(call:types.CallbackQuery,state:FSMContext):
    await call.message.answer('Rasm yuboring',reply_markup=cancel)
    await call.answer('🪑Stol stullar tanlandi',cache_time=60)
    await state.set_state(admin.container6)

@dp.callback_query_handler(text='container7',state=admin.select_container,user_id=ADMINS)
async def add_pic(call:types.CallbackQuery,state:FSMContext):
    await call.message.answer('Rasm yuboring',reply_markup=cancel)
    await call.answer('🛌👼Bolalar uchun Manej tanlandi',cache_time=60)
    await state.set_state(admin.container7)

@dp.callback_query_handler(text='container8',state=admin.select_container,user_id=ADMINS)
async def add_pic(call:types.CallbackQuery,state:FSMContext):
    await call.message.answer('Rasm yuboring',reply_markup=cancel)
    await call.answer('🛏Bir kishilik kravat tanlandi',cache_time=60)
    await state.set_state(admin.container8)

@dp.callback_query_handler(text='container9',state=admin.select_container,user_id=ADMINS)
async def add_pic(call:types.CallbackQuery,state:FSMContext):
    await call.message.answer('Rasm yuboring',reply_markup=cancel)
    await call.answer('⚒Ish jarayoni tanlandi',cache_time=60)
    await state.set_state(admin.container9)

#photo handler
@dp.message_handler(content_types='photo',state=admin.container1)
async def add_pic(msg:types.Message,state:FSMContext):
    try:
        photo=msg.photo[-1].file_id
        caption=msg.caption
        await db.add_capture1(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)
    except:
        
        await db.create_table_capture1()
        photo=msg.photo[-1].file_id
        caption=msg.caption
        await db.add_capture1(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)

@dp.message_handler(content_types='photo',state=admin.container2)
async def add_pic(msg:types.Message,state:FSMContext):
    try:
        photo=msg.photo[-1].file_id
        caption=msg.caption
        await db.add_capture2(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)
    except:
       
        await db.create_table_capture2()
        photo=msg.photo[-1].file_id
        caption=msg.caption
        await db.add_capture2(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)

@dp.message_handler(content_types='photo',state=admin.container3)
async def add_pic(msg:types.Message,state:FSMContext):
    try:
        photo=msg.photo[-1].file_id
        caption=msg.caption
        await db.add_capture3(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)
    except:
        
        await db.create_table_capture3()
        photo=msg.photo[-1].file_id
        caption=msg.caption
        await db.add_capture3(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)

@dp.message_handler(content_types='photo',state=admin.container4)
async def add_pic(msg:types.Message,state:FSMContext):
    photo=msg.photo[-1].file_id
    caption=msg.caption
    try: 
        await db.add_capture4(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)
    except:
        
        await db.create_table_capture4()
        await db.add_capture4(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)

@dp.message_handler(content_types='photo',state=admin.container5)
async def add_pic(msg:types.Message,state:FSMContext):
    photo=msg.photo[-1].file_id
    caption=msg.caption
    try:
        await db.add_capture5(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)
    except:
        
        await db.create_table_capture5()
        await db.add_capture5(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)

@dp.message_handler(content_types='photo',state=admin.container6)
async def add_pic(msg:types.Message,state:FSMContext):
    photo=msg.photo[-1].file_id
    caption=msg.caption
    try:
        await db.add_capture6(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)
    except:
        await db.create_table_capture6()
        await db.add_capture6(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)

@dp.message_handler(content_types='photo',state=admin.container7)
async def add_pic(msg:types.Message,state:FSMContext):
    photo=msg.photo[-1].file_id
    caption=msg.caption
    try:
        await db.add_capture7(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)
    except:
        await db.create_table_capture7()
        await db.add_capture7(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)

@dp.message_handler(content_types='photo',state=admin.container8)
async def add_pic(msg:types.Message,state:FSMContext):
    photo=msg.photo[-1].file_id
    caption=msg.caption
    try:
        await db.add_capture8(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)
    except:
        await db.create_table_capture8()
        await db.add_capture6(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)

@dp.message_handler(content_types='photo',state=admin.container9)
async def add_pic(msg:types.Message,state:FSMContext):
    photo=msg.photo[-1].file_id
    caption=msg.caption
    try:
        await db.add_capture9(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)
    except:
        await db.create_table_capture9()
        await db.add_capture9(file_id=photo,caption=caption)
        await msg.answer('Rasim qoshildi',reply_markup=SaveButton)

#save button
@dp.message_handler(Text(equals='✅Saqlash', ignore_case=True), state='*',user_id=ADMINS)
async def cancel_state(message: types.Message, state: FSMContext):
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
        await message.reply('💾 Malumotlar saqlandi',reply_markup=types.ReplyKeyboardRemove())

    except Exception as e:
        print(e)

