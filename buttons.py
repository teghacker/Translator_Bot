from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup , KeyboardButton

sahifa = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Russion", callback_data="ru"), InlineKeyboardButton(text="English", callback_data="en")],
        [InlineKeyboardButton(text="Italian", callback_data="it"), InlineKeyboardButton(text="Arabic", callback_data="ar")]
    ]
)

yana = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Tilni o'zgartirish")]
    ],resize_keyboard=True
)


