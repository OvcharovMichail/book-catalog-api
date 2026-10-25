import os
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

app = FastAPI(title="Book Catalog API")

books_db = []

class Book(BaseModel):
    title: str
    author: str
    year: int

@app.on_event("startup")
async def startup_event():
    logger.info(f"Book Catalog API starting. Version: {APP_VERSION}")

@app.get("/health")
def health_check():
    logger.info("Health check requested")
    return {"status": "ok"}

@app.get("/version")
def get_version():
    logger.info("Version requested")
    return {"version": APP_VERSION}

@app.post("/books")
def add_book(book: Book):
    if book.year < 1000 or book.year > 2100:
        logger.warning(f"Invalid book year: {book.year}")
        raise HTTPException(status_code=400, detail="Year must be between 1000 and 2100")
    
    books_db.append(book.model_dump())
    logger.info(f"Book added: '{book.title}' by {book.author}")
    return {"message": "Book added successfully", "book": book}

@app.get("/books")
def get_all_books():
    logger.info(f"Returning {len(books_db)} books")
    return {"books": books_db, "total_count": len(books_db)}

@app.get("/books/author/{author_name}")
def get_books_by_author(author_name: str):
    filtered = [b for b in books_db if author_name.lower() in b["author"].lower()]
    logger.info(f"Found {len(filtered)} books by author '{author_name}'")
    return {"author": author_name, "books": filtered, "count": len(filtered)}