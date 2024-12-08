topics = ["Sport", "Music", "Literature", "Technology"]

topics_text = "\n".join(f"- {topic}" for topic in topics)

hello_text = (f"Привет! Я бот для практики иностранного языка с искусственным интеллектом. "
              f"В данный момент общение будет происходить на английском языке "
              f"Для общения на другом на языке, вам нужно указать его в чате, например - lets go speak spanish:\n\n"
              f"Пример тем, на которые вы можете пообщаться:\n\n"
              f"{topics_text}\n\n"
              f"Вы можете выбрать тему, написав её в чат, или предложить свою. "
              f"Например - lets go disscus about Sport:\n\n "
              f"Чтобы очистить историю диалога(это следует делать при переходе на другой язык) "
              f"нажмите кнопку \"Очистить историю\"")

eng_ai_promt = (
    "You are a friendly language learning assistant. Your main job is to help users improve their language skills:\n\n"
    "1. Analyze their messages for spelling, grammar, and stylistic errors.\n"
    " - There is no need to analyze the presence of errors in the sentence with the entered topic\n"
    " - If errors are found, **always point them out**.\n"
    " - Provide the correct version of the sentence.\n"
    " - **Always clearly explain why the correct version is correct and what was wrong with the original version.** "
    "Use simple language and examples to make it easy to understand.\n\n"
    "2. After fixing the errors, respond to the content of the user's message in a friendly and engaging way:\n"
    " - Share related facts or comments on the topic.\n"
    " - Ask questions to continue the conversation.\n\n"
    "3. Always follow the following order:\n"
    " - **First: analyze and correct errors (if any).**\n"
    " - **Second: respond to the content")


goodbye_message = "Goodbye! Чтобы поговорить снова, напиши /start\n\n"
