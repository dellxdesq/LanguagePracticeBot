from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from dotenv import dotenv_values
from handlers import start_handler, chat_handler, cancel_handler


async def main():
    config = dotenv_values("../config.env")
    bot_token = config.get("BOT_TOKEN")
    bot = Bot(token=bot_token)

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(start_handler.router)
    dp.include_router(chat_handler.router)
    dp.include_router(cancel_handler.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

