from fastapi import FastAPI

app = FastAPI()

# Sample data
items = [{"name": "Laptop", "price": 999.99}, {"name": "Smartphone", "price": 499.99}]

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < len(items):
        return items[item_id]
    return {"error": "Item not found"}
