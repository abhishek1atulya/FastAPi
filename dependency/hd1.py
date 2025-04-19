from fastapi import FastAPI, Depends

app = FastAPI()

# ✅ Dependency Function for Database Session
def get_db():
    db = {"connection": "database_connected"}  # Simulated DB connection
    try:
        yield db  # Return database connection
    finally:
        db.clear()  # Close connection (cleanup)

# ✅ Using the Dependency in an API Route
@app.get("/items/")
def read_items(db: dict = Depends(get_db)):
    return {"message": "Data fetched", "db_status": db}
