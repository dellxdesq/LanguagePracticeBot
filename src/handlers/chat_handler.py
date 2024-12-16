from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram import F
from settings.states import ChatStates
from service.ai_service import ChatGPT42AI
from handlers.cancel_handler import cancel_command
from settings.shared import db
from settings.constants import SENDERS
import asyncio
import re
router = Router()
ollama_ai = ChatGPT42AI()


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
        # Отправка уведомления "Печатает..."
        typing_message = await message.answer("Печатает...✍🏻")

        # Получаем ответ от AI
        ai_response = await ollama_ai.get_response(user_message)

        # Удаляем сообщение "Печатает..."
        await typing_message.delete()

        # Форматируем ответ
        formatted_response = format_ai_response_html(ai_response)

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
        await message.answer(formatted_response, parse_mode='HTML')
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")


def format_ai_response_html(ai_response):
    lines = ai_response.splitlines()  # Разбиваем текст на строки
    formatted_lines = []

    for line in lines:
        # Если строка начинается с **, убираем их
        if line.startswith("**"):
            line = line[2:].strip()
        # Если строка начинается с *, убираем её
        elif line.startswith("*"):
            line = line[1:].strip()

        # Заменяем слова в кавычках "текст" на <b>текст</b>
        line = re.sub(r'"(.*)"', r'<b>\1</b>', line)

        # Убираем все ** в строке
        line = line.replace("**", "")
        # Убираем все * в строке

        line = line.replace("*", "")

        # Добавляем строку в список
        formatted_lines.append(line)

    return "\n".join(formatted_lines)

