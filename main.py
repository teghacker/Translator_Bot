import asyncio
import logging
from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import callback_query, Message, FSInputFile
from confik import *
from buttons import *
from states import *
from googletrans import Translator
from gtts import gTTS
t = Translator()
router = Router()
bot = Bot(token=token)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
dp.include_router(router)
@router.message(CommandStart())
async def star(message: Message, state: FSMContext):
    await message.answer(f"""👋 Salom {message.from_user.full_name}

Qaysi tilga tarjima qilmoqchisiz""", reply_markup=sahifa)
    await message.delete()
    await state.set_state(Tarjiman.soz)


@router.callback_query(F.data, Tarjiman.soz)
async def star(call: callback_query, state: FSMContext):
    await state.update_data({'text':call.data})
    await call.message.answer(f"""So'z kiriting:""")
    await state.set_state(Tarjiman.yana)


@router.message(F.text, Tarjiman.yana)
async def star(message: Message, state: FSMContext):
    xabar = message.text
    data = await state.get_data()
    if not xabar == "Tilni o'zgartirish":
        a=t.translate(text=xabar, dest=f'{data.get('text')}')
        voice1 = gTTS(a.text, lang="ru")
        voice1.save("m.mp3")
        voice2 = FSInputFile('m.mp3')
        await message.answer_voice(voice=voice2, caption=f"{a.text}", reply_markup=yana)
        await message.answer("So'z kiriting:")
        await state.set_state(Tarjiman.yana)
    else:
        await state.clear()
        await message.answer(f"""Gaplariningizni qaysi tilga o'girmoqchisiz""", reply_markup=sahifa)
        await state.set_state(Tarjiman.soz)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())