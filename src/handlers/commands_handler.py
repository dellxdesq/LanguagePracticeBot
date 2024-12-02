from aiogram import Router
from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from settings.states import ChatStates
from service.eng_ai_service import OllamaAI
from settings.keyboard import cancel_menu
from settings.texts import hello_text, spanish_hello_text
from settings.shared import db

router = Router()
ollama_ai = OllamaAI()

@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    """Обработчик команды /start"""
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name

    # Проверка и создание профиля в базе данных
    await db.create_user(user_id, username, full_name)

    # Проверка наличия активного диалога
    active_chat = await db.get_active_chat(user_id=user_id)

    """Обработчик команды /start"""
    try:
        if active_chat:
            # Если есть активный диалог, уведомляем пользователя
            await message.answer(
                text=(
                    "У вас уже есть активный диалог. Вы можете продолжить его. "
                    "Если хотите завершить текущий диалог, используйте команду /cancel."
                ),
                reply_markup=cancel_menu
            )
            await state.set_state(ChatStates.CHAT)
        else:
            # Если активного диалога нет, создаём новый
            chat_id = await db.create_chat(user_id=user_id, chat_state=ChatStates.CHAT.state.split(":")[1])
            await message.answer(
                text=hello_text,
                reply_markup=cancel_menu
            )
            await state.set_state(ChatStates.CHAT)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")

@router.message(Command("spanish"))
async def switch_to_spanish(message: types.Message, state: FSMContext):
    """Обработчик выбора испанского языка"""
    user_id = message.from_user.id

    # Проверяем, есть ли активный испанский чат
    active_chat = await db.get_active_chat(user_id=user_id, chat_state=ChatStates.SPANISH_CHAT.state.split(":")[1])
    if active_chat:
        await message.answer(
            "Вы уже общаетесь на испанском языке. Продолжайте диалог или завершите его командой /cancel."
        )
        await state.set_state(ChatStates.SPANISH_CHAT)
    else:
        # Проверяем наличие любого другого активного чата
        other_chat = await db.get_active_chat(user_id=user_id)
        if other_chat:
            await message.answer(
                "У вас уже есть активный диалог. Завершите текущий диалог командой /cancel, чтобы переключиться на испанский."
            )
            await state.set_state(ChatStates.CHAT)
        else:
            # Если активного чата нет, создаём новый для испанского
            chat_id = await db.create_chat(user_id=user_id, chat_state=ChatStates.SPANISH_CHAT.state.split(":")[1])
            await state.set_state(ChatStates.SPANISH_CHAT)
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




