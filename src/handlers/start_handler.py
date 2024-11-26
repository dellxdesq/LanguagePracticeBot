from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from settings.states import ChatStates
from service.ai_service import OllamaAI
from settings.keyboard import cancel_menu
router = Router()

ollama_ai = OllamaAI()

@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    """Обработчик команды /start"""
    #logger.info(f"Получена команда /start от пользователя: {message.from_user.id}")
    try:
        topics = ["Sport", "Music", "Literature", "Technology"]
        topics_text = "\n".join(f"- {topic}" for topic in topics)

        await message.answer(
            f"Привет! Я бот для практики иностранного языка с искусственным интеллектом. "
            f"В данный момент доступно общение на английском языке, но скоро появятся и другие. "
            f"Вот пример тем, на которые вы можете пообщаться:\n\n"
            f"{topics_text}\n\n"
            f"Вы можете выбрать тему, написав её в чат, или предложить свою. "
            f"Чтобы прекратить общение, нажмите кнопку \"Отмена\"",
            reply_markup=cancel_menu
        )
        current_state = await state.get_state()
        #logger.info(f"Текущее состояние перед установкой: {current_state}")

        await state.set_state(ChatStates.CHAT)
        #logger.info(f"Состояние установлено: {ChatStates.CHAT}")
    except Exception as e:
        #logger.error(f"Ошибка в обработчике /start: {e}")
        await message.answer("Произошла ошибка при выполнении команды /start")