Topic = " For LOOPS"
print(Topic.center(50))

name = "Abhishek"
for i in name:
    print(i)
    if (i == "b"):
        print("This is Something Special")


Colors = ["Red","Green","Blue","Yellow"]
for color in Colors:
    print(color) 
    for i in color:
        print(i)   


for K in range(5):
    print(K+1)

for K in range(6):
    print(K+1) 

#for s in range(100):
  #  print(s+1)       

#for Numbers in range(1,2001):
    #print(Numbers)

for Numbers in range(1,12,3):
    print(Numbers)
