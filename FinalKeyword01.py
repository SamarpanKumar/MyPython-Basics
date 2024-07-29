Topic = "Final Clause"
print(Topic.center(50))

def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the Index!: "))
        print(l[i])
        return 1
    except:
        print("some error  Occurred")
        return 0
    
    finally:
        print("I am always Executed")

x = func1()
print(x)

try:
    num = int(input("Enter an Integer!: "))
except ValueError:
    print("Number entered is not an integer") 
else:
    print("Integer Accepted") 
finally:
    print("This block is always executed.")
                  