from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Product(BaseModel):
    id: UUID = uuid4()
    qty: str


class Order(BaseModel):
    user_id: Optional[UUID] = uuid4()
    fulfilled: Optional[bool] = False
    products: List[Product]
