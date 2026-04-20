# Multiplication Table Printer
number = 3

for i in range(1, 11):
    if i == 5:   # If i is 5, skip the multiplication and move to the next iteration
        continue
    print(number, 'x', i, '=', number * i)
