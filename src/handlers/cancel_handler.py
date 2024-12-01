from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from settings.states import ChatStates
from service.eng_ai_service import OllamaAI
from settings.texts import goodbye_message

router = Router()

ollama_ai = OllamaAI()


@router.callback_query(lambda c: c.data == "cancel", ChatStates.CHAT)
async def cancel_command(message: types.Message, state: FSMContext):
    """Обработчик команды /cancel"""
    try:
        current_state = await state.get_state()
        if current_state:
            await state.clear()
            await message.answer(goodbye_message)
        else:
            await message.answer("Невозможно завершить, нет активного общения.")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")