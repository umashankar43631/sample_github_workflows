"""
This module contains unit tests for the FastAPI application defined in app.py.
It includes tests for the home route, item route, and user route.
"""

from fastapi.testclient import TestClient
from sample import app  # Importing from app.py

client = TestClient(app)

def test_home():
    """
    Test the home route.

    This test checks if the home route returns a status code of 200 and the expected JSON response.

    Returns:
        None
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world"}

def test_read_item():
    """
    Test the item route.

    This test checks if the item route returns a status code of 200 and the expected JSON response
    when provided with an integer item_id.

    Args:
        item_id (int): The ID of the item.

    Returns:
        None
    """
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}

def test_read_user():
    """
    Test the user route.

    This test checks if the user route returns a status code of 200 and the expected JSON response
    when provided with a string username.

    Args:
        username (str): The username.

    Returns:
        None
    """
    response = client.get("/users/johndoe")
    assert response.status_code == 200
    assert response.json() == {"username": "johndoe"}