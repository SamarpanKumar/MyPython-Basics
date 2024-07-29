Topic = "Modes in a file"
print(Topic.center(50))
#READING A FILE.

#f = open('myfile01.txt','r')
#print(f)
#text = f.read()
#print(text)
#f.close()

# TO CREATE AUTOMATICALLY NEW TXT FILE.
F = open("myfile02.txt",'w')
text = F.read()
print(text)
F.close()

#WRITING A FILE.
#f = open("myfile01.txt",'w')
#f.write("Hello World!")
#f.close()

#APPENDING IN A FILE
#f = open("myfile01.txt",'a')
#f.write("HI This is Samarpan Kumar Python Developer.")
#f.close()

#FILE ALREADY EXIST
#f = open("myfile01.txt",'x')
#f.write("HI This is Samarpan Kumar Python Developer.")
#f.close()

#BINARY IN A FILE.
#f = open("Room.jpg",'rb')
#text = f.read()
#print(text)
#f.close()


with open('myfile01.txt', 'a') as f:
    f.write("Hey i am inside with")