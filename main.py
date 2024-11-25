import asyncio
from dotenv import dotenv_values
from bot import TelegramBot

if __name__ == "__main__":
    # Загрузка переменных из файла config.env
    config = dotenv_values("config.env")

    # Получение токена
    bot_token = config.get("BOT_TOKEN")

    bot = TelegramBot(bot_token)

    asyncio.run(bot.run())  # Теперь вызываем метод run для запуска бота
