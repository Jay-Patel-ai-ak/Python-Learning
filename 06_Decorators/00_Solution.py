# Learning Decorators in Python 

def my_decorator(string):
    def wrapper1(func):
        
        def wrapper():
            print(string)
            print("Artificial Intelligence is the future of technology.")
            func()
            print("All AI is ML but not all ML is AI.")
        return wrapper
    return wrapper1

@my_decorator("Hello AI ML")
def greet():
    print("Hello AI ML")
greet()