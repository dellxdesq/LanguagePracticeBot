from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from settings.states import ChatStates
from service.eng_ai_service import OllamaAI
from settings.texts import goodbye_message
from settings.shared import db

router = Router()

ollama_ai = OllamaAI()


@router.callback_query(lambda c: c.data == "cancel", ChatStates.CHAT)
async def cancel_command(message: types.Message, state: FSMContext):
    """Обработчик команды /cancel"""
    user_id = message.from_user.id

    try:
        current_state = await state.get_state()
        if current_state:
            active_chat = await db.get_active_chat(user_id=user_id, chat_state=current_state.split(":")[1])
            if active_chat:
                active_chat.is_active = False
            await active_chat.save()
            
            await state.clear()
            await message.answer(goodbye_message)
        else:
            await message.answer("Невозможно завершить, нет активного общения.")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")