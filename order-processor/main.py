from fastapi import FastAPI
import pika

app = FastAPI()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='order')

user_id = "1"
orders = []


@app.get("/")
async def root():
    return {"company": "Manavsepeti"}


@app.get("/api/v1/orders")
async def fetch_orders():
    """Fetches all the orders..."""
    return orders


@app.get("/api/v1/process-orders")
async def process_orders():
    """
    Receives an order and send it to RabbitMQ...
    input: models.Order
    """
    def callback(ch, method, properties, body):
        """
        callback function of RabbitMQ receiver.
        output: models.Order
        """
        print(" [x] Received %r" % body)
        # body["fulfilled"] = True
        orders.append(body)

    channel.basic_consume(
        queue='order',
        auto_ack=True,
        on_message_callback=callback
    )
    channel.start_consuming()
