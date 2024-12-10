import hashlib
from tortoise import Tortoise
from dotenv import load_dotenv
from service.models import Message, User, UserChat
import os
import uuid

load_dotenv()

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'language_practice_db')
DB_USER = os.getenv('DB_USER', 'postgres_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', '123456')

# Соль для хэширования
SALT = os.getenv("HASH_SALT", "default_salt")

def generate_user_hash(user_id: int, username: str) -> str:
    raw_data = f"{user_id}-{username}-{SALT}"
    return hashlib.sha256(raw_data.encode()).hexdigest()

class Database:
    async def init(self):
        await Tortoise.init(
            db_url=f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
            modules={"models": ["service.models"]},  # Подключаем нашу модель
        )
        await Tortoise.generate_schemas()  # Создаём таблицы, если их нет

    async def get_user(self, user_id: int, username: str):
        unique_hash = generate_user_hash(user_id, username)
        user, created = await User.get_or_create(unique_hash=unique_hash)
        return user

    async def close(self):
        await Tortoise.close_connections()

    async def save_message(self, user_id: int, username: str, sender: str, content: str, chat_state: str = None, chat_id: str = None):
        unique_hash = generate_user_hash(user_id, username)
        user = await User.get(unique_hash=unique_hash)
        await Message.create(
            user=user,
            sender=sender,
            content=content,
            chat_state=chat_state,
            chat_id=chat_id
        )

    async def create_chat(self, user_id: int, username: str, chat_state: str):
        chat_id = str(uuid.uuid4())  # Генерация нового уникального chat_id
        unique_hash = generate_user_hash(user_id, username)
        user = await User.get(unique_hash=unique_hash)
        await UserChat.create(user=user, chat_id=chat_id, chat_state=chat_state)
        return chat_id

    async def get_active_chat(self, user_id: int, username: str, chat_state: str = None):
        unique_hash = generate_user_hash(user_id, username)
        query = UserChat.filter(user_id=unique_hash, is_active=True)
        if chat_state:
            query = query.filter(chat_state=chat_state)
        return await query.first()

    async def end_active_chat(self, user_id: int, username: str):
        unique_hash = generate_user_hash(user_id, username)
        active_chat = await UserChat.filter(user_id=unique_hash, is_active=True).first()

        if active_chat:
            # Завершаем активный чат, ставим is_active в False
            active_chat.is_active = False
            await active_chat.save()
            return True  # Успешно завершили чат
        return False  # Не найден активный чат для завершения    

    async def get_chat_history(self, chat_id: str):
        messages = await Message.filter(chat_id=chat_id).order_by("timestamp").values("sender", "content")
        return messages
