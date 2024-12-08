from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from settings.states import ChatStates
from service.ai_service import OllamaAI
from settings.texts import goodbye_message
from settings.shared import db
from service.models import UserChat

router = Router()
ollama_ai = OllamaAI()

#Заглушка
async def cancel_command(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("У вас нет активного диалога.")
        return

    # Сброс состояния
    await state.clear()

    # Ответ пользователю
    await message.answer(goodbye_message)


