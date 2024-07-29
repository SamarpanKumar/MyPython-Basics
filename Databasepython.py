import mysql.connector
mydb = mysql.connector.connect(
    host ='localhost' ,
    user ='root',
    password = 'root',
    database ='python'
)
print(mydb)

mycursor = mydb.cursor()
#mycursor.execute("Create table xyz (id int, name varchar(255))")
mycursor.execute("alter table xyz add column city varchar(255)")

