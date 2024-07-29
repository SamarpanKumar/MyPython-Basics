def abc(a,b):
    c = 67
    d = 45
    return a+b+c+d, a+b
x = abc(12,14) 
#x ,b = abc(12,14)
print(x)
#print(b),

#Keyword Argument
def fgh(name = "", age = ""):
    return name, age
x = fgh(name ="Samarpan", age = 22)
print(x)