def decorator(func): #decorator function takes a function as an argument
    def wrapper(x):
        return func( x * 2)
    return wrapper

@decorator
def my_function(x): # This function will be wrapped by the decorator
    return x + 1    
result = my_function(5)
print(result)  # Output: 11
