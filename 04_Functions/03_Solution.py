# Polymorphism in Functions - Same Function Name, Different Parameters.

def add(a, b, c):
    return a + b + c  
print(add(1, 2, 3))  # Output: 6

# multiply 

def multiply(p1, p2):
    return p1 * p2


print(multiply(8, 5))
print(multiply('a', 5))
print(multiply(5, 'a'))