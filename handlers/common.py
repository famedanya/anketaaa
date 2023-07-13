from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from data.users import users_data

common_router = Router()


@common_router.message(Command('start'))
async def process_start_command(message: Message):
    await message.answer(text='Этот бот демонстрирует работу FSM\n\n'
                              'Чтобы перейти к заполнению анкеты - '
                              'отправьте команду /fillform')


@common_router.message(Command('show'))
async def handle_show(message: Message):
    current_user = users_data[message.from_user.id]
    if current_user['is_male']:
        gender = 'Мужской'
    else:
        gender = 'Женский'
    name = current_user["name"]
    age = current_user["age"]
    description = current_user['description']
    photo = current_user['photo']

    await message.answer_photo(photo, caption=f'{name}, {age}\nПол: {gender}\nО себе: {description}')