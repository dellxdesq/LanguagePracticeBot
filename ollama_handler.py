from ollama import chat, ChatResponse

class OllamaAI:
    def __init__(self, model_name="llama3"):
        self.model_name = model_name
        self.messages = []

    def get_response(self, user_input: str) -> str:
        """Метод для получения ответа от модели с учетом контекста и инструкций."""
        try:
            prompt = f"""
            You are an engaging and knowledgeable assistant. 
            The user wants to discuss the topic: "{user_input}". 
            - Respond in a friendly and conversational tone.
            - Ask follow-up questions to keep the conversation going.
            - If appropriate, include an interesting fact or example related to the topic.
            """

            self.messages.append({'role': 'system', 'content': prompt})
            self.messages.append({'role': 'user', 'content': user_input})

            response: ChatResponse = chat(model=self.model_name, messages=self.messages)
            model_reply = response.message.content
            self.messages.append({'role': 'assistant', 'content': model_reply})

            return model_reply
        except Exception as e:
            return f"Произошла ошибка при запросе к Ollama: {e}"


