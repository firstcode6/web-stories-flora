FROM python:3.7

# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1

# где будут храниться собранный проект
WORKDIR /src_flora

# Установка модулей для линукс
RUN apt update && apt install -y gcc

# Установка питон модулей
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY stories_flora .

CMD sh start.sh
