username = "Armakuni"

def scope_test():
    username = "Hello Armakuni"
    print(username)
    
print(username)  # Output: Armakuni
scope_test()     # Output: Hello Armakuni


# Example 
x = 100      # Global variable
def fun(y):
    z = x + y
    return z
result = fun(1)
print(result)  # Output: 101

def fun1():
    global x  # Its bad practice to use global keyword inside function.
    x = 200
fun1()
print(x)  # Output: 200



a = 1 # Global Scope
def out():
    a = 2 # Enclosing Scope
    
    def inn():
        a = 3 # Local Scope
        print(a) 
        
    inn()
out()

x = "I am Global"  # G: Global Scope

def outer_function():
    x = "I am Enclosing"  # E: Enclosing Scope

outer_function()
print(x)  