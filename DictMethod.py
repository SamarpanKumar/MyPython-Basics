Topic = "Dictionary Methods"
print(Topic.center(50))

# Update
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}
ep1.update(ep2)
ep1.clear()
ep1.pop(122)
ep1.popitem()
del ep1[122]
print(ep1)

info = {'name':'Akshay','age':24,'eligible':True}
print(info)
info.update({'age': 23})
info.update({'DOB': 1999})
print(info)

# Removing Items From Dictionary:
#clear()
info = {'name':'JaiGopal','age':19,'eligible':True}
info.clear()
print(info)

#pop()
info = {'name':'SAMARPAN', 'age':22 , 'eligible':True}
info.pop('eligible')
print(info)

#popitem()
info = {'name':"Andrew",'age': 19,'eligible':True,'DOB':2003}
info.popitem()
print(info)

#del
info = {'name':'peter','age': 19, 'eligible':True,'DOB':2003}
del info['age']
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)

