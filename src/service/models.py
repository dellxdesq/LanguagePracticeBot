from tortoise import fields
from tortoise.models import Model

class User(Model):
    user_id = fields.BigIntField(pk=True)  # уникальный идентификатор пользователя
    username = fields.CharField(max_length=255, null=True)
    full_name = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "users"
