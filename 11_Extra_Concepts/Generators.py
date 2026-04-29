def gen_value():
    yield 1
    yield 2
    yield 3
    
for value in gen_value():
    print(value)
    
    

def demo():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")
    
g = demo()
print(next(g))  # Start and 1
print(next(g))  # Middle and 2
# print(next(g))  # End and StopIteration