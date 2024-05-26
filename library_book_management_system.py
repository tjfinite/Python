#Books list
books = [
    {'title': 'Book1', 'author': 'Author1', 'year': 1999, 'qty': 4},
    {'title': 'Book2', 'author': 'Author2', 'year': 2000, 'qty': 0},
    {'title': 'Book3', 'author': 'Author3', 'year': 2001, 'qty': 0},
    {'title': 'Book4', 'author': 'Author4', 'year': 2002, 'qty': 3}
]

#Library information
library_info = ("LibraryName", "LibraryAddress")

#Books availability
book_availability = {
    "Book1": True,
    "Book2": False,
    "Book3": False,
    "Book4": True
}

#Print the books list
print("Books:")
for book in books:
    print(book)

#Print the library information
print("\nLibrary information:")
print (library_info)

#Print the books availability
print("\nBooks availability:")
print(book_availability)