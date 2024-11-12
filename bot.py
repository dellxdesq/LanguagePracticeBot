from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, ConversationHandler

# Токен бота от BotFather
TOKEN = '3'

# Определяем состояния для обработки диалога
MENU, LANGUAGE_SELECTION, SUPPORT = range(3)

# Обработчик команды /start
async def start(update: Update, context: CallbackContext) -> int:
    # Отправляем приветственное изображение
    with open('images/main.png', 'rb') as photo:
        await update.message.reply_photo(
            photo=photo,
            caption="Приветствую, я бот для практики иностранного языка с искусственным интеллектом.\n"
                    "Выберите опцию, нажав на меню"
        )
    return MENU

# Обработчик для меню
async def menu(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        "Выберите опцию:",
        reply_markup=ReplyKeyboardMarkup([["Выбор языка", "Поддержка"]], resize_keyboard=True)
    )
    return MENU

# Обработчик для выбора языка
async def language_selection(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        "Выберите язык:",
        reply_markup=ReplyKeyboardMarkup([["Английский", "Испанский", "Китайский"], ["Меню"]], resize_keyboard=True)
    )
    return LANGUAGE_SELECTION

# Обработчик для поддержки
async def support(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        "Вы обратились в поддержку. Чем могу помочь?\nВы можете вернуться в меню, нажав 'Меню'.",
        reply_markup=ReplyKeyboardMarkup([["Меню"]], resize_keyboard=True)
    )
    return SUPPORT

# Основная функция для настройки бота
def main():
    app = Application.builder().token(TOKEN).build()

    # ConversationHandler для управления диалогом с различными состояниями
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MENU: [
                MessageHandler(filters.Regex("^Меню$"), menu),
                MessageHandler(filters.Regex("^Выбор языка$"), language_selection),
                MessageHandler(filters.Regex("^Поддержка$"), support)
            ],
            LANGUAGE_SELECTION: [
                MessageHandler(filters.Regex("^(Английский|Испанский|Китайский)$"), language_selection),
                MessageHandler(filters.Regex("^Меню$"), menu)
            ],
            SUPPORT: [
                MessageHandler(filters.Regex("^Меню$"), menu)
            ]
        },
        fallbacks=[CommandHandler("start", start)],
    )

    app.add_handler(conv_handler)

    # Запускаем бота
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
