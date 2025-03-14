from fastapi.testclient import TestClient
from sample import app  # Importing from app.py

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world"}

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}

def test_read_user():
    response = client.get("/users/johndoe")
    assert response.status_code == 200
    assert response.json() == {"username": "johndoe"}