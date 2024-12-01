from tortoise import fields
from tortoise.models import Model

class User(Model):
    user_id = fields.BigIntField(pk=True)  # уникальный идентификатор пользователя
    username = fields.CharField(max_length=255, null=True)
    full_name = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "users"

class Message(Model):
    id = fields.IntField(pk=True)  # Уникальный идентификатор сообщения
    user = fields.ForeignKeyField("models.User", related_name="messages")  # Ссылка на пользователя
    sender = fields.CharField(max_length=10)  # "user" или "bot"
    content = fields.TextField()  # Текст сообщения
    chat_state = fields.CharField(max_length=50, null=True)  # Состояние чата (например, "CHAT")
    timestamp = fields.DatetimeField(auto_now_add=True)  # Время отправки

    class Meta:
        table = "messages"
        indexes = [
            ("user_id", "chat_state"),  # Индекс для ускорения фильтрации по пользователю и состоянию
        ]
