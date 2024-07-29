Topic = "For Loop with else"
print(Topic.center(50))
#Python allows the else keyword to be used with the for and while loops too. 
#The else block appears after the body of the loop. 
#The statements in the else block will be executed after all iterations are completed.
# The program exits the loop only after the else block is executed.
for i in range(6):
    print(i)
    if i == 4:
        break

else:
    print("Sorry no i")
x = 0
while x < 7:
    print(x)
    x = x + 1
    #if x == 5:
       # break
else:
    print("sorry no x")

for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of Loop")    

for t in range(5):
    print("iteration no {} in for loop".format(t+1))

else:
    print("else block in Loop.")
print("Out of the Loop")    