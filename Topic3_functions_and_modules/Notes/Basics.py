def multiply(*args):
    product = 1 
    try:
        for i in args:
            if not isinstance(i, (int)):
                raise ValueError(f"Non-numeric input detected: {i}")
            product *= i
        return product
    except ValueError as e:
        return str(e)
    
print(multiply(1,2,3,4,5))