from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram import F
from settings.states import ChatStates
from service.ai_service import OllamaAI
from handlers.cancel_handler import cancel_command
from settings.shared import db
from settings.constants import SENDERS
import asyncio
import re
router = Router()
ollama_ai = OllamaAI()


@router.message(F.text, ChatStates.CHAT)
async def chat_with_ai(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username or "anonymous"  # Имя может быть None
    user_message = message.text

    # Обработка команды остановки диалога
    if user_message.lower() == "остановить диалог" or user_message == "/clear":
        await cancel_command(message, state)
        return

    user = await db.get_user(user_id=user_id, username=username)
    active_chat = await db.get_active_chat(user_id=user_id, username=username, chat_state=ChatStates.CHAT.state.split(":")[1])

    chat_id = active_chat.chat_id
    history = await db.get_chat_history(chat_id=chat_id)
    ollama_ai.set_history(history)

    current_state = await state.get_state()
    state_name = current_state.split(":")[1] if current_state else None

    await db.save_message(
        user_id=user_id,
        username=username,
        sender=SENDERS["user"],
        content=user_message,
        chat_state=state_name,
        chat_id=chat_id
    )

    try:
        # Получаем ответ от AI
        typing_message = await message.answer("Печатает...✍🏻")

        # Получаем ответ от модели
        ai_response = ollama_ai.get_response(user_message)

        # Удаляем сообщение "Печатает..."
        await typing_message.delete()

        # Форматируем ответ
        formatted_response = format_ai_response(ai_response)

        # Сохраняем сообщение в базе данных
        await db.save_message(
            user_id=user_id,
            username=username,
            sender=SENDERS["bot"],
            content=ai_response,
            chat_state=state_name,
            chat_id=chat_id
        )

        # Отправляем отформатированный ответ пользователю
        await message.answer(formatted_response, parse_mode='MarkdownV2')
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")

def format_ai_response(ai_response):
    # Экранируем специальные символы для MarkdownV2
    def escape_markdown_v2(text):
        return re.sub(r'([_*[\]()~`>#+\-=|{}.!])', r'\\\1', text)

    lines = ai_response.splitlines()  # Разбиваем текст на строки
    formatted_lines = []

    for line in lines:
        if line.startswith("**"):  # Если строка начинается с **, убираем их
            formatted_lines.append(escape_markdown_v2(line[2:].strip()))
        elif line.startswith("*"):  # Если строка начинается с *, убираем её
            formatted_lines.append(escape_markdown_v2(line[1:].strip()))
        else:  # Остальные строки обрабатываем только для экранирования
            formatted_lines.append(escape_markdown_v2(line))

    return "\n".join(formatted_lines)
