# Используем официальный образ Python
FROM python:3.13-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости в контейнер
COPY requirements.txt /app/

# Установить зависимости системы
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    jq \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всю папку проекта в контейнер
COPY . /app/

# Запускаем бота
CMD ["python", "src/bot.py"]
