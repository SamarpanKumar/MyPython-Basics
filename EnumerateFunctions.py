Topic = "Enumerate Function in Python"
a = '''The enumerate function is a built-in function in Python 
that allows you to loop over a sequence 
(such as a list, tuple, or string) 
and get the index and value of each element in the sequence at the same time.'''
print(Topic.center(50))

marks = [12,56,32,98,12,45,1,4]
#index = 0
#for mark  in marks:
    #print(mark)
    #if(index == 3):
     #   print("Samarpan, very Good!")
    #index +=1

for  index,mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Samarpan, you are intelligent.")

#Loop over a list and print the index value  of each element.
fruits = ["Apple","banana","mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)




#Loop over a list and print the index (starting at 1) and value of each element.
fruits = ["Apple","banana","mango"]
for index, fruit in enumerate(fruits, start = 1):
    print(index, fruit)



#Loop over a tuple and print the index and value of each element
colors = ('red','green','blue')
for index, color in enumerate(colors, start= 1):
    print(index , color)

#Loop over a string and print the index and value of each character
s = "hello"
for index,c in enumerate(s):
    print(index, c)