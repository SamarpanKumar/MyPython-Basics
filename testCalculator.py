#test make a calculator

#This is a Normal way!
a = int(input("Enter your First number:"))
b = int(input("Enter your second number:"))

print("The sum of", a, "-",b , "=", a - b)
print("The sum of", a, "*",b , "=", a * b)
print("The sum of", a, "/",b , "=", a / b)
print("The sum of", a, "//",b , "=", a // b)
print("The sum of", a, "%",b , "=", a % b)
print("The sum of", a, "**",b , "=", a ** b)


c = int(input("Enter your First number:"))
d = int(input("Enter your second number:"))
#\n for next line
choice = int(input("press 1 for add\npress 2 for multilply\npress 3 for Divide\npress 4 for substract:"))
if choice==1:
     print(c+d)
     print("The sum of", c, "+",d , "=", c + d)
elif choice ==2:
     print(c*d)
     print("The sum of", c, "*",d , "=", c * d)
elif choice ==3:
     print(c%d) 
     print("The sum of", c, "%",d , "=", c % d)
elif choice==4:
     print(c-d)
     print("The sum of", c, "-",d , "=", c - d)

else:
     print("please Choose the Above options!!!")