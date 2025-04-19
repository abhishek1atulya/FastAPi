from fastapi import FastAPI, Depends

app = FastAPI()


class Database:
    def __init__(self):
        self.connection = "Connected to Database"

    def get_data(self):
        return "Fetching data..."

    def close(self):
        return "Closing database connection."

# Create a dependency that returns an instance of the Database class
def get_database():
    db = Database()
    try:
        yield db  # Yield the database instance to be used in the route
    finally:
        db.close()  # Cleanup: Close the connection after use

@app.get("/data/")
def get_data(db: Database = Depends(get_database)):
    return {"message": db.get_data()}
