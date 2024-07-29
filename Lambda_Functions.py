#def double (x):
#    return x*2

#print(double(5))

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3,5,10))

def appl(fx, value):
    return 6 + fx(value)
print(appl(lambda x: x * x, 2))


# Lambda function to calculate the product of two numbers,
# with additional print statement
x = 5,
y = 2
lambda x, y: print(f'{x} * {y} = {x * y}')