Topic = " A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it."
print(Topic.center(50))

def my_generator():
    for i in range (5000000000):
        # Complex Computations
        yield i
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

#for j in gen:
# print(j)