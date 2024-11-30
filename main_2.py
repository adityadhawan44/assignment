class Library:
    def __init__(self):
        self.books = []
        self.book_details = {}
        self.authors = set()

    # Method to add a book
    def add_book(self, title, author, year):
        if title not in self.books:
            # Add title to the books list
            self.books.append(title)
            # Add book details to the dictionary
            self.book_details[title] = {"author": author, "year": year}
            # Add author to the set of authors
            self.authors.add(author)
            print(f'Book "{title}" added to the library.')
        else:
            print(f'The book "{title}" is already in the library.')

    # Method to remove a book by title
    def remove_book(self, title):
        if title in self.books:
            # Get the author of the book before removing it
            author_to_remove = self.book_details[title]["author"]
            # Remove the book from the list and the dictionary
            self.books.remove(title)
            del self.book_details[title]
            
            # Remove author from the authors set only if they have no other books
            if not any(book for book in self.books if self.book_details.get(book, {}).get("author") == author_to_remove):
                self.authors.remove(author_to_remove)
                
            print(f'Book "{title}" removed from the library.')
        else:
            print(f'The book "{title}" is not found in the library.')

    # Method to list all books
    def list_books(self):
        if self.books:
            print("List of books in the library:")
            for title in self.books:
                details = self.book_details[title]
                print(f'Title: {title}, Author: {details["author"]}, Year: {details["year"]}')
        else:
            print("No books in the library.")

    # Method to list all unique authors
    def list_authors(self):
        if self.authors:
            print("List of authors in the library:")
            for author in self.authors:
                print(f'Author: {author}')
        else:
            print("No authors in the library.")

# Main program to demonstrate the use of data structures
def main():
    # Creating a library object
    library = Library()

    # Adding books to the library
    library.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
    library.add_book("1984", "George Orwell", 1949)
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    
    # Listing books and authors
    library.list_books()
    library.list_authors()

    # Removing a book from the library
    library.remove_book("1984")

    # Listing books and authors after removal
    library.list_books()
    library.list_authors()

if __name__ == "__main__":
    main()
