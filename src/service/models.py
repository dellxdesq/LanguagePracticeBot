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
    chat_state = fields.CharField(max_length=50, null=True)  # Состояние чата (например, "ENG_CHAT")
    chat_id = fields.CharField(max_length=100, null=True)  # Новый параметр для идентификации чата
    timestamp = fields.DatetimeField(auto_now_add=True)  # Время отправки

    class Meta:
        table = "messages"
        indexes = [
            ("user_id", "chat_state", "chat_id"),  # Добавляем индекс для chat_id
        ]

class UserChat(Model):
    chat_id = fields.CharField(max_length=100, pk=True)  # Уникальный идентификатор чата
    user = fields.ForeignKeyField("models.User", related_name="chats")  # Ссылка на пользователя
    chat_state = fields.CharField(max_length=50)  # Состояние чата (например, "ENG_CHAT")
    is_active = fields.BooleanField(default=True)  # Флаг активности чата
    timestamp = fields.DatetimeField(auto_now_add=True)  # Время начала чата

    class Meta:
        table = "user_chats"

