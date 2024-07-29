class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python.")
k = Employee("Kamal Kumar", 1)
k.showDetails()
s = Employee("Sameep Kumar" , 2)
s.showDetails()
m = Employee("Meena Kumari ", 3)
m.showDetails()
f = Programmer("Samarpan Kumar", 4)
f.showDetails()
f.showLanguage()
e = Employee("Rajat Dass ",  152 ) 
e.showDetails()   


#   Single  Inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child(Parent):
    def func2(self):
        print("This is in child class.")

object1 =Child()
object1.func1()
object1.func2()

#   Multiple Inheritance
class Mother:
    mothername = ""
    
    def mother(self):
        print(self.mothername)

class Father:
    fathername = ""

    def father(self):
        print(self.fathername)      

class Son(Mother, Father):
    def parents(self):
        print(f"Father name is: {self.fathername}")
        print("Mother name is: ", self.mothername)

s1 = Son()
s1.fathername = "Papa ji"
s1.mothername = "Mummy ji"
s1.parents()

# Multilevel Inheritance
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def __init__(self, Fathername, grandfathername):
        self. fathername =Fathername
        Grandfather.__init__(self, grandfathername)

class son(Father):
    def __init__(self, sonname,  fathername, grandfathername):
        self.sonname = sonname
        Father.__init(self, fathername, grandfathername)

    def  print_name(self):
        print('Grandfather name : ', self.grandfathername )
        print(f"Father name : {self.fathername}")
        print(f"Son name : {self.sonname}")
s1 = son('Kamal','Samarpan', 'Harbhaj')
print(s1.grandfathername)
s1.print_name()

#   Hierarchical Inheritance:
class Parent1():
    def func1(self):
        print("This function is in Parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

object1 = Child1()
object2 = Child2() 
object1.func1()
object1.func2() 
object1.func1()
object2.func3()


#   Hybrid Inheritance
class School:
    def func1(self):
        print("This function is in school.")

class Student1(School):
    def func2(self):
        print("This function is in student 1.")

class Student2(Student1):
     def func4(self):
         print("This function is in student 3.")       
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

object = Student3()
object.func1()
object.func2()

        












