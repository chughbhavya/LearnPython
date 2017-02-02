import mysql.connector

conn = mysql.connector.connect(user = "root", password = "bhavyaroot", host = "localhost"
                               ,database = "university")
mycursor = conn.cursor()
mycursor.execute("""Create table if not exists Customer
(
id int primary key,
name varchar(30),
email varchar(30),
city varchar(30),
age int,
gender char(1)
)""")

mycursor.execute(""" Insert into Customer values
(11, "Bhavya", "chugh.bhavya@gmail.com", "Plano", 25, "F")""")
mycursor.execute(""" Insert into Customer values
(2, "Milind", "chugh.bhavya@gmail.com", "Plano", 25, "F")""")
mycursor.execute(""" Insert into Customer values
(3, "Mansi", "chugh.bhavya@gmail.com", "Plano", 25, "F")""")
conn.commit()
mycursor.execute("Select * from Customer")
mylist = mycursor.fetchall()
for i in mylist:
    print(i)
