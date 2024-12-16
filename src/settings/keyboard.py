from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Остановить диалог", callback_data="cancel")],
        [KeyboardButton(text="Старт", callback_data="start")]
    ],
    resize_keyboard=True, one_time_keyboard=True
)





