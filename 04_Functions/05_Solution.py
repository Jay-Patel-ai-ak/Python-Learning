# # Default Parameter Value : Greet the person with the default message "Hello"

def greet():
    print("Hello, World!")
    greet()
    
# Function with Parameters
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")