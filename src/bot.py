from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import os
from dotenv import load_dotenv, dotenv_values
from service.db import Database
from settings.routers import main_router

db = Database()

async def main():
    await db.init()
    config = dotenv_values(".env")

    # Получение токена
    bot_token = config.get("BOT_TOKEN")

    bot = Bot(token=bot_token)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(main_router)

    await dp.start_polling(bot)

    # Закрытие соединения с базой данных
    await db.close()

if __name__ == "__main__":
    asyncio.run(main())

