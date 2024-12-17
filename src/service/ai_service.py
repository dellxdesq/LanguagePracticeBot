import aiohttp
import logging
from settings.texts import eng_ai_promt
from dotenv import dotenv_values

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatGPT42AI:
    def __init__(self, max_history=10):
        config = dotenv_values(".env")

        self.api_key = config.get("API_KEY")
        self.url = config.get("API_URL")
        self.headers = {
            "Content-Type": "application/json",
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com"
        }
        self.max_history = max_history
        self.messages = [
            {
                "role": "system",
                "content": eng_ai_promt,
            }
        ]

    async def get_response(self, user_input: str) -> str:
        try:
            # Сокращение истории, если она превышает лимит
            if len(self.messages) > self.max_history:
                self.messages = [self.messages[0]] + self.messages[-(self.max_history-1):]

            # Добавляем сообщение пользователя в историю
            self.messages.append({"role": "user", "content": user_input})

            logger.info(f"Отправляем запрос модели с историей: {self.messages}")

            # Создаем payload для запроса
            payload = {
                "model": "gpt-4.2",
                "messages": self.messages,
                "webaccess": True
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
                        logger.error(f"Ошибка API: {response.status}, {await response.text()}")
                        return f"Произошла ошибка при запросе к API: {response.status}, {await response.text()}"

        except Exception as e:
            logger.error(f"Ошибка при запросе к ChatGPT 4.2: {e}")
            return f"Произошла ошибка: {e}"

    def set_history(self, history: list):
        self.messages = [
            {"role": "system", "content": eng_ai_promt}
        ] + [
            {"role": "user" if m["sender"] == "user" else "assistant", "content": m["content"]}
            for m in history
        ]
