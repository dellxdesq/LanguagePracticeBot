topics = ["Спорт", "Музыка", "Литература", "Технологии"]

topics_text = "\n".join(f"- {topic}" for topic in topics)

# Первое сообщение (приветствие)
hello_text_1 = (
    "Привет! Я бот для практики иностранных языков. Общение со мной похоже на разговор с человеком, а твои сообщения остаются конфиденциальными.\n\n"
    "Сейчас я говорю на английском, но можешь выбрать другой язык — просто напиши, на каком! Например: 'J'aimerais vous parler de littérature en français' или 'Ich möchte auf Deutsch über Musik sprechen.'\n\n"
    "Если я начну путаться в языках, напиши /clear для очистки истории или кнопку для остановки диалога.\n"
)

# Второе сообщение (советы по использованию)
hello_text_2 = (
    "Вот несколько тем для начала:\n\n"
    f"{topics_text}\n\n"
    "Напиши любую из них или предложи свою тему.\n\n"
    "Лучше сразу указать язык, чтобы мне было проще понять тебя. Не стесняйся уточнять детали — я сделаю наш разговор интересным!"
)

eng_ai_promt = (
    "You are a strict yet friendly language learning assistant. "
    "Always analyze user messages for spelling, grammar, and stylistic errors. "
    "If errors are found, point them out, provide the correct version, and explain why it is correct in simple language. "
    "Always respond in the same language the user uses. Do not answer in Russian; if they write in Russian, say you do "
    "not understand and ask to switch to another language."
    "After correcting errors, respond to the content of the message in a friendly way, share relevant comments, and ask questions to continue the conversation. "
    "Always analyze and correct errors first, then respond to the message content."
)

goodbye_message = "Goodbye! Чтобы поговорить снова, напиши /start\n\n"
