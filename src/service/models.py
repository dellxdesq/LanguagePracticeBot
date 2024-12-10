from tortoise import fields
from tortoise.models import Model

class User(Model):
    unique_hash = fields.CharField(max_length=64, pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"

class Message(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="messages", to_field="unique_hash")
    sender = fields.CharField(max_length=10)
    content = fields.TextField()
    chat_state = fields.CharField(max_length=50, null=True)
    chat_id = fields.CharField(max_length=100, null=True)
    timestamp = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "messages"
        indexes = [
            ("user_id", "chat_state", "chat_id"),
        ]

class UserChat(Model):
    chat_id = fields.CharField(max_length=100, pk=True)
    user = fields.ForeignKeyField("models.User", related_name="chats", to_field="unique_hash")
    chat_state = fields.CharField(max_length=50)
    is_active = fields.BooleanField(default=True)
    timestamp = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user_chats"
