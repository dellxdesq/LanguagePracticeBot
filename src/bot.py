from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import os
from dotenv import load_dotenv
from handlers import start_handler, chat_handler, cancel_handler
from service.db import Database

db = Database()

async def main():
    # Инициализация базы данных
    await db.init()

    # Загружаем переменные окружения из .env файла
    load_dotenv()

    # Получаем токен из переменной окружения
    bot_token = os.getenv("BOT_TOKEN")

    # Проверяем, что токен был найден
    if bot_token is None:
        raise ValueError("BOT_TOKEN не найден! Проверьте файл .env.")
    else:
        print(f"Токен успешно загружен: {bot_token}")

    bot = Bot(token=bot_token)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Регистрация обработчиков
    dp.include_router(start_handler.router)
    dp.include_router(chat_handler.router)
    dp.include_router(cancel_handler.router)

    await dp.start_polling(bot)

    # Закрытие соединения с базой данных
    await db.close()

if __name__ == "__main__":
    asyncio.run(main())

