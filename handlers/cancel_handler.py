from aiogram import types, Router

from aiogram.fsm.context import FSMContext
from settings.states import ChatStates
from service.ai_service import OllamaAI

#from bot import logger

router = Router()

ollama_ai = OllamaAI()


@router.callback_query(lambda c: c.data == "cancel", ChatStates.CHAT)
async def cancel_command(message: types.Message, state: FSMContext):
    """Обработчик команды /cancel"""
    try:
        current_state = await state.get_state()
        #logger.info(f"Получена команда /cancel. Текущее состояние: {current_state}")

        if current_state:
            await state.clear()
            #logger.info(f"Состояние очищено для пользователя {message.from_user.id}")
            await message.answer("Goodbye! Если захочешь поговорить снова, напиши /start")
        else:
            await message.answer("Невозможно завершить, нет активного общения.")
    except Exception as e:
        #logger.error(f"Ошибка в обработчике /cancel: {e}")
        await message.answer(f"Произошла ошибка: {e}")