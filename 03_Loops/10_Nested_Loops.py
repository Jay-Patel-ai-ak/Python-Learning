# Nested Loops 
# A nested loop is a loop that is inside another loop. The inner loop will be executed one time for each iteration of the outer loop.

# Example 1: Nested For Loops
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"Outer loop iteration: {i}, Inner loop iteration: {j}")  
        
# Example 2: Nested While Loops
i = 1  # Outer loop variable
while i <= 3:  # Outer loop
    j = 1  # Inner loop variable
    while j <= 3:  # Inner loop
        print(f"Outer loop iteration: {i}, Inner loop iteration: {j}")
        j += 1  # Increment inner loop variable
    i += 1  # Increment outer loop variable