import asyncio
from aiogram import Router
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from service.spanish_ai_service import SpanishOllamaAI
from handlers.cancel_handler import cancel_command
from settings.states import ChatStates

router = Router()
spanish_ollama_ai = SpanishOllamaAI()

@router.message(F.text, ChatStates.SPANISH_CHAT)
async def spanish_chat_with_ai(message: types.Message, state: FSMContext):
    """Обработчик сообщений пользователя в испанском чате"""
    current_state = await state.get_state()
    print(f"Текущие состояние: {current_state}")
    user_message = message.text
    print(f"Сообщение пользователя: {user_message}")

    if user_message == "Остановить диалог":
        await cancel_command(message, state)
        return
    try:
        await message.answer("Печатает...✍🏻")
        ai_response = spanish_ollama_ai.get_response(user_message)
        await message.answer(ai_response)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
