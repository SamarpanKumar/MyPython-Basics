dict1 = {"a":23,"b":45}
print(dict1)
# for adding element:
dict1["c"] =14
print(dict1)
#for Update element
dict1["c"] = 456
print(dict1)
# For deleting Element:
dict1.pop("a")
print(dict1)
#For delete last item:
dict1.popitem()

print(dict1["b"])

print(dict1.keys())
print(dict1.values())
print(dict1.items())

