from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] 
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.post("/items/", status_code=201)
def create_item(item: Item):
    print(item)
    return {"name": item.name, "price": item.price, "is_offer": item.is_offer}
# In this example, the Item class is a Pydantic model that defines the structure of the 
# request body for the create_item endpoint.  