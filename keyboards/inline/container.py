from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

container_key=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🏚Yotoqxona kampilekt',callback_data='container1'),
            InlineKeyboardButton(text='🛋Divan kreslo',callback_data='container2')
        ],
        [
            InlineKeyboardButton(text='🪟Trimo',callback_data='container3'),
            InlineKeyboardButton(text='🪟Penal kamot',callback_data='container4')
        ],
        [
            InlineKeyboardButton(text='🗄Gorka',callback_data='container5'),
            InlineKeyboardButton(text='🪑Stol stullar',callback_data='container6')
        ],
        [
            InlineKeyboardButton(text='🛌Troyka',callback_data='container7'),
            InlineKeyboardButton(text='🛏Bir kishilik kravat',callback_data='container8')
        ],
        [
            InlineKeyboardButton(text='🛠Ish jarayoni',callback_data='container9'),
        ]
    ]
)

cancel=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='❌Bekor qilish',callback_data='cancel_add')
        ]
    ]
)
#user
container_user=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🏚Yotoqxona kampilekt',callback_data='container1'),
            InlineKeyboardButton(text='🛋Divan kreslo',callback_data='container2')
        ],
        [
            InlineKeyboardButton(text='🪟Tremo',callback_data='container3'),
            InlineKeyboardButton(text='🪟Penal kamot',callback_data='container4')
        ],
        [
            InlineKeyboardButton(text='🗄Gorka',callback_data='container5'),
            InlineKeyboardButton(text='🪑Stol stullar',callback_data='container6')
        ],
        [
            InlineKeyboardButton(text='🛌Troyka',callback_data='container7'),
            InlineKeyboardButton(text='🛏Bir kishilik kravat',callback_data='container8')
        ],
        [
            InlineKeyboardButton(text='🛠Ish jarayoni',callback_data='container9')
        ],
        [
             InlineKeyboardButton(text='☎️Admin bilan boglanish',callback_data='ChatStart')
        ]
    ]
)
#wipe data
ClearButton=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Tasdiqlas",callback_data='clear_confirm'),
            InlineKeyboardButton(text="🚫Bekor qilish",callback_data='cancel')
        ]
    ]
)
