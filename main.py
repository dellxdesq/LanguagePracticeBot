from ollama_handler import OllamaAI
from bot import TelegramBot

if __name__ == "__main__":
    bot_token = "7645375910:AAF1eaxwLsTFPHlqdPMOg-A-Oof_B1H34Cc"
    bot = TelegramBot(bot_token)
    bot.run()

