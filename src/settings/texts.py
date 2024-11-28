topics = ["Sport", "Music", "Literature", "Technology"]
spanish_topics = ["Deporte", "Música", "Literatura", "Tecnología"]

topics_text = "\n".join(f"- {topic}" for topic in topics)
spanish_topics_text = "\n".join(f"- {topic}" for topic in spanish_topics)

hello_text = (f"Привет! Я бот для практики иностранного языка с искусственным интеллектом. "
              f"В данный момент доступно общение на английском языке, но скоро появятся и другие. "
              f"Вот пример тем, на которые вы можете пообщаться:\n\n"
              f"{topics_text}\n\n"
              f"Вы можете выбрать тему, написав её в чат, или предложить свою. "
              f"Чтобы прекратить общение, нажмите кнопку \"Остановить диалог\"")

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


spanish_ai_promt = (
    "Eres un asistente amigable para el aprendizaje de idiomas. "
    "Tu trabajo principal es ayudar a los usuarios a mejorar sus habilidades lingüísticas:\n\n"
    "1. Analiza sus mensajes en busca de errores ortográficos, gramaticales y de estilo.\n"
    "- No es necesario analizar la presencia de errores en la oración con el tema ingresado\n"
    "- Si se encuentran errores, **siempre señálalos**.\n"
    "- Proporciona la versión correcta de la oración.\n"
    "- **Explica siempre claramente por qué la versión correcta es correcta y qué estaba mal con la versión original.** "
    "Usa un lenguaje simple y ejemplos para que sea fácil de entender.\n\n"
    "2. Después de corregir los errores, responde al contenido del mensaje del usuario de una manera amigable y atractiva:\n"
    "- Comparte hechos o comentarios relacionados con el tema.\n"
    "- Haz preguntas para continuar el conversación.\n\n"
    "3. Siga siempre el siguiente orden:\n"
    " - **Primero: analizar y corregir errores (si los hay).**\n"
    " - **Segundo: responder al contenido")

spanish_hello_text = (f"Язык именён на Испанский. "
                      f"Вот пример тем, на которые вы можете пообщаться:\n\n"
                      f"{spanish_topics_text}\n\n"
                      f"Вы можете выбрать тему, написав её в чат, или предложить свою. "
                      f"Чтобы прекратить общение, нажмите кнопку \"Остановить диалог\"")

goodbye_message = "Goodbye! Если захочешь поговорить снова, напиши /start"
