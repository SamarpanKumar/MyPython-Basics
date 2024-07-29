Topic = 'is_VS_== in Python.'
print(Topic.center(50))
a = None
b = None

print(a is b) #Exact Location of the object in memory
print(a is None) # Exact location of object in memory
print( a == b) # value

Topic2 = 'Lists'
print(Topic2)
a = [1, 2, 3] # Lists are mutable, not immutable
b = [1, 2, 3]
print( a == b) #True
print( a is b) #False

Topic3 = 'Strings'
print(Topic3)
a = "Hello" # strings are immutable
b = "Hello"
print( a == b) #True
print( a is b) #True

Topic4 = 'Integers'
print(Topic4)
a = 5 # integers are immutable
a = 5

print(a is b) # True
print(a == b) # True

