from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup , KeyboardButton, WebAppInfo

sahifa = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Russion", callback_data="Russion"), InlineKeyboardButton(text="English", callback_data="English")],
        [InlineKeyboardButton(text="Italian", callback_data="Italian"), InlineKeyboardButton(text="Arabic", callback_data="Arabic")]
    ]
)

yana = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Tilni o'zgartirish")]
    ],resize_keyboard=True
)


