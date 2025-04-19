from fastapi import FastAPI, Depends

app = FastAPI()

# Simulating a database connection
def get_db():
    db = "Database Connection"
    return db

@app.get("/items/")
def get_items(db: str = Depends(get_db)):
    return {"db_connection": db}
