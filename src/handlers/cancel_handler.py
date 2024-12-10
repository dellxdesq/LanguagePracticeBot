from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from settings.states import ChatStates
from service.ai_service import OllamaAI
from settings.texts import goodbye_message
from settings.shared import db
from service.models import UserChat

router = Router()
ollama_ai = OllamaAI()

# Заглушка для команды отмены
async def cancel_command(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username or "anonymous"  # Имя может быть None

    user = await db.get_user(user_id=user_id, username=username)

    active_chat = await db.get_active_chat(user_id=user_id, username=username, chat_state=ChatStates.CHAT.state.split(":")[1])

    if active_chat is None:
        await message.answer("У вас нет активного диалога.")
    else:
        await state.clear()

        await message.answer(goodbye_message)
