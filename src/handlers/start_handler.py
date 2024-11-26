from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from src.settings.states import ChatStates
from src.service.ai_service import OllamaAI
from src.settings.keyboard import cancel_menu
from src.settings.texts import hello_text
router = Router()

ollama_ai = OllamaAI()

@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    """Обработчик команды /start"""
    try:

        await message.answer(
            text=hello_text,
            reply_markup=cancel_menu
        )
        current_state = await state.get_state()

        await state.set_state(ChatStates.CHAT)
    except Exception as e:
        await message.answer("Произошла ошибка при выполнении команды /start")