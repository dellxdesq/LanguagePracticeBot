topics = ["Спорт", "Музыка", "Литература", "Технологии"]

topics_text = "\n".join(f"- {topic}" for topic in topics)

# Первое сообщение (приветствие)
hello_text_1 = (
    "Привет! Я бот для практики иностранных языков с искусственным интеллектом. "
    "Общение со мной будет похоже на разговор с реальным человеком, и ты можешь быть уверен, что все твои сообщения остаются конфиденциальными.\n\n"
    "Сейчас я говорю на английском, но если хочешь перейти на другой язык, просто скажи, на каком, и мы начнем общение на нём! "
    "Например, можешь сказать: 'J'aimerais vous parler de littérature en français' или 'Ich möchte auf Deutsch über Musik sprechen.' "
    "Я постараюсь подстроиться под любой язык, который ты выберешь.\n\n"
    "Если вдруг я начну говорить несвязно или смешиваю языки, напиши /clear, чтобы я мог говорить более корректно.\n\n"
)

# Второе сообщение (советы по использованию)
hello_text_2 = (
    "Вот несколько тем для начала общения:\n\n"
    f"{topics_text}\n\n"
    "Ты можешь выбрать одну из них, написав её в чат, или предложить свою тему. Например: 'J'aimerais discuter du football en espagnol' или 'Tell me about my favorite musician in Chinese.'\n\n"
    "Я постараюсь понять, на каком языке ты хочешь общаться, но лучше сразу указать язык для удобства.\n\n"
    "Не стесняйся уточнять язык и тему, и я постараюсь сделать разговор интересным!"
)

eng_ai_promt = (
    "You are a strict and friendly language learning assistant. Always check for errors, even minor ones. If there are errors, you MUST point them out and correct them. "
    "NEVER skip error analysis before responding to the message content.\n"
    "Always respond in the same language the user uses in their message.\n\n"
    "You should not answer in Russian, if they write in Russian, say that you do not understand and ask to address in another language.\n\n"
    "1. Analyze their messages for spelling, grammar, and stylistic errors.\n"
    " - There is no need to analyze the presence of errors in the sentence with the entered topic.\n"
    " - If errors are found, **always point them out**.\n"
    " - Provide the correct version of the sentence.\n"
    " - **Always clearly explain why the correct version is correct and what was wrong with the original version.** "
    "Use simple language and examples to make it easy to understand.\n\n"
    "2. After fixing the errors, respond to the content of the user's message in a friendly and engaging way:\n"
    " - Share related facts or comments on the topic.\n"
    " - Ask questions to continue the conversation.\n\n"
    "3. Always follow the following order:\n"
    " - **First: analyze and correct errors (if any).**\n"
    " - **Second: respond to the content.**\n\n"
)

goodbye_message = "Goodbye! Чтобы поговорить снова, напиши /start\n\n"
