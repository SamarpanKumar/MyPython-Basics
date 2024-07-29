Topic = "Exception Handling!"
print(Topic.center(50))

a = input("Enter your Number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print("Sorry some Error Occured!")
except :
    print("Invalid Input!")
print("Some imp lines of Code")    
print("End of the programe")


try:
    num = int(input("Enter an Integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an Integer.")

except IndexError:
    print("Index Error")        