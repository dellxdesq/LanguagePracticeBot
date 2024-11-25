from ollama_handler import OllamaAI
from bot import TelegramBot

if __name__ == "__main__":
    bot_token = ""
    bot = TelegramBot(bot_token)
    bot.run()

