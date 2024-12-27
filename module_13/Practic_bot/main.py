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
    await message.answer(text=f'Добро пожаловать, {message.from_user.username}!\n{texts.start}',
                         reply_markup=start_kb)


@dp.message(F.text == 'О нас')
async def info(message: Message):
    await message.answer_photo(photo='https://horoshomall.ru/upload/iblock/040/bez-nazvaniya-_19_.png',
                               caption=texts.about,
                               reply_markup=start_kb)


@dp.message(F.text == 'Стоимость')
async def start(message: Message):
    await message.answer('Что вас интересует?', reply_markup=catalog_kb)


@dp.callback_query(F.data == 'medium')
async def buy_m(callback: CallbackQuery):
    await callback.message.answer_photo(photo='https://ir.ozone.ru/s3/multimedia-b/w500/6401020931.jpg',
                                        caption=texts.m_game,
                                        reply_markup=buy_kb)
    await callback.answer()


@dp.callback_query(F.data == 'big')
async def buy_l(callback: CallbackQuery):
    await callback.message.answer_photo(photo='https://www.mosigra.ru/image/data/mosigra.product.main/554/074/DSC_2210.jpg',
                                        caption=texts.l_game,
                                        reply_markup=buy_kb)
    await callback.answer()


@dp.callback_query(F.data == 'mega')
async def buy_xl(callback: CallbackQuery):
    await callback.message.answer_photo(photo='https://novate.ru/files/u32501/board-games-6.jpg', caption=texts.xl_game, reply_markup=buy_kb)
    await callback.answer()


@dp.callback_query(F.data == 'other')
async def buy_other (callback: CallbackQuery):
    await callback.message.edit_text(text=texts.other, reply_markup=buy_kb)
    await callback.answer()


@dp.callback_query(F.data == 'back_to_catalog')
async def back_to_catalog(callback: CallbackQuery):
    await callback.message.answer(text=texts.menu, reply_markup=catalog_kb)
    await callback.answer()


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')