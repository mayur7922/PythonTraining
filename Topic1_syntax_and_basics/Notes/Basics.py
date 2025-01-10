# ------------- Recursive funtion fun
# def fun(n):
#     if n == 0 : return
#     print(n)
#     fun(n - 1)

# fun(5)



# ------------- default arguments
# def greet(name="Guest"):
#     print(f"Hello, {name}!")

# greet()        # Output: Hello, Guest!
# greet("Alice") # Output: Hello, Alice!

# ------------- positional and keyword arguments
# def fun(Name, Age):
#     print("His name is",Name,"and his age is",Age)

# fun("Alice",22)
# fun(Age = 22, Name = "Alice")

# ------------- * args

def fun(*args):
    print(sum(args))

fun(1,2,3)

# ------------- * kwargs