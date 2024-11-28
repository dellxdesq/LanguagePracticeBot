from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_menu_with_language = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Остановить диалог", callback_data="cancel")],
    ],
    resize_keyboard=True, one_time_keyboard=True
)

# Клавиатура для выбора языка
language_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
