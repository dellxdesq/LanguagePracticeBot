from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram import F
from settings.states import ChatStates
from service.eng_ai_service import OllamaAI
from handlers.cancel_handler import cancel_command
from settings.shared import db
from settings.constants import SENDERS
import asyncio

router = Router()
ollama_ai = OllamaAI()


@router.message(F.text, ChatStates.CHAT)
async def chat_with_ai(message: types.Message, state: FSMContext):
    """Обработчик сообщений пользователя в чате на английском"""

    user_message = message.text

    # Получаем текущее состояние без префикса
    current_state = await state.get_state()
    state_name = current_state.split(":")[1] if current_state else None

    # Сохранение сообщения пользователя
    await db.save_message(
        user_id=message.from_user.id,
        sender=SENDERS["user"],
        content=user_message,
        chat_state=state_name
    )

    print(f"Текущее состояние: {current_state}")
    user_message = message.text
    print(f"Сообщение пользователя: {user_message}")

    if message.text == "Остановить диалог":
        await cancel_command(message, state)
        return
    try:
        await message.answer("Печатает...✍🏻")
        ai_response = ollama_ai.get_response(user_message)

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
