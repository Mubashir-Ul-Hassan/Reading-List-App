# Reading List

A small command-line app that searches books by **title** or **author** using live data from the [Open Library API](https://openlibrary.org/developers/api) and saves your personal reading list to a JSON file.

## Features
- Search books by title or author (live API data)
- Save books to `reading_list.json`
- View and remove saved books
- Duplicate books are not saved twice

## Install
```bash
git clone https://github.com/Mubashir-Ul-Hassan/Reading-List-App.git
cd Reading-List-App
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run
```bash
python main.py
```

## Sample output

![App Demo](screenshots/screenshot.png)

```
=== Reading List ===
1. Search by title
2. Search by author
3. View my reading list
4. Remove a book
5. Quit

Choose: 1
Enter title: the hobbit
1. The Hobbit - J.R.R. Tolkien (1937)
2. The Hobbit Companion - David Day (1975)
Number to save (Enter to skip): 1
Saved: The Hobbit
```

`reading_list.json`:
```json
[
  {
    "key": "/works/OL262758W",
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937
  }
]
```

## Tech
Python 3, `requests`, Open Library Search API (no API key needed).
