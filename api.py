import requests

SEARCH_URL = "https://openlibrary.org/search.json"
HEADERS = {"User-Agent": "reading-list-project (student assignment)"}


def search_books(query, by="title", limit=5):
    """Search Open Library. `by` is 'title' or 'author'. Returns a list of dicts."""
    params = {
        by: query,
        "limit": limit,
        "fields": "key,title,author_name,first_publish_year",
    }
    try:
        response = requests.get(SEARCH_URL, params=params, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Could not reach Open Library: {error}")
        return []

    books = []
    for doc in response.json().get("docs", []):
        books.append({
            "key": doc.get("key"),
            "title": doc.get("title", "Unknown title"),
            "author": ", ".join(doc.get("author_name", ["Unknown author"])),
            "year": doc.get("first_publish_year"),
        })
    return books
