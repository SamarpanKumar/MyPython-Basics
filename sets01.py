Topic = "Python Sets"
print(Topic.center(50))

# Sets are unordered collection of Data items. They store multiple items in a single variable. Set items are seperated by commas and enclosed within curly brackets{}. sets are unchangeable, meaning you cannot change items of set once created. Sets do not contain duplicate items
#Set doesn't allow Duplicate items.
s = {2,4,2,6} 
print(s)

# sets Do not mantain order.
info = {"Carla", 19, False, 5.9, 19}
print(info)

# type of set
a = "Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is a set."
print(a)
harry = set()
print(type(harry))

info = {'Carla',19, False, 5.9}
for values in info:
    print(values) 