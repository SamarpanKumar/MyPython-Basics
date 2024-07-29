Topic = "Python Class and objects"
print(Topic.center(50))

class Person:
    name  = "Samarpan"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

obj1 = Person()
obj2 = Person()
obj3 = Person() # Default

obj1.name = "Shubham"
obj1.occupation = "Accountant"

obj2.name = 'Nikita'
obj2.occupation = "HR"

#print(a.name, a.occupation)
obj1.info()
obj2.info()
obj3.info() # Default



class profession:
    name = 'Sid'
    work = 'Khurrana Industries'
    def info(self):
        print(f"{self.name} is CEO at {self.work}")

obj2 = profession()
obj3 = profession()     
obj3.name = "Manu"
obj3.info() 
obj2.info()  


class Details:
    name = "Roshan"
    age  = 20
    

obj1 = Details()
print(obj1.name)
print(obj1.age)


