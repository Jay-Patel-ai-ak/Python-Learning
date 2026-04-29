# Magic / Dunder Method in Python

str1 = "Hello"
str2 = "World"

new_str = str1 + str2
print(new_str)

new_str = str1.__add__(str2) # Explicit way to call the add method of str class
print(new_str)

new_str = len(str1)
print(new_str)

new_str = str1.__len__() # Explicit way to call the len method of str class
print(new_str)


def func ():
    pass

print(type(func))
