from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import register_handlers

class TelegramBot:
    def __init__(self, token: str):
        self.bot = Bot(token=token)
        self.storage = MemoryStorage()
        self.dispatcher = Dispatcher(storage=self.storage)

        # Регистрация обработчиков
        register_handlers(self.dispatcher)

    async def run(self):
        """Запуск бота"""
        await self.dispatcher.start_polling(self.bot)
