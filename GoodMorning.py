import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)


Topic = ("Making GOOD MORNING!")
print(Topic.center(50))
Time = time.strftime('%H:%M:%S')
print(Time)
str = input("Enter your Name: ")
hours = int(time.strftime('%H'))
if(hours>=0 and hours<=11):
    print("Hello",str.capitalize(),"Good Morning Sir!"," Time:", hours)
elif(hours>=12 and hours<=17):
    print("Hello",str.capitalize(),"Good Afternoon Sir!"," Time:", hours) 
else:
    print("Hello",str.capitalize(),"Good Evening Sir!"," Time:", hours) 
