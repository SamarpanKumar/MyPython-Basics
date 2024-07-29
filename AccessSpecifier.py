Topic = "Access Specifier"
print(Topic.center(50))

A1 = 'Public Access Specifier'
print(A1.center(50))

class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age
# public variable
        self.name = name
# public variable

obj = Student(21, "Samarpan")
obj.age = 23    #Rename
print(obj.name) 
print(obj.age)


A2 = "Private Access Modifier"
print(A2.center(50))

class Student:
    def __init__(self, age, name):
        self.__age = age    # An Indicataion of private variable

        def __funName(self): # An Indication of private Function
            self.y = 34
            print(self.y)
class Subject(Student):
    pass

obj = Student(23, "Harry")
obj1 = Subject

#calling by object of class Student
print(obj.__age)
print(obj.__funName())

# calling by object of class subject
print(obj1.__age)
print(obj1.__funName())



A3 = 'Name Mangling'
print(A3.center(50))

class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute)
#Output: I am a nonmangled attribute
print(my_object.__mangled_attribute)
# Throws an AttributeError
print(my_object._MyClass__mangled_attribute)
# Output: I am a mangled attribute.

A4 = 'Protected Access Modifier'
print(A4.center(50))

class Student:
    def __init__(self):
        self._name = "Samar"
    def _funName(self): # protected method

       return "SamarpanKumar"
class Subject(Student):
    #inherited class     
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student Class
print(obj._name)
print(obj1._funName())

# calling bby object of Subject class
print(obj1._name)
print(obj1._funName())