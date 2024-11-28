from aiogram import Router
from aiogram import types, F
from aiogram.filters import Command

from aiogram.fsm.context import FSMContext
from src.settings.states import ChatStates
from src.service.ai_service import OllamaAI
from src.settings.keyboard import cancel_menu_with_language, language_menu
from src.settings.texts import hello_text


router = Router()
ollama_ai = OllamaAI()

@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    """Обработчик команды /start"""
    try:
        await message.answer(
            text=hello_text,
            reply_markup=cancel_menu_with_language
        )
        current_state = await state.get_state()

        await state.set_state(ChatStates.CHAT)
    except Exception as e:
        await message.answer("Произошла ошибка при выполнении команды /start")

@router.message(F.text == "Сменить язык")
async def change_language(message: types.Message):
    """Обработчик кнопки 'Сменить язык'"""
    await message.answer(
        text="Выберите язык из списка:",
        reply_markup=language_menu
    )

@router.message(F.text == "Назад")
async def go_back_to_main_menu(message: types.Message):
    """Обработчик кнопки 'Назад'"""
    await message.answer(
        text="Возврат в основное меню.",
        reply_markup=cancel_menu_with_language
    )

@router.message(F.text == ["Китайский", "Испанский"])
async def select_language(message: types.Message, state: FSMContext):
    """Обработчик выбора языка"""
    selected_language = message.text
    # Сохранение выбранного языка в состоянии (или другой логике)
    await state.update_data(selected_language=selected_language)
    await message.answer(
        text=f"Вы выбрали язык: {selected_language}.",
        reply_markup=cancel_menu_with_language
    )