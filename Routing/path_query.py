from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Sample data
items = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Smartphone", "price": 499.99},
    {"name": "Tablet", "price": 299.99},
    {"name": "Headphones", "price": 79.99},
    {"name": "Laptop", "price": 119.99}
]

@app.get("/items/")
def get_items(search: Optional[str] = None, skip: int = 0, limit: int = 10):
    if search:
        filtered_items = [item for item in items if search.lower() == item["name"].lower()]
    else:
        filtered_items = items
    return filtered_items[skip: skip + limit]
