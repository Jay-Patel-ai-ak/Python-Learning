# How __repr__ works; How also used for debugging

class Student: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def __repr__(self): 
        return f"Student(name='{self.name}', age={self.age})"
    
students = [Student("Alice", 20), Student("Bob", 22), Student("Charlie", 19)]
print(students)  # This will use the __repr__ method for each Student object in the list


# How __str__ works; How also used for user-friendly display
class Employee: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def __str__(self): 
        return f"{self.name} is {self.age} years old."

Employees = [Employee("David", 30), Employee("Eve", 28), Employee("Frank", 35)]
print(Employees)