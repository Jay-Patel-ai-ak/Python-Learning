import numpy as np

a = np.array([1, 2, 3])
b = np.array([3, 2, 1])

def addition(a, b):
   return np.add(a, b)

result = addition(a, b)
print(result)

## Here, addition is function 
## a & b are arguments
## np.add is the function that performs addition on the arrays a and b.
## return is used to send the result back to the caller.

a = np.array([1, 2, 3])
b = np.array([3, 2, 1])

addition = lambda x, y: np.add(x, y)

result = addition(a, b)
print(result)

## addition - Its a function 
## lambda - It is a keyword used to create anonymous functions in Python.
## x , y - parameters
## np.add - Its a function that performs addition on the arrays x and y.
## return is implicit in lambda functions.