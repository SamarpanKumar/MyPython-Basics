# Strings are Immutable
a = "!!!Harry!! !!!!!!!!! Harry"
print(len(a)) #Length of Alphabets
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry","John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "welcome to the Console!!! "
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the console!!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console!!!"
print(str1.endswith("to",4,10))

str1 = "He's name is Dan.He is an honest man."
print(str1.find("is"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 ="Welcome"
print(str1.isalpha)