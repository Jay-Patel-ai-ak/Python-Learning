# Create a function to compute factorial of a number n .

# Factorial of N
n = int(input("enter n: "))

fact = 1
for i in range (1, n+1):
    fact *= i
print("factorial = ", fact)

