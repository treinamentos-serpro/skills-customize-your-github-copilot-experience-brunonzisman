from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sample FastAPI App")


class Item(BaseModel):
    name: str
    price: float


items = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 25.50},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI API"}


@app.get("/items")
def read_items():
    return items


# TODO: implement POST /items
# TODO: implement GET /items/{item_id}
# TODO: implement PUT /items/{item_id}
# TODO: implement DELETE /items/{item_id}
