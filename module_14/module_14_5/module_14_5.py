import asyncio
from operator import is_not

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardMarkup

from config import TOKEN
from crud_functions import get_all_products, is_included, add_user
import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Инициализация бота и создание диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создание состояния пользователя
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight =State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


# Создание меню клавиатуры
keyboard_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')],
        [KeyboardButton(text='Регистрация')],
    ],
    resize_keyboard=True
)

# Создание инлайн клавиатур
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
        ]
    ]
)

inline_keyboard_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Вернуться в меню', callback_data='back to menu')]
    ]
)

inline_keyboard_products = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')],
         [InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')],
    ]
)

# Обработчик команды /start
@dp.message(CommandStart())
async def start_message(message: Message):
    await message.reply('Привет! Я бот помогающий твоему здоровью.',  reply_markup=keyboard_start)


# Обработчик сообщения
@dp.message(F.text == 'Рассчитать')
async def main_menu(message: Message):
    await message.reply(text='Выберите опцию', reply_markup=inline_keyboard)


@dp.message(F.text == 'Купить')
async def get_buying_list(message: Message):
    products = await get_all_products()
    for product in products:
        await message.answer_photo(
            photo=product[4],
            caption=f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
    await message.answer(text='Выберите продукт для покупки:', reply_markup=inline_keyboard_products)


# Обработчик инлайн кнопки
@dp.callback_query(F.data == 'formulas')
async def get_formulas(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text='Формула: 10 х Вес (кг) + 6.25 * Рост (см) - 5 * Возраст (г)', reply_markup=inline_keyboard_back)


@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text='Вы успешно приобрели продукт!')


@dp.callback_query(F.data == 'back to menu')
async def back_to_menu(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text='Выберите опцию', reply_markup=inline_keyboard)


@dp.callback_query(F.data.lower() == 'calories')
async def set_age(callback: CallbackQuery, state: FSMContext):
    await state.set_state(UserState.age)
    await callback.answer('')
    await callback.message.answer(text="Введите свой возраст:")


# Обработчик изменения состояния age
@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age = message.text)
    await state.set_state(UserState.growth)
    await message.answer('Введите свой рост:')


# Обработчик изменения состояния growth
@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth = message.text)
    await state.set_state(UserState.weight)
    await message.answer('Введите свой вес:')


# Обработчик изменения состояния weight
@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    age, weight, growth = list(data.values())
    result = 10 * int(weight) + 6.25 * int(growth) - 5 * int(age)
    await message.reply(f'Ваша норма калорий: {result}', reply_markup=inline_keyboard_back)
    await state.clear()


@dp.message(F.text == 'Регистрация')
async def sign_up(message: Message, state: FSMContext):
    await state.set_state(RegistrationState.username)
    await message.answer('Введите имя пользователя (только латинский алфавит):')


@dp.message(RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    user = await is_included(message.text)
    if not user :
        await state.update_data(username = message.text)
        await state.set_state(RegistrationState.email)
        await message.answer('Введите свой email:')
    else:
        await message.answer(f'Пользователь {message.text} существует, введите другое имя:')
        await state.set_state(RegistrationState.username)


@dp.message(RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    await state.update_data(email = message.text)
    await state.set_state(RegistrationState.age)
    await message.answer('Введите свой возраст:')


@dp.message(RegistrationState.age)
async def set_age(message: Message, state: FSMContext):
    try:
        await state.update_data(age = message.text)
        data = await state.get_data()
        username, email, age = list(data.values())
        await add_user(username, email, age)
        await message.answer('Регистрация прошла успешно')
    except Exception as ex:
        await message.answer('Произошла ошибка на сервере, попробуйте позже')
        print(f'Произошла ошибка {ex}')




async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')