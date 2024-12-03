from tortoise import fields
from tortoise.models import Model

class User(Model):
    user_id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=255, null=True)
    full_name = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "users"

class Message(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="messages")
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
    user = fields.ForeignKeyField("models.User", related_name="chats")
    chat_state = fields.CharField(max_length=50)
    is_active = fields.BooleanField(default=True)
    timestamp = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user_chats"

