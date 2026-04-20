# Loops in Python 
# For Loop
for i in range(5):
    print(i)
    
# While Loop
count = 0
while count < 5:
    print(count)
    count += 1
    
# Break and Continue
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(i)
