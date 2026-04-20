# Generate sequence of numbers , typically in a loop , using range() function.

# The function has 3 parameters:
# 1. start (default=0) - the number to start from
# 2. stop - the number to stop before (not included)
# 3. step (default=1) - how much to increase by each time 

# single argument - start
for i in range(5):
    print(i)
# output: 0, 1, 2, 3, 4


# 2 arguments - start, stop
for i in range(1, 6):
    print(i)
# output: 1, 2, 3, 4 , 5


# 3 arguments - start, stop, step
for i in range(1, 10, 2):
    print(i)
# output: 1, 3, 5, 7, 9