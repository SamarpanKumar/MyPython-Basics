Topic = "Define is a Function!"
print(Topic.center(50))

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First Number is Greater.")
    else:
        print("Second Number is Greater.")

def islesser(a,b):
    pass

a = 7
b = 9
calculateGmean(a,b)
isGreater(a,b)
#gmean1 = (a*b)/(a+b)
#print(gmean1)

c = 9
d = 10
calculateGmean(c,d)    
isGreater(c,d)
#gmean2 = (c*d)/(c+d)
#print(gmean2)

f = 10
g = 3
calculateGmean(f,g)
isGreater(f,g)