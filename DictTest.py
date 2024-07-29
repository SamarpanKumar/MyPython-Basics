print("""Storing Names and Birthdays in a DictionaryIn this section we look at a program that keeps your
friends’ names and birthdays in a dictionary. Each entry in the dictionary uses a friend’s name as
the key and that friend’s birthday as the value. You can use the program to look up your friends’
birthdays by enter-ing their names.The program displays a menu that allows the user to make one of
the following choices:
1.Look up a birthday
2.Add a new birthday
3.Change a birthday
4.Delete a birthday
5.Quit the program
The program initially starts with an empty dictionary,so you have to choose item 2 from the menu to
add a new entry. Once you have added a few entries ,you can choose item 1 to look up a specific
person’s birthday, item 3 to change an existing birthday in the dictionary, item 4 to delete a
birthday from the dictionary ,or item 5 to quit the program.""")

a = {}
b = True
while b:
    choice = int(input("enter 1,2,3,4: "))
    if choice == 1:
        name = input("enter the name: ")
        print(a[name])
    elif choice ==2:
        name = input("Enter you Name: ")
        dateb = int(input("Enter your Date: "))
        a[name] = dateb
        print(a)
    elif choice == 3:
        name = input("Enter your Name: ")
        dateb = input("Enter your Number: ")
        a[name] = dateb 
        print(a)
    elif choice == 4:
        name = input("Enter the name: ")
        a.pop(name) 
        print(a) 
    else: 
     s= input("Enter to restart y/n ")
     if s =='y':
        b = True
     else:
        b = False    
