# Library Management System


from datetime import datetime, timedelta

import json

with open("books_data.json", "r", encoding="utf-8") as f:
    library = json.load(f)

try:
    with open("lent_books.json", "r", encoding="utf-8") as f:
        lent_books = json.load(f)
except FileNotFoundError:
    lent_books = []


# Function for Authentication
def login():
    print("Welcome to Library Management System\n")
    user_id = input("Enter User ID: ").strip()
    password = input("Enter Password: ").strip()
    if user_id == "Admin" and password == "Admin123":
        return "Admin"
    elif user_id == "User" and password == "User123":
        return "User"
    else:
        print("Invalid credentials!\n")
        return None


# Book Operations
def add_book():
    title = input("Enter Book Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    author = input("Enter Author Name: ").strip()
    if not author:
        print("Author cannot be empty.")
        return

    genre = input("Enter Genre: ").strip()
    if not genre:
        print("Genre cannot be empty.")
        return

    try:
        year = int(input("Enter Year of Publication: ").strip())
    except ValueError:
        print("Invalid year format.")
        return

    book = {"title": title, "author": author, "genre": genre, "year": year}
    library.append(book)

    with open("books_data.json", "w", encoding="utf-8") as f:
        json.dump(library, f, indent=4)

    print("Book added successfully.\n")


def view_books():  # Function to view all books
    if not library:
        print("No books in the library.\n")
    else:
        print("\nBooks in Library:")
        for idx, book in enumerate(library, 1):
            print(
                f"{idx}. {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']}"
            )


def remove_book():
    title = input("Enter Book Title to Remove: ").strip()
    author = input("Enter Author Name: ").strip()

    try:
        year = int(input("Enter Year of Publication: ").strip())
    except ValueError:
        print("Invalid year format.")
        return

    for book in library:
        if (
            book["title"].lower() == title.lower()
            and book["author"].lower() == author.lower()
            and book["year"] == year
        ):
            confirm = (
                input(
                    f"Are you sure you want to remove '{title}' by {author} ({year})? (y/n): "
                )
                .strip()
                .lower()
            )
            if confirm == "y":
                library.remove(book)

                with open("books_data.json", "w", encoding="utf-8") as f:
                    json.dump(library, f, indent=4)

                print("Book removed successfully.\n")
            else:
                print("Removal cancelled.\n")
            return

    print("Book not found with that title, author, and year.\n")


def view_all_lent_books():  # Function to lend a book
    if not lent_books:
        print("No books have been lent out.\n")
    else:
        print("All Lent Books:")
        for idx, record in enumerate(lent_books, 1):
            b = record["book"]
            br = record["borrower"]
            print(f"{idx}. '{b['title']}' by {b['author']} ({b['year']})")
            print(
                f"    Borrowed by: {br['name']} | Phone: {br['phone']} | Address: {br['address']}\n"
            )


def view_user_lent_books():
    name = input("Enter your name to check your borrowed books: ").strip().lower()
    user_books = [r for r in lent_books if r["borrower"]["name"].lower() == name]

    if not user_books:
        print("You have not borrowed any books.\n")
    else:
        print(f"Books borrowed by {name.title()}:")
        for idx, record in enumerate(user_books, 1):
            b = record["book"]
            print(f"{idx}. '{b['title']}' by {b['author']} ({b['year']})")


def update_book():
    title = input("Enter Book Title to Update: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            print("Leave blank to keep existing value.")
            new_author = input("Enter new Author: ").strip()
            new_genre = input("Enter new Genre: ").strip()
            new_year = input("Enter new Year of Publication: ").strip()

            if new_author:
                book["author"] = new_author
            if new_genre:
                book["genre"] = new_genre
            if new_year:
                try:
                    book["year"] = int(new_year)
                except ValueError:
                    print("Invalid year format.")
                    return

            with open("books_data.json", "w", encoding="utf-8") as f:
                json.dump(library, f, indent=4)

            print("Book updated successfully.\n")
            return

    print("Book not found.\n")


def save_data():
    with open("books_data.json", "w", encoding="utf-8") as f:
        json.dump(library, f, indent=4)
    with open("lent_books.json", "w", encoding="utf-8") as f:
        json.dump(lent_books, f, indent=4)


def search_book():
    keyword = (
        input("Enter keyword to search (title/author/genre/year): ").strip().lower()
    )
    if not keyword:
        print("Keyword cannot be empty.")
        return

    results = [
        book
        for book in library
        if keyword in book["title"].lower()
        or keyword in book["author"].lower()
        or keyword in book["genre"].lower()
        or keyword == str(book["year"])
    ]
    if results:
        print("Search results:")
        for idx, book in enumerate(results, 1):
            print(
                f"{idx}. {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']}"
            )
    else:
        print("No matching books found.\n")


# Lending System
def lend_book():
    title = input("Enter title of book to lend: ").strip()
    name = input("Enter your name: ").strip()

    borrower_loans = [
        record
        for record in lent_books
        if record["borrower"]["name"].lower() == name.lower()
    ]

    if len(borrower_loans) >= 3:
        print("You have already borrowed 3 books. Return one before borrowing more.\n")
        return

    for book in library:
        if book["title"].lower() == title.lower():
            confirm = input(f"Lend '{title}' to {name}? (y/n): ").strip().lower()
            if confirm != "y":
                print("Lending cancelled.\n")
                return

            phone = input("Enter your phone number: ").strip()
            address = input("Enter your address: ").strip()

            if not all([name, phone, address]):
                print("All borrower details are required.\n")
                return

            due_date = datetime.now() + timedelta(days=14)

            lent_books.append(
                {
                    "book": book,
                    "borrower": {"name": name, "phone": phone, "address": address},
                    "due_date": due_date.strftime("%Y-%m-%d"),
                }
            )
            library.remove(book)

            with open("books_data.json", "w", encoding="utf-8") as f:
                json.dump(library, f, indent=4)

            with open("lent_books.json", "w", encoding="utf-8") as f:
                json.dump(lent_books, f, indent=4)

            print(f"Book '{title}' lent to {name} successfully.")
            print(f"Due date: {due_date.strftime('%Y-%m-%d')}\n")
            return

    print("Book not available.\n")


def return_book():
    title = input("Enter title of book to return: ").strip()
    for record in lent_books:
        if record["book"]["title"].lower() == title.lower():
            library.append(record["book"])

            due_date_str = record.get("due_date")
            if due_date_str:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                if datetime.now() > due_date:
                    late_days = (datetime.now() - due_date).days
                    fine = late_days * 10  # ₹10 per day
                    print(f"Returned late by {late_days} days. Fine = ₹{fine}.")

            lent_books.remove(record)

            with open("books_data.json", "w", encoding="utf-8") as f:
                json.dump(library, f, indent=4)

            with open("lent_books.json", "w", encoding="utf-8") as f:
                json.dump(lent_books, f, indent=4)

            print(f"Book '{title}' returned successfully.\n")
            return

    print("No record of this book being lent.\n")


def rate_book(title: str):
    # Search in library first
    for book in library + [record["book"] for record in lent_books]:
        if book["title"].lower() == title.lower():
            try:
                rating = int(input("Rate this book (1–5): "))
                if rating < 1 or rating > 5:
                    print("Rating must be between 1 and 5.")
                    return
            except ValueError:
                print("Invalid input. Enter a number between 1 and 5.")
                return

            review = input("Write a short review: ")
            book.setdefault("ratings", []).append({"rating": rating, "review": review})
            save_data()
            print("Thanks for rating!")
            return
    print("Book not found. Cannot rate.\n")


def view_book_ratings():
    title = input("Enter the book title to see ratings: ").strip()
    for book in library + [record["book"] for record in lent_books]:
        if book["title"].lower() == title.lower():
            ratings = book.get("ratings", [])
            if not ratings:
                print("No ratings for this book yet.\n")
                return
            print(f"Ratings for '{book['title']}':")
            for idx, r in enumerate(ratings, 1):
                print(f"{idx}. Rating: {r['rating']}/5 | Review: {r['review']}")
            return
    print("Book not found.\n")


def display_menu(role):
    while True:
        print("\n\n=== Library Menu ===\n")
        print("1. View all books\n")
        print("2. Search for a book\n")
        print("3. Lend a book\n")
        print("4. Return a book\n")

        if role == "Admin":
            print("5. Add a book\n")
            print("6. Remove a book\n")
            print("7. Update a book\n")
            print("8. View all lent books\n")
            print("9. Exit\n")
        else:
            print("5. View my lent books\n")
            print("6. Rate a book\n")
            print("7. View ratings\n")
            print("8. Exit\n")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_books()
        elif choice == "2":
            search_book()
        elif choice == "3":
            lend_book()
        elif choice == "4":
            return_book()

        if role == "Admin":
            if choice == "5":
                add_book()
            elif choice == "6":
                remove_book()
            elif choice == "7":
                update_book()
            elif choice == "8":
                view_all_lent_books()
            elif choice == "9":
                print("\nGoodbye!\n")
                break
            else:
                if choice not in [str(n) for n in range(1, 10)]:
                    print("\nInvalid choice.\n")
        else:  # User menu
            if choice == "5":
                view_user_lent_books()
            elif choice == "6":
                title = input("Enter the title of the book you want to rate: ").strip()
                rate_book(title)
            elif choice == "7":
                view_book_ratings()  
            elif choice == "8":
                print("\nGoodbye!\n")
                break
            else:
                if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                    print("\nInvalid choice.\n")

if __name__ == "__main__":
    user_role = None
    while not user_role:
        user_role = login() 
    display_menu(user_role)
