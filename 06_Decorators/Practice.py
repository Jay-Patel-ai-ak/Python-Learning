# without passing args and kwargs to wrapper function.
def debug (func):
    def wrapper():
        return func()
    return wrapper

@debug
def hello():
    print("Hello, World!")
    
hello()