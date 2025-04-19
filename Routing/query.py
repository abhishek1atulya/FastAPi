from fastapi import FastAPI

App = FastAPI()

# Sample data
items = [{"name": "Laptop", "price": 999.99}, {"name": "Smartphone", "price": 499.99}]

@App.get("/items/")
def get_items(skip: int = 0, limit: int = 10):
    return items[skip: skip + limit]
