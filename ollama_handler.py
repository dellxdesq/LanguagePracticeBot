from ollama import chat, ChatResponse

class OllamaAI:
    def __init__(self, model_name="llama3", max_history=10):
        self.model_name = model_name
        self.max_history = max_history  # Ограничение на количество сообщений в истории
        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are an interesting and knowledgeable assistant."
                    "Answer in a friendly and conversational manner."
                    "Ask clarifying questions to keep the conversation going, "
                    "but don't ask too many, 2 or 3 questions will do."
                    "Analyze the users messages for grammatical, syntactical, or lexical errors, "
                    "and provide clear and constructive feedback. "
                    "Explain each mistake, if any, and suggest corrections. "
                    "If there are no mistakes, encourage the user by pointing out what they did well. "
                    "Maintain a friendly and supportive tone."
                ),
            }
        ]  # Начальная инструкция для модели

    def get_response(self, user_input: str) -> str:
        """Метод для получения ответа от модели с учетом истории диалога."""
        try:
            if len(self.messages) > self.max_history:
                self.messages = self.messages[-self.max_history:]
            # Добавляем сообщение пользователя в историю
            self.messages.append({'role': 'user', 'content': user_input})

            # Получаем ответ от модели
            response: ChatResponse = chat(
                model=self.model_name,
                messages=self.messages,
            )
            model_reply = response.message.content

            # Сохраняем ответ модели в истории
            self.messages.append({'role': 'assistant', 'content': model_reply})

            return model_reply
        except Exception as e:
            return f"Произошла ошибка при запросе к Ollama: {e}"



