

import csv

# Step 1
def read_books(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)# Read the file as a dictionary
        books = []
        for row in reader:
            books.append(row)
        return books

# Step 2
def search_by_author(author_name, books):
    result = []# Initialize an empty list to store the search results
    for book in books:
        if book['author'] == author_name:
            result.append(book)
    return result


# Step 3
def search_by_isbn(isbn, books):
    for book in books:
        if book['ISBN'] == isbn:
            return {'title': book['title'], 'price': book['price']}
    return None



# Step 4
def search_by_price_range(min_price, max_price, books):
    result = []
    for book in books:
        price = float(book['price'])
        if price >= min_price and price <= max_price:
            result.append(book)
    return result



# Step 5
def main():
    filename = input("Enter CSV file name: ")
    books = read_books(filename)
    while True:
        print("\nSelect search option:")
        print("1. Search by author")
        print("2. Search by ISBN")
        print("3. Search by price range")
        print("4. Add new book")
        print("5. Quit")# Loop until the user chooses to quit
        choice = input("Enter choice (1-5): ")
        if choice == '1':
            author_name = input("Enter author name: ")
            result = search_by_author(author_name, books)
            if result:
                print("\nBooks written by", author_name)
                for book in result:
                    print(book['title'], book['ISBN'], book['price'])
            else:
                print("No books found.")
        elif choice == '2':
            isbn = input("Enter ISBN: ")
            result = search_by_isbn(isbn, books)
            if result:
                print("\nTitle:", result['title'])
                print("Price:", result['price'])
            else:
                print("Book not found.")
        elif choice == '3':
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            result = search_by_price_range(min_price, max_price, books)
            if result:
                print("\nBooks within price range:")
                for book in result:
                    print(book['title'], book['ISBN'], book['price'])
            else:
                print("No books found.")
        elif choice == '4':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            price = input("Enter price: ")
            new_book = {'title': title, 'author': author, 'ISBN': isbn, 'price': price}
            books.append(new_book)
            with open(filename, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=new_book.keys())
                writer.writerow(new_book)
            print("Book added successfully.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()