Topic = "DocString"
print(Topic.center(50))

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2) ## Will mutliply by its own n.
square(5)
print(square.__doc__)    

# Another Example
def square(n):
    '''Takes in number n, returns the square of n'''
    print(n**2) # ** is Exponential
square(2)
print(square.__doc__)    