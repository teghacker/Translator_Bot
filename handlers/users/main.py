import asyncio
import logging
from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import callback_query, Message, FSInputFile
from keyboards.reply.buttons import *
from states.states import *
from googletrans import Translator
from gtts import gTTS

t = Translator()

router = Router()


# @router.message(Command('star'))
# async def star(message: Message):
#     await message.answer()
    

@router.callback_query(F.data == "Russion")
async def star(call: callback_query, state: FSMContext):
    await call.message.answer(f"""So'z kiriting:""")
    await state.set_state(Tarjiman.soz)

@router.callback_query(F.data == "English")
async def star(call: callback_query, state: FSMContext):
    await call.message.answer(f"""So'z kiriting:""")
    await state.set_state(Eng.soz)

@router.callback_query(F.data == "Italian")
async def star(call: callback_query, state: FSMContext):
    await call.message.answer(f"""So'z kiriting:""")
    await state.set_state(IT.soz)

@router.callback_query(F.data == "Arabic")
async def star(call: callback_query, state: FSMContext):
    await call.message.answer(f"""So'z kiriting:""")
    await state.set_state(Arabic.soz)

@router.message(F.text, Eng.soz)
async def star(message: Message, state: FSMContext):
    xabar = message.text
    if not xabar == "Tilni o'zgartirish":
        a=t.translate(text=xabar, dest='en')
        voice1 = gTTS(a.text, lang="en")
        voice1.save("m.mp3")
        voice2 = FSInputFile('m.mp3')
        await message.answer_voice(voice=voice2, caption=f"{a.text}", reply_markup=yana)
        await message.answer("So'z kiriting:")
        await state.set_state(Eng.soz)
    else:
        await state.clear()
        await message.answer(f"""Gaplariningizni qaysi tilga o'girmoqchisiz""", reply_markup=sahifa)

@router.message(F.text, IT.soz)
async def star(message: Message, state: FSMContext):
    xabar = message.text
    if not xabar == "Tilni o'zgartirish":
        a=t.translate(text=xabar, dest='it')
        voice1 = gTTS(a.text, lang="it")
        voice1.save("m.mp3")
        voice2 = FSInputFile('m.mp3')
        await message.answer_voice(voice=voice2, caption=f"{a.text}", reply_markup=yana)
        await message.answer("So'z kiriting:")
        await state.set_state(IT.soz)
    else:
        await state.clear()
        await message.answer(f"""Gaplariningizni qaysi tilga o'girmoqchisiz""", reply_markup=sahifa)

@router.message(F.text, Arabic.soz)
async def star(message: Message, state: FSMContext):
    xabar = message.text
    if not xabar == "Tilni o'zgartirish":
        a=t.translate(text=xabar, dest='ar')
        voice1 = gTTS(a.text, lang="ar")
        voice1.save("m.mp3")
        voice2 = FSInputFile('m.mp3')
        await message.answer_voice(voice=voice2, caption=f"{a.text}", reply_markup=yana)
        await message.answer("So'z kiriting:")
        await state.set_state(Arabic.soz)
    else:
        await state.clear()
        await message.answer(f"""Gaplariningizni qaysi tilga o'girmoqchisiz""", reply_markup=sahifa)

@router.message(F.text, Tarjiman.soz)
async def star(message: Message, state: FSMContext):
    xabar = message.text
    if not xabar == "Tilni o'zgartirish":
        a=t.translate(text=xabar, dest='ru')
        voice1 = gTTS(a.text, lang="ru")
        voice1.save("m.mp3")
        voice2 = FSInputFile('m.mp3')
        await message.answer_voice(voice=voice2, caption=f"{a.text}", reply_markup=yana)
        await message.answer("So'z kiriting:")
        await state.set_state(Tarjiman.soz)
    else:
        await state.clear()
        await message.answer(f"""Gaplariningizni qaysi tilga o'girmoqchisiz""", reply_markup=sahifa)

