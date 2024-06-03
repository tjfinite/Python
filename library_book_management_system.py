#Books list (list of dictionaries)
books = [
    {'title': 'Book1', 'author': 'Author1', 'year': 1999, 'qty': 4},
    {'title': 'Book2', 'author': 'Author2', 'year': 2000, 'qty': 0},
    {'title': 'Book3', 'author': 'Author3', 'year': 2001, 'qty': 0},
    {'title': 'Book4', 'author': 'Author4', 'year': 2002, 'qty': 3},
    {'title': 'Book5', 'author': 'Author4', 'year': 2002, 'qty': 34}
]

#Library information (tuple)
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

#Search for a book by title
def search_book_by_title(title):
    for book in books:
        if book['title'] == title:
            return book
    return None
search_title = input("Enter the book title to search: ")
book = search_book_by_title(search_title)
if book:
    print("\nBook found:")
    print("Title:", book['title'])
    print("Author:", book['author'])
    print("Year:", book['year'])
    print("Quantity:", book['qty'])
else:
    print("\nBook not found.")

#Search for a book by author
def search_book_by_author(author):
    for book in books:
        if book['author'] == author:
            return book
    return None
search_author = input("Enter the book author to search: ")
book = search_book_by_author(search_author)
if book:
    print("\nBook found:")
    print("Title:", book['title'])
    print("Author:", book['author'])
    print("Year:", book['year'])
    print("Quantity:", book['qty'])
else:
    print("\nBook not found.")

#Search for a book by year
def search_book_by_year(year):
    for book in books:
        if book['year'] == year:
            return book
    return None
search_year = int(input("Enter the book year to search: "))
book = search_book_by_year(search_year)
if book:
    print("\nBook found:")
    print("Title:", book['title'])
    print("Author:", book['author'])
    print("Year:", book['year'])
    print("Quantity:", book['qty'])
else:
    print("\nBook not found.")
