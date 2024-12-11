import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

from module_13.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')