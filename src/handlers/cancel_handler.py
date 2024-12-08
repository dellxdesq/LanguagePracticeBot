from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from settings.states import ChatStates
from service.eng_ai_service import OllamaAI
from settings.texts import goodbye_message
from settings.shared import db
from service.models import UserChat

router = Router()
ollama_ai = OllamaAI()

#Заглушка
async def cancel_command(message: types.Message, state: FSMContext):
    await message.answer("История очищена")


