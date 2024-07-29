txt = "The best things in life are free!"
print("free" in txt)

txt1 = "The best things in life are free!"
print("expensive" not in txt1)

txt2 = "The best thing in life are free!"
if"expensive" not in txt2:
    print("No, 'expensive' is not present.")

#Slicing
b = "Hello, World!"
print(b[2:5])

c = "Hello world!"
print(c[:5]) # Slicing from the Start

d = "Hello world!"
print(d[2:]) # Slice to the end.

e = "Hello world!"
print(e[-5:-2])

#UPPER CASE
a = "Hello World!"
print(a.upper())

b = "HOW'S YOU DOIN!"
print(b.lower())

c = "   Hello, World!"
print(c.strip()) # removes White space.

d = "Hello, World!"
print(d.replace("H","J"))

e = "Hello, World!"
print(e.split(","))

# Format
age = 36
txt = "My name is john, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))

#Escape Characters
txt = "we are the so-called \"Vikings\" from the north."
print(txt)

#Boolean values
#a = int(input("Enter your 1st Number: "))
#b = int(input("Enter your 2nd NUmber: "))
#print(a>b)
print(10> 9)
print(10 == 9)
print(10 < 9)

#Evaluate Values and Variable.
print(bool("Hello"))
print(bool(15))




# Function as return or Boolean.
def myFunction():
    return True

print(myFunction())

def myFunction() :
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")    

#Check if an object is an integer or not:
x = 200
print(isinstance(x,int))  

# List
thisList = ["apple","banana","Cherry"]
print(thisList)

thislist1 = ["apple","banana","Cherry"]
print(len(thislist1))

# List Items - Data types
list1 = ["apple","banana","Cherry"]
list2 = [1,5,7,9,3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

# A List with Strings, integers and boolean values:
list2 = ["abc", 34, True, 40,"male"]
print(list2)

# type()
mylist = ["apple","banana","cherry"]
print(type(mylist))

#List() Constructor
thislist2 = list(("apple","banana","cherry"))
print(thislist2)

#Access items
thislist3 = ["apple","banana","cherry"]
print(thislist3[1])
print(thislist3[-1])

#range of indexes
thislist4 = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist4[2:5])
print(thislist4[:4])
print(thislist4[2:])
print(thislist4[-4:-1])

#Check if item Exists
thislist5 = ["apple","banana","cherry"]
if "apple" in thislist5:
    print("YES, 'apple' is in the fruits list")

#Change the second item:
thislist6 = ["apple","banana","cherry"]
thislist6[1] = "blackcurrent"
print(thislist6)

#Change the Range of Item Values
thislist7 = ["apple","banana","cherry","orange","kiwi","mango"]
thislist7[1:3] = ["blackcurrent","watermelon"]
print(thislist7)

# Change the second value by replacing it with two new values:
thislist8 = ["apple","banana","cherry"]
thislist8[1:2] = ["blackCurrent", "watermelon"]
print(thislist8)

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist9 = ["apple","banana","cherry"]
thislist9[1:3] = ["watermelon"]
print(thislist9)

# Append Items
thislist10 = ["apple","banana","cherry"]
thislist10.append("orange")
print(thislist10)

#Insert an item as the second position.
thislist = ["apple","banana","cherry"]
thislist.insert(1,"orange")
print(thislist)

# Extend List
thislist = ["apple","banana","cherry"]
tropical = ["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)

#Add any iterable
#Add elements of a tuple to a list:
thislist = ["apple","banana","cherry"]
thistuple = ("kiwi","orange")
thislist.extend(thistuple)
print(thislist)

#Remove from the list:
thislist = ["apple","banana","cherry","banana"]
thislist.remove("banana")
print(thislist)

# Remove Specified index
thislist =["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

# Remove the last item:
thislist = ["apple","banana","cherry"]
thislist.pop() #This will remove the last item.
print(thislist)

thislist = ["apple","banana","cherry"]
del thislist[0] #removing the  first item.
print(thislist)

#Deleting the Item
thislist = ["apple","banana","cherry"]
del thislist

# Clearing the list Content:
thislist =["apple","banana","cherry"]
thislist.clear()
print(thislist)

# LOOP LISTS
thislist = ["apple","banana","cherry"]
for x in thislist:
    print(x)
    
# Loop through index Numbers
thislist = ["apple","banana","cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Using the While Loop with list
#thislist = ["apple","banana","cherry"]
#i = 0
#while i < len(thislist):  
#    print(thislist[i]) 

#Looping Using List Comprehension
thislist = ["apple","banana","cherry"] 
[print(x) for x in thislist]
                 
# without List Comprehension
fruits = ["apple","banana","cherry","kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)        

#With list Comprehension
fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Only accept itmes that are not apple
newlist = [x for x in fruits if x != "apple"]

#You can use the range() function to create an iterable:
newlist = [x for xn in range(10)]

#accept only numbers lower than 5
newlist = [ x for x in range(10) if x < 5]

#Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

#Set all values in the new list 'hello'
newlist = ['hello' for x in fruits]

# Return "orange " instead of "banana":
newlist = [x if x !=  "banana" else "orange" for x in fruits]

#Sort list Alphanumerically
thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort()
print(thislist)

# Sort the List numerically:
thislist1 = [100,50,65,82,23]
thislist1.sort()
print(thislist1)

#Sort the list descending:
thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100,50,65,82,23]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort function
def myfunc(n):
    return abs(n - 23)

thislist = [100,50,65,82,23]
thislist.sort(key = myfunc)
print(thislist)

#Case Insensitive Sort
thislist = ["banana","orange","kiwi","cherry"]
thislist.sort()
print(thislist)

# Lower Case in List
thislist = ["banana","Orange","Kiwi","cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse order
thislist = ["banana","Orange","Kiwi","cherry"]
thislist.reverse()
print(thislist)
#Python  Copy List

thislist = ["apple","banana","cherry"]
mylist = thislist.copy()
print(mylist)

#Join Two Lists by using the + operator
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

#Another way to join two lists is by appending all the items from list2 into list1
list1 = ["a","b","c"]
list2 = [1,2,3]
for x in list2:
    list1.append(x)
print(list1)    

#Extend
list1 = ["a","b","c"]
list2 = [1,2,3]
list1.extend(list2)
print(list1)

# TUPLES
# Tuples are unchangeable, meaning that we cannot change, add or remove items  after the tuple has been created.
thistuple = ("apple","banana","cherry","apple","cherry")
print(thistuple)

#Tuple Length
thistuple = ("apple","banana","cherry")
print(len(thistuple))

#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc",34,True,40,"male")
print(tuple1)

# The tuple() Constructor
thistuple = tuple(("apple","banana","cherry")) #note the double round - brackets. 
print(thistuple)

# Access Tuple Items
thistuple = ("apple","banana","cherry")
print(thistuple[1])

#Check if Item Exists
thistuple = ("apple","banana","cherry")
if "apple" in thistuple:
    print("yes, 'apple' is in the fruits tuple")

#Convert the Tuple into a list to be able to change it:
x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Convert this tuple into a list, add "Orange", and convert it back into a tuple:
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("Orange")
thistuple = tuple(y)
print(thistuple)

# Create a new Tuple with the value "orange", and add that tuple:
thistuple = ("apple","banana","kiwi")
y = ("orange",)
thistuple += y
print(thistuple)

# Unpacking a Tuple:
fruits = ("apple","banana","cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# using Asterisk*
fruits = ("apple","banana","cherry","strawberry","raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# add a list of values the "tropic" variable:
fruits = ("apple","mango","pineapple","cherry")

(green,*tropic,red) = fruits
print(green)
print(tropic)
print(red)

#Loop through the items and print the values:
thistuple = ("apple","banana","cherry")
for x in thistuple:
    print(x)

#Loop through the index Numbers:
thistuple = ("apple","banana","cherry")
for i in range(len(thistuple)):
    print(thistuple[i])   

#Multiply the fruits tuple by 2:
fruits = ("apple","banana","cherry")
mytuple = fruits * 2
print(mytuple)     

# Sets
thisset = {"apple","banana","cherry"}
print(len(thisset))

#Access Set Items
thisset = {"apple","banana","cherry"}
for x in thislist:
    print(x)

# Set With if else
thisset = {"apple","banana","cherry"}
if "apple" in thisset:
    print("Yes, Apple is there.")
else:
    print("x is not there!")     

#Check if "banana" is present in the set:
thisset = {"apple","banana","cherry"}
print("banana" in thisset)

#Check if "banana" is not in the set:
thisset = {"apple","banana","cherry"}
print("banana"  not in thisset)

#Add Items in the Set:
thisset = {"apple","banana","cherry"}
thisset.add("orange")
print(thisset)

# Add sets:
thisset = {"apple","banana","cherry"}
tropical = {"pineapple","mango","papaya"}

thisset.update(tropical)

print(thisset)

# Add any iterable means Tuple, List:
thisset = {"apple","banana","cherry"}
mylist = ["kiwi","orange"]
thisset.update(mylist)
print(thisset)

#union() method return a new set with all items from both Sets.
#join set1 and set2 into a new set:
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

#Use | operator instead of the union() method, and you will get the same result.
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1 | set2
print(set3)

# The union() method allows you to join a set with other data types,like lists or tuples.
x = {"a","b","c"}
y = (1,2,3)
z = x.union(y)
print(z)

#Print a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" :1965
}
print(thisdict)



    



