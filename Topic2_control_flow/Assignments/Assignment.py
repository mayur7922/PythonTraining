
# # Write a program to classify numbers as prime, composite, or neither (for negative or zero values). Ensure it handles invalid inputs gracefully.

def isPrime(n):

    try:
        if n <= 1 : return False

        if (n == 2 or n == 3) : return True
        if(n % 2 == 0 or n % 3 == 0) : return False;

        for i in range(5,int(n**0.5) + 1,6) :
            if n % i == 0 :
                return False
            elif n % (i + 2) == 0 :
                return False

        return True;
    except:
        print("Error: Invalid input! Please enter a valid number.")

def solve():

    try:
        num = int(input("Enter the number : "))

        if num <= 1: 
            print("Neither a prime nor a composite")
        elif isPrime(num) == True:
            print("This is a prime number")
        else :
            print("This is a composite number")
    except:
        print("Error: Invalid input! Please enter a valid number.")

solve()

# Create a program to implement a simple text-based menu system for a library that allows users to add, remove, search, and list books. Use loops and conditional statements effectively.

def libraryManagement():
    books = []

    while 1 :
        print("Enter 1 to add a book")
        print("Enter 2 to remove a book")
        print("Enter 3 to search a book")
        print("Enter 4 to list all the books")
        print("Enter 5 to exit")

        opt = int(input("Enter your choice : "))

        if opt == 1 :
            book = str(input("Enter the name of the book : "))
            books.append(book)
            print("Book has been added successfully")
        elif opt == 2 :
            size = len(books)
            if size == 0 :
                print("No book is available in the library")
            book = str(input("Enter the name of the book : "))
            for i in range(size):
                if(books[i] == book):
                    books.pop(i)
                    print("Book has been deleted successfully")
                    break;
        elif opt == 3 :
            isAvailable = False
            size = len(books)
            if size == 0 :
                print("No book is available in the library")
            book = str(input("Enter the name of the book : "))
            for i in range(size):
                if(books[i] == book):
                    isAvailable = True
                    break;
            if isAvailable == True:
                print("Book is available")
            else: print("Book is not available")
        elif opt == 4 :
            print("Following are the books available in the library : ")
            print(books)
        else :
            break


libraryManagement()

# Write a robust ATM transaction simulator that includes options for checking balances, depositing, withdrawing money, and exiting. Handle invalid inputs and edge cases.