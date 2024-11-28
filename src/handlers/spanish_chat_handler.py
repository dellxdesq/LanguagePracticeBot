from aiogram import Router
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from src.settings.states import ChatStates
from src.settings.keyboard import cancel_menu_with_language, language_menu
from src.service.spanish_ai_service import SpanishOllamaAI
from src.handlers.cancel_handler import cancel_command
from src.settings.states import ChatStates
router = Router()

spanish_ollama_ai = SpanishOllamaAI()
@router.message(F.text, ChatStates.SPANISH_CHAT)
async def spanish_chat_with_ai(message: types.Message, state: FSMContext):
    """Обработчик сообщений пользователя в испанском чате"""
    current_state = await state.get_state()
    print(f"Текущие состояние: {current_state}")  # Логируем текущее состояние
    user_message = message.text
    print(f"Сообщение пользователя: {user_message}")  # Логируем сообщение пользователя

    if user_message == "Остановить диалог":
        await cancel_command(message, state)  # Обрабатываем команду остановки диалога
        return
    try:
        ai_response = spanish_ollama_ai.get_response(user_message)  # Получаем ответ от AI
        await message.answer(ai_response)  # Отправляем ответ пользователю
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")  # Обрабатываем ошибки
