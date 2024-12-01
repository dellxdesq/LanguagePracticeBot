from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from settings.states import ChatStates
from service.eng_ai_service import OllamaAI
from aiogram import F
from handlers.cancel_handler import cancel_command
import asyncio

router = Router()
ollama_ai = OllamaAI()


@router.message(F.text, ChatStates.CHAT)
async def chat_with_ai(message: types.Message, state: FSMContext):
    """Обработчик сообщений пользователя в чате на английском"""
    current_state = await state.get_state()
    print(f"Текущее состояние: {current_state}")
    user_message = message.text
    print(f"Сообщение пользователя: {user_message}")

    if message.text == "Остановить диалог":
        await cancel_command(message, state)
        return
    try:
        await message.answer("Печатает...✍🏻")
        ai_response = ollama_ai.get_response(user_message)
        await message.answer(ai_response)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
