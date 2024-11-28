from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_menu_with_language = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Остановить диалог", callback_data="cancel")],
        [KeyboardButton(text="Сменить язык", callback_data="change_language")]
    ],
    resize_keyboard=True, one_time_keyboard=True
)

# Клавиатура для выбора языка
language_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Китайский")],
        [KeyboardButton(text="Испанский")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
