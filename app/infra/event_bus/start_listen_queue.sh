#!/bin/bash

while ! nc -z rabbitmq 5672; do sleep 30; done
python3 /app/infra/event_bus/listen_queue.py
