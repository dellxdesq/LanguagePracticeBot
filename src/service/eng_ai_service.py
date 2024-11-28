from ollama import chat
import logging
from src.settings.texts import eng_ai_promt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OllamaAI:
    def __init__(self, model_name="llama3", max_history=10):
        self.model_name = model_name
        self.is_first_message = True
        self.max_history = max_history
        self.messages = [
            {
                "role": "system",
                "content": eng_ai_promt,
            }
        ]

    def get_response(self, user_input: str) -> str:
        """Метод для получения ответа от модели с учетом истории диалога."""
        try:
            if len(self.messages) > self.max_history:
                self.messages = self.messages[-self.max_history:]
            if self.is_first_message:
                user_input = f"Go discuss topic of {user_input}"
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





