Topic = "Python Dictionary"
print(Topic.center(50))

dict = {
    "Harry": "Human Being",
    "spoon": "object"
}

print(dict["Harry"])

dic = {
    344: "Harry",
    56: "Shubham",
    678: "Zakir",
    567: "Neha"
}
print(dic[344])

info = {'name':'Ravi','age':20,'eligiblity':True}
print(info)
print(info['name'])
print(info.get('name'))
print(info.keys())
print(info.values())

for key in info.keys():
    print(info[key])

for key in info.keys():
    print(f"The Value responding to the {key} is {info[key]}")    

print(info.items())  
for key, value in info.items():
    print(f"The Value responding to the {key} is {value}")