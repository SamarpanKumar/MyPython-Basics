#Data Structure: Organize Data
# list : Group of elements
#heterogenous:
#arrays : same type of Data Elements:

list1 = [12,34,"jittu"]
print(list1)
list1.append(54) # For Adding single Element>
print(list1)
list1.insert(1,2344) # 1 is position.
print(list1)
list1.extend([123,155,345,3454354343,343434]) # Adding lists
print(list1)
list1.remove(343434)
print(list1)
list1.pop() #wiil atoumatically delete last element.
print(list1)
print(list1[2]) # 2 is index value position

print(list1[1:6]) # Slicing.

# Comprehension List.
list12=[x for x in range(1,10)]
print(list12)

# make to count the input user.
a = int(input("Enter any Number: "))
list13=[]

for i in range(a):
    s =input("enter the name: ")
    list13.append(s)
print(list13)

# test prroject:
# Make a list 100 and separate odd and even in the list.

# Create a list of 100 numbers

numbers = list(range(1, 101))

# Separate odd and even numbers into two lists
odd_numbers = [num for num in numbers if num % 2 != 0]
even_numbers = [num for num in numbers if num % 2 == 0]

# Print the lists
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

# Another example: 
List15 =[x for x in range(1,100)] 
odd=()
even = ()
for x in List15:
    if x%2==0:
        even.append(x)

    else:
        odd.append(x)
print(odd)
print(even)        


