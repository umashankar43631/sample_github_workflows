from fastapi import FastAPI

app = FastAPI()

@app.route("/")
def home():
    return "Hello world"

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/{username}")
def read_user(username: str):
    return {"username": username}