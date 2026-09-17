books = [
    {"title": "Python Basics", "author": "John Smith"},
    {"title": "Learn Programming", "author": "Ali Ahmad"},
    {"title": "Computer Science", "author": "Sara Omar"}
]


def show_books():
    print("\n--- All Books ---")
    for book in books:
        print("Title:", book["title"])
        print("Author:", book["author"])
        print()


def search_book():
    title = input("Enter book title: ")

    for book in books:
        if book["title"].lower() == title.lower():
            print("\nBook found!")
            print("Title:", book["title"])
            print("Author:", book["author"])
            return

    print("Book not found.")


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        "title": title,
        "author": author
    }

    books.append(book)
    print("Book added successfully!")


while True:
    print("\n===== Library App =====")
    print("1. Show all books")
    print("2. Search for a book")
    print("3. Add a book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_books()

    elif choice == "2":
        search_book()

    elif choice == "3":
        add_book()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")