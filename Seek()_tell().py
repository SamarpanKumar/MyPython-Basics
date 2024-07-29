Topic = "seek() and tell() Functions"
print(Topic.center(50))

#   SEEK() FUNCTION!
'''
The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position. For example:
'''
#with open('myfile05.txt','r') as f:
# Move to the  10th byte in the file.
#    f.seek(10)
#Read the next 5 bytes
#    data = f.read(5)
#    print(data)

# TRUNCATE FUNCTION!
'''When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.'''
#with open("Sample.txt",'w') as f:
#    f.write('Hello World!')
#    f.truncate(3)

#with open("Sample.txt",'r') as f:
#    data = f.read()
#    print(data)


# TELL FUNCTION()
'''
The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position. For example:
'''
with open("myfile06.txt",'r') as f:
#   read the first 10 bytes 
    data = f.read(10)
#Save the current position 
    current_position = f.tell()
#Seek to the saved Position
    f.seek(current_position)
print(f.seek)