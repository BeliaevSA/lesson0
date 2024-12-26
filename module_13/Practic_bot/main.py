import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from config import *
import texts
from keyboards import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(texts.start, reply_markup=start_kb)


@dp.message(F.text == 'О нас')
async def info(message: Message):
    await message.answer(texts.about, reply_markup=start_kb)


@dp.message(F.text == 'Стоимость')
async def start(message: Message):
    await message.answer('Что вас интересует?', reply_markup=catalog_kb)


@dp.callback_query(F.data == 'medium')
async def buy_m(callback: CallbackQuery):
    await callback.message.edit_text(text=texts.m_game, reply_markup=buy_kb)
    await callback.answer()


@dp.callback_query(F.data == 'big')
async def buy_l(callback: CallbackQuery):
    await callback.message.edit_text(text=texts.l_game, reply_markup=buy_kb)
    await callback.answer()


@dp.callback_query(F.data == 'mega')
async def buy_xl(callback: CallbackQuery):
    await callback.message.edit_text(text=texts.xl_game, reply_markup=buy_kb)
    await callback.answer()


@dp.callback_query(F.data == 'other')
async def buy_other (callback: CallbackQuery):
    await callback.message.edit_text(text=texts.other, reply_markup=buy_kb)
    await callback.answer()


@dp.callback_query(F.data == 'back_to_menu')
async def back_to_menu(callback: CallbackQuery):
    await callback.message.edit_text(text=texts.menu, reply_markup=catalog_kb)
    await callback.answer()


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')