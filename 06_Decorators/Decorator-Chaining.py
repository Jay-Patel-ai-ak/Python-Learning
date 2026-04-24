# Decorator Chaining - Multiple wrappers on top of each other. 
# Execute from top to bottom, but return from bottom to top.

def shirt(func):
    def wrapper():
        print ("I'm wearing Red shirt")
        func()
    return wrapper

def pant (func):
    def wrapper():
        print ("I'm wearing Black pant")
        func()
    return wrapper

def sneakers(func):
    def wrapper():
        print ("I'm wearing Nike AIR MAX sneakers")
        func()
    return wrapper

@sneakers  # prints first, but executes last
@pant      # prints second, but executes second
@shirt     # prints third, but executes first
def dress():
    print ("I'm ready to go out")
dress()

