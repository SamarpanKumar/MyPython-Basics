l =[11,45,1,2,4,6,1,1]
print(l)
print(l.append(7))
print(l.sort(reverse=True))
print(l.reverse())
print(l.index(1))
print(l.count(1))
m = l.copy()
m[0] = 0
print(l.insert(1, 899))
m = [900,1000,1100]
k = l+m
print(k)
print(l.extend(m))
print(l)

#This Method Sorts the List in ascending Order. The Original list is updated
colors = ["violet","indigo","blue","Green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

# Reverse Method In List
colors = ["Violet","Indigo","blue","Green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)

# Index()
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))

#Count()
colors = ["violet","green","Indigo","blue","green"]
print(colors.count("green"))
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(1))

#copy()
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)