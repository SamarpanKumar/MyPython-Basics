#Error Handling:
try:
    print(1/"n")
except ZeroDivisionError:
    print("error because int not disible by zero")
except TypeError:
    print("error int not divisble by string")
finally:
    print("adfgfg")            
