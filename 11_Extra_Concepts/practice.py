x = 100 # Global variable

def f1():
    x = 200 # Local variable in f1
    def f2(): 
        print(x)
    f2()
f1()

# Why 200 is printed instead of 100? -- Because of the concept of scope in Python.