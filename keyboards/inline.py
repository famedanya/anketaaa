from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callbacks.form import GenderCallbackData

male_inline_button = InlineKeyboardButton(
    text='Мужчина',
    callback_data=GenderCallbackData(is_male=True).pack()
)
female_inline_button = InlineKeyboardButton(
    text='Женщина',
    callback_data=GenderCallbackData(is_male=False).pack()
)

gender_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [male_inline_button, female_inline_button]
])