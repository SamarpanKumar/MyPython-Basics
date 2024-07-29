print("<<<Hello This is Python World>>>")
print("Data Types:")
int
str
complex
list
tuple
dict
set
bool
float

print("Variables") 
a = 45 #integer
b = 67.4 #Float
f = "Hello world" #String
print(type(a))
print(type(f))
c =4.5 #Float
print(type(c),type(a))

print("Arithmatic operations")
print(f"The sum of", a, "+", b, "+", c, "=" ,a + b + c )
c = a/b # will give float value
print(c)
c = a//b # wil give integer value
print(c)
c = 2**3
print(c)

c = 2%5
print(c)
a= 56
b =67
print("the sum of", a,"+",b,"=", (a+b))
print("f string")

a = int(input("Enter the Value:"))
b = int(input("Enter the number:"))
print(f"the sum of {a} + {b} = {a+b}")
# .format string
print("the sum of {0} + {1} = {2}".format(a,b,(a+b)))

z = 1 + 2
print(z)