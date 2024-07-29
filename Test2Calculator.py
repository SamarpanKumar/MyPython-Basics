#with while Loop:
c = True
while c:
    a = int(input("Enter you first Number: "))
    b = int(input("Enter you Second Number: "))

    choice =int(input("Enter 1st Number For Addition\nEnter 2nd Number for substraction\nEnter 3rd Number of Multiplication\nEnter 4th Number for Division: "))
    if choice == 1:
       print(a, "+", b,"=", a+b)
    elif choice == 2:
       print(a,"-",b,"=", a-b) 
    elif choice == 3:
       print(a, "*", b,"=", a*b)
    elif choice == 4:
       print(a,"%",b,"=", a%b) 
    s= int(input("Do you want to use again or not press 1 or 0: "))
    if s==1:
         c =True
    else:
         c = False  

