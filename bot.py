from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes
from ollama_handler import OllamaAI

class TelegramBot:
    def __init__(self, token: str):
        self.token = token
        self.ollama_ai = OllamaAI()
        self.application = Application.builder().token(self.token).build()

        self.START, self.CHAT = range(2)  # Добавляем новое состояние для диалога

    async def start(self, update, context: ContextTypes.DEFAULT_TYPE) -> int:
        # Перечисляем темы в приветственном сообщении
        topics = ["Sport", "Music", "Literature", "Technology"]
        topics_text = "\n".join(f"- {topic}" for topic in topics)  # Формируем текстовый список тем

        # Подготавливаем клавиатуру для будущей реализации языков
        #keyboard = [
        #   [KeyboardButton("Español (Spanish)"), KeyboardButton("中文 (Chinese)")],
        #]
        #markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

        # Отправляем приветственное сообщение с темами
        await update.message.reply_text(
            f"Привет! Я бот для практики иностранного языка с искусственным интеллектом. "
            f"В данный момент доступно общение на английском языке, но скоро появятся и другие. "
            f"Вот пример тем, на которые вы можете пообщаться:\n\n"
            f"{topics_text}\n\n"
            f"Вы можете выбрать тему, написав её в чат, или предложить свою. "
            f"Чтобы прекратить общение напишите в чат /cancel",
            #reply_markup=markup
        )
        return self.CHAT

    async def chat(self, update, context: ContextTypes.DEFAULT_TYPE) -> int:
        user_input = update.message.text
        ai_response = self.ollama_ai.get_response(user_input)
        await update.message.reply_text(ai_response)
        return self.CHAT

    async def cancel(self, update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.message.reply_text("Goodbye! Если захочешь поговорить снова, напиши /start.")
        return ConversationHandler.END

    def run(self):
        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler("start", self.start)],
            states={
                self.CHAT: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.chat)],
            },
            fallbacks=[CommandHandler("cancel", self.cancel)],
        )

        self.application.add_handler(conversation_handler)
        self.application.run_polling()
