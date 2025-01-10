# 1) Write a program to calculate the area and perimeter of different geometric shapes(square, rectangle, parallelogram, triangle, circle) based on user input. The program should include error handling for invalid inputs.

# For square :

def areaOfSquare():
    try : 
        side = int(input("Enter the side length of the square : "))
        if side <= 0 : print("Invalid input! Please enter a valid number.")
        area = side * side
        print("Area of the square is : ", area)
    except :
        print("Invalid input! Please enter a valid number.")

areaOfSquare()

# For rectangle :

def areaOfRectangle():
    try :
        length = int(input("Enter the length of the rectangle : "))
        bredth = int(input("Enter the bredth of the rectangle : "))
        if length <= 0 or bredth <= 0 : 
            print("Invalid input! Please enter a valid number.")
        area = length * bredth
        print("Area of the given rectangle is : ", area)
    except :
        print("Invalid input! Please enter a valid number.")

areaOfRectangle()

# 2) Develop a program to take user input for multiple numbers, store them in a list, and compute basic statistical metrics like mean, median, mode, and standard deviation.

def calculateMean(arr,n):
    Mean = 0.0
    mean = 0.0;

    for i in range(5):
        mean += arr[i]

    mean /= n
    return mean

def calculateMedian(arr,n):
    Median = 0.0

def calculateMode(arr,n):
    Mode = 0.0

def calculateStandardDeviation(arr,n):
    StandardDeviation = 0.0

def arrayOperations():
    arr = [];

    n = 5;

    for i in range(n):
        num = int(input("Enter the value : "))
        arr.append(num)

    print(calculateMean(arr,n))
    print(calculateMedian(arr,n))
    print(calculateMode(arr,n))
    print(calculateStandardDeviation(arr,n))


arrayOperations()

# 3) Create a real-world problem-solving program, such as calculating monthly loan payments based on principal, rate of interest, and tenure.