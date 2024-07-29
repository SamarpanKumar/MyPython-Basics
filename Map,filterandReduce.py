# MAP
#def cube(x):
#    return x * x * x

#print(cube(2))

'''List of numbers'''
#l = [1, 2, 4, 6, 4, 3]
#newl = []
#for item in l:
#    newl.append(cube(item))

'''map(function, iterable)'''
#newl = list(map(cube, l))
''' newl list each number using the function'''
#newl = list(map(lambda x: x*x*x, l))
#print(newl)

#FILTER
'''filter(predicate, iterable)''' 
#def filter_function(a):
#    return a>2

#newnewl = list(filter(filter_function, l))
#print(newnewl)

from functools import reduce

#List of Numbers:
numbers = [1, 2, 3, 4, 5]  # Last one will remain constant.
# numbers = [1 + 2 = 3 + 3 = 6 + 4 = 10]
# numbers = [10, 5]
# numbers = [15]

# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
    return x + y

sum = reduce(mysum, numbers)

#print the sum
print(sum)


