Topic = 'dir(), __dict__, and help() methods in Python'
print(Topic.center(50))

x = [1, 2, 3]
print(dir(x)) #Directory Methods
print(x.__add__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__) #In dictionary format.

print(help(Person))

