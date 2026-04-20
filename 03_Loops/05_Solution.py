# First Non Repeated Character in a String

input_str = "swiss"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break
