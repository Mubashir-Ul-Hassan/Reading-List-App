import json
import os

FILE_NAME = "reading_list.json"


def load_list():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_list(books):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=2, ensure_ascii=False)


def add_book(book):
    """Add a book unless it is already saved. Returns True if added."""
    books = load_list()
    if any(b["key"] == book["key"] for b in books):
        return False
    books.append(book)
    save_list(books)
    return True


def remove_book(index):
    """Remove book by 0-based index. Returns the removed book or None."""
    books = load_list()
    if 0 <= index < len(books):
        removed = books.pop(index)
        save_list(books)
        return removed
    return None
