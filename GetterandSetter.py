#Getters in Python
class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def value(self):
        return self._value
    
obj  = MyClass(10)
obj.value
obj.show()




#Setter in Python.
class MyClass1:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def value(self):
        return 10 * self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value/10

obj = MyClass1(10)
obj.value = 20
print(obj.value)
obj.value     

