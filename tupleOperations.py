tuple1 = (0,1,2,31,2,3,1,3,2,3)
#res = tuple1.count(3)
#res = tuple1.index(3)
#res = tuple1.index(2)
res = tuple1.index(3,4,8)
#res = len(tuple1)

print('Count of 3 in tuple1 is: ', res)

# Manipulating Tuples:
countries = ("Spain","Italy","India","England","Germany")
temp = list(countries)
temp.append("Russia") # Add item
temp.pop(3) #Remove item
temp[2] = "Finland" # change Item
countries = tuple(temp)
print(countries)

#Another Example for Manipulating tuples:
countries = ("Pakistan","Afghanistan","Bangladesh","ShriLanka")
countries2 = ("vietnam","India","China")
southEastAsia = countries + countries2
print(southEastAsia)

Tuple = (0,1,2,5,2,3,1,3,2)
res = Tuple.index(3)
print('First Occurence of 3 is', res)

Countries = ("NYC","America","South Africa", "Newzealand","India")
change = list(Countries)
change.append("Korea") # Add Items
change.pop(1) # Removing Item
change[1] = "Seattle"
Countries = tuple(change)
print(Countries)









 
