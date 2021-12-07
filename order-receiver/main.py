from fastapi import FastAPI

app = FastAPI()

user_id = "1"
product1 = {'id': "11", 'qty': 5}
product2 = {'id': "12", 'qty': 1}
product_list = [product1, product2]
query_message = {'user_id': user_id, 'products': product_list}


@app.get("/")
async def root():
    return {"company": "Manavsepeti"}


@app.get("/api/v1/orders")
async def fetch_orders():
    """Fetches all the orders..."""
    return query_message


@app.post("/api/v1/orders")
async def receive_order():
    """
    Receives an order and send it to RabbitMQ...
    input: models.Order
    """
    return {'message': "The order was sent to the query..."}
