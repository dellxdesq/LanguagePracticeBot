from aiogram import Router
from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from src.settings.states import ChatStates
from src.service.eng_ai_service import OllamaAI
from src.settings.keyboard import cancel_menu
from src.settings.texts import hello_text, spanish_hello_text

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
        print(current_state)

        await state.set_state(ChatStates.CHAT)
    except Exception as e:
        await message.answer("Произошла ошибка при выполнении команды /start")

@router.message(Command("spanish"))
async def switch_to_spanish(message: types.Message, state: FSMContext):
    """Обработчик выбора испанского языка"""
    await state.clear()  # Очищаем текущее состояние
    await state.set_state(ChatStates.SPANISH_CHAT)  # Устанавливаем новое состояние
    await message.answer(
        text=spanish_hello_text,
        reply_markup=cancel_menu
    )
    print("Состояние установлено на SPANISH_CHAT")  # Логируем установку состояния

@router.message(Command("chinese"))
async def switch_to_spanish(message: types.Message, state: FSMContext):
    """Обработчик выбора китайского языка"""
    await state.clear()  # Очищаем текущее состояние
    await state.set_state(ChatStates.CHINESE_CHAT)  # Устанавливаем новое состояние
    await message.answer(
        text="чат на китайском",
        reply_markup=cancel_menu
    )
    print("Состояние установлено на CHINESE_CHAT")  # Логируем установку состояния



