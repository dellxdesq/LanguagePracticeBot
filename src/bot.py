from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from dotenv import dotenv_values
from settings.routers import main_router

async def main():
    config = dotenv_values("../config.env")
    bot_token = config.get("BOT_TOKEN")
    bot = Bot(token=bot_token)

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(main_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

