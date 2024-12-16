from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from settings.states import ChatStates
from service.ai_service import ChatGPT42AI
from settings.texts import goodbye_message
from settings.shared import db
from service.models import UserChat
from settings.keyboard import cancel_menu

router = Router()
ollama_ai = ChatGPT42AI()

# Заглушка для команды отмены
async def cancel_command(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username or "anonymous"  # Имя может быть None

    user = await db.get_user(user_id=user_id, username=username)

    # Завершаем активный чат в базе данных
    chat_ended = await db.end_active_chat(user_id=user_id, username=username)

    if not chat_ended:
        await message.answer("У вас нет активного диалога.")
    else:
        await state.clear()  # Сбрасываем состояние
        await message.answer(
            text=goodbye_message,
            reply_markup=cancel_menu  # Прикрепляем клавиатуру с кнопкой
        )
