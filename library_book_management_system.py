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
book_availability = {book['title']: book['qty'] > 0 for book in books}

#Print the library information
print ("Library name:",library_info[0])
print ("Library address:",library_info[1])

#Print the books names
print("\nBooks:")
for book in books:
    print(book['title'])

#Print the author names
print("\nAuthors:")
for book in books:
    print(book['author'])

#Print the books availability
print("\nBooks availability:")
for title, available in book_availability.items():
    status = "Yes" if available else "No"
    print("{}: {}".format(title, status))

#Print the books year
print("\nBooks year:")
for book in books:
    print("{}: {}".format(book['title'], book['year']))