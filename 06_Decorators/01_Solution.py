import time

# Timing function execution using Decorators. 
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer  # Decorator => timer is decorator function and example_function is decorated function.
def example_function(n):
    time.sleep(2)  # Simulate a time-consuming task 

example_function(5)
  
# What is Wrapper Function - A function that is defined inside a decorator function & used to wrap the original function..

