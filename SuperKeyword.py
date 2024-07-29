class ParentClass:
    def parent_method(self):
        print("This is the parent method. ")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Harry")
        super().parent_method()
    def child_method(self):
        print("This is the child method.")


Child_object = ChildClass()
Child_object.parent_method()
Child_object.child_method()

# 2nd Super Example.
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id,lang):   
        super().__init__(name, id)
        self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry","2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)


# 3rd Super Example.
class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")

class ParentClass2:
    def parent_method(self):
        print("This is the child method.")
        
class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()        

child_object = ChildClass()
child_object.child_method()                


