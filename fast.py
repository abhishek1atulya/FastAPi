from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

items = []

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/")
def get_items():
    return {"items": items}

@app.post("/items/", status_code=201)
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id >= len(items) or item_id < 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
