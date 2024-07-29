Topic = "Breaking Loop!"
print(Topic.center(50))

for number in range(12):
    if(number == 10):
        break
    print("5 X", number + 1, "=", 5 *(number + 1))

print("Loop ko CHorh kr Nikal Gya.") 

for Numbers in range(15):
    if(Numbers == 5 ):
        break
    print("2 X", Numbers + 1,"=", 2 * (Numbers + 1))
print("Loop Break.")


for Num in range(13):
    if(Num == 10):
        break
    print("12 X", Num + 1,"=",12 * (Num + 1))
print("Loop Break!")

# This is Break Statement while using!
i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break

for i in range(1,101,1):
    print(i, end = " ")
    if(i == 50):
        break
    else:
        print("Mississippi")
print("Thank you")            