import asyncio
from aiogram import Router
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from service.spanish_ai_service import SpanishOllamaAI
from handlers.cancel_handler import cancel_command
from settings.states import ChatStates
from settings.shared import db
from settings.constants import SENDERS

router = Router()
spanish_ollama_ai = SpanishOllamaAI()

@router.message(F.text, ChatStates.SPANISH_CHAT)
async def spanish_chat_with_ai(message: types.Message, state: FSMContext):
    """Обработчик сообщений пользователя в испанском чате"""

    # Получаем текущее состояние без префикса
    current_state = await state.get_state()
    state_name = current_state.split(":")[1] if current_state else None

    print(f"Текущие состояние: {current_state}")
    user_message = message.text
    print(f"Сообщение пользователя: {user_message}")

    # Сохранение сообщения пользователя
    await db.save_message(
        user_id=message.from_user.id,
        sender=SENDERS["user"],
        content=user_message,
        chat_state=state_name
    )

    if user_message == "Остановить диалог":
        await cancel_command(message, state)
        return
    try:
        await message.answer("Печатает...✍🏻")
        ai_response = spanish_ollama_ai.get_response(user_message)

        # Сохранение ответа бота
        await db.save_message(
            user_id=message.from_user.id,
            sender=SENDERS["bot"],
            content=ai_response,
            chat_state=state_name
        )

        await message.answer(ai_response)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
