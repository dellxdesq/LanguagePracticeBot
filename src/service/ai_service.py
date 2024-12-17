import aiohttp
import logging
from dotenv import dotenv_values
from settings.texts import eng_ai_promt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChatGPT42AI:
    def __init__(self, max_history=10):
        config = dotenv_values(".env")

        self.api_key = config.get("API_KEY")
        self.url = config.get("API_URL")
        self.headers = {
            "Content-Type": "application/json",
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": "chatgpt-42.p.rapidapi.com"
        }
        self.max_history = max_history
        self.messages = []  # История сообщений теперь начинается с пустого списка

    async def get_response(self, user_input: str, temperature=0.9, top_k=5, top_p=0.9) -> str:
        try:
            # Сокращение истории, если она превышает лимит
            if len(self.messages) >= self.max_history:
                self.messages = self.messages[-(self.max_history - 1):]

            # Добавляем сообщение пользователя в историю
            self.messages.append({"role": "user", "content": user_input})

            logger.info(f"Отправляем запрос модели с историей: {self.messages}")

            # Создаем payload для запроса
            payload = {
                "messages": self.messages,
                "system_prompt": "You are a strict yet friendly language learning assistant. "
                                 "Always analyze user messages for spelling, grammar, and stylistic errors. "
                                 "If errors are found, point them out, provide the correct version, and explain why it is correct in simple language. "
                                 "Always respond in the same language the user uses. Do not answer in Russian; if they write in Russian, say you do "
                                 "not understand and ask to switch to another language."
                                 "After correcting errors, respond to the content of the message in a friendly way, share relevant comments, and ask questions to continue the conversation. "
                                 "Always analyze and correct errors first, then respond to the message content.",
                "temperature": 0.9,
                "top_k": 5,
                "top_p": 0.9,
                "image": "",
                "max_tokens": 200,
                "web_access": False
            }

            # Асинхронный POST-запрос к API
            async with aiohttp.ClientSession() as session:
                async with session.post(self.url, json=payload, headers=self.headers) as response:
                    if response.status == 200:
                        response_data = await response.json()
                        model_reply = response_data.get("result", "")
                        if model_reply:
                            logger.info(f"Ответ модели: {model_reply}")

                            # Добавляем ответ модели в историю
                            self.messages.append({"role": "assistant", "content": model_reply})
                            return model_reply
                        else:
                            logger.error("Ответ API не содержит контента.")
                            return "Ошибка: Ответ API не содержит контента."
                    else:
                        error_message = await response.text()
                        logger.error(f"Ошибка API: {response.status}, {error_message}")
                        return f"Произошла ошибка при запросе к API: {response.status}, {error_message}"

        except Exception as e:
            logger.error(f"Ошибка при запросе к ChatGPT 4.2: {e}")
            return f"Произошла ошибка: {e}"

    def set_history(self, history: list):
        """
        Заменяет текущую историю общения на новую.
        """
        self.messages = [
            {"role": "user" if m["sender"] == "user" else "assistant", "content": m["content"]}
            for m in history
        ]
