Topic= "Function Arguments!"
print(Topic.center(50))

def average(a = 9,b =1 ):
    print("The Average is ", (a+b)/2)

average(4, 5)    
#average(1,5)
#average(b = 9)
#average(a = 12)
#average(b = 9, a = 22)

def average1 (c,d,e=1):
    print("The Average1 is ",(c+d+e) / 2)

average(9,5)

def average(*numbers):
    #print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
        #print("Average is: ", sum/ len(numbers))
        #return 7
        return sum / len(numbers)

c = average(5,6,7,1)
print(c)

#average(5,6)

def name(fname, mname="John",lname="Whatson"):
    print("Hello,",fname,mname,lname)
name("Amy", "Agarwal","Jain")


#def name(**name):
    #print(type(name))
    #print("Hello,", name["fname"],
    #name["mname"], name["lname"])

    #name(mname="Buchanan",lname = "Barnes", 
    #fname = "James")
