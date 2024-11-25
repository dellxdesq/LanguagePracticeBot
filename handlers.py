from aiogram import types
from aiogram.filters import Command
from states import State
from aiogram.fsm.context import FSMContext
from states import ChatStates
from ollama_handler import OllamaAI

ollama_ai = OllamaAI()  # Создаем экземпляр внутри обработчиков

async def start_command(message: types.Message, state: FSMContext):
    """Обработчик команды /start"""
    topics = ["Sport", "Music", "Literature", "Technology"]
    topics_text = "\n".join(f"- {topic}" for topic in topics)

    await message.answer(
        f"Привет! Я бот для практики иностранного языка с искусственным интеллектом. "
        f"В данный момент доступно общение на английском языке, но скоро появятся и другие. "
        f"Вот пример тем, на которые вы можете пообщаться:\n\n"
        f"{topics_text}\n\n"
        f"Вы можете выбрать тему, написав её в чат, или предложить свою. "
        f"Чтобы прекратить общение, напишите /cancel"
    )
    await state.set_state(ChatStates.CHAT)


async def chat_with_ai(message: types.Message, state: FSMContext):
    """Обработчик сообщений пользователя"""
    user_input = message.text

    try:
        ai_response = ollama_ai.get_response(user_input)
        await message.answer(ai_response)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")


async def cancel_command(message: types.Message, state: FSMContext):
    """Обработчик команды /cancel"""
    try:
        current_state = await state.get_state()
        if current_state:
            await state.clear()
            await message.answer("Goodbye! Если захочешь поговорить снова, напиши /start")
        else:
            await message.answer("Невозможно завершить, нет активного общения.")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")


def register_handlers(dispatcher):
    """Регистрация обработчиков команд в диспетчере"""
    dispatcher.message.register(start_command, Command("start"))
    dispatcher.message.register(chat_with_ai, State(ChatStates.CHAT))
    dispatcher.message.register(cancel_command, Command("cancel"), State("*"))