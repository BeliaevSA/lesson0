import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from module_13.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight =State()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message(F.text.lower() == 'calories'.lower())
async def set_age(message: Message, state: FSMContext):
    await state.set_state(UserState.age)
    await message.answer("Введите свой возраст:")


@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age = message.text)
    await state.set_state(UserState.growth)
    await message.answer('Введите свой рост:')


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth = message.text)
    await state.set_state(UserState.weight)
    await message.answer('Введите свой вес:')


@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    age, weight, growth = list(data.values())
    print(type(age))
    result = 10 * int(weight) + 6.25 * int(growth) - 5 * int(age)
    await message.answer(f'Ваша норма калорий: {result}')
    await state.clear()


async def main():

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')