from api import search_books
from storage import add_book, load_list, remove_book

MENU = """
=== Reading List ===
1. Search by title
2. Search by author
3. View my reading list
4. Remove a book
5. Quit
"""


def show_books(books):
    for i, b in enumerate(books, start=1):
        year = b["year"] or "n/a"
        print(f"{i}. {b['title']} - {b['author']} ({year})")


def search_and_save(by):
    query = input(f"Enter {by}: ").strip()
    if not query:
        return
    results = search_books(query, by=by)
    if not results:
        print("No books found.")
        return
    show_books(results)
    choice = input("Number to save (Enter to skip): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(results):
        book = results[int(choice) - 1]
        if add_book(book):
            print(f"Saved: {book['title']}")
        else:
            print("Already in your list.")


def view_list():
    books = load_list()
    if not books:
        print("Your reading list is empty.")
    else:
        show_books(books)


def remove_flow():
    books = load_list()
    if not books:
        print("Nothing to remove.")
        return
    show_books(books)
    choice = input("Number to remove: ").strip()
    if choice.isdigit():
        removed = remove_book(int(choice) - 1)
        print(f"Removed: {removed['title']}" if removed else "Invalid number.")


def main():
    while True:
        print(MENU)
        choice = input("Choose: ").strip()
        if choice == "1":
            search_and_save("title")
        elif choice == "2":
            search_and_save("author")
        elif choice == "3":
            view_list()
        elif choice == "4":
            remove_flow()
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
