# Debugging Function calls with Decorators.

def debug (func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(repr(arg) for arg in args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        print(f"Calling {func.__name__} with args: {args_str}, kwargs {kwargs_str}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("Hello, World!")

@debug
def greet (name, greeting="Hello"):
    print(f"{greeting}, {name}!")
    
hello()
greet("Armakuni", greeting = "Hola")