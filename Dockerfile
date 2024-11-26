FROM python:3.12.3

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app

COPY ./src /usr/src/app

CMD ["python", "src/bot.py"]