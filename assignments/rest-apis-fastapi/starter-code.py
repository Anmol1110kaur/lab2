"""
FastAPI REST API Starter Code

This is a starter template for building a REST API with FastAPI.
Implement the endpoints and models below to create a functional API.

Key concepts to implement:
- FastAPI app initialization
- Pydantic models for request/response validation
- HTTP methods (GET, POST, PUT, DELETE)
- Path and query parameters
- Request body handling
- Basic error handling
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(
    title="Assignment API",
    description="A REST API built with FastAPI",
    version="1.0.0"
)


# Define Pydantic models for request/response validation
class Item(BaseModel):
    """Model representing an item with validation"""
    id: Optional[int] = Field(None, description="Item ID (auto-generated)")
    name: str = Field(..., min_length=1, description="Item name")
    description: Optional[str] = Field(None, description="Item description")
    price: float = Field(..., gt=0, description="Item price (must be positive)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Laptop",
                "description": "High-performance laptop",
                "price": 999.99
            }
        }


# In-memory storage (for demonstration purposes)
items_db: List[Item] = [
    Item(id=1, name="Item 1", description="First item", price=10.0),
    Item(id=2, name="Item 2", description="Second item", price=20.0),
]


# Root endpoint
@app.get("/", tags=["Root"])
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the FastAPI Assignment API"}


# TODO: Implement GET endpoint to retrieve all items
@app.get("/items/", tags=["Items"], response_model=List[Item])
def get_all_items(skip: int = Query(0, ge=0), limit: int = Query(10, gt=0)):
    """
    Retrieve all items with pagination support.
    
    - **skip**: Number of items to skip (default: 0)
    - **limit**: Max number of items to return (default: 10)
    """
    # TODO: Implement pagination logic
    return items_db[skip : skip + limit]


# TODO: Implement GET endpoint to retrieve a specific item by ID
@app.get("/items/{item_id}", tags=["Items"], response_model=Item)
def get_item(item_id: int):
    """
    Retrieve a specific item by ID.
    
    - **item_id**: The ID of the item to retrieve
    """
    # TODO: Find and return the item, or raise HTTPException(404) if not found
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


# TODO: Implement POST endpoint to create a new item
@app.post("/items/", tags=["Items"], response_model=Item, status_code=201)
def create_item(item: Item):
    """
    Create a new item.
    
    - **item**: Item object to create
    """
    # TODO: Validate input, assign ID, add to database, and return the created item
    # Hint: Generate a new ID based on the current items
    pass


# TODO: Implement PUT endpoint to update an item
@app.put("/items/{item_id}", tags=["Items"], response_model=Item)
def update_item(item_id: int, item: Item):
    """
    Update an existing item.
    
    - **item_id**: The ID of the item to update
    - **item**: Updated item object
    """
    # TODO: Find the item, update it, and return the updated item
    # Raise HTTPException(404) if not found
    pass


# TODO: Implement DELETE endpoint to remove an item
@app.delete("/items/{item_id}", tags=["Items"], status_code=204)
def delete_item(item_id: int):
    """
    Delete an item by ID.
    
    - **item_id**: The ID of the item to delete
    """
    # TODO: Find and remove the item, or raise HTTPException(404) if not found
    pass


# TODO: Add custom exception handler for specific error scenarios (optional)


if __name__ == "__main__":
    # To run the API:
    # 1. Install FastAPI: pip install fastapi uvicorn
    # 2. Run the server: uvicorn starter_code:app --reload
    # 3. Visit http://localhost:8000/docs for interactive documentation
    pass
