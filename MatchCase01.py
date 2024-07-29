x = int(input("Enter the Value of x: "))
# x is the variable to match
match x:
    #if x is 0
    case 0:
        print("X is zero")
    case 3:
        print("X is Three")
    case 4:
        print("x is Four")

    #case with if-condition
    case _ if x!= 90:
        print(x,"x is not 90")
    case _ if x!= 80:
        print("x is not 80")
    case _ if x!= 100:
        print("x is not 100")
    case _:
        print(x)
