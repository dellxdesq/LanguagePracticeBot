from ollama import chat, ChatResponse
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OllamaAI:
    def __init__(self, model_name="llama3", max_history=10):
        self.model_name = model_name
        self.max_history = max_history
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
        ]

        # Читаем параметры подключения из переменных окружения
        self.ollama_host = os.getenv("OLLAMA_HOST", "localhost")
        self.ollama_port = os.getenv("OLLAMA_PORT", "11434")

    def get_response(self, user_input: str) -> str:
        """Метод для получения ответа от модели с учетом истории диалога."""
        try:
            if len(self.messages) > self.max_history:
                self.messages = self.messages[-self.max_history:]

            self.messages.append({'role': 'user', 'content': user_input})
            logger.info(f"Отправляем запрос модели с историей: {self.messages}")

            # Здесь вызывается метод Ollama chat
            response = chat(model=self.model_name, messages=self.messages)
            model_reply = response.message.content
            logger.info(f"Ответ модели: {model_reply}")

            self.messages.append({'role': 'assistant', 'content': model_reply})
            return model_reply
        except Exception as e:
            logger.error(f"Ошибка при запросе к Ollama: {e}")
            return f"Произошла ошибка при запросе к Ollama: {e}"



