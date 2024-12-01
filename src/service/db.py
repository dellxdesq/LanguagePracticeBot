from tortoise import Tortoise
from dotenv import load_dotenv
from src.service.models import User
import os

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
