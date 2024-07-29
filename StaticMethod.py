Topic = "Static Method"
print(Topic.center(50))

class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n 

    @staticmethod #by Using @Staticmethod we dont have to use self, easy .
    def add(a,b):
        return a + b       
    
#result = Math.add(1,2)
# print(result) #Output: 3
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)


#print(Math.add(7,2))
