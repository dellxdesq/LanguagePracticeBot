from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from settings.states import ChatStates
from settings.keyboard import cancel_menu
from settings.texts import hello_text_1, hello_text_2
from settings.shared import db
from service.db import generate_user_hash 

router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username or "anonymous"  # Имя может быть None

    unique_hash = generate_user_hash(user_id=user_id, username=username)

    user = await db.get_user(user_id=user_id, username=username)

    active_chat = await db.get_active_chat(user_id=user_id, username=username, chat_state=ChatStates.CHAT.state.split(":")[1])
    if not active_chat:
        chat_id = await db.create_chat(user_id=user_id, username=username, chat_state=ChatStates.CHAT.state.split(":")[1])

 # Отправка первого сообщения
    await message.answer(
        text=hello_text_1,
        reply_markup=cancel_menu
    )

    # Отправка второго сообщения с темами и уточнениями
    await message.answer(
        text=hello_text_2,
        reply_markup=cancel_menu
    )

    await state.set_state(ChatStates.CHAT)
