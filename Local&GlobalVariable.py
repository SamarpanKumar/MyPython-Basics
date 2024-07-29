x = 50
y = "Hello, World!"

x = 10 # Global variable
def myfunction():
    global x
    x = 5 #this will change the value of the global variablex
    y = 7 #local variable


print(myfunction())
print(x) #prints 5 
# prints(y) # this will cause an error because y is a local variable and is not accessible outside of the function.



