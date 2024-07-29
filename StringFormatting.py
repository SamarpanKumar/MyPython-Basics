letter = "Hey, my name is {1} and I am from {0}"
country = "India"
name = "Samarpan"

print(letter.format(country,name))

print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2*30}"))
print()

val = 'Geeks'
print(f"{val} for {val} is a portal for {val}")
name = "Samarpan"
age = 23
print(f"Hello, My Name is {name} and I'm {age} years Old.")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

print(f"{2*30}")