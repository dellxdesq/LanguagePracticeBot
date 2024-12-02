from ollama import chat, ChatResponse
import logging
from settings.texts import spanish_ai_promt
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SpanishOllamaAI:
    def __init__(self, model_name="llama3.2", max_history=10):
        self.model_name = model_name
        self.is_first_message = True
        self.max_history = max_history
        self.messages = [
            {
                "role": "system",
                "content": spanish_ai_promt,
            }
        ]

        # Читаем параметры подключения из переменных окружения
        self.ollama_host = os.getenv("OLLAMA_HOST", "localhost")
        self.ollama_port = os.getenv("OLLAMA_PORT", "11434")

    def get_response(self, user_input: str) -> str:
        if not user_input:
            print("Сообщение не дошло блять")
        """Метод для получения ответа от модели с учетом истории диалога."""
        try:
            if len(self.messages) > self.max_history:
                self.messages = self.messages[-self.max_history:]
            if self.is_first_message:
                user_input = f"Hablemos de {user_input}"
                self.is_first_message = False  # После первого обращения флаг отключается

            self.messages.append({'role': 'user', 'content': user_input})
            logger.info(f"Отправляем запрос модели с историей: {self.messages}")

            response = chat(model=self.model_name, messages=self.messages)
            model_reply = response.message.content
            logger.info(f"Ответ модели: {model_reply}")
            self.messages.append({'role': 'assistant', 'content': model_reply})
            return model_reply
        except Exception as e:
            logger.error(f"Ошибка при запросе к Ollama: {e}")
            return f"Произошла ошибка при запросе к Ollama: {e}"

    def set_history(self, history: list):
        """Загружает историю из базы данных."""
        self.messages = [
            {"role": "system", "content": spanish_ai_promt}
        ] + [{"role": "user" if m["sender"] == "user" else "assistant", "content": m["content"]} for m in history]



