from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from src.settings.states import ChatStates
from src.service.ai_service import OllamaAI
from aiogram import F
#from bot import logger
from src.handlers.cancel_handler import cancel_command

router = Router()
ollama_ai = OllamaAI()

@router.message(F.text)
async def chat_with_ai(message: types.Message, state: FSMContext):

    """Обработчик сообщений пользователя"""
    #logger.info(f"Сообщение от пользователя: {message.text}")
    current_state = await state.get_state()
    #logger.info(f"Текущее состояние перед обработкой: {current_state}")
    test = message.text
    print(test)
    if message.text == "Отмена":
        await cancel_command(message, state)
        return
    # Проверяем состояние корректно
    if current_state != ChatStates.CHAT.state:
        #logger.warning("Состояние не соответствует ожидаемому ChatStates.CHAT")
        await message.answer("Что-то пошло не так. Попробуйте снова запустить /start")
        return

    try:
        ai_response = ollama_ai.get_response(message.text)
        await message.answer(ai_response)
    except Exception as e:
        #logger.error(f"Ошибка в обработчике общения: {e}")
        await message.answer(f"Произошла ошибка: {e}")