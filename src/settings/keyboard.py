from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Очистить историю", callback_data="cancel")],
    ],
    resize_keyboard=True, one_time_keyboard=True
)

