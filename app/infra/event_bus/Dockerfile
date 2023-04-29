FROM python:3.11-slim

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && apt install netcat -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pika

RUN mkdir /app/infra
RUN mkdir /app/infra/event_bus
RUN mkdir /app/infra/event_bus/data

COPY __init__.py /app/
COPY __init__.py /app/infra/
COPY __init__.py /app/infra/event_bus/
COPY listen_queue.py /app/infra/event_bus

ADD start_listen_queue.sh /start_listen_queue.sh

CMD ["/start_listen_queue.sh"]
