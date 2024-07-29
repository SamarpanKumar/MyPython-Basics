Topic = "Raising Custom Errors!"
print(Topic.center(50))

a = int(input("Enter any value between 5 and 9: "))

if(a < 5 or a > 9):
    raise ValueError("Value should be between 5 and 9")

salary = int(input("Enter Salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid Salary")




a = input("Enter any value between 5 and 9.W Write 'quit to quit.")
def myfunc():
    if a == "quit":
        print("program Quitted")
    else:
        if(int(a)<5 or int(a)>9):
            raise ValueError("Value Should be between 5 and 9")
        else:
            print(a)
        myfunc()
