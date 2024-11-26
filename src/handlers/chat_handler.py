from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from src.settings.states import ChatStates
from src.service.ai_service import OllamaAI
from aiogram import F
from src.handlers.cancel_handler import cancel_command

router = Router()
ollama_ai = OllamaAI()

@router.message(F.text)
async def chat_with_ai(message: types.Message, state: FSMContext):
    """Обработчик сообщений пользователя"""
    current_state = await state.get_state()
    test = message.text
    print(test)
    if message.text == "Остановить диалог":
        await cancel_command(message, state)
        return
    if current_state != ChatStates.CHAT.state:
        await message.answer("Что-то пошло не так. Попробуйте снова запустить /start")
        return

    try:
        ai_response = ollama_ai.get_response(message.text)
        await message.answer(ai_response)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")