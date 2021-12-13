# -manavsepeti-rabbitmq-fastapi

Pub-Sub mechanism on top of REST-API endpoints...

Installation process is demonstrated below.

There are two FastAPI applications in this repository.

First one is `order-receiver` which receives orders from clients and send them to a RabbitMQ queue.

Second one is `order-processor` which receives orders from a RabbitMQ queue and process them.


## Installation

1. Run RabbitMQ as a container.
```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
```

2. Create a virtual Python environment with `requirements.txt`.
```bash
python -m venv venv
pip install -r requirements.txt
```

3. Start `order-processor`.
```bash
cd order-processor
uvicorn main:app --reload --port 5000
```

4. Start `order-receiver`.
```bash
cd order-receiver
uvicorn main:app --reload --port 8000
```
