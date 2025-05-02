import pickle
from datetime import datetime, timedelta

books = []

def load_books():
    global books
    try:
        with open("library_data.pkl", "rb") as f:
            books = pickle.load(f)
    except:
        books = []

def save_books():
    with open("library_data.pkl", "wb") as f:
        pickle.dump(books, f)

def add_book(title, author):
    books.append({"title": title, "author": author, "borrowed": False, "due_date": None})

def borrow_book(title):
    for book in books:
        if book["title"] == title and not book["borrowed"]:
            book["borrowed"] = True
            book["due_date"] = datetime.now() + timedelta(days=14)
            save_books()
            return f"You borrowed {title}. Due date: {book['due_date']}"
    return "Book is not available."

def return_book(title):
    for book in books:
        if book["title"] == title and book["borrowed"]:
            book["borrowed"] = False
            book["due_date"] = None
            save_books()
            return f"You returned {title}."
    return "This book wasn't borrowed."

def search_book(title):
    for book in books:
        if book["title"] == title:
            overdue = False
            if book["borrowed"] and book["due_date"] < datetime.now():
                overdue = True
            return f"Title: {book['title']}, Author: {book['author']}, Borrowed: {book['borrowed']}, Overdue: {overdue}"
    return "Book not found."

def main():
    load_books()

    while True:
        action = input("Enter action (add/borrow/return/search/exit): ").lower()

        if action == "add":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
            print(f"Book '{title}' added.")

        elif action == "borrow":
            title = input("Enter book title to borrow: ")
            print(borrow_book(title))

        elif action == "return":
            title = input("Enter book title to return: ")
            print(return_book(title))

        elif action == "search":
            title = input("Enter book title to search: ")
            print(search_book(title))

        elif action == "exit":
            print("Exiting the library system.")
            break

if __name__ == "__main__":
    main()
