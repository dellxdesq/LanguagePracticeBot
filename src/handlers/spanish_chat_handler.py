from aiogram import Router
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from src.settings.states import ChatStates
from src.settings.keyboard import cancel_menu_with_language, language_menu
from src.service.bloom_service import BloomService

router = Router()

@router.message(ChatStates.SPANISH_CHAT)
async def chat_with_spanish_bloom(message: types.Message, state: FSMContext):
    """Обработчик чата на испанском языке"""
    try:
        # Логирование состояния и текста
        print(f"Текущее состояние: {await state.get_state()}")
        print(f"Сообщение: {message.text}")

        # Проверка на наличие текста сообщения
        if message.text:
            # Генерация ответа через BloomService
            response = BloomService.generate_response(prompt=message.text)
            await message.answer(
                text=response,
                reply_markup=cancel_menu_with_language
            )
        else:
            await message.answer("Пожалуйста, отправьте сообщение.")
    except Exception as e:
        await message.answer("Произошла ошибка при обработке сообщения.")
        print(f"Error: {e}")  # Логирование ошибки


@router.message(F.text == "Остановить диалог")
async def stop_dialog(message: types.Message, state: FSMContext):
    """Обработчик остановки диалога"""
    await state.clear()  # Сбрасываем состояние FSM
    await message.answer(
        text="Диалог остановлен. Вы можете начать заново, используя команду /start.",
        reply_markup=types.ReplyKeyboardRemove()  # Убираем клавиатуру
    )