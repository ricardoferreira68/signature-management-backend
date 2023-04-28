FROM python:3.11-slim

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pika

RUN mkdir /app/infra
RUN mkdir /app/infra/event_bus
RUN mkdir /app/infra/event_bus/data

COPY __init__.py /app/
COPY __init__.py /app/infra/
COPY __init__.py /app/infra/event_bus/
COPY listen_queues.py /app/infra/event_bus

# CMD ["sleep", "60"]

# CMD ["python", "/app/infra/event_bus/listen_queues.py"]
