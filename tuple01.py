tup = (1,2,76,342,32,"green", True)
#tup[0] = 90 # Tupple Cannot be Changed!.
print(tup)
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
#print(tupe[34])

if 342 in tup:
    print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)

# For Practice this is another example:
tup1 = (62,84,445,9,449,"Red",True, 90,100)
print(type(tup1), tup1)
#tup1[0] = 90
print(len(tup1)) #For counting The tuple within!
print(tup1[0])
print(tup1[-1])
print(tup1[2])

if 445 in tup1:
    print("Yes 445 is present in tup1")
else:
    print("445 is not present in the Tuple1")

tupe3 = tup1[1:4]
print(tupe3)    