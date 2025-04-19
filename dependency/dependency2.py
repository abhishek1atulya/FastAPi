from fastapi import FastAPI, Depends
from dependency.dependency1 import get_db

app = FastAPI()


def get_user(user_id: int):
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id, "Unknown User")

@app.get("/users/{user_id}")
def get_user_info(user_id: int, db: str = Depends(get_db), user: str = Depends(get_user)):
    return {"user": user, "db_connection": db}
