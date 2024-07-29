Topic = 'Constructors in Python'
print(Topic.center(50))

# Default Constructor in python.
Topic1 = "Default Constructor"
print(Topic1.center(50))
class Details:
    def __init__(self):
        print("animal Crab belongs to Crustaceans group")
obj = Details()


# Parameterised Constructor in Python.
Topic2 = "Parameterised Constructor"
print(Topic2.center(50))
class Person:

    def __init__(self, name, occ):
        print("Hey I am a Person")
        self.name = name
        self.occ = occ

    def info (self):
        print(f"{self.name} is a {self.occ}")


obj = Person("Harry", "Developer") 
obj1 = Person("Divya", "HR")
obj.info()
obj1.info()
# print(a.name)
#obj.name = "Divya"
#obj.occ = "HR"
#obj.info()


#Another Example of Parameterized Constructor in Python.
Topic3 = 'Another Parameterized Constructor example:'
print(Topic3.center(50))
class Details1:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

    def info(self):
            print(f"{self.animal} belongs to the {self.group}")

obj5 = Details1("Crab","Crustaceans")            
obj5.info()




