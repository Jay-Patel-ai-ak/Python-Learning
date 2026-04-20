# Recursive Function 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5)) 

# Exit strategy: The base case (n == 0) serves as the exit strategy for the recursion.