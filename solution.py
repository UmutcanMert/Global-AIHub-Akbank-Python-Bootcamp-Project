class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        try:
            self.file = open(self.file_name, "a+")
        except Exception as e:
            print(f"Error: {e}")

    def __del__(self):
        """
            close the file
        """
        self.file.close()

    def list_books(self):
        """
            show all books in database
        """
        self.file.seek(0)  # Move the file pointer to the beginning
        lines = self.file.readlines()
        if not lines:
            print("No books available.")
        else:
            print("List of books:")
            for line in lines:
                book_info = line.strip().split(',')
                book_name, author, release_date, num_pages = book_info
                print(f"Book: {book_name}, Author: {author} release_date: {release_date} num_pages:{num_pages}")

    def add_book(self):
        """
            add the book to the file
        """
        book_name = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        release_date = input("Enter the first release year: ")
        num_pages = input("Enter the number of pages: ")

        book_info = f"{book_name},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        lines = self.file.readlines()
        self.file.seek(0)
        books_to_keep = []
        for line in lines:
            if title_to_remove not in line:
                books_to_keep.append(line)
        self.file.truncate(0)
        self.file.seek(0)
        self.file.writelines(books_to_keep)
        print(f"Book '{title_to_remove}' removed successfully.")


# Create an object named “lib” with “Library” class.
lib = Library()

# Create a menu to interact with the “lib” object.
while True:
    print("*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
