from fastapi.testclient import TestClient
from app_final import app, books_db
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_db():
    books_db.clear()

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_add_and_get_book():
    book_data = {"title": "1984", "author": "George Orwell", "year": 1949}
    
    response = client.post("/books", json=book_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Book added successfully"
    
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json()["total_count"] == 1
    assert response.json()["books"][0]["title"] == "1984"

def test_invalid_year():
    book_data = {"title": "Future Book", "author": "Unknown", "year": 3000}
    response = client.post("/books", json=book_data)
    assert response.status_code == 400
    assert "Year must be between 1000 and 2100" in response.json()["detail"]

def test_search_by_author():
    client.post("/books", json={"title": "Book A", "author": "J.K. Rowling", "year": 1997})
    client.post("/books", json={"title": "Book B", "author": "J.R.R. Tolkien", "year": 1954})
    
    response = client.get("/books/author/rowling")
    assert response.status_code == 200
    assert response.json()["count"] == 1
    assert response.json()["books"][0]["title"] == "Book A"