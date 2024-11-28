from transformers import AutoModelForCausalLM, AutoTokenizer

class BloomService:
    def __init__(self, model_name="bigscience/bloom-560m", max_length=50):
        """
        Инициализация модели BLOOM
        :param model_name: Название модели (по умолчанию bigscience/bloom-560m)
        :param max_length: Максимальная длина ответа
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.max_length = max_length

    def generate_response(self, prompt: str) -> str:
        print(f"Получен запрос: {prompt}")  # Логирование запроса
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(
            inputs["input_ids"],
            max_length=self.max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            do_sample=True,
            temperature=0.7
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Ответ от модели: {response}")  # Логирование ответа
        return response
