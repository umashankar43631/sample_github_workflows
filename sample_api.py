"""
This module contains FastAPI routes for handling dynamic integer and string values.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    """
    Returns a greeting message.
    """
    return {"message": "Hello world"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Returns the item ID.
    
    Args:
        item_id (int): The ID of the item.
    
    Returns:
        dict: A dictionary containing the item ID.
    """
    return {"item_id": item_id}

@app.get("/users/{username}")
def read_user(username: str):
    """
    Returns the username.
    
    Args:
        username (str): The username.
    
    Returns:
        dict: A dictionary containing the username.
    """
    return {"username": username}

# Ensure the file ends with a newline