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


class Database:
    async def init(self):
        """Инициализация базы данных и подключения к ней через Tortoise ORM"""
        await Tortoise.init(
            db_url=f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
            modules={"models": ["service.models"]},  # Подключаем нашу модель
        )
        await Tortoise.generate_schemas()  # Создаём таблицы, если их нет

    async def create_user(self, user_id: int, username: str, full_name: str):
        """Создание пользователя в базе данных"""
        await User.get_or_create(user_id=user_id, username=username, full_name=full_name)

    async def get_user(self, user_id: int):
        """Получение пользователя по user_id"""
        return await User.get(user_id=user_id)

    async def close(self):
        """Закрытие соединения с базой данных"""
        await Tortoise.close_connections()

    async def save_message(self, user_id: int, sender: str, content: str, chat_state: str = None, chat_id: str = None):
        """Сохранение сообщения в базе данных."""
        user = await User.get(user_id=user_id)
        await Message.create(
            user=user,
            sender=sender,
            content=content,
            chat_state=chat_state,
            chat_id=chat_id  # Учет chat_id
        )

    async def create_chat(self, user_id: int, chat_state: str):
        """Создание нового чата для пользователя"""
        chat_id = str(uuid.uuid4())  # Генерация нового уникального chat_id
        user = await User.get(user_id=user_id)
        await UserChat.create(user=user, chat_id=chat_id, chat_state=chat_state)
        return chat_id

    async def get_active_chat(self, user_id: int):
        """Получение активного чата для пользователя"""
        return await UserChat.filter(user_id=user_id, is_active=True).first()

    async def get_chat_history(self, chat_id: str):
        """Получение истории чата по chat_id."""
        messages = await Message.filter(chat_id=chat_id).order_by("timestamp").values("sender", "content")
        return messages