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

    user_id = message.from_user.id
    user_message = message.text

    active_chat = await db.get_active_chat(user_id=user_id, chat_state=ChatStates.CHAT.state.split(":")[1])
    if not active_chat:
        await message.answer("У вас нет активного чата. Используйте команду /start для начала нового диалога.")
        return

    chat_id = active_chat.chat_id
    history = await db.get_chat_history(chat_id=chat_id)
    ollama_ai.set_history(history)

    current_state = await state.get_state()
    state_name = current_state.split(":")[1] if current_state else None

    await db.save_message(
        user_id=user_id,
        sender=SENDERS["user"],
        content=user_message,
        chat_state=state_name,
        chat_id=chat_id
    )

    if user_message.lower() == "очистить историю" or user_message == "/clear":
        await cancel_command(message, state)
        return
    try:
        await message.answer("Печатает...✍🏻")
        ai_response = ollama_ai.get_response(user_message)

        await db.save_message(
            user_id=user_id,
            sender=SENDERS["bot"],
            content=ai_response,
            chat_state=state_name,
            chat_id=chat_id
        )

        await message.answer(ai_response)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
