from aiogram.filters.callback_data import CallbackData


class GenderCallbackData(CallbackData, prefix='gender'):
    is_male: bool
    # True - мужчина
    # False - женщина