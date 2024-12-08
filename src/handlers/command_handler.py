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
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name

    await db.create_user(user_id, username, full_name)
    chat_id = await db.create_chat(user_id=user_id, chat_state=ChatStates.CHAT.state.split(":")[1])
    await message.answer(
        text=hello_text,
        reply_markup=cancel_menu
    )
    await state.set_state(ChatStates.CHAT)






