from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup , KeyboardButton

sahifa = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🇷🇺 Russion", callback_data="ru"), InlineKeyboardButton(text="🇺🇸 English", callback_data="en")],
        [InlineKeyboardButton(text="🇮🇹 Italian", callback_data="it"), InlineKeyboardButton(text="🇸🇦 Arabic", callback_data="ar")],
        [InlineKeyboardButton(text="🇯🇵 Japan", callback_data="ja"), InlineKeyboardButton(text=" 🇫🇷 French", callback_data="fr")],
        [InlineKeyboardButton(text="🇮🇳 Hindi", callback_data="hi"), InlineKeyboardButton(text="🇮🇩 Indonesian", callback_data="id")],
        [InlineKeyboardButton(text="🇩🇪 German", callback_data="de"), InlineKeyboardButton(text="🇹🇷 Turk", callback_data="tr")],
        [InlineKeyboardButton(text="🇰🇷 Korean", callback_data="ko"), InlineKeyboardButton(text="🇹🇯 Tajik", callback_data="tg")],
        [InlineKeyboardButton(text="🇨🇳 Chinese", callback_data="zh-cn"), InlineKeyboardButton(text="🇰🇿 Kazakh", callback_data="kk")],
    ]
)

yana = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Tilni o'zgartirish")]
    ],resize_keyboard=True
)


