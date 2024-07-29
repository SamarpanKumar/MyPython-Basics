#Defining a Functions


print("<<<Make Calculator using Define class>>>")
Choice = input("Enter Choice +, -, %,*: ")
num1 = int(input("Enter your First Number: "))
num2 = int(input("Enter your second number: "))
def add(a,b):
    print("result: ", a+b )
def Substraction(a,b):
    print("result: ", a-b )
def Division(a,b):
    print("result: ", a%b )    
def Multiplication(a,b):
    print("result: ", a*b )

if Choice == "+":
    add(num1,num2)
elif Choice == "-":
    Substraction(num1,num2)
elif Choice == "%":
    Multiplication(num1,num2)        
elif Choice == "*":
    Multiplication(num1,num2)
           


