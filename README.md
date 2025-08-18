# Library Management System (Python)

A console-based Library Management System built in Python. This system allows users to manage books, lend and return books, and maintain borrower records. Admins have additional privileges for managing the library.

---

## Features

### User Authentication
- Login as `Admin` or `User` with separate credentials.
- Basic authentication to restrict access to administrative features.

### Book Management (Admin Only)
- Add new books with title, author, genre, and year of publication.
- Update book information.
- Remove books from the library.
- View all books in the library.

### Lending System
- Users can borrow books (up to 3 at a time).
- Record borrower details: name, phone number, and address.
- Automatic calculation of **due date** for borrowed books.
- Return books and check for **late fines** (`₹10 per day`).

### Viewing Borrowed Books
- Admin can view all lent books along with borrower details.
- Users can view their own borrowed books.

### Search Functionality
- Search books by title, author, genre, or year.

### Book Ratings
- Users can rate books (1–5) and leave short reviews.
- Ratings and reviews are stored in the system.

---

## File Structure

```
Library\_Management\_System\_Demo/
│
├── books\_data.json        # Stores all book details
├── lent\_books.json        # Stores lent books and borrower info
├── Library\_Management\_System\_Try.py  # Main Python script
└── README.md
````

---

## How to Run

1. Clone the repository:

```
git clone https://github.com/Mohit26-BM/Library_Management_System_Demo.git
cd Library_Management_System_Demo
````

2. Ensure you have Python installed (Python 3.8+ recommended).

3. Run the main script:

```
python Library_Management_System_Try.py
```

4. Follow the on-screen menu to interact with the system.

---

## Notes

* The system currently works via the console (command line interface).
* Data is stored in JSON files (`books_data.json` and `lent_books.json`) for simplicity.
* Late fines are automatically calculated when returning overdue books.
* Each user can borrow a maximum of 3 books at a time.
* Ratings and reviews are saved per book but cannot be edited or deleted yet.

---

## Future Enhancements

* Add a GUI using Tkinter for easier interaction.
* Implement editing and deleting of book reviews.
* Support multiple copies of a book.
* Improve search functionality with partial matches and filtering.

```
