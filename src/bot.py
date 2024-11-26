from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from dotenv import dotenv_values
from src.handlers import start_handler, chat_handler, cancel_handler


async def main():
    config = dotenv_values("settings/config.env")

    # Получение токена
    bot_token = config.get("BOT_TOKEN")

    bot = Bot(token=bot_token)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Регистрация обработчиков
    dp.include_router(start_handler.router)
    dp.include_router(chat_handler.router)
    dp.include_router(cancel_handler.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

