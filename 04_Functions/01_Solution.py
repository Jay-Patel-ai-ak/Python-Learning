# Basic Function Syntax

def greet():
    print("Hello, World!")
    greet()
    
# Function with Parameters
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

# Function with Return Value
def add(a, b):    # a & b are parameters
    return a + b
result = add(5, 3)  # 5 & 3 are arguments
print(result)  # Output: 8

# Functions can return a result using the return keyword.
def avg(a, b, c):
    return (a + b + c) / 3  # Fnx to computer average of 3 nums
print(avg(1, 2, 3))


# Calculate & return square of a number
def square(number):
    return number ** 2


result = square(4)
print(16)