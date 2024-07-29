#info = {2,4,2,6}
#print(info)

s1 ={1,2,5,6}
s2 ={3,6,7}
print(s1.union(s2))
print(s1.update(s2))
print(s1, s2)

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
cities3 = cities.union(cities2)
print(cities3)

cities4 = cities.intersection(cities2) 
print(cities4)

cities.intersection_update(cities2)
print(cities)

cities5 = {cities.symmetric_difference(cities2)}
print(cities5)

cities6 = {cities.difference(cities2)}
print(cities6)

cities7 = {"Tokyo", "Seoul","Kabul", "Madrid"}
cities8 = {"Tokyo" , "Seoul"," Kabul","Madrid"}
print(cities7.isdisjoint(cities8))